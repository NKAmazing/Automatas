import const as cs
import functions as ft
import time
import user as us

def main():
    user = us.User()
    while True:
        print(cs.MENU)
        inp = input("")
        inp = inp.lower()
        if inp == 'a':
            user.list_session_id()
            ft.return_menu()
        elif inp == 'b':
            user.print_csv()
            ft.return_menu()
        elif inp == 'c':
            ft.return_menu()
        elif inp == 'd':
            ft.return_menu()
        elif inp == 'e':
            ft.return_menu()
        elif inp == 'f':
            ft.return_menu()
        elif inp == 'g':
            ft.return_menu()
        elif inp == 'h':
            print(cs.HELP)
            time.sleep(3)
            ft.return_menu()
        elif inp == 'i':
            ft.return_menu()
        elif inp == 'q':
            ft.exit_program()
            break
        else:
            ft.error_menu()

if __name__ == '__main__':
    main()
    