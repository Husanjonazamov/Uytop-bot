from aiogram.types import CallbackQuery
from loader import dp, bot
from utils import texts, buttons
from utils.env import ADMIN




@dp.callback_query_handler(lambda c: c.data.startswith("check_"))
async def handle_check_callback(callback_query: CallbackQuery):
    data = callback_query.data.split("_")
    
    if data[1] == "edit":
        await callback_query.answer("Ushbu e'lon allaqachon tasdiqlangan.")
        return

    listing_id = int(data[1])
    tg_id = int(data[2])
    
    await callback_query.answer()
    
    await bot.edit_message_reply_markup(
        chat_id=ADMIN,
        message_id=callback_query.message.message_id,
        reply_markup=buttons.edit_check_button()  
    )
    
    await bot.send_message(
        chat_id=tg_id,
        text=texts.CHEC_USER
    )
    
