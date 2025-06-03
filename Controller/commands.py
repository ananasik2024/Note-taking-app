import Repository.loadFromFile as lF
import Repository.writeToFile as wF
from Models.Note import Note


def add_note():
    title = input("💡Введите заголовок новой заметки:\n")
    body = input("📝 Напишите текст заметки:\n")
    note = Note(title=title, body=body)
    array_notes = lF.read_file()
    for i in array_notes:
        if Note.get_id() == i.get_id():
            Note.set_id()
    array_notes.append(note)
    wF.write_file(array_notes, 'w')
    print("Заметка добавлена в журнал!🥰")


def show(txt):
    array_notes = lF.read_file()

    if array_notes:
        if txt == "all":
            print("📒 ЖУРНАЛ ЗАМЕТОК 📒")
            print("**********************")
            for i in array_notes:
                print(i.map_note())

        elif txt == "ID":
            for i in array_notes:
                print("ID: ", i.get_id())
            id = input("\nВведите id заметки: ")
            flag = True
            for i in array_notes:
                if id == i.get_id():
                    print(i.map_note())
                    flag = False
            if flag:
                print("🤷🏼‍♀️ Нет такого ID")

        elif txt == "date":
            date = input("📆 Введите дату в формате: dd.mm.yyyy: ")
            flag = True
            for i in array_notes:
                date_note = str(i.get_date())
                if date == date_note[:10]:
                    print(i.map_note())
                    flag = False
            if flag:
                print("🤷🏼‍♀️ Нет такой даты")
        else:
            print("Журнал заметок пустой 🫙")


def del_notes():
    id = input("Введите ID удаляемой заметки: ")
    array_notes = lF.read_file()
    flag = False

    for i in array_notes:
        if id == i.get_id():
            array_notes.remove(i)
            flag = True

    if flag:
        wF.write_file(array_notes, 'w')
        print("Заметка с id: ", id, " успешно удалена!😊")
    else:
        print("🤷🏼‍♀️ Нет такого id")


def change_note():
    id = input("Введите ID изменяемой заметки: ")
    array_notes = lF.read_file()
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
        print("Заметка с id: ", id, " успешно изменена!😊")
    else:
        print("🤷🏼‍♀️ Нет такого id")








