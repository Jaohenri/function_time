"""Implements the Stock class, which represents a product inventory."""

class Stock:
    """Class that represents the stock control of a product.

        Allows controlling the product stock, with methods like sell and replenish while
        ensuring that the stock of a product is never a negative number.
    """

    def __init__(self, name: str, stock: int):
        """Initialize a product with an initial stock quantity.

        Args:
            name (str): Name of the product.
            stock (int): Initial product stock.

        Raises:
            ValueError: If the initial stock is negative.
        """

        self.name = name
        self.stock = stock

    @property
    def stock(self) -> int:
        """Get the current stock quantity.

        Returns:
            int: Current product stock.
        """
        return self.__stock

    @stock.setter
    def stock(self, new_stock: int) -> None:
        """Sets a new stock quantity

        Ensures that the is stock is never negative.
        If it receives a negative value, a exception is raised.

        Args:
            new_stock (int): New product stock quantity

        Raises:
            ValueError: If the new product quantity is less than 0.
        """
        if new_stock < 0:
            raise ValueError("Stock can't be negative")
        self.__stock = new_stock

    def sell(self, quantity: int) -> None:
        """Represents a sale of the product.

        Raises an execption if the quantity of the sale is greater than the product stock.

        Args:
            quantity (int): Quantity of the product sold.

        Raises:
            ValueError: If the sale makes the stock negative.
        """
        self.stock -= quantity
        print(f"You sold {quantity} {self.name} units. "
              f"The new stock for this item is {self.stock}")

    def replenish(self, quantity: int) -> None:
        """Increses the product stock based on the quantity given.

        Args:
            quantity (int): Quantity of Stock that will be replenished.
        """
        self.stock += quantity
        print(f"You made a replacement order for {quantity} {self.name} units. "
        f"The new stock for this item is {self.stock}")

if __name__ == "__main__":
    ps5 = Stock("PS5", 10)
    ps5.sell(5)
    ps5.replenish(3)
