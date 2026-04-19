import json
from notifier.emailer import EmailNotifier
from notifier.telegram import TelegramNotifier
from notifier.rate_limit import RateLimiter

from client import fetch_raw_data
from parser import parse_raw_data
from writer import write_row


def load_config() -> dict:
    with open("config.json", "r") as f:
        return json.load(f)


def check_for_event() -> dict | None:
    """
    Fetch a phrase, parse it, log it.
    If successful, return the parsed phrase dict.
    """
    raw = fetch_raw_data()
    parsed = parse_raw_data(raw)

    if parsed["valid"]:
        write_row(parsed)
        return parsed

    return None


def main() -> None:
    config = load_config()

    email_notifier = EmailNotifier(config["smtp"])
    telegram_notifier = TelegramNotifier(config["telegram"])

    limiter = RateLimiter(cooldown_seconds=30)

    event = check_for_event()

    if event:
        phrase = event["phrase"]
        message = f"Daily phrase: {phrase}"

        if limiter.allow():
            email_success = email_notifier.send(message)
            telegram_success = telegram_notifier.send(message)

            if not email_success:
                print("runner: failed to send email alert")
            if not telegram_success:
                print("runner: failed to send telegram alert")

        else:
            print("runner: alert blocked by rate limiter")


if __name__ == "__main__":
    main()
