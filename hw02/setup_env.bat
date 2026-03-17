@echo off
echo ========================================
echo  正在创建 Python 虚拟环境...
echo ========================================
python -m venv venv
if errorlevel 1 (
    echo ❌ 创建虚拟环境失败，请检查 Python 是否安装并添加到 PATH
    pause
    exit /b 1
)

echo ========================================
echo  激活虚拟环境并安装依赖...
echo ========================================
call venv\Scripts\activate
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ 依赖安装失败
    pause
    exit /b 1
)

echo ========================================
echo  ✅ 环境配置完成！
echo  接下来你可以运行：python chatbot_deepseek.py
echo ========================================
echo.
pause
