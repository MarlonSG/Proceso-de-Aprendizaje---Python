class Ticket:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def __str__(self):
        return f"ID: {self.id} | {self.name} | Price: ${self.price:.2f} | Available: {self.quantity}"
        
    def decrease_quantity(self, amount=1):
        if self.quantity >= amount:
            self.quantity -= amount
            return True
        return False
        
    def increase_quantity(self, amount=1):
        self.quantity += amount
        
class ShoppingCart:
    def __init__(self):
        self.items = {}  # Dictionary with ticket_id as key and quantity as value
        
    def add_ticket(self, ticket, quantity=1):
        if ticket.id in self.items:
            self.items[ticket.id] += quantity
        else:
            self.items[ticket.id] = quantity
            
    def remove_ticket(self, ticket_id, quantity=1):
        if ticket_id in self.items:
            if self.items[ticket_id] <= quantity:
                del self.items[ticket_id]
            else:
                self.items[ticket_id] -= quantity
            return True
        return False
        
    def get_total(self, ticket_system):
        total = 0
        for ticket_id, quantity in self.items.items():
            ticket = ticket_system.get_ticket_by_id(ticket_id)
            if ticket:
                total += ticket.price * quantity
        return total
        
    def clear(self):
        self.items = {}
        
    def is_empty(self):
        return len(self.items) == 0
        
class TicketSystem:
    def __init__(self):
        self.tickets = []
        self.cart = ShoppingCart()
        self.initialize_tickets()
        
    def initialize_tickets(self):
        # Add some sample tickets
        self.tickets.append(Ticket(1, "Concert - General Admission", 50.00, 100))
        self.tickets.append(Ticket(2, "Concert - VIP", 150.00, 20))
        self.tickets.append(Ticket(3, "Theater Show", 75.00, 50))
        self.tickets.append(Ticket(4, "Sports Event", 35.00, 200))
        self.tickets.append(Ticket(5, "Comedy Night", 25.00, 75))
        
    def display_tickets(self):
        print("\n=== AVAILABLE TICKETS ===")
        for ticket in self.tickets:
            print(ticket)
            
    def get_ticket_by_id(self, ticket_id):
        for ticket in self.tickets:
            if ticket.id == ticket_id:
                return ticket
        return None
        
    def buy_ticket(self, ticket_id, quantity=1):
        ticket = self.get_ticket_by_id(ticket_id)
        if not ticket:
            print(f"Error: Ticket with ID {ticket_id} not found.")
            return False
            
        if ticket.quantity < quantity:
            print(f"Error: Only {ticket.quantity} tickets available for {ticket.name}.")
            return False
            
        # Add to cart
        self.cart.add_ticket(ticket, quantity)
        print(f"{quantity} {ticket.name} ticket(s) added to your cart.")
        return True
        
    def display_cart(self):
        if self.cart.is_empty():
            print("\nYour shopping cart is empty.")
            return
            
        print("\n=== YOUR SHOPPING CART ===")
        total = 0
        for ticket_id, quantity in self.cart.items.items():
            ticket = self.get_ticket_by_id(ticket_id)
            subtotal = ticket.price * quantity
            total += subtotal
            print(f"{ticket.name} x {quantity} - ${subtotal:.2f}")
            
        print(f"\nTotal: ${total:.2f}")
        
    def checkout(self):
        if self.cart.is_empty():
            print("\nYour shopping cart is empty. Nothing to purchase.")
            return False
            
        # Display cart for confirmation
        self.display_cart()
        
        confirm = input("\nDo you want to complete this purchase? (y/n): ").lower()
        if confirm != 'y':
            print("Purchase cancelled.")
            return False
            
        # Process the purchase
        for ticket_id, quantity in list(self.cart.items.items()):  # Use list to avoid runtime error during iteration
            ticket = self.get_ticket_by_id(ticket_id)
            ticket.decrease_quantity(quantity)
            
        total = self.cart.get_total(self)
        
        print("\n=== PURCHASE SUCCESSFUL ===")
        print(f"Total amount: ${total:.2f}")
        print("Thank you for your purchase!")
        
        # Clear the cart after purchase
        self.cart.clear()
        return True
        
    def remove_from_cart(self, ticket_id, quantity=1):
        ticket = self.get_ticket_by_id(ticket_id)
        if not ticket:
            print(f"Error: Ticket with ID {ticket_id} not found.")
            return False
            
        if self.cart.remove_ticket(ticket_id, quantity):
            print(f"{quantity} {ticket.name} ticket(s) removed from your cart.")
            return True
        else:
            print(f"Error: Ticket with ID {ticket_id} not in your cart.")
            return False
            
def main():
    ticket_system = TicketSystem()
    
    while True:
        print("\n=== TICKET SYSTEM MENU ===")
        print("1. View Available Tickets")
        print("2. Buy Tickets")
        print("3. View Shopping Cart")
        print("4. Remove Ticket from Cart")
        print("5. Checkout")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            ticket_system.display_tickets()
            
        elif choice == '2':
            ticket_system.display_tickets()
            try:
                ticket_id = int(input("\nEnter the ID of the ticket you want to buy: "))
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Quantity must be positive.")
                else:
                    ticket_system.buy_ticket(ticket_id, quantity)
            except ValueError:
                print("Please enter valid numbers.")
                
        elif choice == '3':
            ticket_system.display_cart()
            
        elif choice == '4':
            ticket_system.display_cart()
            if not ticket_system.cart.is_empty():
                try:
                    ticket_id = int(input("\nEnter the ID of the ticket you want to remove: "))
                    quantity = int(input("Enter quantity to remove: "))
                    if quantity <= 0:
                        print("Quantity must be positive.")
                    else:
                        ticket_system.remove_from_cart(ticket_id, quantity)
                except ValueError:
                    print("Please enter valid numbers.")
                    
        elif choice == '5':
            ticket_system.checkout()
            
        elif choice == '6':
            print("\nThank you for using the Ticket System. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()

