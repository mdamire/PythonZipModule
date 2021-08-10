"""Create A module to execute 7za command"""
import subprocess

class Exec7za():
    def __init__(self, *param):
        self.args = list(param)
        self.completed_process = ''

    def add_args(self, *param):
        self.args.extend(param)

    def get_args(self) -> list:
        return ['7za'] + self.args

    def run(self) -> int:
        cp = subprocess.run(self.get_args(), text=True, capture_output=True)
        self.completed_process = cp
        return self.completed_process.returncode

    def get_returncode(self) -> int:
        if isinstance(self.completed_process, subprocess.CompletedProcess):
            return self.completed_process.returncode
        return -1

    def get_stdout(self) -> str:
        if isinstance(self.completed_process, subprocess.CompletedProcess):
            return self.completed_process.stdout
        return ""
    
    def get_stderr(self) -> str:
        if isinstance(self.completed_process, subprocess.CompletedProcess):
            return self.completed_process.stderr
        return ""

    
        