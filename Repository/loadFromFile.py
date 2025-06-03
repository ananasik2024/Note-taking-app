import json
from Models.Note import Note

def read_file():
    try:
        with open("Notes.json", "r", encoding='utf-8') as file:
            data = json.load(file)
            notes = []
            for item in data:
                note = Note(
                    id=item.get("id"),
                    title=item.get("title"),
                    body=item.get("body"),
                    date=item.get("date"))
                notes.append(note)
            return notes
    except FileNotFoundError:
        print("⚠️ Файл notes.json не найден. Возвращаю пустой список.")
        return []
    except json.JSONDecodeError:
        print("⚠️ Файл Notes.json поврежден или пуст. Возвращаю пустой список.")
        return []
