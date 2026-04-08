# Astro CLI 🚀

**[English](README.md)** | **[中文](README_ZH.md)** | **[日本語](README_JA.md)** | **[Français](README_FR.md)**

> 宇宙へのゲートウェイ — コマンドラインから天文データを照会

[![License](https://img.shields.io/badge/License-BSD%203Clause-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![Astropy](https://img.shields.io/badge/astropy-6.0%2B-orange.svg)](https://www.astropy.org/)
[![npm version](https://img.shields.io/npm/v/astroquery-cli.svg)](https://www.npmjs.com/package/astroquery-cli)

---

## ✨ Astro CLI とは？

**Astro CLI** は、複数の天文データサービスへの迅速なアクセスを提供するモダンなコマンドラインツールです。[Astroquery](https://astroquery.readthedocs.io/) と他のデータアクセス方法（直接API呼び出し、HTTPリクエスト）を統合し、天文学者、研究者、および誰でもターミナルから効率的に天文データベースを照会できるようにします。

*17のデータソース。1つのコマンド。美しい出力。多言語サポート。将来のサービスに拡張可能。*

---

## 🧩 サポートされるデータソース

17の異なる天文データベースとサービスからデータを照会：

| サービス | 説明 | コマンド | エイリアス |
|---------|------------|----------|--------|
| [SIMBAD](https://simbad.cds.unistra.fr/) | 基礎天文データと天体識別 | `astrocli simbad` | `astrocli sim` |
| [VizieR](https://vizier.cds.unistra.fr/) | カタログデータベース検索 | `astrocli vizier` | `astrocli viz` |
| [ALMA](https://almascience.org/) | ALMA電波望遠鏡観測 | `astrocli alma` | - |
| [ESASky](https://www.esa.int/Enabling_Support/Operations/ESASky/) | 天域可視化 | `astrocli esasky` | - |
| [Gaia](https://www.cosmos.esa.int/gaia/) | ESA Gaiaミッションデータ | `astrocli gaia` | - |
| [IRSA](https://irsa.ipac.caltech.edu/) | 赤外線科学アーカイブ | `astrocli irsa` | - |
| [HEASARC](https://heasarc.gsfc.nasa.gov/) | X線とガンマ線データ | `astrocli heasarc` | `astrocli hea` |
| [JPL Horizons](https://ssd.jpl.nasa.gov/) | 太陽系暦 | `astrocli jpl` | - |
| [MAST](https://mast.stsci.edu/) | 宇宙望遠鏡アーカイブ (HST, JWST等) | `astrocli mast` | - |
| [ADS](https://ui.adsabs.harvard.edu/) | 天体物理学文献検索 | `astrocli ads` | - |
| [NED](https://ned.ipac.caltech.edu/) | 銀河外データベース | `astrocli ned` | - |
| [NIST](https://physics.nist.gov/ASD/) | 原子スペクトルデータベース | `astrocli nist` | - |
| [NASA Exoplanet](https://exoplanetarchive.ipac.caltech.edu/) | 系外惑星カタログ | `astrocli exoplanet` | `astrocli exo` |
| [SDSS](https://www.sdss.org/) | スローン・デジタル・スカイ・サーベイ | `astrocli sdss` | - |
| [ESO](https://www.eso.org/) | 欧州南天天文台 | `astrocli eso` | - |
| [Splatalogue](https://www.splatalogue.org/) | 分子線データベース | `astrocli splatalogue` | `astrocli spl` |
| [**AAVSO VSX**](https://www.aavso.org/vsx/) | 変光星インデックス | `astrocli aavso` | `astrocli aav` |
| [**Fermi-LAT**](https://fermi.gsfc.nasa.gov/) | ガンマ線望遠鏡データ | `astrocli fermi` | `astrocli fer` |

---

## 🌟 主な機能

- **📦 マルチソースアクセス**: 単一インターフェースから17以上の天文データベースを照会
- **🌏 国際化UI**: 英語、中国語（簡体字）、日本語、フランス語の組み込みサポート
- **📊 豊富な出力**: CSV、ECSV、FITSなどへのエクスポートをサポートする美しくフォーマットされたテーブル
- **⚡ スマートなデフォルト**: 合理的なデフォルトと広範なカスタマイズオプション
- **🔍 サービスヘルス**: 組み込みの接続テスト（`--ping`）とフィールド検証（`--field`）
- **🧑‍💻 シェル補完**: Bash、Zsh、Fishの自動補完サポート
- **🌌 拡張可能**: 新しい天文データサービスを簡単に追加

---

## 📦 インストール

Astro CLIは複数のインストール方法を提供します。あなたに合った方法を選択してください：

### 方法1：npmグローバルインストール（推奨）

```bash
# グローバルインストール（Node.js ≥18 と Python 3.11+ が必要）
npm install -g astroquery-cli

# インストール後、以下の3つのコマンドが利用可能：
astroquery-cli --help    # 完全なコマンド名
aqc --help               # 短いコマンド（推奨）
astrocli --help          # エイリアスコマンド

# 例：SIMBADでM31を照会
astrocli simbad object "M31"
```

### 方法2：npx/pnpm直接実行

```bash
# npxを使用（インストール不要）
npx astroquery-cli --help

# pnpmを使用
pnpm astroquery-cli --help

# 例
npx astroquery-cli simbad object "M31"
```

### 方法3：PyPIインストール（Pythonユーザー向け）

```bash
# PyPIからPythonパッケージをインストール
pip install aqc-cli

# インストール後、利用可能なコマンド：
aqc --help
astrocli --help
```

### 方法4：ソースからインストール

```bash
git clone https://github.com/inoribea/astrocli.git
cd astrocli
pip install -e .
```

---

### 📋 パッケージ名

| プラットフォーム | パッケージ名 | インストールコマンド |
|----------|--------------|-----------------|
| **npm** | `astroquery-cli` | `npm install -g astroquery-cli` |
| **PyPI** | `aqc-cli` | `pip install aqc-cli` |

インストール後、3つのコマンドがすべて利用可能：
- `astroquery-cli` - 完全なコマンド名
- `aqc` - 短いコマンド（推奨）
- `astrocli` - エイリアスコマンド

---

### 環境変数

- `AC_PYTHON` - Pythonインタープリタパスを指定
- `AC_VENV_DIR` - カスタム仮想環境キャッシュディレクトリ（デフォルト：`~/.cache/astrocli`）
- `AC_FORCE_INSTALL=1` - Python依存関係の強制再インストール/アップグレード
- `AC_DEBUG` - デバッグモードを有効化
- `AC_LANG` - デフォルト言語を設定（en/zh/ja/fr）

---

## 🌐 多言語サポート

出力言語を即座に切り替え：

```bash
astrocli --lang en simbad object "M31"    # 英語
astrocli --lang zh simbad object "M31"    # 中国語
astrocli --lang ja simbad object "M31"    # 日本語
astrocli --lang fr simbad object "M31"    # フランス語
```

サポートされる言語：**English (en)**、**中文 (zh)**、**日本語 (ja)**、**Français (fr)**

---

## 🙏 謝辞

- [aqc-mcp](https://github.com/inoribea/aqc-mcp) - AIアシスタント用MCPサーバー
- [Astroquery](https://astroquery.readthedocs.io/) - 天文データアクセスライブラリ
- [Typer](https://typer.tiangolo.com/) - モダンCLIフレームワーク
- [Rich](https://github.com/Textualize/rich) - 美しいターミナル出力
- [AAVSO](https://www.aavso.org/) - アメリカ変光星観測者協会
- [Fermi Team](https://fermi.gsfc.nasa.gov/) - フェルミガンマ線宇宙望遠鏡

---

## 📄 ライセンス

BSD 3-Clauseライセンス