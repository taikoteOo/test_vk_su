import os

def read_download_log(steam_path, lines=50):
    log_path = os.path.join(steam_path, "logs", "content_log.txt")

    if not os.path.exists(log_path):
        return []

    with open(log_path, "r", encoding="utf-8", errors="ignore") as file:
        return file.readlines()[-lines:]