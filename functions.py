
    

    

# This file contains the functions used in our singer program.


def addsingers(singers_list):

    # Ask the user for the singer's name and song
    # .upper() converts the input to uppercase
    singers = input("Enter the name of a singer: ").upper()
    song = input("Enter the name of a song: ").upper()

    # Check if either the singer name or song is empty
    if not singers or not song:
        print("Not allowed. Add a valid name")

    else:
        # Add both values together as a tuple inside the list
        # Example: ("ATIF ASLAM", "TAJDAAR-E-HARAM")
        singers_list.append((singers, song))

        print("Singer added successfully.")
        print(f"List of singers: {singers_list}")
        print(f"Name {singers}")
        print(f"Song {song}")


def removesingers(singers_list):

    # pop(0) removes the first item from the list
    # Index 0 always represents the first item
    singers_list.pop(0)

    print(f"List of singers after remove: {singers_list}")


def display_singers(singers_list):

    # If the list is empty, there is nothing to display
    if not singers_list:
        print("No singers in the list. Add the singers first.")

    else:

        # Go through each singer in the list
        for singer in singers_list:

            # singer[0] is the singer's name
            # singer[1] is the song name
            print(f"{singer[0]} - {singer[1]}")

        # [0] gets the first tuple in the list
        # [0][0] gets the singer name from that tuple
        # [0][1] gets the song from that tuple

        print(f"{singers_list[0][0]} is the singer at top of the list")
        print(f"{singers_list[0][1]} is the song at top of the list")