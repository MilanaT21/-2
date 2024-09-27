def sum_0(numbers):
    last_index = -1
    last_index_2 = -1

    for i in range(len(numbers)):
        if numbers[i] == 0:
            last_index_2 = last_index
            last_index = i
    if last_index - last_index_2 == 1:
        return 0
    if last_index != -1 and last_index_2 != -1:
        return sum(numbers[last_index_2 + 1:last_index])
    return 0

numbers = [1, 2, 0, 3, 4, 0, 5, 6, 5, 1, 5, 7, 0, 5]
print(sum_0(numbers))
