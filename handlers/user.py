def start_handler(update, context):
    update.message.reply_text('Welcome! Use /help to see available commands.')


def help_handler(update, context):
    help_text = "Available commands:\n/start - Welcome message\n/help - List of commands\n/tools - Available tools\n/generate - Generate content\n/image - Generate images\n/video - Generate videos\n/chat - Chat with the bot\n/profile - User profile commands\n/buy - Purchase options"
    update.message.reply_text(help_text)


def tools_handler(update, context):
    update.message.reply_text('Here are the available tools...')


def generate_handler(update, context):
    update.message.reply_text('Generating content...')


def image_handler(update, context):
    update.message.reply_text('Generating image...')


def video_handler(update, context):
    update.message.reply_text('Generating video...')


def chat_handler(update, context):
    update.message.reply_text('Start chatting!')


def profile_handler(update, context):
    update.message.reply_text('Accessing your profile...')


def buy_handler(update, context):
    update.message.reply_text('Here are your purchase options...')