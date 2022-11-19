# ex 1

def sum_of_parameters(*args, **kwargs):
    param_sum = 0

    for arg in args:
        if type(arg) in [int, float]:
            param_sum += arg

    for key in kwargs:
        if type(kwargs[key]) in [int, float]:
            param_sum += kwargs[key]

    return param_sum


print("Ex 1\n")
print(f"The output of sum_of_parameters(1, 5, -3, 'abc', [12, 56, 'cad']) "
      f"is {sum_of_parameters(1, 5, -3, 'abc', [12, 56, 'cad'])}")

print(f"The output of sum_of_parameters() is {sum_of_parameters()}")

print(f"The output of sum_of_parameters(2, 4, 'abc', param_1=2) is {sum_of_parameters(2, 4, 'abc', param_1=2)}\n")


# ex 2


def recursive_sum(n):
    return 0 if n == 0 else n + recursive_sum(n - 1)


def even_recursive_sum(n):
    if n % 2 == 1:
        return even_recursive_sum(n - 1)
    return 0 if n == 0 else n + even_recursive_sum(n - 2)


def odd_recursive_sum(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return odd_recursive_sum(n - 1)
    return 1 if n == 1 else n + odd_recursive_sum(n - 2)


print("Ex 2\n")
print(f"The output of recursive_sum(10) is {recursive_sum(10)}")

print(f"The output of even_recursive_sum(7) is {even_recursive_sum(7)}")
print(f"The output of even_recursive_sum(1) is {even_recursive_sum(1)}")

print(f"The output of odd_recursive_sum(6) is {odd_recursive_sum(6)}")
print(f"The output of odd_recursive_sum(0) is {odd_recursive_sum(0)}\n")


# ex 3
def return_integer_value():
    value = input("Enter a value: ")
    try:
        return int(value)
    except ValueError:
        return 0


print("Ex 3\n")
print(f"Value entered = {return_integer_value()}")
print(f"Value entered = {return_integer_value()}")
