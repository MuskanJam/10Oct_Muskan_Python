from user import User

class ProductManager(User):
    def __init__(self):
      super().__init__('Product Manager')

    def manage_all_stocks(self):
      print("Product Manager - Manage All Product Stocks")
      print("1. Add New Product")
      print("2. Update Product Stock")
      print("3. Delete Product")
      print("4. View All Products")
      print("5. Go back")
      choice = input("Enter your choice: ")
      if choice == '1':
        self.add_newproduct()
      elif choice == '2':
        self.update_stock()
      elif choice == '3':
        self.delete_product()
      elif choice == '4':
        self.view_all_stocks()
      elif choice == '5':
        return
      else:
        print("Invalid choice. Please try again.")
        self.manage_all_stocks()
        pass

    def add_newproduct(self):
      product_name = input("Enter the product name: ")
      stock_quantity = int(input("Enter the stock quantity: "))
      price = int(input("Enter the price: "))

      query = "INSERT INTO products (product_name, stock_quantity, price) VALUES (%s, %s, %s)"
      values = (product_name, stock_quantity, price)
      if self._db.execute_query(query, values):
        print("Product added successfully!")
      else:
        print("Failed to add the product.")

    def delete_product(self):
      self.view_all_stocks()
      product_id = int(input("Enter the product ID to delete: "))
      confirmation = input(f"Are you sure you want to delete product {product_id}? (Y/N): ").upper()
      if confirmation == 'Y':
        query = "DELETE FROM products WHERE product_id=%s"
        values = (product_id,)
        if self._db.execute_query(query, values):
          print("Product deleted successfully!")
        else:
          print("Failed to delete product.")
      elif confirmation == 'N':
        print("Deletion canceled.")
      else:
        print("Invalid choice. Please enter 'Y' or 'N'.")

    def update_stock(self, product_id, new_quantity):
      self.view_all_stocks()
      product_id = int(input("Enter the product ID to update stock: "))
      new_quantity = int(input("Enter the new stock quantity: "))

      query = "UPDATE products SET stock_quantity=%s WHERE product_id=%s"
      values = (new_quantity, product_id)
      if self._db.execute_query(query, values):
        print("Stock updated successfully!")
      else:
        print("Failed to update stock.")
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
