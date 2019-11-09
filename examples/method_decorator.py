from websocket_commands.function_decorators import category, categories, message_handler


@category('test')
def c1(message):
    print('test', message)


@category('test2')
def c1(message):
    print('test2', message)


print(categories)
message_handler(
    dict(
        type='test',
        message='Test message'
    )
)
message_handler(
    dict(
        type='test2',
        message='Test2 message'
    )
)
