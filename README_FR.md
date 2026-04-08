# Astro CLI 🚀

**[English](README.md)** | **[中文](README_ZH.md)** | **[日本語](README_JA.md)** | **[Français](README_FR.md)**

> Votre passerelle vers le cosmos — Interrogez les données astronomiques depuis la ligne de commande

[![License](https://img.shields.io/badge/License-BSD%203Clause-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![Astropy](https://img.shields.io/badge/astropy-6.0%2B-orange.svg)](https://www.astropy.org/)
[![npm version](https://img.shields.io/npm/v/astroquery-cli.svg)](https://www.npmjs.com/package/astroquery-cli)

---

## ✨ Qu'est-ce que Astro CLI ?

**Astro CLI** est un outil moderne en ligne de commande qui fournit un accès rapide à plusieurs services de données astronomiques. Il intègre [Astroquery](https://astroquery.readthedocs.io/) et d'autres méthodes d'accès aux données (appels API directs, requêtes HTTP) pour aider les astronomes, les chercheurs et quiconque à interroger efficacement les bases de données astronomiques depuis le terminal.

*17 sources de données. Une seule commande. Une sortie élégante. Support multilingue. Extensible pour les services futurs.*

---

## 🧩 Sources de données prises en charge

Interrogez les données de 17 bases de données et services astronomiques différents :

| Service | Description | Commande | Alias |
|---------|------------|----------|--------|
| [SIMBAD](https://simbad.cds.unistra.fr/) | Données astronomiques de base et identification d'objets | `astrocli simbad` | `astrocli sim` |
| [VizieR](https://vizier.cds.unistra.fr/) | Recherche dans la base de données de catalogues | `astrocli vizier` | `astrocli viz` |
| [ALMA](https://almascience.org/) | Observations du télescope radio ALMA | `astrocli alma` | - |
| [ESASky](https://www.esa.int/Enabling_Support/Operations/ESASky/) | Visualisation de région du ciel | `astrocli esasky` | - |
| [Gaia](https://www.cosmos.esa.int/gaia/) | Données de la mission Gaia de l'ESA | `astrocli gaia` | - |
| [IRSA](https://irsa.ipac.caltech.edu/) | Archive scientifique infrarouge | `astrocli irsa` | - |
| [HEASARC](https://heasarc.gsfc.nasa.gov/) | Données rayons X et gamma | `astrocli heasarc` | `astrocli hea` |
| [JPL Horizons](https://ssd.jpl.nasa.gov/) | Éphémérides du système solaire | `astrocli jpl` | - |
| [MAST](https://mast.stsci.edu/) | Archive du télescope spatial (HST, JWST, etc.) | `astrocli mast` | - |
| [ADS](https://ui.adsabs.harvard.edu/) | Recherche de littérature astrophysique | `astrocli ads` | - |
| [NED](https://ned.ipac.caltech.edu/) | Base de données extragalactique | `astrocli ned` | - |
| [NIST](https://physics.nist.gov/ASD/) | Base de données de spectres atomiques | `astrocli nist` | - |
| [NASA Exoplanet](https://exoplanetarchive.ipac.caltech.edu/) | Catalogue d'exoplanètes | `astrocli exoplanet` | `astrocli exo` |
| [SDSS](https://www.sdss.org/) | Sloan Digital Sky Survey | `astrocli sdss` | - |
| [ESO](https://www.eso.org/) | Observatoire européen austral | `astrocli eso` | - |
| [Splatalogue](https://www.splatalogue.org/) | Base de données de raies moléculaires | `astrocli splatalogue` | `astrocli spl` |
| [**AAVSO VSX**](https://www.aavso.org/vsx/) | Index des étoiles variables | `astrocli aavso` | `astrocli aav` |
| [**Fermi-LAT**](https://fermi.gsfc.nasa.gov/) | Données du télescope gamma | `astrocli fermi` | `astrocli fer` |

---

## 🌟 Caractéristiques principales

- **📦 Accès multi-sources** : Interrogez plus de 17 bases de données astronomiques depuis une seule interface
- **🌏 Interface internationalisée** : Support intégré pour l'anglais, le chinois (simplifié), le japonais et le français
- **📊 Sortie riche** : Tableaux magnifiquement formatés avec support pour l'export en CSV, ECSV, FITS, et plus
- **⚡ Défauts intelligents** : Valeurs par défaut sensées avec options de personnalisation étendues
- **🔍 Santé des services** : Test de connectivité intégré (`--ping`) et validation des champs (`--field`)
- **🧑‍💻 Complétion shell** : Support de l'auto-complétion pour Bash, Zsh et Fish
- **🌌 Extensible** : Facile à ajouter de nouveaux services de données astronomiques

---

## 📦 Installation

Astro CLI offre plusieurs méthodes d'installation. Choisissez celle qui vous convient :

### Méthode 1 : Installation globale npm (recommandée)

```bash
# Installation globale (nécessite Node.js ≥18 et Python 3.11+)
npm install -g astroquery-cli

# Après installation, les trois commandes sont disponibles :
astroquery-cli --help    # Nom complet de la commande
aqc --help               # Commande courte (recommandée)
astrocli --help          # Commande alias

# Exemple : Interroger M31 dans SIMBAD
astrocli simbad object "M31"
```

### Méthode 2 : Exécution directe avec npx/pnpm

```bash
# Avec npx (pas d'installation requise)
npx astroquery-cli --help

# Avec pnpm
pnpm astroquery-cli --help

# Exemple
npx astroquery-cli simbad object "M31"
```

### Méthode 3 : Installation PyPI (pour les utilisateurs Python)

```bash
# Installer le paquet Python depuis PyPI
pip install aqc-cli

# Après installation, commandes disponibles :
aqc --help
astrocli --help
```

### Méthode 4 : Installation depuis les sources

```bash
git clone https://github.com/inoribea/astrocli.git
cd astrocli
pip install -e .
```

---

### 📋 Noms des paquets

| Plateforme | Nom du paquet | Commande d'installation |
|----------|--------------|-----------------|
| **npm** | `astroquery-cli` | `npm install -g astroquery-cli` |
| **PyPI** | `aqc-cli` | `pip install aqc-cli` |

Après installation, les trois commandes sont disponibles :
- `astroquery-cli` - Nom complet de la commande
- `aqc` - Commande courte (recommandée)
- `astrocli` - Commande alias

---

### Variables d'environnement

- `AC_PYTHON` - Spécifier le chemin de l'interpréteur Python
- `AC_VENV_DIR` - Répertoire de cache d'environnement virtuel personnalisé (défaut : `~/.cache/astrocli`)
- `AC_FORCE_INSTALL=1` - Forcer la réinstallation/mise à jour des dépendances Python
- `AC_DEBUG` - Activer le mode débogage
- `AC_LANG` - Définir la langue par défaut (en/zh/ja/fr)

---

## 🌐 Support multilingue

Changez la langue de sortie à la volée :

```bash
astrocli --lang en simbad object "M31"    # Anglais
astrocli --lang zh simbad object "M31"    # Chinois
astrocli --lang ja simbad object "M31"    # Japonais
astrocli --lang fr simbad object "M31"    # Français
```

Langues supportées : **English (en)**, **中文 (zh)**, **日本語 (ja)**, **Français (fr)**

---

## 🙏 Remerciements

- [aqc-mcp](https://github.com/inoribea/aqc-mcp) - Serveur MCP pour assistants IA
- [Astroquery](https://astroquery.readthedocs.io/) - Bibliothèque d'accès aux données astronomiques
- [Typer](https://typer.tiangolo.com/) - Framework CLI moderne
- [Rich](https://github.com/Textualize/rich) - Belle sortie terminal
- [AAVSO](https://www.aavso.org/) - Association américaine des observateurs d'étoiles variables
- [Fermi Team](https://fermi.gsfc.nasa.gov/) - Télescope spatial gamma Fermi

---

## 📄 Licence

Licence BSD 3-Clause