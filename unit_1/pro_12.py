#Write a program to display the use of local, global and nonlocal variables.

x = 10

def show_global():
    print("Global variable inside function:", x)

def show_local():
    x = 20   
    print("Local variable:", x)

def show_nonlocal():
    x = 30   

    def inner():
        nonlocal x
        x = 40
        print("Nonlocal variable (inside inner function):", x)

    inner()
    print("Value after inner function (nonlocal):", x)



print("Global variable:", x)

show_global()
show_local()
show_nonlocal()

print("Global variable after functions:", x)
