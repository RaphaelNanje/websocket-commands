# import unittest

from websocket_commands.websocket_commands import command, command_functions


def command_handler(message: dict):
    if 'type' in message:
        if (type := message.get('type')) in command_functions:
            command_functions.get(type)(message)


@command('test')
def c1(message):
    print('test', message)


@command('test2')
def c1(message):
    print('test2', message)


# class MyTestCase(unittest.TestCase):
#     def test_decorator(self):
#         self.assertEqual(True, False)
#
#
# if __name__ == '__main__':
#     unittest.main()

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
