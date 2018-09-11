
def read_int(message):
    value = input(message)
    while not value.isdigit():
        value = input(message)
    return int(value)

TICKET_PRICE = 10
tickets_remaining = int(100)
while tickets_remaining >0:
    name = input("what is your name?: ")
    print("Hello {}, there are currently {} tickets remaining".format(name, tickets_remaining))
    cart_tickets = int(0)
    tickets_remaining = tickets_remaining - cart_tickets

    cart_tickets = read_int("How many tickets would you like?  ")

    while tickets_remaining >= 1 and cart_tickets > 0:
        if cart_tickets > tickets_remaining:
            print("There are only {} tickets available!".format(tickets_remaining))
            cart_tickets = cart_tickets - cart_tickets
        else:
            print("That will cost ${}".format(cart_tickets * TICKET_PRICE))
            print("You currently have {} tickets, and".format(cart_tickets), tickets_remaining, "are left.")
            keep_shopping = input("Would you like any more tickets? (Y/N)  ")
            if keep_shopping.lower() == "y":
                tickets_remaining >= 1
                more_tickets = read_int("How many?  ")
                cart_tickets = cart_tickets + more_tickets
            if keep_shopping.lower() == "n":
                checkout = input("Proceed to checkout? (Y/N)  ")
                if checkout.lower() == "y":
                    print("Sold")
                    tickets_remaining -= cart_tickets
                    cart_tickets = 0
                else:
                    keep_shopping = input("Would you like to keep shopping? (Y/N)  ")
                    if keep_shopping.lower() == "n":
                        cart_tickets -= cart_tickets
        if cart_tickets == 0:    
            print("Your cart is currently empty")
    print("{} Tickets Remaining".format(tickets_remaining))


if tickets_remaining == 0:
    print("Tickets are sold out")
    

    