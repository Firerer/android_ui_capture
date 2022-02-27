import os
import dotenv

print("once")

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

OUT_DIR = os.path.join(ROOT_DIR, "saveScreen")
if not os.path.exists(OUT_DIR):
    os.mkdir(OUT_DIR)

dotenv.load_dotenv()

PHONE_SERIAL = os.environ.get("phoneId")
TABLET_SERIAL = os.environ.get("tabletId")
