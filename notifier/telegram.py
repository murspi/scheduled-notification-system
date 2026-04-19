import json
import urllib.request
import urllib.parse
from typing import Mapping, Any
from notifier import Notifier

class TelegramNotifier(Notifier):
    def __init__(self, telegram_config: Mapping[str, Any]) -> None:
        self.token = telegram_config["bot_token"]
        self.chat_id = telegram_config["chat_id"]

        self.api_url = f"https://api.telegram.org/bot{self.token}/sendMessage"

    def send(self, message: str) -> bool:
        data = {
            "chat_id": self.chat_id,
            "text": message
        }

        encoded_data  = urllib.parse.urlencode(data).encode("utf-8")

        try:
            request = urllib.request.Request(self.api_url, data=encoded_data)
            with urllib.request.urlopen(request, timeout=10) as response:
                result = json.loads(response.read().decode("utf-8"))

                return result.get("ok", False)
            
        except Exception as e:
            print(f"TelegramNotifier: Error sending message: {e}")
            return False