# region Numeric Systems

# numeric representation in action
"""
Spreadsheets:https://codeforces.com/contest/1/problem/B
"""
def solution_spreadsheets():
    """
    Converting from decimal to letter representation can be done by using radix-26 system after decreasing the given number by one.s
    """
    import re
    P1 = re.compile("R(\d+)C(\d+)")
    P2 = re.compile("([A-Z]+)(\d+)")

    def to_letters(n):
        letters = []
        while n > 0:
            n = n - 1
            n, r = n//26, n%26
            letters.append(chr(65+r))
        return "".join(letters[::-1])
    
    def to_numbers(letters):
        n = len(letters)
        s = 0
        for i in range(n):
            s = s + (ord(letters[i])-64)*26**(n-1-i)
        return s
    
    t = int(input())
    while (t:=t-1) >= 0:
        s = input()
        match = P1.match(s)
        if match:
            r,c = match.groups()
            print(to_letters(int(c))+r)
            continue
        match = P2.match(s)
        c,r = match.groups()
        print("R{0}C{1}".format(r,to_numbers(c)))

# binary representation in action
"""
Given the set of nubers from 1 to n (n<=20), find all the subsets of the set.
"""
def solution_subsets():
    """
    The number of subsets of a set with n elements is 2**n. In our model, each subset is represented by k in binary form, where 
    0<=k<2**n. In the binrary form, 0 for the j-th bit means the element j is not in the subset and 1 means the element is in the subset.
    """
    n = int(input())
    print("Subset 1:")
    print("{}")
    for i in range(1,2**n): # 2**n subsets
        print("Subset {0}:".format(i+1))
        print("{",end="")
        for j in range(n): # n elements
            if i & (1<<j):
                print(j+1,end=",")
        print("}")

# endregion Numeric Systems





# region Number Theory

def find_number_of_divisors(n):
    """
    Find the number of divisors of each number from 1 to n.
    """
    sieve = [0] * (n+1)
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            sieve[j] += 1
    return sieve

def find_divisors(n):
    """
    Find all the divisors of each number from 1 to n.
    The idea is for each number from 1 to n, we annotate
    who have it as divisor.
    """
    sieve = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            sieve[j].append(i)
    return sieve

def pow(a,n,m):
    """
    Calculate a**n % m, based on the fact that
    a**n mod m = (a mod m)**n mod m
    """
    x = 1
    while n > 0:
        if n % 2 :
            x = (x * a) % m
        a = (a * a) % m
        n = n // 2
    return x
    

# Variant of Erastosthenes sieve in action
"""
Counting divisors:https://cses.fi/problemset/task/1713
"""
def solution_countring_divisors():
    import sys
    n = int(sys.stdin.readline())

    sieve = find_number_of_divisors(100000)
    for _ in range(n):
        x = int(sys.stdin.readline())
        sys.stdout.write(str(sieve[x]) + "\n")

"""
Common Divisors:https://cses.fi/problemset/task/1081
"""
def solution_common_divisors():
    """
    We can solve this in O(max(x_i)log(max(x_i))), having into account that for a given x, we can check how many
    numbers have x as a divisor by counting the number of multiples of x that are present in the input array. So
    we proceed as follows:
    1. Find the maximum value in the array.
    2. For each value from the maximum down to 1, we count the number of multiples of the value in the array.
    3. If the count is greater than 1, we return the value.

    NOTE: Notice that this solution can solve the general case where we must find k numbers such that their greatest 
    common divisor is as large as possible, just by checking the count against k-1.
    """
    import sys
    divisors_count = [0] * 1000001
    int(sys.stdin.readline())
    mx = -1
    for i in map(int, sys.stdin.readline().split()):
        divisors_count[i] += 1
        mx = max(mx, i)

    for i in range(mx, 0, -1):
        count = 0
        for j in range(i, mx+1, i):
            count += divisors_count[j]
        if count > 1:
            sys.stdout.write(str(i) + "\n")
            break

# Modular exponentiation in action        
"""
Exponentiation :https://cses.fi/problemset/result/9690081/
"""
def solution_exponentiation():
    """
    The problem is asking to calculate a**b % M for each pair of a and b.
    """
    import sys
    M = 10**9 + 7
    n = int(sys.stdin.readline())
    results = []
    for _ in range(n):
        a,b = map(int, sys.stdin.readline().split())
        results.append(str(pow(a,b,M)))
    sys.stdout.write("\n".join(results))

"""
Exponentiation II:https://cses.fi/problemset/task/1712
"""
def solution_exponentiation_ii():
    """
    Let be M a prime number, the for any natural n we have
    n = k*(M-1) + n%(M-1), then x^n % M = x^(k*(M-1) + n%(M-1)) % M = [(x^(M-1))^k * x^(n%(M-1))] % M.
    By Fermat's little theorem, x^(M-1) % M = 1, then x^n % M = x^(n%(M-1)) % M.
    """
    import sys
    M = 10**9 + 7
    n = int(sys.stdin.readline())
    results = []
    for _ in range(n):
        a,b,c = map(int, sys.stdin.readline().split())
        b_c = pow(b,c,M-1)
        results.append(str(pow(a,b_c,M)))
    sys.stdout.write("\n".join(results))

# endregion Number Theory
if __name__ == "__main__":
    solution_subsets()