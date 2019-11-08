from typing import Dict

command_classes: Dict[str, object] = dict()


class CommandClass:
    """
    This class will keep track of all classes it decorates. The command type will be passed
    as a argument to the decorator and will be used for automatically keeping track of commands.
    """

    def __init__(self, type: str) -> None:
        self.type = type

    def __call__(self, cls):
        cls.type = self.type
        command_classes[self.type] = cls
        return cls


def command_handler(message: dict):
    cls = command_classes.get(message['type'], None)
    if cls:
        cls().execute(message)
    else:
        print('Command type not recognized:', message)
