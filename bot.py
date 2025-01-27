import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import requests

# ===== SETTINGS =====
TELEGRAM_TOKEN = "7154080701:AAEG_87V_B0BJwJBAIynW4LBWN6UEsXzdlk"  # From BotFather
DEEPSEEK_API_KEY = "sk-5a3f000c34f341c18240033afdf3ff26"  # From DeepSeek
# =====================

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    
    # Prepare request to DeepSeek
    headers = {"Authorization": f"Bearer {sk-5a3f000c34f341c18240033afdf3ff26}"}
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": user_message}]
    }
    
    try:
        response = requests.post("https://api.deepseek.com/v1/chat/completions", json=data, headers=headers)
        ai_response = response.json()['choices'][0]['message']['content']
    except Exception as e:
        ai_response = f"Oops! Error: {str(e)}"
    
    await update.message.reply_text(ai_response)

# Start the bot
app = Application.builder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
print("Bot is running...")
app.run_polling()