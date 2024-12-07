class Article:
    #empty list
    empty_list = []
    def __init__(self, author, magazine, title: str):
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title length must be between 5 and 50 characters.")
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.empty_list.append(self)
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        raise AttributeError("Title is immutable.")
article = Article("Author Name", "Magazine Name", "How to wear a tutu with style")
print(article.title)
def test_title_is_immutable_str(self):
    #title is an immutable string
    author = Author("Carry Bradshaw")
    magazine = Magazine("Vogue", "Fashion")
    article_1 = Article(author, magazine, "How to wear a tutu with style")
 
    # Attempting to change the title should raise an exception
    with self.assertRaises(AttributeError):
        article_1.title = 500
article = Article("Author Name", "Magazine Name", "How to wear a tutu with style")
print(article.title)  

class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass