import requests
from utils.env import BASE_URL, BOT_TOKEN
from utils import texts



def send_webapp_button(chat_id):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": texts.START,
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "🛍 Magazin",
                        "web_app": {
                            "url": f"{BASE_URL}"
                        }
                    }
                ],
                [
                    {
                        "text": "🛒 Buyurtmalarim",
                        "web_app": {
                            "url": f"{BASE_URL}/profile/orders"
                        }
                    },
                    {
                        "text": "📞 Bog'lanish",
                        "callback_data": "contact_info"
                    }
                ]
            ]
        }
    }
    response = requests.post(url, json=payload)
    
    if not response.ok:
        print("❌ Inline tugma yuborishda xatolik:", response.text)







def set_menu_webapp():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/setChatMenuButton"
    payload = {
        "menu_button": {
            "type": "web_app",
            "text": "Magazin",
            "web_app": {
                "url": f"{BASE_URL}"
            }
        }
    }
    response = requests.post(url, json=payload)

    if not response.ok:
        print("❌ Menu tugmasi qo'shishda xatolik:", response.text)
