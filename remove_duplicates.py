def remove_duplicates(sequence):
    identified = set()
    result = []
    for i in sequence:
        if i not in identified:
            result.append(i)
            identified.add(i)
    return result

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result) 