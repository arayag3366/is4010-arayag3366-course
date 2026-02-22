class Book:
    """
    A class representing a physical book.

    Attributes
    ----------
    current_year : int
        The current year used to calculate the age of the book (default is 2025).
    title : str
        The title of the book.
    author : str
        The author of the book.
    year : int
        The publication year of the book.
    """

    current_year = 2025

    def __init__(self, title: str, author: str, year: int):
        """
        Initialize a new Book instance.

        Parameters
        ----------
        title : str
            The title of the book.
        author : str
            The author of the book.
        year : int
            The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        """
        Return a user-friendly string representation of the book.

        Returns
        -------
        str
            The book information in the format: '"Title" by Author (Year)'.
        """
        return f"\"{self.title}\" by {self.author} ({self.year})"
    
    def get_age(self) -> int:
        """
        Calculate the age of the book based on the current year.

        Returns
        -------
        int
            The number of years since the book was published.
        """
        return self.current_year - self.year
    

class EBook(Book):
    """
    A class representing an electronic book (eBook), inheriting from Book.

    Attributes
    ----------
    file_size : int
        The size of the eBook file in megabytes (MB).
    """

    def __init__(self, title: str, author: str, year: int, file_size: int):
        """
        Initialize a new EBook instance.

        Parameters
        ----------
        title : str
            The title of the eBook.
        author : str
            The author of the eBook.
        year : int
            The publication year of the eBook.
        file_size : int
            The file size of the eBook in megabytes (MB).
        """
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self) -> str:
        """
        Return a user-friendly string representation of the eBook.

        Returns
        -------
        str
            The eBook information including file size in the format: 
            '"Title" by Author (Year) (File Size MB)'.
        """
        parent_str = super().__str__()
        return f"{parent_str} ({self.file_size} MB)"