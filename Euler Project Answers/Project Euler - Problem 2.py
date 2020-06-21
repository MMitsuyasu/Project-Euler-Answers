# Project Euler: Problem 2

## Even Fibonacci Numbers:
# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
#     1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

# Solving with Python (3.8.1)

############################################################################

## Practice work

# Problem parts
#    Fibonacci sequence <= 4 million
#    Find SUM of EVEN valued terms

# Strategy
#    Process to identify Fibonacci numbers
#    Process to determine if number is even
#    Add even numbers together


## Identify Fibonacci numbers

#fibA = 0
#fibB = 1
#fibNew = 0

# Using For Loop
#for x in range(10):
#    fibNew = fibA + fibB
#    print(fibNew)
#    fibA = fibB
#    fibB = fibNew

# Using While Loop
#while fibNew <= 100:
#    fibNew = fibA + fibB
#    print(fibNew)
#    fibA = fibB
#    fibB = fibNew


## Determine if value is even

#def isEven(x):
#   if x % 2 == 0:
#       return True

# Testing function
#x = 2  
#if isEven(x) == True:
#    print("It's even")
#else:
#    print("it's odd")
    

## Identify Even Fibonacci numbers

#fibA = 0
#fibB = 1
#fibNew = 0

# Using While Loop
#while fibNew <= 100:
#    fibNew = fibA + fibB
#    fibA = fibB
#    fibB = fibNew
#    print(fibNew)
#    if isEven(fibNew) == True:
#        print("It's even!")


############################################################################
############################################################################

## Official Solution Used

## SOLUTION: Adding even Fibbonacci numbers (putting it all together)

def isEven(x):
   if x % 2 == 0:
       return True

fibA = 0
fibB = 1
fibNew = 0

total = 0
limit = 4000000

while fibNew <= limit:
    fibNew = fibA + fibB
    fibA = fibB
    fibB = fibNew
    print(fibNew)
    if fibNew <= limit and isEven(fibNew) == True:
        total = total + fibNew

print("Toal is %d" % total)


############################################################################
############################################################################

## SOLUTION NOTES

# If put if statement before generating new number,
#    wouldn't have to include limit check twice
#    i.e
#       while fibNew <= limit:
#           if isEven(fibNew) == True:
#               total = total + fibNew
#           fibNew = fibA + fibB
#           fibA = fibB
#           fibB = fibNew
# I'd thought I'd have to include an "else" statement
#    and would therefore have to put the code for generating newFib twice
#        (in both the "if" and the "else" statements)
#    I forgot that if I'd just outdented to parallel, would run next

# Could have put test for even-ness directly in
#    i.e.
#        while fibNew <= limit:
#            if fibNew % 2 == 0
#                total = total + fibNew
#            ...
# I'd generated the function to test even-ness
#    b/c I thought I'd have to run it in both an "if" and an "else" statement

# Because Fibonacci sequence is even every 3rd number, can simply add each 3rd
#    i.e.
#       fibA = 1
#       fibB = 1
#       fibC = fibA + fibB
#
#       total = 0
#       limit = 4000000
#
#       while fibC <= limit:
#           total = total + fibC
#           fibA = fibB + fibC
#           fibB = fibC + fibA
#           fibC = fibA + fibB
#
#       print("Toal is %d" % total)
# I did notice the every 3rd number pattern,
#    but hadn't considered how I could set up a sequence to calculate this
#    Until I really thought about the order in the example,
#       I still thought the multiple references might throw the calculations off
#       But it works
#           Total uses numbers from previous set
#           Next 3 numbers are generated in order
#           Aren't changed until used, or are using numbers from current set

# Terms of Fibonacci sequence can be written as a function of any previous terms
#    Rewrite component terms as a sum of previous terms
#        Can combine and rewrite until establish function of target terms
#        Since even numbers occur every 3rd term
#            Aim for the 3rd and 6th previous terms of Fibonacci sequence
#                (the first and second previous even terms)
#        Proof
#            A, B, C, D, E, F
#            6, 5, 4, 3, 2, 1
#
#            G = F + E
#              = (E+D) + E
#              = 2E + D
#              = 2(D+C) + D
#              = 2D + 2C + D
#              = 3D + 2C
#              = 3D + C + C
#              = 3D + C + (B + A)
#              = 3D + (C + B) + A
#              = 3D + D + A
#              = 4D + A
#    Can use this equation so program only has to generate even terms
#        fibA = 2
#        fibB = 8
#        fibC = 0
#
#        limit = 4000000
#        total = fibA + fibB
#
#        while fibC <= limit:
#            total = total + fibC
#            fibC = (4*fibB) + fibA
#            fibA = fibB
#            fibB = fibC
#            print(fibC)
#
#        print("The total is %d" % total)
#    

