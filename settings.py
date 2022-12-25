import pathlib
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")

#takes the parent location of this file and sets it to be base directory
BASE_DIR = pathlib.Path(__file__).parent

#sets the commands directory to be in the cmds folder
COGS_DIR = BASE_DIR / "cogs"