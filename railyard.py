# I did it as a class because it seemed to make sense as such, I hope this is allowed as the documentation made no mention of classes.
# I also used sets as they make some simple things easier, again not sure of the tolerance regarding sets.

class Railyard:
    def __init__(self, yard_file):
        self.tracks = []
        self.locomotive_count = 0
        self.destination_count = 0
        self.load_yard(yard_file)
        self.update_counts()

    def load_yard(self, yard_file):
        try:
            f = open(yard_file, 'r')
            for line in f:
                track = list(line.strip())
                self.tracks.append(track)
            f.close()
        except FileNotFoundError:
            print(f"Error: The yard file '{yard_file}' does not exist.")
            exit(1)

    def update_counts(self):
        locos = 0
        for track in self.tracks:
            if "T" in track:
                locos += 1
        self.locomotive_count = locos
        destinations = set()
        for track in self.tracks:
            for car in track:
                if car.islower():
                    destinations.add(car)
        self.destination_count = len(destinations)

    def print_yard(self):
        i = 1
        for track in self.tracks:
            print(f"{i}: {''.join(track)}")
            i += 1
        print(f"Locomotive count: {self.locomotive_count}")
        print(f"Destination count: {self.destination_count}")

    def move_cars(self, count, from_track, to_track):
        from_track -= 1
        to_track -= 1
        if from_track == to_track:
            print("Error: The to-track and from-track are the same.")
            return
        if not (0 <= from_track < len(self.tracks) and 0 <= to_track < len(self.tracks)):
            print("Error: Invalid track number.")
            return
        if 'T' not in self.tracks[from_track]:
            print("Error: The from-track does not have a locomotive.")
            return
        if 'T' in self.tracks[to_track]:
            print("Error: The to-track already has a locomotive.")
            return
        if count < 0:
            print("Error: The user asks to move a negative number of cars.")
            return
        
        num_cars = 0
        for car in self.tracks[from_track]:
            if car.islower():
                num_cars += 1
        loco_index = self.tracks[from_track].index('T')

        if count > num_cars:
            print("Error: The from-track doesn’t have enough cars to satisfy the required move.")
            return
        
        cars_to_move = self.tracks[from_track][loco_index - count:loco_index + 1]

        remaining_space = self.tracks[to_track].count('-') - 2
        if remaining_space < num_cars:
            print("Error: The to-track doesn’t have enough space to hold the moved cars.")
            return
        
        existing_cars = []
        for car in self.tracks[to_track]:
            if car.islower():
                existing_cars.append(car)

        self.tracks[to_track] = ['-'] * (remaining_space - len(cars_to_move) + 1) + existing_cars + cars_to_move + ['-']
        self.tracks[from_track] = ['-'] * (count + 1) + self.tracks[from_track][:loco_index - count] + ['-']

        self.check_departure(to_track)
        self.update_counts()

    def check_departure(self, track_num):
        track = self.tracks[track_num]
        cars = track[:-1]
        temp = set()
        for car in cars:
            if car.islower():
                temp.add(car)
        if cars and len(temp) == 1:
            destination = cars[0]
            print(f"*** ALERT*** The train on track {track_num + 1}, which had {len(cars)} cars, departs for destination {destination}.")
            self.tracks[track_num] = ['-'] * len(track)

    def run(self):
        self.print_yard()
        while self.locomotive_count > 0:
            command = input("What is your next command? ").strip().lower()
            if command == "quit":
                print("Quitting!")
                break
            elif command == "dump":
                self.dump()
            elif command.startswith("move"):
                parts = command.split()
                if len(parts) != 4:
                    print("Error: Invalid number of arguments for the move command.")
                    continue
                try:
                    count, from_track, to_track = map(int, parts[1:])
                    self.move_cars(count, from_track, to_track)
                except ValueError:
                    print("Error: One of the parameters to move was not an integer.")
            self.print_yard()

if __name__ == "__main__":
    yard_file = input("Please give the name of the yard file: ").strip()
    railyard = Railyard(yard_file)
    railyard.run()
