import os
from dotenv import load_dotenv

load_dotenv()


class Params:

    def __init__(self):
        self.MY_PATH = os.getenv("my_path")
