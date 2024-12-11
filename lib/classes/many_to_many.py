class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters.")

        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of the Author class.")

        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class.")

        self.author = author
        self.magazine = magazine
        self._title = title

        author._articles.append(self)
        author._magazines.add(magazine)
        magazine.add_article(self)

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of the Author class.")
        self._author = value

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class.")
        self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise TypeError("Name must be a non-empty string.")
        self._name = name
        self._articles = []  # List of Article instances
        self._magazines = set()  # Set of Magazine instances

    @property
    def name(self):
        return self._name

    @property
    def articles(self):
        return self._articles[:]

    @property
    def magazines(self):
        return list(self._magazines)

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class.")
        if not isinstance(title, str) or not title.strip():
            raise TypeError("Title must be a non-empty string.")
        
        # Check if an article with the same title and magazine already exists
        for article in self._articles:
            if article.title == title and article.magazine == magazine:
                return article
        
        article = Article(self, magazine, title)
        self._magazines.add(magazine)
        return article

    @property
    def topic_areas(self):
        if not self._magazines:
            return []
        return list({magazine.category for magazine in self._magazines})

    def __repr__(self):
        return f"Author({self.name})"


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or not category.strip():
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        self._articles = []  # List of Article instances

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def add_article(self, article):
        if not isinstance(article, Article):
            raise TypeError("Article must be an instance of the Article class.")
        if article not in self._articles:
            self._articles.append(article)

    @property
    def articles(self):
        return self._articles[:]

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = {article.author for article in self._articles}
        return {author for author in authors if len([article for article in self._articles if article.author == author]) > 2}

    def __repr__(self):
        return f"Magazine({self.name}, {self.category})"
