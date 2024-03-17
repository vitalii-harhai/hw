from colorama import Fore, Style


class Colorizer:
    """
    Colorize the text in the terminal
    """
    def __init__(self, color: str):
        self.color = color.upper()

    def __enter__(self):
        if self.color in list(Fore.__dict__):
            print(Fore.__getattribute__(self.color), end='')
        else:
            print(Fore.RED, f'{self.color} is not available in CLI!')
            print(Fore.GREEN, 'Available command colors:', ', '.join(list(Fore.__dict__)), Style.RESET_ALL)

    def __exit__(self, exit_type, exit_value, exit_tb):
        print(Style.RESET_ALL, end='')


print('\033[93m', end='')
print('aaa')
print('bbb')
print('\033[0m', end='')
print('ccc')

with Colorizer('red1'):
    print('printed in red')
print('printed in default color')
