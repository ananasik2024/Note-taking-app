from datetime import datetime
import Controller.counter as counter


class Note:
    def __init__(self, 
                 id: str = None,
                 title: str = "текст", 
                 body: str = "текст",
                 date: str = None):
        self.id = id if id else str(counter.counter())
        self.title = title
        self.body = body
        self.date = date if date else datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    def get_id(self) -> str:
        return self.id

    def get_title(self) -> str:
        return self.title

    def get_body(self) -> str:
        return self.body

    def get_date(self) -> str:
        return self.date

    def set_id(self):
        self.id = str(counter.counter())

    def set_title(self, title: str):
        self.title = title

    def set_body(self, body: str):
        self.body = body

    def set_date(self):
        self.date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    def map_note(self) -> str:
        return (
            f"\nID: {self.id}\n"
            f"Название: {self.title}\n"
            f"Описание: {self.body}\n"
            f"Дата публикации: {self.date}"
        )
