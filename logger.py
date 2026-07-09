from datetime import datetime
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"


def log(message: str):

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    text = f"[{now}] {message}"

    print(text)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")