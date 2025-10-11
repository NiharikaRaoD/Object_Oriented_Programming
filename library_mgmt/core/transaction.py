""" This module defines Transaction class for library borrows and returns """

from core.assets import LibraryAsset
from core.users import Person
from datetime import datetime


class Transaction:
    """Represents a borrowing or returning transaction in the library system

    Attributes:
        person (Person): The person performing the transaction
        item (LibraryAsset): The asset involved in the transaction
    """

    def __init__(self, person: Person, item: LibraryAsset):
        """Initializes a Transaction instance.

        Args:
            person (Person): The person performing the transaction
            item (LibraryAsset): The asset being borrowed or returned
        """
        self._person = person
        self._item = item
        self._id:str = None
        self._borrowdate:datetime = datetime.now()



    @property
    def person(self) -> Person:
        """Returns the person involved in the transaction

        Returns:
            Person: The person who borrowed or returned the item
        """
        return self._person
    
    @property
    def item(self) -> LibraryAsset:
        """Returns the item involved in the transaction

        Returns:
            LibraryAsset: The borrowed or returned asset
        """
        return self._item
