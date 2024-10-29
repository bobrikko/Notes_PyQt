class Note:
    def __init__(self, title="", content=""):
        self.title = title
        self.content = content

    def __repr__(self):
        return f"<Note title={self.title}>"
