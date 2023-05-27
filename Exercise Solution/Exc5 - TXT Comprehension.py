input_file = open('passage.txt', 'r+')

no_lines = 0
chars_count = {}

for line in input_file.readlines():
    no_lines += 1

    for c in line:
        if c.isalpha():
            chars_count[c.lower()] = chars_count.get(c.lower(), 0) + 1

# sort by value
chars_count = dict(sorted(chars_count.items(), key=lambda x: x[1]))

print(no_lines)
print('Max repeat char: ', max(chars_count.items(), key=lambda x: x[1]), 'Min repeat char:', min(chars_count.items(), key=lambda x: x[1]))
print(chars_count)
