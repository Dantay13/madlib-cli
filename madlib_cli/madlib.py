from madlib_cli.template import parse_template, merge


def read_template(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"{file_path} not found.")


def main():
    print("Welcome to the Madlib CLI!")
    print("You'll be prompted to fill in parts of a story, and then you'll get to "
          "read the story with your words in it!")

    # Choose a template file
    choice = input("Choose a template: 1) Dark and Stormy Night or 2) Make Me a Video Game: ")
    if choice == "1":
        file_path = "../assets/dark_and_stormy_night_template.txt"
    elif choice == "2":
        file_path = "../assets/make_me_a_video_game_template.txt"
    else:
        print("Invalid choice. Exiting.")
        return

    # Read and parse the template
    template = read_template(file_path)
    stripped_template, parts = parse_template(template)

    # Get user input for each part
    user_words = []
    for part in parts:
        word = input(f"Please provide a {part}: ")
        user_words.append(word)

    # Merge user input with the template
    completed_madlib = merge(stripped_template, user_words)

    # Display the completed Madlib
    print("\nHere's your Madlib:\n")
    print(completed_madlib)

    # Write the completed Madlib to a new file
    with open("completed_madlib.txt", "w") as file:
        file.write(completed_madlib)

    print("\nYour Madlib has been saved to 'completed_madlib.txt'.")


if __name__ == "__main__":
    main()
