# 2025/6/18 17:52
# -*- coding:UTF-8 -*-
import os
import shutil

# 原始文件路径
source_file = r"E:\FeishuDownload\100\简单文字.docx"  # 假设是.docx文件，如果是.doc请修改

# 目标目录（确保目录存在）
target_dir = r"E:\FeishuDownload\100目录"
os.makedirs(target_dir, exist_ok=True)

# 生成100个副本
for i in range(1, 101):
    new_filename = f"简单文字{i}.docx"  # 修改扩展名以匹配原始文件
    target_path = os.path.join(target_dir, new_filename)

    # 复制文件
    shutil.copy2(source_file, target_path)
    print(f"已创建: {target_path}")

print("文件复制完成！共创建100个副本。")