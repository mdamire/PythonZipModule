
class ZipComplete():

    def __init__(self, returncode, stdout, stderr) -> None:
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr

    def get_returncode(self) -> int:
        return self.returncode

    def get_stdout(self) -> str:
        return self.stdout

    def get_stderr(self) -> str:
        return self.stderr