import os from telegram import Update from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN = os.getenv("BOT_TOKEN")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): await update.message.reply_text("سلام! ربات فعال است.")
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE): await update.message.reply_text("پیام شما دریافت شد.")
def main(): app = Application.builder().token(TOKEN).build() app.add_handler(CommandHandler("start", start)) app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo)) print("ربات شروع به کار کرد...") app.run_polling()
if name == "main": main()
