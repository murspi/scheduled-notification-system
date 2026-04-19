import random
from pathlib import Path

PHRASE_FILE = Path("phrases.txt")

def fetch_raw_data():
    # Fetching a random phrase from phrases.txt
    phrases = PHRASE_FILE.read_text(encoding="utf-8").splitlines()
    phrase = random.choice(phrases)
    return {"phrase": phrase}