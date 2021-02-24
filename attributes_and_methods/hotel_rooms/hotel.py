from attributes_and_methods.hotel_rooms.room import Room


class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room_number == room.number:
                result = room.take_room(people)
                if result == True:
                    self.guests += people
                    return
                return result

    def free_room(self, room_number):
        for room in self.rooms:
            if room_number == room.number:
                guests = room.guests
                result = room.free_room()
                if result == True:
                    self.guests -= guests

    def print_status(self):
        free_rooms = map(str, [room.number for room in self.rooms if not room.is_taken])
        taken_rooms = map(str, [room.number for room in self.rooms if room.is_taken])
        print(f"Hotel {self.name} has {self.guests} total guests")
        print(f"Free rooms: {', '.join(free_rooms)}")
        print(f"Taken rooms: {', '.join(taken_rooms)}")


hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

hotel.print_status()
