# Scheduled Notification System

A Python automation tool that sends scheduled notifications via **Email** and **Telegram**.
Designed to demonstrate clean modular architecture, configuration management, and safe handling of secrets.

---

## 🚀 Features

* Sends scheduled notifications automatically
* Email notifications using SMTP
* Telegram bot notifications
* Rate limiter to prevent spam
* Logs every sent message to `phrases_log.csv`(ignored by Git)
* Clean modular architecture
* Easy to configure and extend
* Safe configuration pattern using `config.example.json`

---

## 📦 Project Structure

```
collector/
│
├── client.py              # Fetches a random phrase
├── parser.py              # Validates and cleans phrase
├── writer.py              # Logs phrase to CSV
├── runner.py              # Main execution logic
├── scheduler.py           # Weekday scheduling
│
├── notifier/
│   ├── __init__.py
│   ├── emailer.py         # Email notifier
│   ├── telegram.py        # Telegram notifier
│   └── rate_limit.py      # Rate limiter
│
├── phrases.txt            # Source of motivational phrases
├── config.example.json    # Template config 
├── config.json            # (ignored by Git)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/scheduled-notification-system.git
cd scheduled-notification-system
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔧 Configuration

This project uses two configuration files:

### `config.example.json`

A **template** file that shows the required structure without containing any real credentials.

Users copy this file and create their own private configuration.


---

### Example Configuration Template

```json
{
    "smtp": {
        "host": "smtp.gmail.com",
        "port": 587,
        "username": "your_email@gmail.com",
        "password": "your_app_password",
        "from_addr": "your_email@gmail.com",
        "to_addr": "recipient_email@gmail.com"
    },
    "telegram": {
        "bot_token": "YOUR_TELEGRAM_BOT_TOKEN",
        "chat_id": "YOUR_CHAT_ID"
    }
}
```

---

## ▶️ Running the Project

### Run once manually

```bash
python runner.py
```

### Run automatically on weekdays

```bash
python scheduler.py
```

---


## 📈 Future Improvements

* Environment variable support (`.env`)
* Docker support
* Multiple notification channels
* Retry logic for failed sends
* Web dashboard

---
