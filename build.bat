@echo off
REM Windows 一键构建脚本
REM 用法：双击运行，或在命令行执行 build.bat
REM 输出：dist\桌面语录.exe

echo 📦 安装依赖...
pip install pyinstaller akshare

echo 🔨 开始打包...
pyinstaller 桌面语录.spec --clean

echo.
echo ✅ 构建完成！
echo    输出：dist\桌面语录.exe
echo.
echo 💡 首次运行提示：
echo    Windows SmartScreen 可能弹出警告，点「更多信息」→「仍要运行」即可
pause
