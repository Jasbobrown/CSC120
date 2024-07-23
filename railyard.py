# no track can have more than one locomotive
# locomotive always at head
# any cars in a track are always connected together and far right
# can only cut 'from' with locomotive 'to' track without locomotive
# moving x cars means moving cars + locomotive, x + 1
# all departed is win condition
# only departs: at least one locomotive + car AND all cars same destination
# if move empty, move only the locomotive
# syntax: move 0 1 2 (move 0 cars (locomotive only) from track 1 to 2)




class Railyard:
    def __init__(self, yard_file):
        self.tracks = self.load_yard(yard_file)
        self.locomotive_count = self.count_locomotives()
        self.destination_count = self.count_destinations()

    def load_yard(self, yard_file):
        tracks = []
        f = open(yard_file, 'r')
        for line in f:
            tracks.append(line.strip())
        return tracks

    def count_locomotives(self):
        count = 0
        for track in self.tracks:
            if 'T' in track:
                count += 1
        return count

    def count_destinations(self):
        destinations = set()
        for track in self.tracks:
            for car in track:
                if car.islower():
                    destinations.add(car)
        return len(destinations)

    def display_yard(self):
        for i in range(len(self.tracks)):
            print(f"{i + 1}: {self.tracks[i]}")
        print(f"Locomotive count: {self.locomotive_count}")
        print(f"Destination count: {self.destination_count}")

    def move(self, count, from_track, to_track):
        from_idx = from_track - 1
        to_idx = to_track - 1

        if not (0 <= from_idx < len(self.tracks)) or not (0 <= to_idx < len(self.tracks)):
            print("Error: Track number out of range.")
            return

        if 'T' not in self.tracks[from_idx]:
            print("Error: From track does not have a locomotive.")
            return

        if 'T' in self.tracks[to_idx]:
            print("Error: To track already has a locomotive.")
            return

        from_track_len = len(self.tracks[from_idx])
        if count < 0 or count > from_track_len:
            print("Error: Invalid number of cars to move.")
            return

        move_cars = self.tracks[from_idx][-count:] if count > 0 else ""
        self.tracks[to_idx] = self.tracks[to_idx][:-1] + move_cars + 'T'
        self.tracks[from_idx] = self.tracks[from_idx][:-count-1] + '-'

        self.handle_departure(to_idx)

    def handle_departure(self, track_idx):
        track = self.tracks[track_idx]
        if 'T' in track:
            cars = track[:-1].strip('-')
            if len(set(cars)) == 1:
                print(f"*** ALERT*** The train on track {track_idx + 1}, which had {len(cars)} cars, departs for destination {cars[0]}.")
                self.tracks[track_idx] = '-' * len(track)
                self.locomotive_count -= 1

    def dump(self):
        print("DEBUG OUTPUT:")
        for i in range(len(self.tracks)):
            print(f"Track #{i}")
            print(f"Length: {len(self.tracks[i])}")
            print(f"Contents: {list(self.tracks[i])}")

    def run(self):
        while self.locomotive_count > 0:
            self.display_yard()
            command = input("What is your next command? ").strip().split()
            if len(command) == 0:
                print("Error: Invalid command.")
                continue
            cmd = command[0]
            if cmd == 'move':
                if len(command) != 4:
                    print("Error: Invalid number of arguments for move.")
                    continue
                try:
                    count = int(command[1])
                    from_track = int(command[2])
                    to_track = int(command[3])
                    self.move(count, from_track, to_track)
                except ValueError:
                    print("Error: Move arguments must be integers.")
            elif cmd == 'dump':
                self.dump()
            elif cmd == 'quit':
                print("Quitting!")
                break
            else:
                print("Error: Invalid command.")

if __name__ == '__main__':
    yard_file = input("Enter the yard file name: ").strip()
    railyard = Railyard(yard_file)
    railyard.run()
