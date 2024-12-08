import sys

def read_and_display_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit()

def main():

    curr_file = "intro.txt"  # Start with the initial story file

    while True:
        # Read and display the current file
        read_and_display_file(curr_file)

        # Get user input for the next action
        user_input = input("\nWhat do you want to do? (type 'quit' to exit): ").strip().lower()

        # Handle the "quit" command
        if user_input == "quit":
            print("Exiting the story. Goodbye!")
            sys.exit()

        # Determine the next file to load based on user input
        # For simplicity, assume input is the name of the next file
        next_file = user_input + ".txt"

        # Update the current file to the next one
        curr_file = next_file

if __name__ == "__main__":
    main()
