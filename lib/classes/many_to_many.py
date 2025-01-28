class Article:

    all = []

    def __init__(self, author, magazine, title):
        if isinstance(author, Author):
            self.author = author
        if isinstance(magazine, Magazine):
            self.magazine = magazine
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) in range(5, 51):
            if not hasattr(self, "title"):
                self._title = title
        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            if not hasattr(self, "name"):
                self._name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        return list(set([magazine.category for magazine in self.magazines()])) or None

class Magazine:

    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) in range(2,17):
            self._name = name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category):
            self._category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        return [article.title for article in Article.all if article.magazine == self] or None

    def contributing_authors(self):
        authors = [article.author for article in Article.all if article.magazine == self]
        return [author for author in authors if authors.count(author) > 1] or None