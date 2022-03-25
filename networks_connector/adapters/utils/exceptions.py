class UserIdError(Exception):
    def __init__(self):
        super().__init__("User id or short name must be a string or an integer")


class InvalidUserId(Exception):
    def __init__(self):
        super().__init__("Invalid user ID")


class ClosedProfile(Exception):
    def __init__(self):
        super().__init__("This profile is closed")


class UserNotFound(Exception):
    def __init__(self):
        super().__init__("Cannot find such user")
