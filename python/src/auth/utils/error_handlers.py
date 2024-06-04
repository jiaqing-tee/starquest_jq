import sys
from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.exceptions import HTTPException
from werkzeug.wrappers.response import Response


class ErrorWrapper(HTTPException):
    def __init__(self, code: int, description: str | None = None, error: Exception | str | None = None, response: Response | None = None) -> None:
        self.code = code
        self.description = description
        if error:
            self.description += f'{ str(error)}'
        if response is None:
            self.response = Response(self.description, self.code)
        self.display_error(self.code, self.description)
        super().__init__(self.description, self.response)
    
    def display_error(self):
        error_message = f'{self.code} {HTTP_STATUS_CODES[self.code]}:\t{self.description}'
        print(error_message, file=sys.stderr)


# Authentication
class MissingAuthHeader(ErrorWrapper):
    def __init__(self, error: Exception | str | None = None, response: Response | None = None) -> None:
        self.code = 401
        self.description = f'Authorization header is not provided.'
        super().__init__(self.code, self.description, error, response)

class MissingBasicAuthentication(ErrorWrapper):
    def __init__(self, error: Exception | str | None = None, response: Response | None = None) -> None:
        self.code = 401
        self.description = f'Basic authentication credentials is not provided.'
        super().__init__(self.code, self.description, error, response)

class UserNotFound(ErrorWrapper):
    def __init__(self, username: str | None = None, error: Exception | str | None = None, response: Response | None = None) -> None:
        self.code = 401
        self.description = f'User "{username}" not found.'
        super().__init__(self.code, self.description, error, response)

class IncorrectUserPassword(ErrorWrapper):
    def __init__(self, error: Exception | str | None = None, response: Response | None = None) -> None:
        self.code = 401
        self.description = f'The username or password is incorrect.'
        super().__init__(self.code, self.description, error, response)

class MissingBearerAuthentication(ErrorWrapper):
    def __init__(self, error: Exception | str | None = None, response: Response | None = None) -> None:
        self.code = 401
        self.description = f'Bearer authentication token is not provided.'
        super().__init__(self.code, self.description, error, response)

class InvalidUserToken(ErrorWrapper):
    def __init__(self, error: Exception | str | None = None, response: Response | None = None) -> None:
        self.code = 401
        self.description = f'Invalid bearer token provided.'
        super().__init__(self.code, self.description, error, response)


# Models
class ErrorInitDb(ErrorWrapper):
    def __init__(self, description: str | None = None, response: Response | None = None) -> None:
        self.code = 500
        super().__init__(self.code, description, None, response)
