import pytest
from classes.many_to_many import Article, Magazine, Author

class TestAuthor:
    """Tests for the Author class in many_to_many.py"""

    def test_has_name(self):
        """Author is initialized with a name"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert author_1.name == "Carry Bradshaw"
        assert author_2.name == "Nathaniel Hawthorne"

    def test_name_is_immutable_string(self):
        """Author name is of type str and cannot change"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert isinstance(author_1.name, str)
        assert isinstance(author_2.name, str)

        with pytest.raises(AttributeError):
            author_1.name = "ActuallyTopher"

    def test_name_len(self):
        """Author name is longer than 0 characters"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert len(author_1.name) > 0
        assert len(author_2.name) > 0

    def test_has_many_articles(self):
        """Author has many articles"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author_1, magazine, "How to wear a tutu with style")
        article_2 = Article(author_1, magazine, "Dating life in NYC")
        article_3 = Article(author_2, magazine, "How to be single and happy")

        assert len(author_1.articles) == 2
        assert len(author_2.articles) == 1
        assert article_1 in author_1.articles
        assert article_2 in author_1.articles
        assert article_3 in author_2.articles

    def test_articles_of_type_articles(self):
        """Author articles are of type Article"""
        author_1 = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author_1, magazine, "How to wear a tutu with style")

        assert isinstance(author_1.articles[0], Article)

    def test_has_many_magazines(self):
        """Author has many magazines"""
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_2, "2023 Eccentric Design Trends")

        assert magazine_1 in author_1.magazines
        assert magazine_2 in author_1.magazines

    def test_magazines_are_unique(self):
        """Author magazines are unique"""
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_2, "2023 Eccentric Design Trends")
        Article(author_1, magazine_2, "Carrara Marble is so 2020")

        assert len(set(author_1.magazines)) == len(author_1.magazines)

    def test_add_article(self):
        """Creates and returns a new article given a magazine and title"""
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        article_1 = author_1.add_article(magazine_1, "How to wear a tutu with style")

        assert isinstance(article_1, Article)
        assert article_1 in author_1.articles

    def test_topic_areas(self):
        """Returns a list of topic areas for all articles by author"""
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        author_1.add_article(magazine_1, "How to wear a tutu with style")
        author_1.add_article(magazine_2, "Carrara Marble is so 2020")

        assert set(author_1.topic_areas) == {"Fashion", "Architecture"}
