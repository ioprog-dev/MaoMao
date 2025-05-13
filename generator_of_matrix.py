from itertools import product

def F(src_dict, in_string):
    # Create a new string based on the transformations in src_dict
    return ''.join(src_dict[char] for char in in_string)

matrix = [[], [], []]
src_dict_a = {
    "Ц": "Г",
    "Г": "Ц",
    "Т": "А",
    "А": "Т"
}
src_dict_b = {"А":"У",
              "Т":"А",
              "Г":"Ц",
              "Ц":"Г"}

# Generate all combinations of 'А', 'Ц', 'Т', 'Г' with a length of 3
matrix[0] = list(map(lambda x: "".join(x), product(['А', 'Ц', 'Т', 'Г'], repeat=3)))
# Apply the transformation using src_dict_a
matrix[1] = list(map(lambda x: F(src_dict_a, x), matrix[0]))
# Uncomment the next line if you want to apply src_dict_b (currently empty)
matrix[2] = list(map(lambda x: F(src_dict_b, x), matrix[1]))

print(matrix)
