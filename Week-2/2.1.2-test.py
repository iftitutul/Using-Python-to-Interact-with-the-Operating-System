#!/usr/bin/env python3

#!/usr/bin/env python3

# In this exercise, we will test your knowledge of reading and writing files by playing around with some text files.

# Let's say we have a text file containing current visitors at a hotel. We'll call it, guests.txt. Run the following code to create the file. The file will automatically populate with each initial guest's first name on its own line.

guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")

guests.close()

# No output is generated for the above code cell. To check the contents of the newly created guests.txt file, run the following code.

with open("guests.txt") as guests:
    for line in guests:
        print(line)
