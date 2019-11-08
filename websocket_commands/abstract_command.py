import abc
from typing import Dict
from typing import List


class AbstractCommand(abc.ABC):
    """
    This inheritable class uses __sub_classes__() to locate all classes
    immediately inheriting it. Only use this if you only plan on going single inheritance,
    as this only keeps track of the top level inheritance.

     This will be tracked:
        class SubClass(AbstractCommand)

     This will not be tracked:
        class SubclassOfSubclass(SubClass)
    """
    type: str = ''

    @abc.abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def __str__(self) -> str:
        return self.type or super().__str__()

    def __repr__(self) -> str:
        return self.type or super().__repr__()


def get_class_commands() -> Dict[str, AbstractCommand.__class__]:
    """
    Returns: All immediate subclasses of the AbstractCommand class

    """
    sub_classes: List[AbstractCommand.__class__] = AbstractCommand.__subclasses__()
    return {v.type: v for v in sub_classes if v.type}


def command_handler(message: dict):
    """
    The default command handler for AbstractCommand subclasses

    Args:
        message: The incoming websocket message
    """
    cls = get_class_commands().get(message['type'], None)
    if cls:
        cls().execute(message)
    else:
        print('Command type not recognized:', message)
