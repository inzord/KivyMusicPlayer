import os

from musicplayer.params.params import Params


class Path:
    @classmethod
    def get_dir_path(cls):
        path_dir = Params().MY_PATH
        if os.path.isdir(path_dir):
            return path_dir
        else:
            print("Dir is not found")
