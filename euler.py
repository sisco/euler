#Brian Sisco
#Started June 23, 2012
#Functions that solve problems in Project Euler

import math
from decimal import *

def prob1():
    #Sum numbers below 1000 that are multiples of 3 or 5
   sum = 0
   for i in range(1000):
       if i % 3 == 0 or i % 5 == 0:
	      sum += i
   return sum
   #returns 233168
   
def prob2():
    #Sum even-valued Fibonacci numbers below 4 million
    sum = 0
    a, b = 1, 2
    while b < 4000000:
        if a % 2 == 0:
            sum += a
        if b % 2 == 0:
            sum += b
        a = a + b
        b = a + b
    return sum
    #returns 4613732
    
def prob3():
    #find largest prime factor of a given number
    num = Decimal(600851475143)
    #primes = erato(Decimal.sqrt(num) + 1)
    primes = erato(Decimal.sqrt(num) * 20)
    for i in primes[::-1]:
        if num % i == 0:
            return i
    return 0
    #result: 6857
    
def erato(max):
    #Find primes using the Sieve of Eratosthenes
    #start with an array of the numbers up to the max
    grid = [i for i in range(max)]
    #for each number, we eliminate it's multiples, starting with two
    for i in range(2, max):
        for j in range(i * 2, max, i):
            #zero out the composite number
            grid[j] = 0
    primes = []
    for i in range(max):
        if grid[i] != 0:
            primes.append(i)
            #if i > 6000 and i < 7000:
                #print i
    print primes[-5:]
    #The 5 primes under 775146 * 20 are 15502847, 15502853, 15502891, 15502901, 15502913
    #The 5 primes under 2 million are 1999891, 1999957, 1999969, 1999979, 1999993
    return primes
    
def prob4():
    #Find the largest palindrome made from the product of two 3-digit numbers.
    max_x, max_y = 0, 0
    #Assumes that the factors will be above 800. If they are not, then the result will be 0, 0, 0
    for x in xrange(999, 800, -1):
        for y in xrange(999, x, -1):
            if is_palindrome(x * y):
                if x * y > max_x * max_y:
                    max_x = x
                    max_y = y
    return (max_x, max_y, max_x*max_y)
    #Result: 913 * 993 = 906609    
    
#Check if a number is a palindrome
def is_palindrome(x):
    x_str = str(x)
    if x_str == x_str[::-1]:
        return True
    return False
    
def prob5():
    #What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    #Combined brute force and hand tuning.
    #Starting with the result (2520) for all numbers up to 10, found the answer for up to 11.
    #Used that as the starting point for all numbers up to 12, etc.
    #It was taking too long to get from the penultimate result to the final one, so I just multiplied by 19.
    x = 12252240
    x = 232792560
    while True:
        for i in range(1, 20):
            if x % i != 0:
                break
        else:
            return x
        x += 1
    #result: 232792560
    
def prob6():
    #Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    #First we will start with the numbers for up through 10.
    sum_squares = 385
    sum = 55
    for i in range(11, 101):
        sum_squares += i*i
        sum += i
    #find the square of the sum
    sum *= sum
    return sum - sum_squares
    #result: 25164150
    
def prob7():
    #By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    #What is the 10 001st prime number?
    primes = erato(1000000)
    if len(primes) > 10000:
        print primes[10001]
    else:
        print "Need more!"
    return "Done!"
    #result: 104743
    
def prob8():
    #Find the greatest product of five consecutive digits in the 1000-digit number.
    grid = "73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"
    product = 0
    for i in range(len(grid) - 4):
        curr = int(grid[i]) * int(grid[i + 1]) * int(grid[i + 2]) * int(grid[i + 3]) * int(grid[i + 4])
        if curr > product:
            product = curr
    return product

def prob9():
    #There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    #Find the product abc.
    #Euclid's Formula: a = m**2 - n**2, b = 2mn, c = m**2 + n**2
    m, n = 2, 1
    a, b, c = 3, 4, 5
    while m < 200:
        while n < m:
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            if a + b + c == 1000:
                return (a, b, c, a*b*c, m, n)
            n += 1
        n = 1    
        m += 1
    return (a, b, c, a*b*c, m, n)    
    #result: 375, 200, 425, 31875000, 20, 5)
    
def prob10():
    #The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    #Find the sum of all the primes below two million.  
    
    #First we get a list of the right primes.    
    primes = erato(2000001)
    #Now we sum them
    sum = 0
    for i in primes:
        sum += i
    return sum - 1
    #Have to subtract 1 in order to not count 1 as a prime
    #result: 142913828922
    
def prob11():
    #In the 20x20 grid below, four numbers along a diagonal line have been marked in red.
    source = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""
    #The product of these numbers is 26  63  78  14 = 1788696.
    #What is the greatest product of four adjacent numbers in any direction (up, down, left, right, or diagonally) in the 20x20 grid?
    
    #idea: have grid as string, split on newline, then have a two dimensional grid
    #gets each line in its own string
    lines = source.split('\n')
    grid = []
    #breaks up each line into its component numbers
    #The first one is skipped because it is the blank line at the start of the input
    for line in lines[1:]:
        grid.append(line.split())
    return grid
    
    max = 0
    #First we'll search for left-right runs
    for line in grid:
        #Start at index 3 to reference the 3 before it.
        for i in line[3:]
if __name__ == "__main__":
    import sys
    print prob11()
  