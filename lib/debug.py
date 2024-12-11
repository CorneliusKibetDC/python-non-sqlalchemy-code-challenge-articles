#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! 🙂 Let's debug 🎉")

    # Example objects for debugging (optional, adjust as needed)
    author = Author("Jane Doe")
    magazine = Magazine("Tech Today", "Technology")
    article = Article(author, magazine, "The Future of AI")

    # Print example objects
    print(author)
    print(magazine)
    print(article)

    # Don't remove this line, it's for debugging!
    ipdb.set_trace()
