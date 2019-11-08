import types
from typing import Dict

command_functions: Dict[str, types.FunctionType] = dict()


def function_command(type: str):
    """
    This decorator registers any function that it is applied to as a command function.
    When commands are processed, if the type passed in the json matches the type added to the command,
    the matching function will be executed.
    Args:
        type: The 'topic' of the command sent. This will be used to identify which function should process a given command
    """

    def register_command(func: types.FunctionType):
        """
        This simply registers the command in the command_functions dictionary
        Args:
            func: The function that is being decorated.

        Returns: The function itself.

        """
        command_functions[type] = func
        return func

    return register_command
