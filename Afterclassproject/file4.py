input_file = open("MY_file.txt", "r")
output_file = open("Updated_file.txt", "w")

line_seen_so_far = set()

for line in input_file:
    if line not in line_seen_so_far:
        output_file.write(line)
        line_seen_so_far.add(line)

input_file.close()
output_file.close()