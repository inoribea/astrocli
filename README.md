# Astro CLI 🚀

**[English](README.md)** | **[中文](README_ZH.md)** | **[日本語](README_JA.md)** | **[Français](README_FR.md)**

> Your gateway to cosmos — Query astronomical data from command line

[![License](https://img.shields.io/badge/License-BSD%203Clause-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![Astropy](https://img.shields.io/badge/astropy-6.0%2B-orange.svg)](https://www.astropy.org/)
[![npm version](https://img.shields.io/npm/v/astroquery-cli.svg)](https://www.npmjs.com/package/astroquery-cli)

---

## ✨ What is Astro CLI?

**Astro CLI** is a modern command-line tool that provides quick access to multiple astronomical data services. It integrates [Astroquery](https://astroquery.readthedocs.io/) and other data access methods (direct API calls, HTTP requests) to help astronomers, researchers, and anyone query astronomical databases efficiently from the terminal.

*17 data sources. One command. Beautiful output. Multi-language support. Extensible for future services.*

---

## 🧩 Supported Data Sources

Query data from 17 different astronomical databases and services:

| Service | Description | Command | Alias |
|---------|------------|----------|--------|
| [SIMBAD](https://simbad.cds.unistra.fr/) | Basic astronomical data & object identification | `astrocli simbad` | `astrocli sim` |
| [VizieR](https://vizier.cds.unistra.fr/) | Catalog database search | `astrocli vizier` | `astrocli viz` |
| [ALMA](https://almascience.org/) | ALMA radio telescope observations | `astrocli alma` | - |
| [ESASky](https://www.esa.int/Enabling_Support/Operations/ESASky/) | Sky region visualization | `astrocli esasky` | - |
| [Gaia](https://www.cosmos.esa.int/gaia/) | ESA Gaia mission data | `astrocli gaia` | - |
| [IRSA](https://irsa.ipac.caltech.edu/) | Infrared Science Archive | `astrocli irsa` | - |
| [HEASARC](https://heasarc.gsfc.nasa.gov/) | X-ray and Gamma-ray data | `astrocli heasarc` | `astrocli hea` |
| [JPL Horizons](https://ssd.jpl.nasa.gov/) | Solar System ephemerides | `astrocli jpl` | - |
| [MAST](https://mast.stsci.edu/) | Space Telescope Archive (HST, JWST, etc.) | `astrocli mast` | - |
| [ADS](https://ui.adsabs.harvard.edu/) | Astrophysics literature search | `astrocli ads` | - |
| [NED](https://ned.ipac.caltech.edu/) | Extragalactic Database | `astrocli ned` | - |
| [NIST](https://physics.nist.gov/ASD/) | Atomic spectra database | `astrocli nist` | - |
| [NASA Exoplanet](https://exoplanetarchive.ipac.caltech.edu/) | Exoplanet catalog | `astrocli exoplanet` | `astrocli exo` |
| [SDSS](https://www.sdss.org/) | Sloan Digital Sky Survey | `astrocli sdss` | - |
| [ESO](https://www.eso.org/) | European Southern Observatory | `astrocli eso` | - |
| [Splatalogue](https://www.splatalogue.org/) | Molecular line database | `astrocli splatalogue` | `astrocli spl` |
| [**AAVSO VSX**](https://www.aavso.org/vsx/) | Variable Star Index | `astrocli aavso` | `astrocli aav` |
| [**Fermi-LAT**](https://fermi.gsfc.nasa.gov/) | Gamma-ray telescope data | `astrocli fermi` | `astrocli fer` |

---

## 🌟 Key Features

- **📦 Multi-Source Access**: Query 17+ astronomical databases from a single interface
- **🌏 Internationalized UI**: Built-in support for English, Chinese (Simplified), and Japanese
- **📊 Rich Output**: Beautifully formatted tables with support for exporting to CSV, ECSV, FITS, and more
- **⚡ Smart Defaults**: Sensible defaults with extensive customization options
- **🔍 Service Health**: Built-in connectivity testing (`--ping`) and field validation (`--field`)
- **🧑‍💻 Shell Completion**: Auto-completion support for Bash, Zsh, and Fish
- **🌌 Extensible**: Easy to add new astronomical data services

---

## 📦 Installation

Astro CLI offers multiple installation methods. Choose the one that suits you:

### Method 1: npm Global Install (Recommended)

```bash
# Global install (requires Node.js ≥18 and Python 3.11+)
npm install -g astroquery-cli

# After installation, all three commands are available:
astroquery-cli --help    # Full command name
aqc --help               # Short command (recommended)
astrocli --help          # Alias command

# Example: Query SIMBAD for M31
astrocli simbad object "M31"
```

### Method 2: npx/pnpm (No Install Required)

```bash
# Using npx (no installation needed)
npx astroquery-cli --help

# Using pnpm
pnpm astroquery-cli --help

# Example
npx astroquery-cli simbad object "M31"
```

### Method 3: PyPI Install (For Python Users)

```bash
# Install Python package from PyPI
pip install aqc-cli

# After installation, available commands:
aqc --help
astrocli --help
```

### Method 4: Install from Source

```bash
git clone https://github.com/inoribea/astroquery-cli.git
cd astroquery-cli
pip install -e .
```

---

### 📋 Package Naming

| Platform | Package Name | Install Command |
|----------|--------------|-----------------|
| **npm** | `astroquery-cli` | `npm install -g astroquery-cli` |
| **PyPI** | `aqc-cli` | `pip install aqc-cli` |

After installation, all three commands are available:
- `astroquery-cli` - Full command name
- `aqc` - Short command (recommended)
- `astrocli` - Alias command

---

### Environment Variables

- `AC_PYTHON` - Specify Python interpreter path
- `AC_VENV_DIR` - Custom virtual environment cache directory (default: `~/.cache/astrocli`)
- `AC_FORCE_INSTALL=1` - Force reinstall/upgrade Python dependencies
- `AC_DEBUG` - Enable debug mode
- `AC_LANG` - Set default language (en/zh/ja)

---

## 📚 Usage

### View All Available Commands

```bash
# Show all available modules and commands
astrocli --help

# Show help for a specific module
astrocli <module> --help
```

### Query Examples

#### 1. Query SIMBAD for an object

```bash
astrocli simbad object "M31"
astrocli simbad object "Crab Nebula" --show-all-cols
```

#### 2. Search VizieR catalogs

```bash
# Find catalogs by keywords
astrocli vizier find-catalogs --keyword photometry --keyword galaxy

# Query a specific catalog
astrocli vizier object "M31" --radius 0.1 --catalog "I/261/gaiadr3"
```

#### 3. Query AAVSO Variable Star Index (NEW!)

```bash
# Query a variable star by name
astrocli aavso object "SS Cyg"

# Search variable stars in a sky region
astrocli aavso region 196.421 18.018 --radius 0.5

# Get results in JSON format
astrocli aavso object "T CrB" --format json
```

#### 4. Query Fermi-LAT Data (NEW!)

```bash
# Query Fermi data for a target
astrocli fermi object "Crab Nebula" --energy "1000,100000" --dates "2020-01-01 00:00:00, 2020-01-02 00:00:00"

# Clear Fermi cache
astrocli fermi clear-cache
```

#### 5. Search ADS literature

```bash
astrocli ads search --title "exoplanet detection"
astrocli ads bibcode "2023A&A...555..959W"
```

---

## 🌐 Multi-Language Support

Change output language on-the-fly:

```bash
astrocli --lang en simbad object "M31"    # English
astrocli --lang zh simbad object "M31"    # Chinese (Simplified)
astrocli --lang ja simbad object "M31"    # Japanese
astrocli --lang fr simbad object "M31"    # French
```

Supported languages: **English (en)**, **Chinese (zh)**, **Japanese (ja)**, **French (fr)**

---

## 🔧 Global Options

| Option | Description |
|--------|-------------|
| `-l, --lang` | Set output language (en/zh/ja) |
| `-p, --ping` | Test connectivity to all services (top-level only) |
| `-f, --field` | Check available fields for a module (top-level only) |
| `-d, --debug` | Enable debug mode with verbose output |
| `-v, --verbose` | Enable verbose output |

---

## 🧑‍💻 Shell Autocompletion

Install completion for your shell:

```bash
astrocli --install-completion bash   # Bash
astrocli --install-completion zsh    # Zsh
astrocli --install-completion fish   # Fish
```

Add this to your shell config (e.g., `~/.zshrc`):

```bash
# For zsh
eval "$(astrocli --install-completion zsh)"

# For bash
eval "$(astrocli --install-completion bash)"
```

---

## 📊 Output & Export

Save query results to file:

```bash
astrocli simbad object "M31" --output-file results.csv

# Specify format explicitly
astrocli simbad object "M31" --output-file data.ecsv --output-format ecsv
```

Supported formats: `csv`, `ecsv`, `fits`, `votable`, `html`, `latex`, `ascii`

---

## 🔍 Testing Service Connectivity

Check if all data services are accessible:

```bash
astrocli --ping
```

---

## 🛠️ Development

### Project Structure

```
astrocli/
├── src/                    # Source code (renamed from astroquery_cli)
│   ├── modules/           # Service-specific modules
│   │   ├── simbad_cli.py
│   │   ├── vizier_cli.py
│   │   ├── aavso_cli.py      # AAVSO VSX
│   │   ├── fermi_cli.py      # Fermi-LAT
│   │   └── ...
│   ├── utils.py            # Common utilities
│   ├── common_options.py   # Shared CLI options
│   ├── i18n.py            # Internationalization
│   └── main.py            # CLI entry point
├── locales/                # Translation files
│   ├── en/LC_MESSAGES/     # English
│   ├── zh/LC_MESSAGES/     # Chinese
│   ├── ja/LC_MESSAGES/     # Japanese
│   └── fr/LC_MESSAGES/     # French
├── package.json           # npm/npx configuration
├── pyproject.toml         # Python package config
└── README.md
```

### Adding a New Module

1. Create `modules/<service>_cli.py` following existing patterns
2. Import in `main.py`'s `setup_subcommands()`
3. Add to README module list
4. Add translations to `locales/` directories

---

## 📄 License

BSD 3-Clause License

---

## 🙏 Acknowledgments

- [aqc-mcp](https://github.com/inoribea/aqc-mcp) - MCP server for AI assistants
- [Astroquery](https://astroquery.readthedocs.io/) - Astronomical data access library
- [Typer](https://typer.tiangolo.com/) - Modern CLI framework
- [Rich](https://github.com/Textualize/rich) - Beautiful terminal output
- [AAVSO](https://www.aavso.org/) - American Association of Variable Star Observers
- [Fermi Team](https://fermi.gsfc.nasa.gov/) - Fermi Gamma-ray Space Telescope