# Astro CLI 🚀

**[English](README.md)** | **[中文](README_ZH.md)** | **[日本語](README_JA.md)** | **[Français](README_FR.md)**

> 你的宇宙之门 — 从命令行查询天文数据

[![License](https://img.shields.io/badge/License-BSD%203Clause-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![Astropy](https://img.shields.io/badge/astropy-6.0%2B-orange.svg)](https://www.astropy.org/)
[![npm version](https://img.shields.io/npm/v/astroquery-cli.svg)](https://www.npmjs.com/package/astroquery-cli)

---

## ✨ 什么是 Astro CLI？

**Astro CLI** 是一个现代命令行工具，提供对多个天文数据服务的快速访问。它集成了 [Astroquery](https://astroquery.readthedocs.io/) 和其他数据访问方法（直接 API 调用、HTTP 请求），帮助天文学家、研究人员以及任何人从终端高效查询天文数据库。

*17个数据源。一个命令。精美输出。多语言支持。可扩展至未来服务。*

---

## 🧩 支持的数据源

从17个不同的天文数据库和服务查询数据：

| 服务 | 描述 | 命令 | 别名 |
|---------|------------|----------|--------|
| [SIMBAD](https://simbad.cds.unistra.fr/) | 基础天文数据与天体识别 | `astrocli simbad` | `astrocli sim` |
| [VizieR](https://vizier.cds.unistra.fr/) | 星表数据库搜索 | `astrocli vizier` | `astrocli viz` |
| [ALMA](https://almascience.org/) | ALMA 射电望远镜观测 | `astrocli alma` | - |
| [ESASky](https://www.esa.int/Enabling_Support/Operations/ESASky/) | 天区可视化 | `astrocli esasky` | - |
| [Gaia](https://www.cosmos.esa.int/gaia/) | ESA Gaia 任务数据 | `astrocli gaia` | - |
| [IRSA](https://irsa.ipac.caltech.edu/) | 红外科学档案 | `astrocli irsa` | - |
| [HEASARC](https://heasarc.gsfc.nasa.gov/) | X射线和伽马射线数据 | `astrocli heasarc` | `astrocli hea` |
| [JPL Horizons](https://ssd.jpl.nasa.gov/) | 太阳系星历表 | `astrocli jpl` | - |
| [MAST](https://mast.stsci.edu/) | 太空望远镜档案 (HST, JWST 等) | `astrocli mast` | - |
| [ADS](https://ui.adsabs.harvard.edu/) | 天体物理学文献搜索 | `astrocli ads` | - |
| [NED](https://ned.ipac.caltech.edu/) | 河外星系数据库 | `astrocli ned` | - |
| [NIST](https://physics.nist.gov/ASD/) | 原子光谱数据库 | `astrocli nist` | - |
| [NASA Exoplanet](https://exoplanetarchive.ipac.caltech.edu/) | 系外行星目录 | `astrocli exoplanet` | `astrocli exo` |
| [SDSS](https://www.sdss.org/) | 斯隆数字巡天 | `astrocli sdss` | - |
| [ESO](https://www.eso.org/) | 欧洲南方天文台 | `astrocli eso` | - |
| [Splatalogue](https://www.splatalogue.org/) | 分子谱线数据库 | `astrocli splatalogue` | `astrocli spl` |
| [**AAVSO VSX**](https://www.aavso.org/vsx/) | 变星索引 | `astrocli aavso` | `astrocli aav` |
| [**Fermi-LAT**](https://fermi.gsfc.nasa.gov/) | 伽马射线望远镜数据 | `astrocli fermi` | `astrocli fer` |

---

## 🌟 主要特性

- **📦 多源访问**：从单一界面查询17+个天文数据库
- **🌏 国际化界面**：内置支持英语、中文（简体）、日语和法语
- **📊 丰富输出**：精美格式化的表格，支持导出为 CSV、ECSV、FITS 等格式
- **⚡ 智能默认值**：合理的默认值和丰富的自定义选项
- **🔍 服务健康检查**：内置连接测试 (`--ping`) 和字段验证 (`--field`)
- **🧑‍💻 Shell 自动补全**：支持 Bash、Zsh 和 Fish 的自动补全
- **🌌 可扩展**：易于添加新的天文数据服务

---

## 📦 安装

Astro CLI 提供多种安装方式。选择适合你的方式：

### 方式一：npm 全局安装（推荐）

```bash
# 全局安装（需要 Node.js ≥18 和 Python 3.11+）
npm install -g astroquery-cli

# 安装后可使用以下任一命令：
astroquery-cli --help    # 完整命令名
aqc --help               # 短命令（推荐）
astrocli --help          # 别名命令

# 示例：查询 SIMBAD 中的 M31
astrocli simbad object "M31"
```

### 方式二：npx/pnpm 直接运行

```bash
# 使用 npx（无需安装）
npx astroquery-cli --help

# 使用 pnpm
pnpm astroquery-cli --help

# 示例
npx astroquery-cli simbad object "M31"
```

### 方式三：PyPI 安装（Python 用户）

```bash
# 从 PyPI 安装 Python 包
pip install aqc-cli

# 安装后可使用命令：
aqc --help
astrocli --help
```

### 方式四：从源码安装

```bash
git clone https://github.com/inoribea/astrocli.git
cd astrocli
pip install -e .
```

---

### 📋 包名说明

| 平台 | 包名 | 安装命令 |
|----------|--------------|-----------------|
| **npm** | `astroquery-cli` | `npm install -g astroquery-cli` |
| **PyPI** | `aqc-cli` | `pip install aqc-cli` |

安装后，三个命令均可使用：
- `astroquery-cli` - 完整命令名
- `aqc` - 短命令（推荐）
- `astrocli` - 别名命令

---

### 环境变量

- `AC_PYTHON` - 指定 Python 解释器路径
- `AC_VENV_DIR` - 自定义虚拟环境缓存目录（默认：`~/.cache/astrocli`）
- `AC_FORCE_INSTALL=1` - 强制重新安装/升级 Python 依赖
- `AC_DEBUG` - 启用调试模式
- `AC_LANG` - 设置默认语言（en/zh/ja/fr）

---

## 📚 使用方法

### 查看所有可用命令

```bash
# 显示所有可用模块和命令
astrocli --help

# 显示特定模块的帮助
astrocli <module> --help
```

### 查询示例

#### 1. 查询 SIMBAD 天体

```bash
astrocli simbad object "M31"
astrocli simbad object "Crab Nebula" --show-all-cols
```

#### 2. 搜索 VizieR 星表

```bash
# 按关键词查找星表
astrocli vizier find-catalogs --keyword photometry --keyword galaxy

# 查询特定星表
astrocli vizier object "M31" --radius 0.1 --catalog "I/261/gaiadr3"
```

#### 3. 查询 AAVSO 变星索引（新功能！）

```bash
# 按名称查询变星
astrocli aavso object "SS Cyg"

# 在天区中搜索变星
astrocli aavso region 196.421 18.018 --radius 0.5

# 以 JSON 格式获取结果
astrocli aavso object "T CrB" --format json
```

#### 4. 查询 Fermi-LAT 数据（新功能！）

```bash
# 查询目标的 Fermi 数据
astrocli fermi object "Crab Nebula" --energy "1000,100000" --dates "2020-01-01 00:00:00, 2020-01-02 00:00:00"

# 清除 Fermi 缓存
astrocli fermi clear-cache
```

#### 5. 搜索 ADS 文献

```bash
astrocli ads search --title "exoplanet detection"
astrocli ads bibcode "2023A&A...555..959W"
```

---

## 🌐 多语言支持

即时切换输出语言：

```bash
astrocli --lang en simbad object "M31"    # 英语
astrocli --lang zh simbad object "M31"    # 中文
astrocli --lang ja simbad object "M31"    # 日语
astrocli --lang fr simbad object "M31"    # 法语
```

支持的语言：**English (en)**、**中文 (zh)**、**日本語 (ja)**、**Français (fr)**

---

## 🔧 全局选项

| 选项 | 描述 |
|--------|-------------|
| `-l, --lang` | 设置输出语言（en/zh/ja/fr） |
| `-p, --ping` | 测试所有服务的连接性（仅顶层） |
| `-f, --field` | 检查模块的可用字段（仅顶层） |
| `-d, --debug` | 启用调试模式和详细输出 |
| `-v, --verbose` | 启用详细输出 |

---

## 🧑‍💻 Shell 自动补全

为你的 shell 安装补全：

```bash
astrocli --install-completion bash   # Bash
astrocli --install-completion zsh    # Zsh
astrocli --install-completion fish   # Fish
```

将此添加到你的 shell 配置（例如 `~/.zshrc`）：

```bash
# 对于 zsh
eval "$(astrocli --install-completion zsh)"

# 对于 bash
eval "$(astrocli --install-completion bash)"
```

---

## 📊 输出与导出

将查询结果保存到文件：

```bash
astrocli simbad object "M31" --output-file results.csv

# 明确指定格式
astrocli simbad object "M31" --output-file data.ecsv --output-format ecsv
```

支持的格式：`csv`、`ecsv`、`fits`、`votable`、`html`、`latex`、`ascii`

---

## 🔍 测试服务连接性

检查所有数据服务是否可访问：

```bash
astrocli --ping
```

---

## 🛠️ 开发

### 项目结构

```
astrocli/
├── src/                    # 源代码（从 astroquery_cli 重命名）
│   ├── modules/           # 服务特定模块
│   │   ├── simbad_cli.py
│   │   ├── vizier_cli.py
│   │   ├── aavso_cli.py      # AAVSO VSX
│   │   ├── fermi_cli.py      # Fermi-LAT
│   │   └── ...
│   ├── utils.py            # 通用工具
│   ├── common_options.py   # 共享 CLI 选项
│   ├── i18n.py            # 国际化
│   └── main.py            # CLI 入口点
├── locales/                # 翻译文件
│   ├── en/LC_MESSAGES/     # 英语
│   ├── zh/LC_MESSAGES/     # 中文
│   ├── ja/LC_MESSAGES/     # 日语
│   └── fr/LC_MESSAGES/     # 法语
├── package.json           # npm/npx 配置
├── pyproject.toml         # Python 包配置
└── README.md
```

### 添加新模块

1. 按照现有模式创建 `modules/<service>_cli.py`
2. 在 `main.py` 的 `setup_subcommands()` 中导入
3. 添加到 README 模块列表
4. 在 `locales/` 目录中添加翻译

---

## 📄 许可证

BSD 3-Clause 许可证

---

## 🙏 致谢

- [aqc-mcp](https://github.com/inoribea/aqc-mcp) - AI 助手的 MCP 服务器
- [Astroquery](https://astroquery.readthedocs.io/) - 天文数据访问库
- [Typer](https://typer.tiangolo.com/) - 现代 CLI 框架
- [Rich](https://github.com/Textualize/rich) - 精美的终端输出
- [AAVSO](https://www.aavso.org/) - 美国变星观测者协会
- [Fermi Team](https://fermi.gsfc.nasa.gov/) - Fermi 伽马射线太空望远镜

---

## 📝 常见问题

<details>
<summary><b>常见问题</b></summary>

### 我可以在没有 Node.js 的情况下使用吗？

可以！从源码安装：`pip install -e .` 或在安装依赖后直接使用 Python。

### 如何添加新的数据服务？

参见上面的 [开发](#-开发) 部分。Astroquery 中的大多数服务都可以用类似的模式封装。

### 为什么有些模块说"未完全实现"？

某些高级功能或边缘情况可能还没有完整的 CLI 覆盖。核心查询功能可以工作，但特殊参数可能需要直接访问底层的 astroquery 库。

### 这个和 astroquery 有什么区别？

**Astro CLI** 是 Astroquery 的命令行界面。把它想象成一个用户友好的封装，让常见任务更容易。它不会取代 Astroquery — 它增强了它！

</details>