# reading files:
# You can read a file with the open function
# open returns a file object to you
# You can read a file object with the read method

file = open("../random.txt")
read = file.read()
file.seek(1)
read_again = file.read()
file.seek(0)

lines = file.readlines()
file.seek(0)
line2 = file.readlines(2)
print(file, read)
print("reading again", read_again)
print("line1--:", lines)
print("line2--:", line2)

# Python reads files by using a cursor
# This is like the cursor you see when you're typing
# After a file is read, the cursor is at the end
# To move the cursor, use the seek method
# To read only part of a file, pass a number of characters into read, or use readline
# To get a list of all lines, use readlines

# close a file
# You can close a file with the close method
# You can check if a file is closed with the closed attribute
# Once closed, a file can't be read again
# Always close files - it frees up system resources!
file.close()

with open("../random.txt", "w") as file:
    # writing to files:
    file.write("I am writing---------\n")
    file.write("I am writing---------\n")

# IMPORTANT: If you open the file again to write, the original contents will be deleted!

# Modes for Opening Files
#
# r - Read a file (no writing) - this is the default
# w - Write to a file (previous contents removed)
# a - Append to a file (previous contents not removed)
# r+ - Read and write to a file (writing based on cursor)

# Reading CSV Files
# CSV files are a common file format for tabular data
# We can read CSV files just like other text files
# Python has a built-in CSV module to read/write CSVs more easily

# Readers accept a delimiter kwarg in case your data isn't separated by commas.

# writing to csv
# writer - creates a writer object for writing to CSV
# writerow - method on a writer to write a row to the CSV
from csv import writer
with open("fighters.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Character", "Move"])
    csv_writer.writerow(["Ryu", "Hadouken"])

# DictWriter - creates a writer object for writing using dictionaries
# fieldnames - kwarg for the DictWriter specifying headers
# writeheader - method on a writer to write header row
# writerow - method on a writer to write a row based on a dictionary

from csv import DictWriter
with open("example.csv", "w") as file:
    headers = ["Character", "Move"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Character": "Ryu",
        "Move": "Hadouken"
    })

# Using lists often means less code
# Using dictionaries is often more explicit




