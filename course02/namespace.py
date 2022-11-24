a = 2

# def function():
#     global message
#     message = "Hello"
#     print(message)
#
#
# function()
# print(message)


def my_func():
    def my_func2():
        print(f"The second function: {msg}")

    global msg
    msg = "Hello"
    my_func2()
    print(f"The first function: {msg}")


my_func()
msg = "Hello 2"

print(msg)
