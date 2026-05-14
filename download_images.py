#!/usr/bin/env python3
"""下载和提取图片素材"""
import os
import fitz  # PyMuPDF
from pathlib import Path

# 创建目录
Path("assets/images").mkdir(parents=True, exist_ok=True)

# 原PDF文件路径
pdf_path = "杭州隐湖云舍旅居社区二季度险端赋能方案.pdf"

def extract_images_from_pdf():
    """从PDF提取所有图片"""
    print(f"正在从 {pdf_path} 提取图片...")

    doc = fitz.open(pdf_path)
    image_count = 0

    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images()

        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            # 保存图片
            filename = f"pdf_extract_{page_num+1}_{img_index+1}.{image_ext}"
            filepath = f"assets/images/{filename}"

            with open(filepath, "wb") as f:
                f.write(image_bytes)

            image_count += 1
            print(f"  -> 提取: {filename} ({len(image_bytes)} bytes)")

    doc.close()
    print(f"提取完成，共 {image_count} 张图片")
    return image_count

def list_extracted_images():
    """列出提取的图片"""
    images_dir = Path("assets/images")
    if not images_dir.exists():
        print("assets/images 目录不存在")
        return

    images = list(images_dir.glob("pdf_extract_*"))
    if not images:
        print("没有找到提取的图片")
        return

    print(f"找到 {len(images)} 张提取的图片:")
    for img in sorted(images):
        size = img.stat().st_size
        print(f"  {img.name} ({size:,} bytes)")

if __name__ == "__main__":
    # 检查PDF是否存在
    if not os.path.exists(pdf_path):
        print(f"错误: 找不到PDF文件 {pdf_path}")
        exit(1)

    # 提取图片
    extract_images_from_pdf()

    # 列出提取的图片
    print()
    list_extracted_images()
