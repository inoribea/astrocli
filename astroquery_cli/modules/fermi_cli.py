"""
Fermi-LAT CLI Module

This module provides CLI interface to query Fermi Large Area Telescope data.
"""

from typing import Optional, List
import typer
from astropy.table import Table as AstropyTable

from ..utils import (
    console,
    display_table,
    handle_astroquery_exception,
    common_output_options,
    save_table_to_file,
    global_keyboard_interrupt_handler,
)
from ..common_options import setup_debug_context
from ..i18n import get_translator
import re
from io import StringIO
from contextlib import redirect_stdout


def get_app():
    import builtins

    _ = builtins._
    help_text = _("Query Fermi Large Area Telescope (LAT) data.")
    app = typer.Typer(
        name="fermi", help=help_text, invoke_without_command=True, no_args_is_help=False
    )

    @app.callback()
    def fermi_callback(
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
        help=builtins._("Query Fermi LAT data for an object or coordinates."),
    )
    @global_keyboard_interrupt_handler
    def query_object(
        ctx: typer.Context,
        target: str = typer.Argument(
            ...,
            help=builtins._(
                "Object name (e.g., 'M31', 'Crab Nebula') or coordinates in J2000 frame."
            ),
        ),
        searchradius: float = typer.Option(
            1.0,
            "--radius",
            "-r",
            help=builtins._("Search radius in degrees (default: 1.0, range: 1-60)."),
        ),
        obsdates: str = typer.Option(
            "",
            "--dates",
            "-d",
            help=builtins._(
                "Observation date range (e.g., '2013-01-01 00:00:00, 2013-01-02 00:00:00')."
            ),
        ),
        timesys: str = typer.Option(
            "Gregorian",
            "--timesys",
            help=builtins._("Time system: 'Gregorian' (default), 'MET', or 'MJD'."),
        ),
        energyrange_MeV: str = typer.Option(
            "",
            "--energy",
            "-e",
            help=builtins._(
                "Energy range in MeV (e.g., '1000, 100000' for 1-100 GeV)."
            ),
        ),
        latdatatype: str = typer.Option(
            "Photon",
            "--type",
            help=builtins._("LAT data type: 'Photon' (default) or 'Extended'."),
        ),
        spacecraftdata: bool = typer.Option(
            True,
            "--spacecraft",
            help=builtins._(
                "Include spacecraft data (default: True). Set --no-spacecraft to disable."
            ),
        ),
        output_file: Optional[str] = common_output_options["output_file"],
        output_format: Optional[str] = common_output_options["output_format"],
        max_rows_display: int = typer.Option(
            10, help=builtins._("Maximum number of rows to display.")
        ),
        show_all_columns: bool = typer.Option(
            False,
            "--show-all-cols",
            help=builtins._("Show all columns in the output table."),
        ),
        no_download: bool = typer.Option(
            False,
            "--no-download",
            help=builtins._("Don't download FITS files, only show URLs."),
        ),
    ):
        """
        Query Fermi LAT database for observations around a target.

        Example: aqc fermi object M31 --dates "2013-01-01 00:00:00, 2013-01-02 00:00:00" --energy "1000, 100000"
        """
        console.print(
            _("[cyan]Querying Fermi LAT for target '{target}'...[/cyan]").format(
                target=target
            )
        )

        try:
            # Import FermiLAT from astroquery
            from astroquery.fermi import FermiLAT

            # Build query parameters
            query_params = {
                "name_or_coords": target,
                "searchradius": searchradius,
                "obsdates": obsdates,
                "timesys": timesys,
                "energyrange_MeV": energyrange_MeV,
                "LATdatatype": latdatatype,
                "spacecraftdata": spacecraftdata,
            }

            console.print(
                _(
                    "[dim]Query parameters: radius={radius}deg, dates={dates}, energy={energy}MeV, type={type}, spacecraft={sc}[/dim]"
                ).format(
                    radius=searchradius,
                    dates=obsdates or "all",
                    energy=energyrange_MeV or "all",
                    type=latdatatype,
                    sc=spacecraftdata,
                )
            )

            # Execute query
            result_url = FermiLAT.query_object(**query_params)

            console.print(_("[green]Query successful![/green]"))
            console.print(_("[bold cyan]Result URL(s):[/bold cyan]"))

            if isinstance(result_url, str):
                result_urls = [result_url]
            elif isinstance(result_url, list):
                result_urls = result_url
            else:
                console.print(_("[yellow]Unexpected result format[/yellow]"))
                result_urls = []

            for url in result_urls:
                console.print(f"  - [blue underline]{url}[/blue underline]")

            # Optionally download FITS files
            if not no_download and result_urls:
                console.print(_("\n[cyan]Downloading FITS files...[/cyan]"))
                import time

                downloaded_files = []

                for url in result_urls:
                    filename = url.split("/")[-1]
                    try:
                        import requests

                        response = requests.get(url, timeout=300, stream=True)
                        total_size = int(response.headers.get("content-length", 0))

                        if response.status_code == 200:
                            with open(filename, "wb") as f:
                                for chunk in response.iter_content(chunk_size=8192):
                                    if chunk:
                                        f.write(chunk)
                            console.print(
                                _(
                                    "[green]  Downloaded: {filename} ({size:.1f} MB)[/green]"
                                ).format(
                                    filename=filename, size=total_size / (1024 * 1024)
                                )
                            )
                            downloaded_files.append(filename)
                        else:
                            console.print(
                                _(
                                    "[yellow]Failed to download: {filename} (HTTP {status})[/yellow]"
                                ).format(filename=filename, status=response.status_code)
                            )
                    except Exception as e:
                        console.print(
                            _(
                                "[yellow]Error downloading {filename}: {error}[/yellow]"
                            ).format(filename=filename, error=str(e))
                        )

                if downloaded_files:
                    console.print(
                        _(
                            "\n[bold green]Successfully downloaded {count} file(s).[/bold green]"
                        ).format(count=len(downloaded_files))
                    )
                    # Create a summary table for display
                    summary_data = []
                    for fname in downloaded_files:
                        summary_data.append({"filename": fname})
                    summary_table = AstropyTable(rows=summary_data, names=["filename"])
                    display_table(
                        ctx,
                        summary_table,
                        title=_("Downloaded Files"),
                        max_rows=max_rows_display,
                        show_all_columns=show_all_columns,
                    )
                    if output_file:
                        save_table_to_file(
                            ctx,
                            summary_table,
                            output_file,
                            output_format,
                            _("Fermi download summary"),
                        )

            else:
                console.print(_("[yellow]No URLs returned from query[/yellow]"))

        except Exception as e:
            handle_astroquery_exception(ctx, e, _("Fermi LAT object"))
            raise typer.Exit(code=1)

    @app.command(name="clear-cache", help=builtins._("Clear Fermi LAT query cache."))
    @global_keyboard_interrupt_handler
    def clear_cache(ctx: typer.Context):
        """
        Clear the Fermi LAT cache to avoid outdated results.
        """
        console.print(_("[cyan]Clearing Fermi LAT cache...[/cyan]"))
        try:
            from astroquery.fermi import FermiLAT

            FermiLAT.clear_cache()
            console.print(_("[green]Cache cleared successfully.[/green]"))
        except Exception as e:
            console.print(
                _("[red]Error clearing cache: {error}[/red]").format(error=str(e))
            )
            raise typer.Exit(code=1)

    return app
