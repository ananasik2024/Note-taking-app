import UI.menuTemplates as m


def menu_console():
    m.print_menu_title("ЖУРНАЛ ЗАМЕТОК")
    print("1 - 📖 Показать все заметки")
    print("2 - 🔍 Показать заметку по ID")
    print("3 - 📅 Показать заметки по дате")
    print("4 - ✏️  Редактировать заметку")
    print("5 - ➕ Добавить новую заметку")
    print("6 - 🗑️  Удалить заметку")
    print("7 - 🚪 Выход из программы")
    m.print_menu_line()
    print("\n👉 Введите пункт из меню: ", end='')


