from yaml import Loader, load
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os

MENU = load(open(
    os.path.join(os.getcwd(), 'tb', 'management', 'commands', 'navigation.yaml'), 
    'r', encoding='utf-8'), Loader=Loader)

def get_static_buttons(context: dict):
    buttons = []
    state = context["new_state"]
    
    if 'static_buttons' not in MENU[state]:
        return buttons
    
    for button_text, params in MENU[state]["static_buttons"].items():
        callback_data = {'new_state': params['new_state']}
        buttons.append(InlineKeyboardButton(
            text=button_text,
            callback_data=str(callback_data)))
    
    return buttons

def get_reply_message(context: dict):
    inline_keyboard = []
    inline_keyboard.append(get_static_buttons(context))
    
    markup = InlineKeyboardMarkup(
        inline_keyboard=inline_keyboard)

    text = eval(MENU[context['new_state']]['message'].format(**context))
    return text, markup