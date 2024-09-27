input_string = input("Введите числа через пробел: ")
array = list(map(int, input_string.split()))
n = len(array)
max_length = 1
current_length = 1
for i in range(1, n):
    if (array[i] >= array[i - 1] and array[i] % 2 != 0) or (array[i] % 2 == 0):
        current_length += 1
        max_length = max(max_length, current_length)
    else:
         current_length = 1

current_length = 1
for i in range(1, n):
    if (array[i] <= array[i - 1] and array[i] % 2 != 0) or (array[i] % 2 == 0):
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 1
print("Длина макс последовательности:", max_length)
