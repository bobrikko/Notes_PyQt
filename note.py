from datetime import datetime

class Note:
    def __init__(self, title="", content="", is_pinned=False):
        self.title = title
        self.content = content
        self.is_pinned = is_pinned
        self.date_added = datetime.now()

    def __repr__(self):
        return f"<Note title='{self.title}', pinned={self.is_pinned}, date_added={self.date_added}>"