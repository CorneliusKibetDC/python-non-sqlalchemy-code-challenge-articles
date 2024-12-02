# Necessary imports
from typing import List, Optional

class Magazine:
    all = []

    def __init__(self, name: str, category: str):
        if not isinstance(name, str) or not isinstance(category, str):
            raise ValueError("Name and category must be strings.")
        if not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters.")
        if not category.strip():
            raise ValueError("Category cannot be empty.")
        self.name = name
        self.category = category
        Magazine.all.append(self)

    def articles(self) -> List["Article"]:
        return [article for article in Article.all if article.magazine == self]

    def contributors(self) -> List["Author"]:
        return list({article.author for article in self.articles()})

    def article_titles(self) -> Optional[List[str]]:
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self) -> Optional[List["Author"]]:
        authors = [author for author in self.contributors() if len(author.articles()) > 2]
        return authors if authors else None

    @staticmethod
    def top_publisher() -> Optional["Magazine"]:
        return max(Magazine.all, key=lambda mag: len(mag.articles()), default=None)


class Author:
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise ValueError("Author name must be a string.")
        self.name = name

    def articles(self) -> List["Article"]:
        return [article for article in Article.all if article.author == self]

    def magazines(self) -> List["Magazine"]:
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine: "Magazine", title: str):
        Article(self, magazine, title)

    def topic_areas(self) -> Optional[List[str]]:
        topics = [magazine.category for magazine in self.magazines()]
        return list(set(topics)) if topics else None


class Article:
    all = []

    def __init__(self, author: Author, magazine: Magazine, title: str):
        if not isinstance(author, Author) or not isinstance(magazine, Magazine) or not isinstance(title, str):
            raise ValueError("Invalid input types for Article.")
        self.author = author
        self.magazine = magazine
        self._title = title  # Use a private variable for title to make it immutable
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Cannot modify the title once it is set.")
