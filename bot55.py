from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Define your bot token here
BOT_TOKEN = '7403190402:AAHUSNtMy4DAprY_I2FAzWc4nnHmaTNJ89E'

# Define your copied content
POST_TEXT_1 = "Murodbek Alimbekov\'s education history: \n\n  2013-2022- Studied at School №10, Khavas; \n\n  2022-2024- Graduated high school at Specialized Boarding School №1 of Gulistan City; \n\n  Completed Web development course with UDEMY, CODECADEMY, freeCodeCamp; \n\n   Accepted to 10 universities in the USA, 2 universities in Australia, 3 (FOR NOW) universities in Uzbekistan, one in the UAE; \n\n  Student of New Uzbekistan University."
POST_TEXT_2 = "In the US:\n\nPenn State University\nUMass Boston\nIowa State University\nWestern New England University\nPace University\nSuffolk University\nThe University of Arizona\nArizona State University\n\nIn Australia:\n\nMacquarie University\nRMIT University\n\nIn the UAE:\n\nBirmingham University in Dubai\n\nIn Uzbekistan:\n\nNew Uzbekistan University\nWestminister International University of Tashkent\n\nDirect Link to Admission Letters:\n @accepted_universities"
POST_TEXT_3 = "Test Scores:\n\nSAT-1250\nIELTS-6.5\nWeb Development Course certification\n\nDirect link to the Certificates:\n@accepted_universities"
POST_TEXT_4 = "Telegram Channel: @be_leader_CEO\nInstagram: instagram.com/murod_alimbekov\nLinkedin: https://www.linkedin.com/in/murodbek-alimbekov-0b20802b2?utm_source=share&ut\nChess.com Username: murod_alimbekov\nYou Tube: www.youtube.com/@be_pro_dev"

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Create multiple buttons
    button1 = KeyboardButton('Education')
    button2 = KeyboardButton('Accepted Universities')
    button3 = KeyboardButton('Certificates')
    button4 = KeyboardButton('Social Interactions')
    
    # Create a keyboard layout with multiple buttons
    keyboard = [
        [button1, button2], 
        [button3, button4]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=False, resize_keyboard=True)
    
    # Send a message with the keyboard
    await update.message.reply_text('Assalomu Alaykum!\n Thanks for your attention. \n Please, use the buttons below:', reply_markup=reply_markup)

# Message handler for button clicks
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Get the text of the incoming message
    text = update.message.text
    
    # Check which button was clicked and respond accordingly
    if text == 'Education':
        await update.message.reply_text(POST_TEXT_1)
    elif text == 'Accepted Universities':
        await update.message.reply_text(POST_TEXT_2)
    elif text == 'Certificates':
        await update.message.reply_text(POST_TEXT_3)
    elif text == 'Social Interactions':
        await update.message.reply_text(POST_TEXT_4)
    else:
        # Handle unexpected messages or commands
        await update.message.reply_text('Use the buttons to get more information.')

# Main function to set up the bot
def main():
    # Create an application object with the bot token
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Register the start command handler
    application.add_handler(CommandHandler('start', start))
    
    
    
    # Register the message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
