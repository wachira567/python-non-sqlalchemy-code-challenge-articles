from .many_to_many import Article, Magazine

class Author:
    """
    The Author class represents an author in the magazine articles system.
    It manages the author's name (immutable), and provides methods to access
    related articles, magazines, and topic areas.
    """

    def __init__(self, name):
        """
        Initializes an Author instance with a name.
        Validation: Name must be a non-empty string.
        This ensures data integrity by preventing invalid names.
        """
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        """
        Property getter for the author's name.
        Returns the stored name as a string.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Property setter for the author's name.
        The name is immutable, so setting it does nothing.
        This prevents changes to the author's name after initialization.
        """
        pass

    def articles(self):
        """
        Returns a list of all Article instances written by this author.
        This method filters the class-level Article.all list to find articles
        where the author matches this instance.
        Concept: Filtering for relationships - dynamically retrieves related objects.
        """
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        """
        Returns a list of unique Magazine instances that this author has contributed to.
        Achieved by collecting magazines from the author's articles and removing duplicates.
        Concept: Many-to-many relationship through articles, ensuring uniqueness.
        """
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        """
        Creates and returns a new Article instance for this author.
        Takes a Magazine instance and a title string.
        This method encapsulates the creation of articles, maintaining the relationship.
        """
        return Article(self, magazine, title)

    def topic_areas(self):
        """
        Returns a list of unique topic areas (magazine categories) for this author's articles.
        If the author has no articles, returns None.
        Concept: Deriving data from relationships, with uniqueness and null handling.
        """
        if not self.articles():
            return None
        return list(set(magazine.category for magazine in self.magazines()))