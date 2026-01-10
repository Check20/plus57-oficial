import telebot

# SECURITY: Real token is hidden for GitHub safety
TOKEN = "YOUR_BOT_TOKEN_HERE"
CONTRATO = "0xc9b356b1dbf3750f5ec401c9ce2c2746d79391ee"
bot = telebot.TeleBot(TOKEN)

print("--- +57 ECOSYSTEM ONLINE ---")

@bot.message_handler(commands=['start'])
def welcome(message):
    text = (
        "💎 *Welcome to the +57 Ecosystem*\n\n"
        "Total Supply: *7,000,000 +57*\n\n"
        "🚀 Send your Polygon wallet address to register.\n"
        "Use /contract for info."
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(commands=['contract'])
def send_contract(message):
    text = (
        "📄 *+57 Contract*\n\n"
        f"Address: \`{CONTRATO}\`\n\n"
        f"🔗 [View on Polygonscan](https://polygonscan.com/address/{CONTRATO})"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(func=lambda m: True)
def save_wallet(message):
    wallet = message.text.strip()
    if wallet.startswith("0x") and len(wallet) == 42:
        with open("wallets.txt", "a") as f:
            user = message.from_user.username if message.from_user.username else "No_User"
            f.write(f"User: @{user} | Wallet: {wallet}\n")
        bot.reply_to(message, "✅ *Wallet registered!*", parse_mode="Markdown")
    else:
        bot.reply_to(message, "❌ Invalid wallet. Must start with 0x.")

bot.infinity_polling()
