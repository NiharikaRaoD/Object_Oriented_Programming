""" This module represents the Product class in the grocery store inventory """

from dataclasses import dataclass

@dataclass
class Product:
    """ Represents a product in the grocery store inventory

    Attributes:
        product_id (int): Unique identifier for the product
        name (str): Name of the product
        category (str): Category or department the product belongs to (e.g., Fruit, Dairy)
        price (float): Price of a single unit of the product
        quantity_in_stock (int): Number of units currently available in stock
        
    """

    product_id: int
    name: str
    category: str
    price: float
    quantity_in_stock: int

    def display_prod_info(self) -> None:
        """Display product details in a readable format."""

        print(
            f"{self.name} - ${self.price:.2f} "
            f"({self.category}) [{self.quantity_in_stock} in stock]"
        )