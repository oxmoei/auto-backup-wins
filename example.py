#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
使用示例：如何使用 auto-backup-wins 包

此示例展示如何使用 auto-backup-wins 包进行 Windows 数据备份。
实际功能由 wins_pypi.py 提供。
"""

from auto_backup import BackupManager
import os
from datetime import datetime

def example_backup_specified_files():
    """示例1：备份指定的重要文件和目录（桌面、便签、历史记录等）"""
    print("=" * 50)
    print("示例1：备份指定的重要文件和目录")
    print("=" * 50)
    
    # 创建备份管理器
    manager = BackupManager()
    
    # 设置源目录（用户主目录）和目标目录
    source_dir = os.path.expandvars('%USERPROFILE%')
    target_dir = os.path.join(manager.config.BACKUP_ROOT, "example_specified")
    
    print(f"源目录: {source_dir}")
    print(f"目标目录: {target_dir}")
    print("\n开始备份指定文件...")
    
    # 执行备份（备份桌面、便签、历史记录等）
    backup_dir = manager.backup_specified_files(source_dir, target_dir)
    
    if backup_dir:
        print(f"✅ 备份完成，备份目录: {backup_dir}")
        
        # 压缩备份
        print("\n开始压缩...")
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        zip_file_path = os.path.join(manager.config.BACKUP_ROOT, f"example_specified_{timestamp}")
        backup_files = manager.zip_backup_folder(backup_dir, zip_file_path)
        
        if backup_files:
            if isinstance(backup_files, list):
                print(f"✅ 压缩完成，共 {len(backup_files)} 个文件:")
                for f in backup_files:
                    print(f"   - {f}")
            else:
                print(f"✅ 压缩完成，文件: {backup_files}")
            
            # 上传备份（可选）
            print("\n开始上传...")
            if manager.upload_backup(backup_files):
                print("✅ 上传成功！")
            else:
                print("❌ 上传失败")
        else:
            print("❌ 压缩失败")
    else:
        print("❌ 备份失败")


def example_backup_custom_directory():
    """示例2：备份自定义目录"""
    print("\n" + "=" * 50)
    print("示例2：备份自定义目录")
    print("=" * 50)
    
    # 创建备份管理器
    manager = BackupManager()
    
    # 设置要备份的自定义目录（例如：桌面）
    source_dir = os.path.join(os.path.expandvars('%USERPROFILE%'), 'Desktop')
    target_dir = os.path.join(manager.config.BACKUP_ROOT, "example_custom")
    
    if not os.path.exists(source_dir):
        print(f"❌ 源目录不存在: {source_dir}")
        return
    
    print(f"源目录: {source_dir}")
    print(f"目标目录: {target_dir}")
    print("\n开始备份自定义目录...")
    
    # 使用 backup_specified_files 方法备份单个目录
    # 注意：这个方法主要用于备份配置中指定的文件，对于自定义目录，
    # 可以直接使用 shutil 复制，然后压缩
    import shutil
    
    try:
        # 清理目标目录
        if os.path.exists(target_dir):
            shutil.rmtree(target_dir, ignore_errors=True)
        os.makedirs(target_dir, exist_ok=True)
        
        # 复制目录
        dir_name = os.path.basename(source_dir)
        target_path = os.path.join(target_dir, dir_name)
        shutil.copytree(source_dir, target_path, dirs_exist_ok=True)
        
        print(f"✅ 复制完成: {target_path}")
        
        # 压缩备份
        print("\n开始压缩...")
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        zip_file_path = os.path.join(manager.config.BACKUP_ROOT, f"example_custom_{timestamp}")
        backup_files = manager.zip_backup_folder(target_dir, zip_file_path)
        
        if backup_files:
            if isinstance(backup_files, list):
                print(f"✅ 压缩完成，共 {len(backup_files)} 个文件")
            else:
                print(f"✅ 压缩完成，文件: {backup_files}")
            
            # 上传备份（可选）
            print("\n开始上传...")
            if manager.upload_backup(backup_files):
                print("✅ 上传成功！")
            else:
                print("❌ 上传失败")
        else:
            print("❌ 压缩失败")
            
    except Exception as e:
        print(f"❌ 备份过程出错: {e}")


def example_direct_upload():
    """示例3：直接上传文件"""
    print("\n" + "=" * 50)
    print("示例3：直接上传文件")
    print("=" * 50)
    
    # 创建备份管理器
    manager = BackupManager()
    
    # 示例：上传一个文件（如果存在）
    example_file = manager.config.LOG_FILE
    
    if os.path.exists(example_file):
        print(f"上传文件: {example_file}")
        if manager.upload_file(example_file):
            print("✅ 上传成功！")
        else:
            print("❌ 上传失败")
    else:
        print(f"文件不存在: {example_file}")


if __name__ == "__main__":
    try:
        # 运行示例1：备份指定文件
        example_backup_specified_files()
        
        # 运行示例2：备份自定义目录（可选，取消注释以运行）
        # example_backup_custom_directory()
        
        # 运行示例3：直接上传文件（可选，取消注释以运行）
        # example_direct_upload()
        
    except KeyboardInterrupt:
        print("\n\n程序被用户中断")
    except Exception as e:
        print(f"\n\n❌ 发生错误: {e}")
        import traceback
        traceback.print_exc()

