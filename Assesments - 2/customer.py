from sqlalchemy import values
from user import User

class Customer(User):
    def __init__(self):
      super().__init__('Customer')

    def purchase_stock(self):
      try:
        product_id = input("Enter the product ID you want to purchase: ")
        product_name = input("Enter the product name you want to purchase: ")
        quantity = int(input("Enter the quantity: "))

        stock_query = "SELECT * FROM products WHERE product_id=%s"
        product = self._db.fetch_data(stock_query, (product_id,))

        if product and 'quantity' in product:
          stock_quantity = product['quantity']
          if stock_quantity >= quantity:
            updated_quantity = stock_quantity - quantity
            update_stock_query = "UPDATE products SET quantity=%s WHERE product_id=%s"
            self._db.execute_query(update_stock_query, (updated_quantity, product_id))

            order_query = "INSERT INTO orders (customer_id, product_id, quantity) VALUES (%s, %s, %s)"
            self._db.execute_query(order_query, (self.customer_id, product_id, quantity))

            print("Purchase successful. Order placed.")
          else:
            print("Not enough stock available.")
        else:
          print("Product not found or out of stock.")
      except ValueError:
        print("Invalid input. Please enter a valid quantity.")

    def view_all_orders(self):
      customer_id = self.customer_id
      orders_query = "SELECT * FROM orders WHERE customer_id=%s"
      orders_data = self._db.fetch_data(orders_query, (customer_id,))
      if not orders_data:
        print("No orders found.")
        return
      print("\nAll Orders:")
      for order in orders_data:
        print(f"Order ID: {order['order_id']}, Product ID: {order['product_id']}, Quantity: {order['quantity']}, Total Cost: ${order['total_cost']}")
        pass

    def place_order(self, product_id, quantity,total_cost):
      customer_id = self.customer_id
      insert_order_query = "INSERT INTO orders (customer_id, product_id, quantity, total_cost) VALUES (%s, %s, %s, %s)"
      self._db.execute_query(insert_order_query, (customer_id, product_id, quantity, total_cost))
      pass

    def view_all_stocks(self):
      query = "SELECT * FROM products"
      product = self._db.fetch_data(query)    
      if product:
        print("\nProduct ID\tProduct Name\tStock Quantity\tPrice")
        print("--------------------------------------------------")
        for products in product:
          print(f"{products[0]}\t\t{products[1]}\t\t{products[2]}\t\t{products[3]}")
      else:
        print("No products available.")
        pass
