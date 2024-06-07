import sys


class ErrorWrapper(Exception):
    def __init__(self, description: str | None = None, error: Exception | str | None = None):
        self.description = description
        self.error = error
        self.display_error()

    def display_error(self):
        error_message = f'{self.description}:\t{str(self.error)}'
        print(error_message, file=sys.stderr)
