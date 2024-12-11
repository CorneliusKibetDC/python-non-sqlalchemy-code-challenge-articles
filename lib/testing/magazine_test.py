import pytest
from classes.many_to_many import Article, Magazine, Author

class TestMagazine:
    """Magazine in many_to_many.py"""

    def test_has_name(self):
        """Magazine is initialized with a name"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert magazine_1.name == "Vogue"
        assert magazine_2.name == "AD"

    def test_name_is_mutable_string(self):
        """Magazine name is of type str and can change"""
        magazine_1 = Magazine("Vogue", "Fashion")
        assert isinstance(magazine_1.name, str)

        magazine_1.name = "New Yorker"
        assert magazine_1.name == "New Yorker"

        with pytest.raises(ValueError):
            magazine_1.name = 2

    def test_name_len(self):
        """Magazine name is between 2 and 16 characters, inclusive"""
        magazine_1 = Magazine("Vogue", "Fashion")
        assert 2 <= len(magazine_1.name) <= 16

        with pytest.raises(ValueError):
            magazine_1.name = "New Yorker Plus X"

    def test_has_category(self):
        """Magazine is initialized with a category"""
        magazine_1 = Magazine("Vogue", "Fashion")
        assert magazine_1.category == "Fashion"

    def test_category_is_mutable_string(self):
        """Magazine category is of type str and can change"""
        magazine_1 = Magazine("Vogue", "Fashion")
        assert isinstance(magazine_1.category, str)

        magazine_1.category = "Lifestyle"
        assert magazine_1.category == "Lifestyle"

        with pytest.raises(ValueError):
            magazine_1.category = 2

    def test_category_len(self):
        """Magazine category has length greater than 0"""
        magazine_1 = Magazine("Vogue", "Fashion")
        assert magazine_1.category != ""

        with pytest.raises(ValueError):
            magazine_1.category = ""

    def test_has_many_articles(self):
        """Magazine has many articles"""
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        article_1 = Article(author_1, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author_1, magazine_1, "Dating life in NYC")
        article_3 = Article(author_1, magazine_2, "2023 Eccentric Design Trends")

        assert len(magazine_1.articles) == 2
        assert len(magazine_2.articles) == 1
        assert article_1 in magazine_1.articles
        assert article_3 in magazine_2.articles

    def test_articles_of_type_articles(self):
        """Magazine articles are of type Article"""
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")

        assert isinstance(magazine_1.articles[0], Article)

    def test_has_many_contributors(self):
        """Magazine has many contributors"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_2, magazine_1, "Dating life in NYC")

        assert len(magazine_1.contributors()) == 2
        assert author_1 in magazine_1.contributors()

    def test_contributors_are_unique(self):
        """Magazine contributors are unique"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_1, "How to be single and happy")
        Article(author_2, magazine_1, "Dating life in NYC")

        assert len(set(magazine_1.contributors())) == len(magazine_1.contributors())

    def test_article_titles(self):
        """Returns list of titles strings of all articles written for that magazine"""
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")

        assert magazine_1.article_titles() == ["How to wear a tutu with style"]

    def test_contributing_authors(self):
        """Returns author list who have written more than 2 articles for the magazine"""
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_1, "How to be single and happy")
        Article(author_1, magazine_1, "Dating life in NYC")

        assert author_1 in magazine_1.contributing_authors()
        assert all(isinstance(author, Author) for author in magazine_1.contributing_authors())
