import UI.userMenuConsole as ui
import Controller.commands as com


def start():
    while True:
        ui.menu_console()
        user_input = input().strip()
        if user_input == '1':
            com.show("all")
        elif user_input == '2':
            com.show("ID")
        elif user_input == '3':
            com.show("date")
        elif user_input == '4':
            com.change_note()
        elif user_input == '5':
            com.add_note()
        elif user_input == '6':
            com.del_notes()
        else:
            print("Программа Журнал заметок завершена")
            break
