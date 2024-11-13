'''
    Book Class for Read.py
    Devin Quinn
'''


class Book:
    def __init__(self, title: str, author: str, length: int, chapters: int):
        self.title = title
        self.author = author
        self.length = length
        self.chapters = chapters
