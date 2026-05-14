#!/usr/bin/env python3
"""生成茶禅雅集活动PDF"""
from reportlab.lib.pagesizes import portrait
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
import os

# 页面尺寸（9:16竖版）
PAGE_WIDTH = 6 * inch  # 1080px at 180dpi
PAGE_HEIGHT = 10.67 * inch  # 1920px at 180dpi

# 颜色定义
DARK_BLUE = HexColor('#1a365d')
GOLD = HexColor('#d4af37')
LIGHT_GRAY = HexColor('#f8f9fa')
WHITE = HexColor('#ffffff')

# 注册字体
pdfmetrics.registerFont(TTFont('STHeiti', '/System/Library/Fonts/STHeiti Medium.ttc'))

def create_pdf():
    """创建PDF文档"""
    output_path = "output/茶禅雅集-老友节高客服务发布会.pdf"
    os.makedirs("output", exist_ok=True)

    c = canvas.Canvas(output_path, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))

    # 生成各页面
    create_cover_page(c)
    create_overview_page(c)
    create_tea_page(c)
    create_zen_page(c)
    create_community_page(c)
    create_contact_page(c)

    c.save()
    print(f"PDF生成完成: {output_path}")

def create_cover_page(c):
    """创建封面页"""
    # 绘制背景图片
    try:
        img = Image.open("assets/images/cover.jpg")
        img_width, img_height = img.size
        ratio = min(PAGE_WIDTH / img_width, PAGE_HEIGHT / img_height)
        new_width = img_width * ratio
        new_height = img_height * ratio
        x = (PAGE_WIDTH - new_width) / 2
        y = (PAGE_HEIGHT - new_height) / 2
        c.drawImage("assets/images/cover.jpg", x, y, new_width, new_height)
    except Exception as e:
        print(f"封面图片加载失败: {e}")
        # 使用纯色背景
        c.setFillColor(DARK_BLUE)
        c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1)

    # 绘制渐变遮罩
    c.setFillColor(DARK_BLUE)
    c.setFillAlpha(0.7)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1)
    c.setFillAlpha(1)

    # 顶部徽章
    badge_width = 1.5 * inch
    badge_height = 0.4 * inch
    badge_x = (PAGE_WIDTH - badge_width) / 2
    badge_y = PAGE_HEIGHT - 1 * inch

    c.setFillColor(GOLD)
    c.roundRect(badge_x, badge_y, badge_width, badge_height, 10, fill=1)

    c.setFillColor(WHITE)
    c.setFont('STHeiti', 12)
    text_x = PAGE_WIDTH / 2
    text_y = badge_y + badge_height / 2 - 4
    c.drawCentredString(text_x, text_y, "尊享邀约")

    # 品牌标识
    c.setFillColor(GOLD)
    c.setFont('STHeiti', 14)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 2.5 * inch, "大家的家 · 隐湖云舍")

    # 主标题
    c.setFillColor(WHITE)
    c.setFont('STHeiti', 36)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 4 * inch, "茶禅雅集")

    # 副标题
    c.setFont('STHeiti', 18)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 4.8 * inch, "老友节高客服务发布会")

    # 底部信息
    c.setFillColor(WHITE)
    c.setFillAlpha(0.8)
    c.setFont('STHeiti', 12)
    c.drawCentredString(PAGE_WIDTH / 2, 1.5 * inch, "2026年5月29-30日")
    c.drawCentredString(PAGE_WIDTH / 2, 1.2 * inch, "杭州 · 西湖畔")
    c.setFillAlpha(1)

    c.showPage()

def create_overview_page(c):
    """创建活动概要页"""
    # 绘制背景图片
    try:
        c.drawImage("assets/images/abstract.jpg", 0, 0, PAGE_WIDTH, PAGE_HEIGHT)
    except Exception as e:
        print(f"概要页图片加载失败: {e}")
        c.setFillColor(LIGHT_GRAY)
        c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1)

    # 绘制遮罩
    c.setFillColor(DARK_BLUE)
    c.setFillAlpha(0.8)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1)
    c.setFillAlpha(1)

    # 标题区域
    title_bg_height = 1.5 * inch
    title_bg_y = PAGE_HEIGHT - 2 * inch

    c.setFillColor(DARK_BLUE)
    c.rect(0, title_bg_y, PAGE_WIDTH, title_bg_height, fill=1)

    # 小标题
    c.setFillColor(GOLD)
    c.setFont('STHeiti', 12)
    c.drawCentredString(PAGE_WIDTH / 2, title_bg_y + title_bg_height - 0.5 * inch, "茶韵禅意")

    # 主标题
    c.setFillColor(WHITE)
    c.setFont('STHeiti', 24)
    c.drawCentredString(PAGE_WIDTH / 2, title_bg_y + 0.3 * inch, "两天一夜沉浸式体验")

    # 描述内容
    c.setFillColor(WHITE)
    c.setFont('STHeiti', 14)

    descriptions = [
        "在西湖畔的园林中",
        "体验茶道与禅修的雅致时光",
        "",
        "尊享专属",
        "高端定制",
        "文化沉浸"
    ]

    y_position = PAGE_HEIGHT - 4 * inch
    for line in descriptions:
        if line:
            c.drawCentredString(PAGE_WIDTH / 2, y_position, line)
        y_position -= 0.4 * inch

    # 底部关键词
    c.setFillColor(GOLD)
    c.setFont('STHeiti', 12)
    keywords = "茶韵 · 禅意 · 尊享 · 沉浸"
    c.drawCentredString(PAGE_WIDTH / 2, 1.5 * inch, keywords)

    c.showPage()

def create_tea_page(c):
    """创建茶韵体验页"""
    # 绘制背景图片
    try:
        c.drawImage("assets/images/tea.jpg", 0, 0, PAGE_WIDTH, PAGE_HEIGHT)
    except Exception as e:
        print(f"茶韵页图片加载失败: {e}")
        c.setFillColor(LIGHT_GRAY)
        c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1)

    # 绘制遮罩
    c.setFillColor(DARK_BLUE)
    c.setFillAlpha(0.6)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1)
    c.setFillAlpha(1)

    # 标题区域
    title_bg_height = 1.5 * inch
    title_bg_y = PAGE_HEIGHT - 2 * inch

    c.setFillColor(DARK_BLUE)
    c.rect(0, title_bg_y, PAGE_WIDTH, title_bg_height, fill=1)

    # 小标题
    c.setFillColor(GOLD)
    c.setFont('STHeiti', 12)
    c.drawCentredString(PAGE_WIDTH / 2, title_bg_y + title_bg_height - 0.5 * inch, "第一日 · 茶")

    # 主标题
    c.setFillColor(WHITE)
    c.setFont('STHeiti', 24)
    c.drawCentredString(PAGE_WIDTH / 2, title_bg_y + 0.3 * inch, "尊享茶道体验")

    # 描述内容
    c.setFillColor(WHITE)
    c.setFont('STHeiti', 14)

    descriptions = [
        "宋韵点茶",
        "田园雅趣",
        "西湖春茶",
        "",
        "在茶园中感受自然",
        "在茶香中品味人生"
    ]

    y_position = PAGE_HEIGHT - 4 * inch
    for line in descriptions:
        if line:
            c.drawCentredString(PAGE_WIDTH / 2, y_position, line)
        y_position -= 0.4 * inch

    # 底部关键词
    c.setFillColor(GOLD)
    c.setFont('STHeiti', 12)
    keywords = "茶韵 · 雅趣 · 自然 · 品味"
    c.drawCentredString(PAGE_WIDTH / 2, 1.5 * inch, keywords)

    c.showPage()

def create_zen_page(c):
    """创建禅意时光页"""
    # TODO: 实现禅意时光页
    c.showPage()

def create_community_page(c):
    """创建品牌介绍页"""
    # TODO: 实现品牌介绍页
    c.showPage()

def create_contact_page(c):
    """创建报名咨询页"""
    # TODO: 实现报名咨询页
    c.showPage()

if __name__ == "__main__":
    create_pdf()