from calendar import day_name
import csv
import sys
from tkinter import dnd
from typing import Sequence


def main():
    strs = []
    counts = []
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("missing command line argument")
        sys.exit()
        
    # TODO: Read database file into a variable
    file = open(sys.argv[1], "r") 
    database = csv.DictReader(file)
    strs = database.fieldnames[1:]
    
    with open(sys.argv[2], "r") as sequence:
    
        # TODO: Read DNA sequence file into a variable
        dna = sequence.read()
    dna_strs = {}
    for str in strs:
        dna_strs[str] = longest_match(dna, str)

    for row in database:
        if all(dna_strs[str] == int(row[str]) for str in dna_strs):
            print(row["name"])
            file.close()
            return
    print("no match")
    file.close()


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
