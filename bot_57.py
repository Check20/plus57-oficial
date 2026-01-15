from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# CONFIGURACIÓN
TOKEN = "TU_TOKEN_DE_BOTFATHER_AQUI"
CONTRATO = "0xc9b356b1dBf3750F5EC401c9cE2C2746d79391eE"
GECKO_LINK = "https://www.geckoterminal.com/polygon_pos/pools/0x1e9bb388367342336c0763a1a8d27adcdc92e61b"
QUICKSWAP_LINK = f"https://quickswap.exchange/#/swap?outputCurrency={CONTRATO}&chain=polygon"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    # Solución al error de "Nombre de usuario no encontrado"
    nombre = user.username if user.username else user.first_name
    
    texto = (
        f"¡Hola {nombre}! 🚀 Bienvenido al bot oficial de **+57** 🇨🇴\n\n"
        f"El token que representa a la comunidad colombiana en #Polygon.\n\n"
        f"📈 **Estado actual:**\n"
        f"• Holders: +85\n"
        f"• Red: Polygon (EVM)\n"
        f"• Liquidez: ¡QUEMADA! 🔥\n\n"
        "Selecciona una opción abajo:"
    )

    keyboard = [
        [InlineKeyboardButton("📈 Ver Gráfica (GeckoTerminal)", url=GECKO_LINK)],
        [InlineKeyboardButton("🛒 Comprar en QuickSwap", url=QUICKSWAP_LINK)],
        [InlineKeyboardButton("🛡️ Ver Contrato", url=f"https://polygonscan.com/token/{CONTRATO}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(texto, reply_markup=reply_markup, parse_mode='Markdown')

if __name__ == '__main__':
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    print("Bot +57 en marcha...")
    application.run_polling()
