import const
import time
from main import *
import user as us

def help_function():
    print(const.JUMP_LINE)
    time.sleep(0.5)
    print(const.HELP)
    time.sleep(2)
    print(const.INFO_HELP)
    inp = input(const.INP_SHOW_DATA)
    if inp.isupper():
        inp = inp.lower()
    if inp == 'y':
        print(const.JUMP_LINE)
        time.sleep(0.5)
        print(const.LOADING_DATA)
        print(const.JUMP_LINE)
        user = us.User()
        user.print_xlsx()
        time.sleep(0.5)
        print(const.JUMP_LINE)
        print(const.LOAD_DATA)
    elif inp == 'n':
        time.sleep(0.5)
    else:
        error_menu()

def return_menu():
    print(const.JUMP_LINE)
    inp = input(const.QUESTION_RET)
    if inp.isupper():
        inp = inp.lower()
    if inp == 'y':
        print(const.JUMP_LINE)
        time.sleep(0.5)
        print(const.RETURN_MENU)
        time.sleep(0.5)
    elif inp == 'n':
        exit_program()
        exit()
    else:
        error_menu()

def exit_program():
    print(const.JUMP_LINE)
    time.sleep(0.5)
    print(const.EXIT)
    time.sleep(0.5)

def error_menu():
    print(const.JUMP_LINE)
    print(const.ERR)
    time.sleep(0.5)
    print(const.JUMP_LINE)
    print(const.RETURN_MENU)
    time.sleep(0.5)


