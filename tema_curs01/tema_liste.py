initial_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(f"Initial list: {initial_list}")

ascending_sorted_list = sorted(initial_list)
print(f"List sorted in ascending order: {ascending_sorted_list}")

descending_sorted_list = sorted(initial_list, reverse=True)
print(f"List sorted in descending order: {descending_sorted_list}")

print(f"Even elements from the initial list: {ascending_sorted_list[1::2]}")

print(f"Odd elements from the initial list: {descending_sorted_list[-1::-2]}")

print(f"The multiples of 3 from the initial list: {ascending_sorted_list[2::3]}")