import sys
from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.exceptions import HTTPException
from werkzeug.wrappers.response import Response


class ErrorWrapper(HTTPException):
    def __init__(self, code: int, description: str | None = None, response: Response | None = None) -> None:
        self.code = code
        self.description = description
        if response is None:
            self.response = Response(self.description, self.code)
        display_error(self.code, self.description)
        super().__init__(self.description, self.response)

# Authentication
class MissingAuthHeader(HTTPException):
    def __init__(self, description: str | None = None, response: Response | None = None) -> None:
        self.code = 401
        self.description = f'Authorization header is not provided.'
        if description:
            self.description += description
        if response is None:
            self.response = Response(self.description, self.code)
        display_error(self.code, self.description)
        super().__init__(self.description, self.response)

class MissingBasicAuthentication(HTTPException):
    def __init__(self, description: str | None = None, response: Response | None = None) -> None:
        self.code = 401
        self.description = f'Basic authentication credentials is not provided.'
        if description:
            self.description += description
        if response is None:
            self.response = Response(self.description, self.code)
        display_error(self.code, self.description)
        super().__init__(self.description, self.response)

class MissingBearerAuthentication(HTTPException):
    def __init__(self, description: str | None = None, response: Response | None = None) -> None:
        self.code = 401
        self.description = f'Bearer authentication token is not provided.'
        if description:
            self.description += description
        if response is None:
            self.response = Response(self.description, self.code)
        display_error(self.code, self.description)
        super().__init__(self.description, self.response)

class InvalidUserToken(HTTPException):
    def __init__(self, description: str | None = None, response: Response | None = None) -> None:
        self.code = 401
        self.description = f'Invalid bearer token provided.'
        if description:
            self.description += description
        if response is None:
            self.response = Response(self.description, self.code)
        display_error(self.code, self.description)
        super().__init__(self.description, self.response)

class NoPermission(HTTPException):
    def __init__(self, username: str | None = None, response: Response | None = None) -> None:
        self.code = 403
        self.description = f'User {username} does not have the permission.'
        if response is None:
            self.response = Response(self.description, self.code)
        display_error(self.code, self.description)
        super().__init__(self.description, self.response)

# Files
class MissingFidParams(HTTPException):
    def __init__(self, description: str | None = None, response: Response | None = None) -> None:
        self.code = 400
        self.description = f'Request parameter "fid" is not provided.'
        if description:
            self.description += description
        if response is None:
            self.response = Response(self.description, self.code)
        display_error(self.code, self.description)
        super().__init__(self.description, self.response)

class UploadError(HTTPException):
    def __init__(self, gridfs_name: str | None = None, description: str | None = None, response: Response | None = None) -> None:
        self.code = 400
        self.description = f'Unable to upload file to {gridfs_name} GridFS: {description}'
        if response is None:
            self.response = Response(self.description, self.code)
        display_error(self.code, self.description)
        super().__init__(self.description, self.response)

class DownloadError(HTTPException):
    def __init__(self, gridfs_name: str | None = None, fid: str | None = None, description: str | None = None, response: Response | None = None) -> None:
        self.code = 400
        self.description = f'Unable to download file from {gridfs_name} GridFs for fid {fid}: {description}'
        if response is None:
            self.response = Response(self.description, self.code)
        display_error(self.code, self.description)
        super().__init__(self.description, self.response)

# Queues
class PublishError(HTTPException):
    def __init__(self, routing_key: str | None = None, body: str | None = None, description: str | None = None, response: Response | None = None) -> None:
        self.code = 500
        self.description = f'Unable to publish to {routing_key} channel with {body}: {description}'
        if response is None:
            self.response = Response(self.description, self.code)
        display_error(self.code, self.description)
        super().__init__(self.description, self.response)

# Models
class ErrorInitDb(HTTPException):
    def __init__(self, description: str | None = None, response: Response | None = None) -> None:
        self.code = 500
        self.description = description
        if response is None:
            self.response = Response(self.description, self.code)
        display_error(self.code, self.description)
        super().__init__(self.description, self.response)

class ErrorInitRabbitmq(HTTPException):
    def __init__(self, description: str | None = None, response: Response | None = None) -> None:
        self.code = 500
        self.description = description
        if response is None:
            self.response = Response(self.description, self.code)
        display_error(self.code, self.description)
        super().__init__(self.description, self.response)


def display_error(status_code, description):
    error_message = f'{status_code} {HTTP_STATUS_CODES[status_code]}:\t{description}'
    print(error_message, file=sys.stderr)
