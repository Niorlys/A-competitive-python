# Competitive Programming
Competitive programming involves developing and utilizing algorithms to solve well-known computational problems in their various forms. Being well-versed in competitive programming can transform you into a well-rounded programmer, capable of creating superior software. It also fosters creativity in solving complex computer science problems that may emerge in future job scenarios. Additionally, competitive programming can be an enjoyable and intellectually stimulating activity. To excel in competitive programming, it's essential to be familiar with several key aspects, as outlined below.

## Be familiar with...
### Be familiar with classic computer science data structure and algorithms
Data structures provide a systematic way of organizing and managing data, enabling programmers to handle complex problems with more clarity and efficiency, and mastery of algorithms not only accelerates the problem-solving process but also enhances the ability to think algorithmically, leading to solutions that are not just functional but also optimized for speed and resource usage.

### Be acquainted with classic computer science problems no matther how hard they are.

Tackling these problems enhances critical thinking and problem-solving abilities. It trains you to approach complex challenges methodically and creatively.The principles and techniques learned from these problems gives you the confidence and expected solving speed when facing variations of theses problems.


# Python's Toolbox for competitive programming
Python's standard (CPython) library and built-ins comes with a set of useful tools to save time and add speed to our scripts in problem solving. Looking speed and efficiency requires to use the standard library as much as posible, since most of the time the tools are optimized using C extension modules, which run faster due to the compiled nature of C. If you check the code of some built-in library, likely will find a pattern like this:
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
This is an example of Python's strategy to optimize performance utilizing C extensions where feasible, coupled with providing Python fallbacks to ensure broad compatibility and ease of use. This balanced approach melds Python's high-level user-friendliness with C's performance advantages. In general programming practice, avoiding treinventing the wheel is recommended for saving time and enhancing efficiency. 
 

To illustrate the impact of this practice, consider the following example where we calculate the sum of the first `n` integers. Instead of using Gauss's formula, we opt for a more straightforward(and naive) approach. The purpose here is to demonstrate the significance of choosing optimal methods in Python. We use the **benchmark.py** module to compare two functions that sum numbers iteratively for `n=10000`. The benchmark report reveals the execution times of both methods:

```
Function                           Average     Median    Maximum    Minimum
---------------------------------------------------------------------------
sum_n_numbers_using_for            0.00306    0.00294    0.00606    0.00268
sum_n_numbers_using_sum_builtin    0.00080    0.00076    0.00137    0.00071
``` 
This comparison clearly shows that Python's built-in sum method is at least three times faster than a manually coded `for`` loop for summing elements in an iterable. Such examples underscore the importance of leveraging Python's built-in capabilities for more efficient programming. In the following sections we explore the Python's standard programming data structure and algorithms. 
## Data Structures
