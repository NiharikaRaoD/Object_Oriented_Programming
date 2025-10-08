""" This module contains all the necessary classes for maintaining Users of the Library Management System """

from abc import ABC, abstractmethod

class Person(ABC):
    """ Abstract base class representing a person who can borrow or return assets in a library """

    @abstractmethod
    def borrow_asset(self, asset_id: str) -> None:
        """ Borrow an asset from the library by its ID

        Args:
            asset_id (str): Unique identifier for the asset being borrowed
        
        Raises:
            NotImplementedError: If the subclass does not implement this method
        """
        pass

    @abstractmethod
    def return_asset(self, asset_id: str) -> None:
        """ Return an asset to the library by its ID

        Args:
            asset_id (str): Unique identifier for the asset being returned

        Raises:
            NotImplementedError: If the subclass does not implement this method
        """
        pass