class Article:
    # Class variable to track all articles
    all = []

    def __init__(self, author, magazine, title):
        # Validate title
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        # Validate author
        if not isinstance(author, Author):
            raise ValueError("Author must be an Author instance")
        # Validate magazine
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be a Magazine instance")

        self._title = title
        self._author = author
        self._magazine = magazine
        # Add to all articles
        Article.all.append(self)

    @property
    def title(self):
        # Return the title
        return self._title

    @title.setter
    def title(self, value):
        # Immutable, do nothing
        pass

    @property
    def author(self):
        # Return the author
        return self._author

    @author.setter
    def author(self, value):
        # Set new author if valid
        if not isinstance(value, Author):
            raise ValueError("Author must be an Author instance")
        self._author = value

    @property
    def magazine(self):
        # Return the magazine
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        # Set new magazine if valid
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be a Magazine instance")
        self._magazine = value


class Author:
    def __init__(self, name):
        # Validate name
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")

        self._name = name

    @property
    def name(self):
        # Return the name
        return self._name

    @name.setter
    def name(self, value):
        # Immutable, do nothing
        pass

    def articles(self):
        # Get all articles by this author
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        # Get unique magazines from articles
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        # Create and return new article
        return Article(self, magazine, title)

    def topic_areas(self):
        # Get unique categories if has articles
        if not self.articles():
            return None
        return list(set(magazine.category for magazine in self.magazines()))


class Magazine:
    # Class variable to track all magazines
    all = []

    def __init__(self, name, category):
        # Validate name
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        # Validate category
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")

        self._name = name
        self._category = category
        # Add to all magazines
        Magazine.all.append(self)

    @property
    def name(self):
        # Return the name
        return self._name

    @name.setter
    def name(self, value):
        # Set new name if valid, else do nothing
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        # Return the category
        return self._category

    @category.setter
    def category(self, value):
        # Set new category if valid, else do nothing
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        # Get all articles for this magazine
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        # Get unique authors
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        # Get titles if has articles
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        # Authors with more than 2 articles
        authors = []
        for author in self.contributors():
            count = 0
            for article in author.articles():
                if article.magazine == self:
                    count += 1
            if count > 2:
                authors.append(author)
        if not authors:
            return None
        return authors

    @classmethod
    def top_publisher(cls):
        # Magazine with most articles, None if no articles
        if not Article.all:
            return None
        return max(cls.all, key=lambda m: len(m.articles()))