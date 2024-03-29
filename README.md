# madlib-cli

Author: Danner Taylor

## problem Domain:

create a command line application that takes advantage of Python’s built in capabilities for reading and writing files.

## Feature Tasks and Requirements

- Create a file called `madlib.py` at root of `madlib_cli` folder, which will contain all of the Python code that you will write relating to your Madlib game.
- Keeping in mind the concept of Single Responsibility Principle, build a command line tool which will perform the following:
  - Print a welcome message to the user, explaining the Madlib process and command line interactions
  - Read a template Madlib file, and parse that file into usable parts.
  - Prompt the user to submit a series of words to fit each of the required components of the Madlib template.
  - With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
  - After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
  - Write the completed text to a new file on your file system (in the repo).
  - Note: A smaller example file is included as well which can be handy when developing/testing.

## Testing Details

You are NOT required to test terminal input/output, AKA print and input functions.

However you ARE expected to have meaningful tests for your application.

So how can we skip testing print and output functionality while still proceeding with confidence?

The resolution to that dilemma is to break down your code so that it is more easily testable.

- Create and test a read_template function that takes in a path to text file and returns a stripped string of the file’s contents.
- read_template should raise a FileNotFoundError if path is invalid.
- Create and test a parse_template function that takes in a template string and returns a string with language parts removed and a separate tuple of those language parts.
- Create and test a merge function that takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.