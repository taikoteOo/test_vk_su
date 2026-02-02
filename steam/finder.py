import winreg
import os


def find_steam_path():
    """
    Ищет путь к установленному Steam через реестр Windows.
    Возвращает путь к папке Steam или None, если Steam не найден.
    """
    registry_locations = [
        (winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam"),
        (winreg.HKEY_LOCAL_MACHINE, r"Software\WOW6432Node\Valve\Steam"),
    ]
    for root, subkey in registry_locations:
        try:
            with winreg.OpenKey(root, subkey) as key:
                install_path, _ = winreg.QueryValueEx(key, "InstallPath")
                if os.path.exists(install_path):
                    return install_path
        except FileNotFoundError:
            continue
    return None