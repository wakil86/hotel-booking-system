import datetime

# Sample data
rooms = {
    101: {"type": "Single", "price": 100, "available": True},
    102: {"type": "Double", "price": 150, "available": True},
    103: {"type": "Suite", "price": 250, "available": True},
}

reservations = {}

# Function to check availability
def check_availability():
    print("Available Rooms:")
    for room_id, details in rooms.items():
        if details["available"]:
            print(f"Room {room_id}: {details['type']} - ${details['price']}")

# Function to book a room
def book_room(room_id, user_name, check_in, check_out):
    if room_id in rooms and rooms[room_id]["available"]:
        rooms[room_id]["available"] = False
        reservations[room_id] = {
            "user": user_name,
            "check_in": check_in,
            "check_out": check_out,
        }
        print(f"Room {room_id} booked successfully!")
    else:
        print("Room not available!")

# Function to cancel a reservation
def cancel_reservation(room_id):
    if room_id in reservations:
        del reservations[room_id]
        rooms[room_id]["available"] = True
        print(f"Reservation for room {room_id} canceled.")
    else:
        print("No reservation found for this room.")

# Main Menu
def main():
    while True:
        print("\nHotel Room Booking System")
        print("1. Check Room Availability")
        print("2. Book a Room")
        print("3. Cancel a Reservation")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            check_availability()
        elif choice == "2":
            room_id = int(input("Enter Room ID: "))
            user_name = input("Enter Your Name: ")
            check_in = input("Enter Check-in Date (YYYY-MM-DD): ")
            check_out = input("Enter Check-out Date (YYYY-MM-DD): ")
            book_room(room_id, user_name, check_in, check_out)
        elif choice == "3":
            room_id = int(input("Enter Room ID to Cancel: "))
            cancel_reservation(room_id)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
