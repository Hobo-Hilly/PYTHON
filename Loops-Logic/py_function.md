
#!/usr/bin/env python

def main():
    print "You are currently in the main function"
    choice = raw_input("Choose: [1], [2], [x]" )
    if choice == '1':
        func1()
    elif choice == '2':
        func2()
    elif choice == 'X':
        exit
    else:
            print "Wrong! Try again my friend!"
            main()

def func1():
    print "You are in function1"
    main()

def func2():
    print "You are in function2"
    main()

main()

# Python reads the code line by line until it hit it's first call to a function. So main() is the first line python acts on when parsing through the script here. you have to define a function BEFORE you call it in the script. This is why 'main()' is at the bottom of the script. Python has to read all the lines of code you used defining the function so that when it's called python know what to do.

------------------------------------------------------------



# here is POC on the py_function.py

Hilly@localhost:~/PYTHON/Loops-Logic$ ./py_function.py 
You are currently in the main function
Choose: [1], [2], [x]2
You are in function2
You are currently in the main function
Choose: [1], [2], [x]1
You are in function1
You are currently in the main function
Choose: [1], [2], [x]x
Wrong! Try again my friend!
You are currently in the main function
Choose: [1], [2], [x]34
Wrong! Try again my friend!
You are currently in the main function
Choose: [1], [2], [x] x

