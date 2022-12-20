num_calls = 0


def exercise(y):
    global num_calls
    num_calls = 3
    print(num_calls, '7')
    num_calls += 1
    return y * y


# print(num_calls, '12')
# print(exercise(4))
# print(num_calls, '14')
x = 1


def f():
    return x


# print(x)
# print(f())
z = [1, 2, "hello", "cinci", ["another", "list"]]
# print(len(z[3]))

x1 = (1, 2, 3)
# x1[1] = 4
# print(x)

a = [1, 2, 3]
b = [4, 5]
# print(a + b * 3)

x2 = [1, 2, 3, 4]
# print(x2[-1:])

x3 = [0, 1, [2]]
x3[2][0] = 3
x3[2].append(4)
x3[2] = 2
# print(x3)


def exercise2(i):
    for i in range(i):
        return i


x4 = exercise2(3)
# print(x4)

a1 = range(10)
y1 = [x * x for x in a1 if x % 2 == 0]
# print(y1)


def make_account():
    return {'balance': 0}


def deposit(account, amount):
    account['balance'] += amount
    return account['balance']


m = make_account()
# print(deposit(m, 10))
