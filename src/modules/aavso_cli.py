"""
AAVSO (American Association of Variable Star Observers) CLI Module

This module provides CLI interface to query the AAVSO VSX (Variable Star Index) database.
"""

from typing import Optional, List
import typer
import requests
from astropy.table import Table as AstropyTable
from astropy.io.votable import parse_single_table
from io import BytesIO

from ..utils import (
    console,
    display_table,
    handle_astroquery_exception,
    common_output_options,
    save_table_to_file,
    global_keyboard_interrupt_handler,
    em,
)
from ..common_options import setup_debug_context
from ..i18n import get_translator
import re
from io import StringIO
from contextlib import redirect_stdout

VSX_BASE_URL = "https://www.aavso.org/vsx/index.php"


def get_app():
    import builtins

    _ = builtins._
    help_text = _("Query the AAVSO Variable Star Index (VSX) database.")
    app = typer.Typer(
        name="aavso", help=help_text, invoke_without_command=True, no_args_is_help=False
    )

    @app.callback()
    def aavso_callback(
        ctx: typer.Context,
        debug: bool = typer.Option(
            False,
            "-t",
            "--debug",
            help=_("Enable debug mode with verbose output."),
            envvar="AQC_DEBUG",
        ),
        verbose: bool = typer.Option(
            False, "-v", "--verbose", help=_("Enable verbose output.")
        ),
    ):
        setup_debug_context(ctx, debug, verbose)

        if ctx.invoked_subcommand is None and not any(
            arg in ["-h", "--help"] for arg in ctx.args
        ):
            help_output_capture = StringIO()
            with redirect_stdout(help_output_capture):
                try:
                    app(ctx.args + ["--help"])
                except SystemExit:
                    pass
            full_help_text = help_output_capture.getvalue()

            commands_match = re.search(
                r"╭─ Commands ─.*?(\n(?:│.*?\n)*)╰─.*─╯", full_help_text, re.DOTALL
            )
            if commands_match:
                commands_section = commands_match.group(0)
                filtered_commands_section = "\n".join(
                    [
                        line
                        for line in commands_section.splitlines()
                        if "Usage:" not in line
                    ]
                )
                console.print(filtered_commands_section)
            else:
                console.print(full_help_text)
            raise typer.Exit()

    @app.command(
        name="object",
        help=builtins._("Query VSX for a variable star by name or identifier."),
    )
    @global_keyboard_interrupt_handler
    def query_object(
        ctx: typer.Context,
        identifier: str = typer.Argument(
            ...,
            help=builtins._(
                "Star identifier or name (e.g., 'SS Cyg', 'T CrB', 'M31')."
            ),
        ),
        format: str = typer.Option(
            "votable",
            "--format",
            "-f",
            help=builtins._("Output format: 'votable' (default), 'json', or 'xml'."),
        ),
        output_file: Optional[str] = common_output_options["output_file"],
        output_format: Optional[str] = common_output_options["output_format"],
        max_rows_display: int = typer.Option(
            50,
            help=builtins._("Maximum number of rows to display. Use -1 for all rows."),
        ),
        show_all_columns: bool = typer.Option(
            False,
            "--show-all-cols",
            help=builtins._("Show all columns in the output table."),
        ),
    ):
        """
        Query the VSX database for a specific variable star by identifier.
        Example: aqc aavso object SS+Cyg
        """
        console.print(
            _(
                "[cyan]Querying AAVSO VSX for identifier: '{identifier}'...[/cyan]"
            ).format(identifier=identifier)
        )

        try:
            params = {
                "view": "query.votable" if format == "votable" else "query",
                "ident": identifier,
                "format": format,
            }

            console.print(
                _("[dim]Request URL: {url}[/dim]").format(url=_build_vsx_url(params))
            )

            response = requests.get(_build_vsx_url(params), timeout=60)

            if response.status_code != 200:
                console.print(
                    _(
                        "[bold red]Error: HTTP {status_code} - {error}[/bold red]"
                    ).format(
                        status_code=em(str(response.status_code)),
                        error=em(
                            str(
                                response.text[:200]
                                if response.text
                                else "No error message"
                            )
                        ),
                    )
                )
                raise typer.Exit(code=1)

            content_type = response.headers.get("Content-Type", "")

            if format == "json":
                import json

                result_data = response.json()
                # Convert JSON to Astropy Table for consistency
                if isinstance(result_data, list) and len(result_data) > 0:
                    result_table = AstropyTable(
                        rows=result_data, names=list(result_data[0].keys())
                    )
                elif isinstance(result_data, dict):
                    result_table = AstropyTable([result_data])
                else:
                    console.print(
                        _(
                            "[yellow]No data found for identifier '{identifier}'.[/yellow]"
                        ).format(identifier=identifier)
                    )
                    return
            elif (
                format == "xml"
                or content_type.startswith("text/xml")
                or content_type.startswith("application/xml")
            ):
                # Parse XML response
                result_table = parse_votable_xml(response.content)
            else:
                # Default VOTable parsing
                result_table = parse_votable_xml(response.content)

            if result_table is not None and len(result_table) > 0:
                console.print(
                    _(
                        "[green]Found {count} result(s) for '{identifier}'.[/green]"
                    ).format(count=len(result_table), identifier=identifier)
                )
                display_table(
                    ctx,
                    result_table,
                    title=_("VSX Results for {identifier}").format(
                        identifier=identifier
                    ),
                    max_rows=max_rows_display,
                    show_all_columns=show_all_columns,
                )
                if output_file:
                    save_table_to_file(
                        ctx, result_table, output_file, output_format, _("VSX query")
                    )
            else:
                console.print(
                    _(
                        "[yellow]No data found for identifier '{identifier}'.[/yellow]"
                    ).format(identifier=identifier)
                )

        except Exception as e:
            handle_astroquery_exception(ctx, e, _("AAVSO VSX object"))
            raise typer.Exit(code=1)

    @app.command(
        name="region", help=builtins._("Query VSX for variable stars in a sky region.")
    )
    @global_keyboard_interrupt_handler
    def query_region(
        ctx: typer.Context,
        ra: float = typer.Argument(
            ..., help=builtins._("Right Ascension in decimal degrees (e.g., 196.421).")
        ),
        dec: float = typer.Argument(
            ..., help=builtins._("Declination in decimal degrees (e.g., 18.018).")
        ),
        radius: float = typer.Option(
            0.1,
            "--radius",
            "-r",
            help=builtins._("Search radius in degrees. Default: 0.1."),
        ),
        maglimit: Optional[float] = typer.Option(
            None, "--maglimit", help=builtins._("Limit stars by maximum magnitude.")
        ),
        format: str = typer.Option(
            "json",
            "--format",
            "-f",
            help=builtins._("Output format: 'json' (default), 'votable', or 'xml'."),
        ),
        output_file: Optional[str] = common_output_options["output_file"],
        output_format: Optional[str] = common_output_options["output_format"],
        max_rows_display: int = typer.Option(
            50,
            help=builtins._("Maximum number of rows to display. Use -1 for all rows."),
        ),
        show_all_columns: bool = typer.Option(
            False,
            "--show-all-cols",
            help=builtins._("Show all columns in the output table."),
        ),
    ):
        """
        Query the VSX database for variable stars within a circular region around coordinates.
        Example: aqc aavso region 196.421 18.018 --radius 0.5
        """
        console.print(
            _(
                "[cyan]Querying AAVSO VSX for region around RA={ra}, Dec={dec} with radius={radius} deg...[/cyan]"
            ).format(ra=ra, dec=dec, radius=radius)
        )

        try:
            params = {
                "view": "api.list",
                "ra": ra,
                "dec": dec,
                "radius": radius,
                "format": format,
            }

            if maglimit is not None:
                params["tomag"] = maglimit

            console.print(
                _("[dim]Request URL: {url}[/dim]").format(url=_build_vsx_url(params))
            )

            response = requests.get(_build_vsx_url(params), timeout=60)

            if response.status_code != 200:
                console.print(
                    _("[bold red]Error: HTTP {status_code}[/bold red]").format(
                        status_code=em(str(response.status_code))
                    )
                )
                raise typer.Exit(code=1)

            content_type = response.headers.get("Content-Type", "")

            if format == "json":
                import json

                result_data = response.json()
                if isinstance(result_data, list) and len(result_data) > 0:
                    result_table = AstropyTable(
                        rows=result_data, names=list(result_data[0].keys())
                    )
                elif isinstance(result_data, dict):
                    result_table = AstropyTable([result_data])
                else:
                    console.print(
                        _(
                            "[yellow]No variable stars found in the specified region.[/yellow]"
                        )
                    )
                    return
            else:
                # Try to parse as VOTable
                try:
                    result_table = parse_votable_xml(response.content)
                except Exception:
                    console.print(
                        _(
                            "[yellow]Could not parse response as VOTable. Try format=json.[/yellow]"
                        )
                    )
                    raise typer.Exit(code=1)

            if result_table is not None and len(result_table) > 0:
                console.print(
                    _(
                        "[green]Found {count} variable star(s) in region.[/green]"
                    ).format(count=len(result_table))
                )
                display_table(
                    ctx,
                    result_table,
                    title=_("VSX Results for Region"),
                    max_rows=max_rows_display,
                    show_all_columns=show_all_columns,
                )
                if output_file:
                    save_table_to_file(
                        ctx,
                        result_table,
                        output_file,
                        output_format,
                        _("VSX region query"),
                    )
            else:
                console.print(
                    _(
                        "[yellow]No variable stars found in the specified region.[/yellow]"
                    )
                )

        except Exception as e:
            handle_astroquery_exception(ctx, e, _("AAVSO VSX region"))
            raise typer.Exit(code=1)

    return app


def _build_vsx_url(params: dict) -> str:
    """Build the VSX API URL with parameters."""
    query_string = "&".join(f"{k}={v}" for k, v in params.items())
    return f"{VSX_BASE_URL}?{query_string}"


def parse_votable_xml(content: bytes) -> Optional[AstropyTable]:
    """Parse VOTable XML content into an Astropy Table."""
    try:
        vo_table = parse_single_table(BytesIO(content))
        return vo_table.to_table()
    except Exception as e:
        console.print(f"[yellow]Could not parse VOTable: {em(str(e))}[/yellow]")
        return None
