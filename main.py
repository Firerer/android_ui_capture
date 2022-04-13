import csv

# import pandas as p
import os

import definitions
import uiautomator2 as u2
from definitions import APK_DIR
from screenCapture import capture_ui_data
from utils.apks import install
from utils.util import *


def main():
    tablet = u2.connect(definitions.TABLET_ID)
    phone = u2.connect(definitions.PHONE_ID)

    def both_install(apk_path):
        install(apk_path, tablet)
        install(apk_path, phone)
        apk_name, main_act = getPackageByApk(apk_path)
        return apk_name

    def both_run(apk_name):
        tablet.app_start(apk_name)
        phone.app_start(apk_name)

    while True:
        apk_paths = os.listdir(definitions.APK_DIR)
        apk_paths = map(lambda x: os.path.join(APK_DIR, x), apk_paths)
        apk_paths = [f for f in apk_paths if os.path.isfile(f)]

        for i in list(enumerate(apk_paths + ["exit", "refresh", "screenshot"])):
            print(i)

        i = int(input("Enter a index: "))
        l = len(apk_paths)
        if i == l:
            break
        elif i == l + 1:
            pass
        elif i == l + 2:
            capture_ui_data()
        else:
            apk_name = both_install(apk_paths[i])
            both_run(apk_name)


if __name__ == "__main__":
    main()
