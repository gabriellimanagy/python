# Open the file with colons
file = open("example.txt", "r", encoding="utf-8")

# Open the output files
part1_file = open("part1.txt", "a", encoding="utf-8")
part2_file = open("part2.txt", "a", encoding="utf-8")

# Read all lines from the file
lines = file.readlines()

# Iterate over all lines in the file
for line in lines:
    # Split the line into parts using ":"
    parts = line.split(":")
    
    # Check if the line contains ":" and has exactly two elements in the list
    if len(parts) == 2:
        # Write the first element to the part1.txt file
        part1_file.write(parts[0])
        
        # Write the second element to the part2.txt file
        part2_file.write(parts[1].rstrip("\n"))

# Close the files
part1_file.close()
part2_file.close()
file.close()
