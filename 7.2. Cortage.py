def add_num(seq, number):
    seq =list(seq)  # Convert tuple to list
    for i_num in range(len(seq)):
        seq[i_num] += number
    return tuple(seq)  # Convert back to tuple

original_tuple = [1, 2, 3, 4, 5]
changeList = add_num(original_tuple, 10)
# Example usage
print("Original list:", original_tuple)
print("Changed list:", changeList)  