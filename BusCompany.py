class Bus:
    def __init__(self, destination, num_seats):
        self.destination = destination
        self.num_seats = num_seats
        self.seats_booked = []

    def book_seat(self, seat_number):
        if seat_number in self.seats_booked:
            return "Seat already booked"
        elif seat_number > self.num_seats:
            return "Invalid seat number"
        else:
            self.seats_booked.append(seat_number)
            return "Seat booked successfully"
buses = [Bus("From Jabalia To Gaza", 50), Bus("From Gaza To KhanYounos", 40), Bus("From Gaza To Nosirat", 35)]

def display_buses():
    for i, bus in enumerate(buses):
        print(f"{i+1}: {bus.destination} ({bus.num_seats} seats)")
def book_seat():
    display_buses()
    bus_choice = int(input("Enter the number of the bus you want to book a seat on: "))
    selected_bus = buses[bus_choice-1]
    seat_choice = int(input("Enter the seat number you want to book: "))
    result = selected_bus.book_seat(seat_choice)
    print(result)
def main():
    while True:
        print("Welcome to the bus booking app")
        print("1. Display buses")
        print("2. Book a seat")
        print("3. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            display_buses()
            print("--------------------------------------------------------")
        elif choice == 2:
            book_seat()
            print("--------------------------------------------------------")
        elif choice == 3:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
