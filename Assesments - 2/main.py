from product_manager import ProductManager
from customer import Customer

def main():
    while True:
        print("\n1. Product Manager\n2. Customer\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            product_manager = ProductManager()
            print("1. Manage All Product Stocks\n2. View All Stocks\n3. Logout")

            product_manager_choice = input("Enter your choice: ")
            if product_manager_choice == '1':
                product_manager.manage_all_stocks()
            elif product_manager_choice == '2':
                product_manager.view_all_stocks()
            elif product_manager_choice == '3':
                print("Logging out Product Manager.")
            else:
                print("Invalid choice. Please try again.")

        elif choice == '2':
            customer = Customer()
            print("1. Purchase Stock\n2. View All Orders\n3. View all stocks\n4. Logout")

            customer_choice = input("Enter your choice: ")
            if customer_choice == '1':
                customer.purchase_stock()
            elif customer_choice == '2':
                customer.view_all_orders()
            elif customer_choice == '3':
                customer.view_all_stocks()
            elif customer_choice == '4':
                print("Logging out Customer.")
            else:
                print("Invalid choice. Please try again.")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()