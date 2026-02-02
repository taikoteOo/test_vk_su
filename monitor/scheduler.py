import time


def run_scheduler(callback, interval, count):
    for _ in range(count):
        callback()
        time.sleep(interval)