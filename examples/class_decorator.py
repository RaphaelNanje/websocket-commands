from websocket_commands.class_decorators import *


# noinspection PyMethodMayBeStatic
@CategoryClass('rain')
class Rain:
    def drop_command(self, message: dict):
        print('drop', message)

    def evaporate_command(self, message: dict):
        print('evaporate', message)


@CategoryClass('test2')
class Test2Command:
    def execute(self, message: dict):
        print(self.type, message)


message_handler(dict(
    type='rain',
    command='drop',
    message='Rain has dropped'
))
message_handler(dict(
    type='rain',
    command='evaporate',
    message='Rain has evaporated'
))
