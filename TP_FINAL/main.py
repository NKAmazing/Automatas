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
        if inp == '1':
            user.list_session_id()
            ft.return_menu()
        elif inp == '2':
            user.datetime_search()
            ft.return_menu()
        elif inp == '3':
            user.total_session_time()
            ft.return_menu()
        elif inp == '4':
            user.mac_user_devices()
            ft.return_menu()
        elif inp == '5':
            user.list_macs_user()
            ft.return_menu()
        elif inp == '6':
            user.mac_ap()
            ft.return_menu()
        elif inp == '7':
            user.traffic_user()
            ft.return_menu()
        elif inp == 'h':
            ft.help_function()
            time.sleep(1)
            ft.return_menu()
        elif inp == '8':
            user.total_traffic()
            ft.return_menu()
        elif inp == 'q':
            ft.exit_program()
            break
        else:
            ft.error_menu()

if __name__ == '__main__':
    main()
    