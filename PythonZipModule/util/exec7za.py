"""Create A module to execute 7za command"""
import subprocess

from .zipcomplete import ZipComplete

class Exec7za():
    def __init__(self, *param):
        self.args = list(param)

    def add_args(self, *param):
        self.args.extend(param)

    def get_args(self) -> list:
        return ['7za'] + self.args

    def run(self) -> int:
        cp = subprocess.run(self.get_args(), text=True, capture_output=True)
        return ZipComplete(cp.returncode, cp.stdout, cp.stderr)


    
        