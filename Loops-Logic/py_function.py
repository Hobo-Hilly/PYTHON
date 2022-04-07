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
