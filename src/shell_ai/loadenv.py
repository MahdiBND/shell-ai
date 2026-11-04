from pathlib import Path
from dotenv import load_dotenv


def loadenv():
    global_path = Path.home() / ".config" / "shell-ai" / ".env"
    load_dotenv(global_path)


current_path = Path.cwd()
