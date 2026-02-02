from steam.finder import find_steam_path
from steam.logs import read_download_log
from steam.parser import parse_download_info
from monitor.scheduler import run_scheduler
from config import CHECK_INTERVAL_SECONDS, CHECK_COUNT


def check_steam():
    steam_path = find_steam_path()

    if not steam_path:
        print("Steam не найден")
        return

    log_lines = read_download_log(steam_path)
    info = parse_download_info(log_lines)
    print(log_lines[-5:])
    if info["status"] == "downloading":
        print(f"Загрузка идёт, скорость: {info['speed']}")
    elif info["status"] == "paused":
        print("Загрузка на паузе")
    else:
        print("Загрузка не идёт")


if __name__ == "__main__":
    print("Steam monitor started")
    run_scheduler(check_steam, CHECK_INTERVAL_SECONDS, CHECK_COUNT)
