input_file = "input.txt"
# input_file = "example.txt"

word_search = []
with open(input_file) as f:
    for line in f.readlines():
        word_search.append([c for c in line.strip()])

directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

word_occurances = 0
word = "XMAS"
for i, line in enumerate(word_search):
    for j, char in enumerate(line):
        if char == word[0]:
            for direction in directions:
                # Set the starting point
                x, y = i, j

                # For the rest of the word
                for letter in word[1:]:
                    # Update the position
                    x += direction[0]
                    y += direction[1]

                    # Check if the position is out of bounds or the letter is different
                    if x < 0 or y < 0 or x >= len(word_search) or y >= len(line):
                        break
                    if word_search[x][y] != letter:
                        break

                # Executed if the loop didn't break
                else:
                    word_occurances += 1

print("Part 1: ", word_occurances)

# Look for the word MAS in the diagonals
diagonal_directions = [
    (-1, -1),
    (1, -1),
    (-1, 1),
    (1, 1),
]
word_occurances = 0
for i, line in enumerate(word_search):
    for j, char in enumerate(line):
        # Check if the "A" has been found
        if char == "A":
            # This is kept track to make sure the diagonals are on the same line
            m_directions = []
            s_directions = []

            for direction in diagonal_directions:
                x, y = i + direction[0], j + direction[1]

                if x < 0 or y < 0 or x >= len(word_search) or y >= len(line):
                    break

                if word_search[x][y] == "M":
                    m_directions.append(direction)
                elif word_search[x][y] == "S":
                    s_directions.append(direction)

            # Check to make sure diagonals are not opposite to each other
            if len(m_directions) == 2 and len(s_directions) == 2:
                if (
                    m_directions[0][0] == m_directions[1][0]
                    or m_directions[0][1] == m_directions[1][1]
                ):
                    word_occurances += 1


print("Part 2: ", word_occurances)
