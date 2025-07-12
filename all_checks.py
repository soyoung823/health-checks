#!/usr/bin/env python3

import shutil
import sys

def check_reboot():
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_absolute, min_percent):
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True

def main():
    if not check_reboot():
        print("Pending Reboot")
        sys.exit(1)
    if check_disk_full("/", 2, 10):
        print("Disk full.")
        sys.exit(1)


