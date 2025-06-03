import Repository.loadFromFile as lF
import Repository.writeToFile as wF
from Models.Note import Note


def add_note():
    title = input("💡Введите заголовок новой заметки:\n")
    body = input("📝 Напишите текст заметки:\n")
    note = Note(title=title, body=body)
    array_notes = lF.read_file()

    # Проверка на уникальность ID
    existing_ids = [n.get_id() for n in array_notes]
    while note.get_id() in existing_ids:
        note.set_id()  # генерация нового ID

    array_notes.append(note)
    wF.write_file(array_notes, 'w')

    print("\n✅ Заметка добавлена в журнал!")
    print(f"🆔 ID новой заметки: {note.get_id()}")
    print_note(note)
    input("Нажмите Enter, чтобы вернуться в меню...")


def show(txt):
    array_notes = lF.read_file()

    if not array_notes:
        print("🫙 Журнал заметок пуст")
        print("Нажмите Enter, чтобы вернуться в меню...")
        input()
        return 

    if txt == "all":
        print("📒 ЖУРНАЛ ЗАМЕТОК 📒")
        print("**********************")
        for i in array_notes:
            print_note(i)

    elif txt == "ID":
        for i in array_notes:
            print(f"ID: {i.get_id()}, Заголовок: {i.get_title()}")
        id = input("\nВведите ID заметки: ").strip()
        found = False
        for i in array_notes:
            if id == i.get_id():
                print_note(i)
                found = True
        if not found:
            print("🤷🏼‍♀️ Нет такого ID")

    elif txt == "date":
        date = input("📆 Введите дату в формате: dd.mm.yyyy: ").strip()
        found = False
        for i in array_notes:
            note_date = i.get_date().split(" ")[0]
            if date == note_date:
                print_note(i)
                found = True
        if not found:
            print("🤷🏼‍♀️ Нет заметок с такой датой")
    print("Нажмите Enter, чтобы вернуться в меню...")
    input()

def print_note(note):
    print("📝 Заметка:")
    print(f"ID: {note.get_id()}")
    print(f"Заголовок: {note.get_title()}")
    print(f"Текст: {note.get_body()}")
    print(f"Дата: {note.get_date()}")
    print("―" * 40)

def del_notes():
    id_to_delete = input("Введите ID удаляемой заметки: ").strip()
    array_notes = lF.read_file()

    new_notes = [note for note in array_notes if note.get_id() != id_to_delete]

    if len(new_notes) == len(array_notes):
        print("🤷🏼‍♀️ Нет такого id")
    else:
        wF.write_file(new_notes, 'w')
        print(f"Заметка с id: {id_to_delete} успешно удалена!😊")

    input("Нажмите Enter, чтобы вернуться в меню...")


def change_note():
    array_notes = lF.read_file()
    if not array_notes:
        print("🫙 Журнал заметок пуст")
        input("Нажмите Enter, чтобы вернуться в меню...")
        return

    print("📒 ЖУРНАЛ ЗАМЕТОК 📒")
    print("**********************")
    for note in array_notes:
        print_note(note)

    input("Нажмите Enter, чтобы выбрать заметку для изменения...")

    id = input("Введите ID изменяемой заметки: ").strip()
    flag = False
    array_notes_new = []

    for i in array_notes:
        if id == i.get_id():
            i.title = input("Измените заголовок заметки:\n")
            i.body = input("Измените текст заметки:\n")
            i.set_date()
            flag = True
        array_notes_new.append(i)

    if flag:
        wF.write_file(array_notes_new, 'w')
        print("Заметка с ID:", id, "успешно изменена!☺️")
    else:
        print("🤷🏼‍♀️ Нет такого ID")

    input("Нажмите Enter, чтобы вернуться в меню...")








