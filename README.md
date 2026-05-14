# 茶禅雅集 · 老友节高客服务发布会

## 项目概述

本项目用于"茶禅雅集 · 老友节高客服务发布会"活动的宣传和策划，包含活动宣传网页、PDF生成脚本和活动策划文档。

## 活动信息

- **活动名称**：茶禅雅集 · 老友节高客服务发布会
- **活动时间**：2026年5月29-30日（两天一夜）
- **活动地点**：大家的家·隐湖云舍旅居社区（杭州西湖区龙井路）
- **活动人数**：20人尊享
- **活动对象**：温州农行渠道高端客户

## 文件结构

```
├── activity-showcase.html          # 活动宣传网页（主页面）
├── index.html                      # 跳转页面（自动跳转到activity-showcase.html）
├── generate_pdf.py                 # PDF生成脚本
├── download_images.py              # 图片下载脚本
├── requirements.txt                # Python依赖
├── assets/
│   ├── images/                     # 图片素材
│   │   ├── new/                    # 从网上搜集的高清大图
│   │   └── pdf_extract/            # 从原PDF提取的图片（备用）
│   └── fonts/                      # 字体文件
├── output/                         # 生成的PDF文件
├── docs/
│   └── superpowers/
│       ├── specs/                  # 设计规格文档
│       └── plans/                  # 实施计划文档
└── *.docx                          # 活动策划文档
```

## 快速开始

### 查看活动宣传网页

直接在浏览器中打开 `activity-showcase.html` 文件，或访问 GitHub Pages：

https://bestwishes-cc.github.io/view/

### 生成PDF文件

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行PDF生成脚本：
```bash
python generate_pdf.py
```

3. 生成的PDF文件位于 `output/茶禅雅集-老友节高客服务发布会.pdf`

## 设计风格

- **主色调**：深蓝 #1a365d、金色 #d4af37、米白 #f8f9fa
- **字体**：思源宋体（Noto Serif SC）、思源黑体（Noto Sans SC）
- **设计元素**：水墨风格、粒子效果、视差滚动、印章动画
- **内容策略**：氛围营造为主，不透露具体流程细节

## 注意事项

1. **合规要求**：避免使用"问禅"字样，使用"茶禅雅集"作为主标题
2. **内容策略**：保持概括性，便于后续行程微调
3. **图片素材**：优先使用从网上搜集的高清大图（assets/images/new/）
4. **目标用户**：年长用户，文字清晰易读

## 部署说明

活动宣传网页已部署到 GitHub Pages：

- **仓库地址**：https://github.com/bestwishes-cc/view
- **访问地址**：https://bestwishes-cc.github.io/view/
- **更新方式**：修改 HTML 文件后，git commit + push 到 main 分支，GitHub Pages 自动部署

## 相关文档

- [活动待确认事项清单](杭州隐湖云舍·灵隐问禅——老友节高客活动待确认事项清单.md)
- [竖版PDF设计规格](docs/superpowers/specs/2026-05-14-茶禅雅集-竖版PDF设计.md)
- [竖版PDF实施计划](docs/superpowers/plans/2026-05-14-茶禅雅集-竖版PDF实施计划.md)

## 更新日志

### 2026-05-14
- 创建活动宣传网页（水墨风格）
- 优化字体大小和背景图对比度，适合年长用户阅读
- 部署到 GitHub Pages
- 创建 PDF 生成脚本
- 建立系统化工作流程规则