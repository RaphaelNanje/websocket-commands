from websocket_commands.class_decorators import CommandClass, command_handler


@CommandClass('test1')
class Test1Command:
    def execute(self, message: dict):
        print(self.type, message)


@CommandClass('test2')
class Test2Command:
    def execute(self, message: dict):
        print(self.type, message)


command_handler(dict(
    type='test1',
    message='Test1 succeeded'
))

command_handler(dict(
    type='test2',
    message='Test2 succeeded'
))
