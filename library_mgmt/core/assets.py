""" This module defines all the assets or items in the library """

from dataclasses import dataclass

@dataclass
class LibraryAsset:
    """Represents an asset in the library such as a book, DVD, or magazine

    Attributes:
        asset_id (str): Unique identifier for the asset
        title (str): Title of the asset
        author (str): Author or creator of the asset
        isbn (str | None): International Standard Book Number, if applicable
        department (str): Department or category the asset belongs to
        publisher (str | None): Publisher of the asset
        type: Type of library item could be Books, DVDs, or Magzines, etc
    """

    asset_id: str
    title: str
    author: str
    isbn: str|None
    department: str
    publisher: str|None
    type: str = 'Books'


@dataclass
class Contact:
    """Stores contact details for a person - student/faculty/librarian

    Attributes:
        name (str): Full name of the person
        phone (str): Phone number
        email (str): Email address
    """

    name: str
    phone: str
    email: str


@dataclass
class Institution:
    """Represents a library institution or branch

    Attributes:
        name (str): Name of the institution
        code (str): Unique institution code
        address (str): Address of the institution
        phone (str): Contact Phone number of the institution
        email (str): Contact email address of the institution
    """

    name: str
    code: str
    address: str
    phone: str
    email: str
    

@dataclass
class Policy:
    """Defines borrowing and fee policies for the library.

    Attributes:
        borrow_days (int): Number of days an item can be borrowed
        late_fee_per_day (int): Fee charged per day after the due date
    """

    borrow_days: int
    late_fee_per_day: int


    