import types
from typing import Dict, Optional

categories: Dict[str, types.FunctionType] = dict()


def category(type: str):
    """
    This decorator registers any function that it is applied to as a command function.
    When commands are processed, if the type passed in the json matches the type argument,
    the matching function will be executed.
    Args:
        type: The 'topic' of the command sent. This will be used to identify which function should process a given command
    """

    def register_category(func: types.FunctionType) -> types.FunctionType:
        """
        This simply registers the category in the categories dictionary
        Args:
            func: The function that is being decorated.
        """
        categories[type] = func
        return func

    return register_category


def message_handler(message: dict, *args, **kwargs) -> Optional[object]:
    """
    This automatically finds and executes the appropriate function that matches the "type" value in the message dict

    Args:
        message: The message passed from the websocket
    """
    if 'type' in message and (type := message.get('type')) in categories:
        # noinspection PyUnboundLocalVariable
        return categories.get(type)(message, *args, **kwargs)
    return None
