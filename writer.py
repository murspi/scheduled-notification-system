import csv
from typing import Dict, Any
from pathlib import Path
from datetime import datetime

CSV_FILE = Path("phrases_log.csv")

def write_row(parsed: Dict[str, Any]) -> None:
    """
    Append a parsed phrase to phrases_log.csv.
    Creates the file with a header if it doesn't exist yet.
    """

    # Define the order of columns
    fieldnames = ["timestamp", "phrase"]

    # Check if file exists
    file_exists = CSV_FILE.exists()

    with CSV_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        # Write header only once
        if not file_exists:
            writer.writeheader()

        # Write the actual row
        writer.writerow({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "phrase": parsed.get("phrase")
        })