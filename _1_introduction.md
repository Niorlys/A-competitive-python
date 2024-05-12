# Competitive Programming
Competitive programming involves developing and utilizing algorithms to solve well-known computational problems in their various forms. Being well-versed in competitive programming can transform you into a well-rounded programmer, capable of creating superior software. It also fosters creativity in solving complex computer science problems that may emerge in future job scenarios. Additionally, competitive programming can be an enjoyable and intellectually stimulating activity. To excel in competitive programming, it's essential to be familiar with several key aspects, as outlined below.

## Be familiar with...
### Be familiar with classic computer science data structure and algorithms
Data structures provide a systematic way of organizing and managing data, enabling programmers to handle complex problems with more clarity and efficiency, and mastery of algorithms not only accelerates the problem-solving process but also enhances the ability to think algorithmically, leading to solutions that are not just functional but also optimized for speed and resource usage. Also, it is useful to do algorithm analysis to know if the time/space complexity of the developed algorithm passes the time/space limits of the problem, so it is good to be familiarized with asymptotic notation of functions. 
 
 **Asymptotic notation and bounds** 
* `f(n) = Ω(g(n))` if there exists positives `c` and `N` such that `f(n)>=cg(n)` for all `n>=N`.
* `f(n) = O(g(n))` if there exists positives `c` and `N` such that `f(n)<=cg(n)` for all `n>=N`.
* The best time for sorting algorithms requiring comparison is `Ω(n log2 n)`.
* `2**10` is approx. `1K`, `2**20` is approx. `1M`.
### Be acquainted with classic computer science problems no matter how hard they are.

Tackling these problems enhances critical thinking and problem-solving abilities. It trains you to approach complex challenges methodically and creatively. The principles and techniques learned from these problems give you the confidence and expected solving speed when facing variations of these problems.


# Python's Toolbox for competitive programming
Python's standard (CPython) library and built-ins come with a set of useful tools to save time and add speed to our scripts in problem-solving. Looking for speed and efficiency requires to use of the standard library as much as possible, since most of the time the tools are optimized using C extension modules, which run faster due to the compiled nature of C. If you check the code of some built-in library, likely will find a pattern like this:
```
def _some_function(*args, **kwargs):
    ...
    ...
    ...

try:
    from _C_library import  _some_function
except:
    pass
```
This is an example of Python's strategy to optimize performance utilizing C extensions where feasible, coupled with providing Python fallbacks to ensure broad compatibility and ease of use. This balanced approach melds Python's high-level user-friendliness with C's performance advantages. In general programming practice, avoiding reinventing the wheel is recommended for saving time and enhancing efficiency. 
 

To illustrate the impact of this practice, consider the following example where we calculate the sum of the first `n` integers. Instead of using Gauss's formula, we opt for a more straightforward(and naive) approach. The purpose here is to demonstrate the significance of choosing optimal methods in Python. We use our implemented **benchmark.py** module to compare two functions that sum numbers iteratively for `n=10000`. The benchmark's report reveals the execution times of both methods:

```
Function                           Average     Median    Maximum    Minimum
---------------------------------------------------------------------------
sum_n_numbers_using_for            0.00306    0.00294    0.00606    0.00268
sum_n_numbers_using_sum_builtin    0.00080    0.00076    0.00137    0.00071
``` 
This comparison clearly shows that Python's built-in `sum` method is at least three times faster than a manually coded `for` loop for summing elements in an iterable. Such examples underscore the importance of using Python's built-in capabilities for more efficient programming. The module **introduction.py** briefly describes the data structures and algorithms included as standard programming. From here onward, each *.md* file will have an associated a *.py* script implementing the methods described, we'll refer to this script as **the script**. 
 
 ## PyPy as a faster option
 PyPy is an alternative Python interpreter with a focus on speed by featuring a **Just In Time** (JIT) compiler, which can significantly speed up the execution of Python code. The JIT compiler in Pypy optimizes the code in runtime identifying and enhancing the performance of frequently executed code. This means that loops, function calls, and mathematical operations can become much faster after the initial iterations. That is why PyPy is particularly effective for long-running programs that perform lots of computations or iterations. If you want to see the difference between CPython and PyPy, visit the [documentation](https://doc.pypy.org/en/latest/cpython_differences.html#). As an example of the performance difference, for the following problem in CodeForces: [The least round way](https://codeforces.com/contest/2/problem/B), submit the memomy optimized solution twice, one time using Python and the other time using PyPy3:
 ```
 from sys import stdin, stdout
from array import array
from math import sqrt
input = stdin.readline
print = stdout.write

def get_2_and_5_powers(m):
    two = five = 0
    m2 = m
    while not m%2:
        two = two + 1
        m = m//2
    while not m2%5:
        five = five + 1
        m2 = m2//5
    return two, five

def _min(*,right, down):
    # Assuming the values of the grid are passed in
    # in that order
    if right <= down:
        return 1, right
    return 2,down

def create_path(path_record, size):
    path = []
    i = j = size - 1
    while i > 0 or j > 0:
        if path_record[i][j] == 2:
            path.append("D")
            i = i-1
            continue
        path.append("R")
        j = j-1
    return "".join(path[::-1])

def cantor_pairing(m, n):
    """Compute the Cantor pairing value for a given pair (m, n)."""
    return ((m + n) * (m + n + 1)) // 2 + n

def cantor_pairing_inverse(z):
    """Compute the inverse of the Cantor pairing for a given z."""
    w = int(((-1 + sqrt(1 + 8 * z)) / 2))
    t = (w ** 2 + w) // 2
    n = z - t
    m = w - n
    return m, n


def find_minimal_path(size,grid, zero):
    path_array2 = [array("B") for j in range(n)]
    path_array5 = [array("B") for j in range(n)]
    dp2 = [array("I") for j in range(n)]
    dp5 = [array("I") for j in range(n)]
    p2,p5= cantor_pairing_inverse(grid[0][0])
    dp2[0].append(p2)
    path_array2[0].append(0)
    dp5[0].append(p5)
    path_array5[0].append(0)
    for i in range(1,size):
        p20i, p50i = cantor_pairing_inverse(grid[0][i])
        p2i0, p5i0 = cantor_pairing_inverse(grid[i][0])
        dp2[0].append(dp2[0][i-1] + p20i)
        path_array2[0].append(1)
        dp2[i].append(dp2[i-1][0] + p2i0)
        path_array2[i].append(2)
        dp5[0].append(dp5[0][i-1] + p50i)
        path_array5[0].append(1)
        dp5[i].append(dp5[i-1][0] + p5i0)
        path_array5[i].append(2)
    
    for i in range(1,size):
        for j in range(1,size):
            p2, p5 = cantor_pairing_inverse(grid[i][j])
            direction, value = _min(right=dp2[i][j-1],down=dp2[i-1][j])
            dp2[i].append(p2 + value)
            path_array2[i].append(direction)
            direction, value = _min(right=dp5[i][j-1],down=dp5[i-1][j])
            dp5[i].append(p5 + value)
            path_array5[i].append(direction)

    value2, value5 = dp2[-1][-1], dp5[-1][-1]

    
    if value2 and value5 and zero:
        _path = ["R" for _ in range(zero[1])]
        _path.extend(("D" for _ in range(zero[0])))
        _path.extend(("R" for _ in range(n-zero[1]-1)))
        _path.extend(("D" for _ in range(n-zero[0]-1)))
        print(f"{1}\n")
        print("".join(_path))
    elif value2 <= value5:
        print(f"{value2}\n")
        print(create_path(path_array2,size))
    else:
        print(f"{value5}\n")
        print(create_path(path_array5,size))

n = int(input())

grid = []
zero = None
for i in range(n):
    grid.append(array("I"))
    for v in map(int, input().split()):
        p2, p5 = get_2_and_5_powers(v or 10)
        grid[-1].append(cantor_pairing(p2,p5))
        if v == 0:
            if not zero:
                zero = i, len(grid[-1]) - 1

find_minimal_path(n,grid,zero)
 ```