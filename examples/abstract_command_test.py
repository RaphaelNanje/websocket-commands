from abc import ABC

from websocket_commands.abstract_command import get_class_commands, AbstractCommand, command_handler


# the 'type' field will be used to find the appropriate class
class Test1Command(AbstractCommand):
    type = 'test1'

    def execute(self, message):
        print(self, message)


class Test2Command(AbstractCommand):
    type = 'test2'

    def execute(self, message):
        print(self, message)


class Test3Command(AbstractCommand):

    def execute(self, message):
        print(self, message)


class BaseCommand(AbstractCommand, ABC):
    pass


# this won't work as __subclasses__ only gets immediate subclasses
class Test4Command(BaseCommand):
    type = 'test4'

    def execute(self, *args, **kwargs):
        pass


command_handler(dict(
    type='test1',
    message='Test1 succeeded'
))

command_handler(dict(
    type='test2',
    message='Test2 succeeded'
))
command_handler(dict(
    type='test3',
    message='Test3 succeeded'
))

print(get_class_commands())
