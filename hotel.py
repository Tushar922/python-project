class Room:
    def __init__(self, room_number, capacity, price_per_night, is_occupied=False):
        self.room_number = room_number
        self.capacity = capacity
        self.price_per_night = price_per_night
        self.is_occupied = is_occupied
        
class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def find_available_rooms(self, capacity_needed):
        available_rooms = []
        for room in self.rooms:
            if not room.is_occupied and room.capacity >= capacity_needed:
                available_rooms.append(room)
        return available_rooms

    def book_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number and not room.is_occupied:
                room.is_occupied = True
                print(f"Room {room_number} booked successfully.")
                return
        print(f"No available room with number {room_number}.")

    def checkout_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number and room.is_occupied:
                room.is_occupied = False
                print(f"Room {room_number} checked out successfully.")
                return
        print(f"No occupied room with number {room_number}.")

    def display_all_rooms(self):
        print("All Rooms:")
        for room in self.rooms:
            print(f"Room Number: {room.room_number}, Capacity: {room.capacity}, Price per Night: {room.price_per_night}, Occupied: {'Yes' if room.is_occupied else 'No'}")

    def calculate_total_revenue(self):
        total_revenue = 0
        for room in self.rooms:
            if room.is_occupied:
                total_revenue += room.price_per_night
        return total_revenue

def display_menu():
    print("\nHotel Management System Menu:")
    print("1. Book a room")
    print("2. Check out a room")
    print("3. Display all rooms")
    print("4. Calculate total revenue")
    print("5. Exit")

if __name__ == "__main__":
    hotel = Hotel("Sample Hotel")

    # Add some rooms to the hotel
    room1 = Room(101, 2, 100)
    room2 = Room(102, 3, 150)
    room3 = Room(103, 1, 80)
    hotel.add_room(room1)
    hotel.add_room(room2)
    hotel.add_room(room3)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            capacity_needed = int(input("Enter the capacity needed: "))
            available_rooms = hotel.find_available_rooms(capacity_needed)
            if available_rooms:
                room_to_book = available_rooms[0]
                hotel.book_room(room_to_book.room_number)
            else:
                print("No available rooms matching the criteria.")
        elif choice == '2':
            room_number = int(input("Enter the room number to check out: "))
            hotel.checkout_room(room_number)
        elif choice == '3':
            hotel.display_all_rooms()
        elif choice == '4':
            total_revenue = hotel.calculate_total_revenue()
            print(f"Total Revenue: ${total_revenue}")
        elif choice == '5':
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice. Please choose again.")