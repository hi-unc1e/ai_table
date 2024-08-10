#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
from pathlib import Path

# 指定要遍历的目录路径
directory_path = '/Users/dpdu/Desktop/opt/spreadsheet_ai_app/src'  # 请替换为您的目录路径

# 遍历目录
for root, dirs, files in os.walk(directory_path):
    for file in files:
        # 检查文件是否以.py结尾
        if file.endswith('.py'):
            # 构建完整的文件路径
            file_path = os.path.join(root, file)

            # 打开文件并读取内容
            code = Path(file_path).read_text()
            # 输出文件名和内容
            print(f'------{file_path}-----\n{code}\n')
