variable = input("Input a number: ")
nr = [1,2,3]
try:
    if variable.isdigit():
        raise ValueError
    print(nr[3])
    variable = int(variable)
    print(a)
except ValueError:
    print("Exception ValueError")
    if variable.isdigit():
        variable = int(variable)
    a = None
except NameError:
    print("Exception NameError")
    a = None
except IndexError:
    print("Exception IndexError")
    print(nr[3:4])
except Exception:
    print("Exception")
else:
    print("There are no exceptions")
finally:
    print("This will always show up")
print(variable, 'variable')
print(a, 'a')
