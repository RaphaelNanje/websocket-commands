from websocket_commands.function_decorators import command, command_functions, command_handler


@command('test')
def c1(message):
    print('test', message)


@command('test2')
def c1(message):
    print('test2', message)


print(command_functions)
command_handler(
    dict(
        type='test',
        message='Test message'
    )
)
command_handler(
    dict(
        type='test2',
        message='Test2 message'
    )
)
