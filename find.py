# Part 1 - a small "find" tool (like a simplified `grep`).
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.

import argparse

# Finish find.py so that it prints every line of a file that contains a given pattern, 
# each prefixed with its line number (counting from 1).
# Then add an optional -i / --ignore-case flag that makes the match ignore upper/lower case.
def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")
    parser.add_argument("-i", "--ignore-case", action="store_true")

    args = parser.parse_args()

    pattern = args.pattern
    if args.ignore_case:
        pattern = pattern.lower()

    with open(args.filename) as f:
        for index, line in enumerate(f, start=1):
            line = line.rstrip("\n")

            compare = line
            if args.ignore_case:
                compare = compare.lower()

            if pattern in compare:
                print(f"{index}: {line}")
    
            
        
        



    # TODO: open args.filename and read its lines. For each line, numbered starting
    #   at 1, print "<number>: <line>" when the line contains args.pattern.
    #   If the --ignore-case flag was given, match without caring about upper/lower
    #   case (hint: compare the lowercased versions of both).
    # with open (args.filename) as f:
    #     for index, line in enumerate(f, start=1):
    #         line = line.rstrip("\n")
    #         compare = line
    #         if args.ignore_case:
    #             line = compare.lower()
            
    #         if pattern in compare:
    #          print(f"{index}: {line}")



if __name__ == "__main__":
    main()
