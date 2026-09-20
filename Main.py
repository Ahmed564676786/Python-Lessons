
    


# Import the functions we created in functions.py
# This allows us to use them in this file

from functions import addsingers, display_singers, removesingers


# Create our starting list of singers
# Each tuple stores: (singer name, song name)

singers_list = [
    ("Ali Zafer", "Muskh"),
    ("Atif Aslam", "Na jana kab sa")
]


# while True keeps the program running continuously
# The loop will stop when we use break

while True:

    # Ask the user which operation they want
    # .upper() changes the input to uppercase
    # So "add", "Add", and "ADD" all become "ADD"

    choice = input(
        "Do you want to add or remove a singer? "
        "(add/remove/display/exit): "
    ).upper()


    # Add a new singer to the list
    if choice == "ADD":
        addsingers(singers_list)


    # Remove the first singer from the list
    elif choice == "REMOVE":
        removesingers(singers_list)


    # Display all singers and their songs
    elif choice == "DISPLAY":
        display_singers(singers_list)


    # Stop the program
    elif choice == "EXIT":
        print("You have exited the program.")
        break


    # If the user enters something that is not
    # ADD, REMOVE, DISPLAY, or EXIT
    else:
        print("Invalid choice. Please try again.")