import inspect
import re
import types
from typing import Dict

pattern = r'(?P<command>\w+)_command'


class CategoryClass:
    """
    This class will keep track of all classes it decorates.
    All methods that end in '_command' will be treated as a CategoryCommand.
    Messages containing a 'command' key will be matched with these CategoryCommand functions.

    See websocket_commands.examples.class_decorator_example.
    """

    def __init__(self, type: str) -> None:
        self.type = type

    # noinspection PyMissingTypeHints
    def __call__(self, cls):
        cls.commands = dict()
        cls.type = self.type
        category_classes[self.type] = cls
        cls.command_functions = dict()
        command_functions = inspect.getmembers(cls, predicate=inspect.isfunction)
        for name, command in command_functions:
            if match := re.match(pattern, name):
                type = match.group('command')
                cls.command_functions[type] = command
        return cls


def message_handler(message: dict, *args, **kwargs):
    if not ((cls := category_classes.get(message['type'], None))
            and (command := message.get('command', None))):
        return None
    # noinspection PyUnboundLocalVariable
    func = cls.command_functions[command]
    return getattr(cls(), func.__name__)(message, *args, **kwargs)


class CategoryClassInterface:
    type: str
    commands: Dict[str, types.FunctionType]


category_classes: Dict[str, object.__class__] = dict()
