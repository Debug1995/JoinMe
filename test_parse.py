from QT_FrontEnd.logic import Logic
import os
import sys


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    Logic.print_user(Logic.get_user(329))
