# chatbot_deepseek.py
from openai import OpenAI
import os

def get_deepseek_client():
    """初始化并返回 DeepSeek 客户端（优先从环境变量读取 API Key）"""
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        # 若未设置环境变量，也可直接在此填写你的 API Key（不推荐上传到 GitHub）
        api_key = "sk-ae6cfd4e34ea446b95b466b9d9af5b8b"
    return OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com"
    )

def chat_with_deepseek(user_input: str) -> str:
    """调用 DeepSeek 模型获取回答"""
    client = get_deepseek_client()
    response = client.chat.completions.create(
        model="deepseek-chat",  # 可切换为 deepseek-code 等其他模型
        messages=[{"role": "user", "content": user_input}],
        temperature=0.7  # 控制输出随机性，0 更保守，1 更发散
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("✅ DeepSeek Chatbot 已启动！输入 'quit' 或 'exit' 退出对话")
    while True:
        user_input = input("你：")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("👋 再见！")
            break
        try:
            reply = chat_with_deepseek(user_input)
            print(f"DeepSeek：{reply}\n")
        except Exception as e:
            print(f"❌ 调用失败：{e}\n")
