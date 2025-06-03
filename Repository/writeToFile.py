import json
from Models.Note import Note

def write_file(array, mode='w'):
    data = []
    for note in array:
        data.append({
            "id": note.get_id(),
            "title": note.get_title(),
            "body": note.get_body(),
            "date": note.get_date()
        })

    try:
        with open("notes.json", mode, encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"⚠️ Ошибка при сохранении заметок: {e}")
