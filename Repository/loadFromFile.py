import json
from Models.Note import Note

def read_file():
    array = []
    try:
        with open("notes.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            for item in data:
                note = Note(
                    id=item.get("id", ""),
                    title=item.get("title", ""),
                    body=item.get("body", ""),
                    date=item.get("date", "")
                )
                array.append(note)
    except FileNotFoundError:
        print("📂 Файл не найден")
    return array