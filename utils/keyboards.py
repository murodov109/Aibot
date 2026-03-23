from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup

# Inline keyboards

def get_main_menu_keyboard():
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Button 1", callback_data='button1')
    button2 = InlineKeyboardButton("Button 2", callback_data='button2')
    keyboard.add(button1, button2)
    return keyboard

# Reply keyboards

def get_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = InlineKeyboardButton("Option 1")
    button2 = InlineKeyboardButton("Option 2")
    keyboard.add(button1, button2)
    return keyboard
