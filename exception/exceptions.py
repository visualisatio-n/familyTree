class RelationNotMappedException(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class CommandNotValidException(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class PersonNotFoundException(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)
