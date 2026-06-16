#!/bin/bash
# macOS 一键构建脚本
# 用法：bash build.sh
# 输出：dist/桌面语录.app

set -e

echo "📦 安装依赖..."
pip install pyinstaller akshare

echo "🔨 开始打包..."
pyinstaller 桌面语录.spec --clean

echo ""
echo "✅ 构建完成！"
echo "   输出：dist/桌面语录.app"
echo ""
echo "💡 首次运行提示："
echo "   macOS 会提示"无法验证开发者"，右键 → 打开 即可"
echo "   或在「系统设置 → 隐私与安全性」中点「仍要打开」"
