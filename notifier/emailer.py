import smtplib
from email.message import EmailMessage
from typing import Mapping, Any
from notifier import Notifier

class EmailNotifier(Notifier):
    def __init__(self, smtp_config: Mapping[str, Any]) -> None:
        self.host = smtp_config["host"]
        self.port = smtp_config["port"]
        self.username = smtp_config["username"]
        self.password = smtp_config["password"]
        self.from_addr = smtp_config["from_addr"]
        self.to_addr = smtp_config["to_addr"]

    def send(self, message: str) -> bool:
        email = EmailMessage()
        email["From"] = self.from_addr
        email["To"] = self.to_addr
        email["Subject"] = "Collector Alert"
        email.set_content(message)

        try:
            with smtplib.SMTP(self.host, self.port, timeout=10) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(email)
            return True
    
        except smtplib.SMTPAuthenticationError:
            print("EmailNotifier: Authentication failed (bad username/password).")
            return False
    
        except smtplib.SMTPConnectError:
            print("EmailNotifier: Could not connect to SMTP server.")
            return False
    
        except smtplib.SMTPException as e:
            print(f"EmailNotifier: SMTP error occurred: {e}")
            return False
    
        except OSError:
            print("EmailNotifier: Network error (no internet or DNS failure).")
            return False