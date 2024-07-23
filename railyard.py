# no track can have more than one locomotive
# locomotive always at head
# any cars in a track are always connected together and far right
# can only cut 'from' with locomotive 'to' track without locomotive
# moving x cars means moving cars + locomotive, x + 1
# all departed is win condition
# only departs: at least one locomotive + car AND all cars same destination
# if move empty, move only the locomotive
# syntax: move 0 1 2 (move 0 cars (locomotive only) from track 1 to 2)

# File path: railyard.py

def read_yard_file(file_name):
    try:
        with open(file_name, 'r') as file:
            tracks = [line.strip() for line in file.readlines()]
        return tracks
    except FileNotFoundError:
        print(f"Error: The yard file '{file_name}' doesn't exist.")
        exit(1)

def initialize_yard(tracks):
    yard = []
    for track in tracks:
        content = list(track.strip('-'))
        yard.append(content[::-1])  # reverse to make the locomotive at index 0
    return yard

def print_yard(yard):
    for i, track in enumerate(yard):
        track_str = ''.join(track[::-1])  # reverse back for display
        print(f"{i + 1}: {track_str}")
    print(f"Locomotive count: {sum(1 for track in yard if 'T' in track)}")
    print(f"Destination count: {len(set(car for track in yard for car in track if car.islower()))}")

def handle_move_command(yard, count, from_track, to_track):
    from_track -= 1
    to_track -= 1
    count = int(count)
    
    if from_track == to_track:
        print("Error: The to-track and from-track are the same.")
        return
    if count < 0:
        print("Error: The user asks to move a negative number of cars.")
        return
    if not yard[from_track] or 'T' not in yard[from_track]:
        print("Error: The from-track is empty, or doesn’t have a locomotive.")
        return
    if yard[to_track] and 'T' in yard[to_track]:
        print("Error: The to-track already has a locomotive.")
        return
    if len(yard[from_track]) < count + 1:  # +1 for the locomotive
        print("Error: The from-track doesn’t have enough cars to satisfy the required move.")
        return
    if len(yard[to_track]) + count + 1 > len(yard[to_track]) + len('-'):
        print("Error: The to-track doesn’t have enough space to hold the moved cars (including the locomotive).")
        return

    # Perform the move
    moving_cars = yard[from_track][:count + 1]
    yard[from_track] = yard[from_track][count + 1:]
    yard[to_track] = moving_cars + yard[to_track]

    print(f"The locomotive on track {from_track + 1} moved {count} cars to track {to_track + 1}.")

    check_and_depart(yard)

def check_and_depart(yard):
    for i, track in enumerate(yard):
        if 'T' in track and len(set(car for car in track if car.islower())) == 1:
            destination = track[1] if len(track) > 1 else ''
            print(f"*** ALERT*** The train on track {i + 1}, which had {len(track) - 1} cars, departs for destination {destination}.")
            yard[i] = []

def handle_dump_command(yard):
    print("DEBUG OUTPUT:")
    for i, track in enumerate(yard):
        print(f"Track #{i}")
        print(f"Length: {len(track) + len('-')}")
        print(f"Contents: {track[::-1]}")

def main():
    yard_file = input("Enter the name of the yard file: ")
    tracks = read_yard_file(yard_file)
    yard = initialize_yard(tracks)

    while True:
        print_yard(yard)
        command = input("What is your next command? ").strip().split()

        if not command:
            print("Error: The command name is not valid.")
            continue
        
        action = command[0]
        
        if action == 'move':
            if len(command) != 4 or not command[1].isdigit() or not command[2].isdigit() or not command[3].isdigit():
                print("Error: The user didn’t provide the right number of arguments for the move command or one of the parameters was not an integer.")
                continue
            handle_move_command(yard, command[1], int(command[2]), int(command[3]))
        elif action == 'dump':
            handle_dump_command(yard)
        elif action == 'quit':
            print("Quitting!")
            break
        else:
            print("Error: The command name is not valid.")

if __name__ == "__main__":
    main()
