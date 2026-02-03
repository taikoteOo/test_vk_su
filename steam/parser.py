import re


def parse_download_info(log_lines):
    result = {
        "status": "idle",
        "speed": None,
        "game": None,
    }

    for line in reversed(log_lines):
        speed_match = re.search(r"Current download rate: ([\d.]+)\s*Mbps", line)
        if speed_match:
            result["status"] = "downloading"
            result["speed"] = speed_match.group(1) + " MB/s"
            return result

        else:
            result["status"] = "paused"
            return result

    return result