#2025/6/4 10:17
# -*- coding:UTF-8 -*-
import os
dangqianmulu = os.getcwd()
print(dangqianmulu)

relpath1 = os.path.relpath(__file__, dangqianmulu)
print(relpath1)

script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)

relative_to_script = os.path.relpath(__file__, script_dir)
print(f"相对于脚本目录的路径: {relative_to_script}")

# 获取当前文件所在目录
file_dir = os.path.dirname(os.path.abspath(__file__))

# 获取相对于某基目录的路径（例如项目根目录）
base_dir = "/path/to/your/project"  # 替换为你的项目根目录
relative_path = os.path.relpath(file_dir, base_dir)
print(f"相对于项目根目录的路径: {relative_path}")