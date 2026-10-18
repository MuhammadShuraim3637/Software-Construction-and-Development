"""A small shopping cart with independent item storage per cart."""


class ShoppingCart:
    """Store products and calculate the total for one shopping cart."""

    def __init__(self):
        self.items = []

    def add_item(self, product_name, price, quantity):
        """Add a product to the cart."""
        self.items.append({
            "name": product_name,
            "price": price,
            "quantity": quantity,
        })

    def calculate_total(self):
        """Return the total price of all products in the cart."""
        return sum(
            item["price"] * item["quantity"]
            for item in self.items
        )


if __name__ == "__main__":
    first_cart = ShoppingCart()
    first_cart.add_item("Notebook", 3.50, 2)
    first_cart.add_item("Pen", 1.25, 4)

    second_cart = ShoppingCart()
    second_cart.add_item("Backpack", 24.99, 1)

    print(f"First cart total: {first_cart.calculate_total():.2f} Pkr")
    print(f"Second cart total: {second_cart.calculate_total():.2f} Pkr")