# Reading-Printing:
# If you are sure that you are using the more efficient algorithm and still you are getting TLE,
# consider optimization when reading and printing
def quick_read_print():
    from sys import stdin, stdout
    input = stdin.readline
    print = stdout.write

    n = input()
    print(f"Here is the input: {n}")

    integer = "57\n" # Simulating reading from stdin, where the strings ends with \n
    print(f"Sum 1:{int(integer)+1}\n") # There is no need to stripping the \n character to perform int()

# region Data Structures
# The following modules implements a bunch of data structures containers and functionalities 
# beyonds the commonly used list, dict or tuple.
from collections import Counter, OrderedDict, deque
from array import array
from heapq import heapify, heappop, heappush, nlargest, nsmallest
from bisect import insort, bisect
import queue

def usageCounter():
    """ 
    A multiset or bag is an unordered collection that allows multiple occurrences of elements. The Counter class, which subclasses the dict 
    class, is designed for counting hashable objects. It transforms iterables into multisets and provides additional functionality, 
    including arithmetic operations between multisets.
    """
    c1 =  Counter("abcdaabbcc")

    print("Counter 1:",c1)
    print("Frequencies 1:")
    for key in c1:
        print(f"{key}:{c1[key]}")

    print("Frequency of 'z':", c1['z'])

    print("Two most commons:", c1.most_common(2))

    c2 = Counter(["a","b","z","a"])

    print("Counter 2:",c2)
    print("Frequencies 2:")
    for key in c2:
        print(f"{key}:{c2[key]}")
    print()

    print("Arithmetic with counter:")
    print("c1 + c2 =", c1 + c2)
    print("c1 - c2 =", c1 - c2)
    print("c1 & c2 =", c1 & c2)
    print("c1 | c2 =", c1 | c2)

def usageOrderedDict():
    """
    An OrderdDict is just a dict subclass that remembers the order in which its keys are added.
    """
    od = OrderedDict(a=1,b=2)
    print(od)
    print()

    od = OrderedDict([("a",100),("b",200)])
    print(od)
    print()
    # Adding a new key at the end
    od["c"] = 300
    # Moving the second key to the end
    od.move_to_end("b")
    print("'b' moved to the end:",od)


def usage_deque():
    """
    Stacks and queues are both types of sequences, but they differ in how elements are added and removed.

    Stack:his sequence operates on a Last-In, First-Out (LIFO) basis. The most recently added element is the first one to be removed. Adding 
    an element to a stack is termed 'pushing', and it happens at the end of the sequence. Essentially, the last element pushed onto the stack 
    is the first one to be removed, reflecting the LIFO principle. 
    
    Queue: In contrast, a queue functions on a First-In, First-Out (FIFO) policy. The element that has been in the sequence the longest is 
    the first to be removed. When a new element is added, or 'enqueued', it joins the end of the sequence. This ordering ensures that elements
    are removed in the same order they were added, embodying the FIFO concept.
    
    Deque: This type of sequence is more flexible, supporting both LIFO and FIFO policies. This means that elements can be added or removed 
    from either end of the sequence. In this way, stacks and queues can be considered degenerated forms of deques, with each restricting removals 
    and additions to just one end of the sequence.
    """

    d = deque('abcd')
    print("d =", d)

    d.append(100)
    d.appendleft(None)
    print("\nAppending:\nd =",d)

    d.extend(range(3))
    d.extendleft('xyz')
    print("\nExtending:\nd =",d)

    print("\nPop right:",d.pop())
    print("\nPop left:", d.popleft())

    d.rotate(4)
    print("\nRotating 4 units right:", d)

    d.rotate(-4)
    print("\nRotating 4 units left:", d)

    # Fixing a max length, so when adding elements with the sequence full, existing elements are discarded.
    d = deque(['x',1,None], maxlen=3)
    print('\n\nDeque with maxlen:', d)

    d.append("discarding first element")
    print("\nAppending right:", d)

    d.appendleft("discarding last element")
    print("\nAppending left:", d)

def usage_array():
    """
    Dealing with large amount of data requires an efficient memory usage. In such scenarios, arrays offer a more memory-efficient 
    solution compared to lists, primarily due to the nature of their data storage. Since an array require all elements to be of a fixed type.
    this constraint allows arrays to employ a more compact memory representation in contrast with a general purpose list. 

    Creating an aray requires a code for specifying the type, in summary:
    
     Code	Type	    Minimum size (bytes)
        b	signed int	            1
        B	unsigned int	        1
        h	signed short	        2
        H	unsigned short	        2
        i	signed int	            2
        I	unsigned int	        2
        l	signed long	            4
        L	unsigned long	        4
        q	signed long long	    8
        Q	unsigned long long	    8
        f	float	                4
        d	double float	        8
    """

    a = array('I',[1,2,3,4,5,6,7])
    print("a =",a)

    a.append(100)
    a.extend(range(5))
    print("\na =", a)

    print("\nSlice 1-3:", a[1:3])
    print("\nPop:",a.pop())
    
def usage_heapq():
    from util.binary_tree_view import print_tree
    """
    Heaps are containers with the min(max) heap property, this is  
    a[k] <= a[2*k+1] and a[k] <= a[2*k+2]( a[k] >= a[2*k+1] and a[k] >= a[2*k+2])
    We will discuss this in more detail later. You can see a well documented guide 
    inside the heapq module.
    """
    arr = [5,2,8,12,4,9,1]
    # Converting the array in a min heap
    heapify(arr)
    print_tree(arr)

    print("Min element in O(1):",heappop(arr))
    heappush(arr,7) # Pushing 7
    print_tree(arr)

    arr = [4,7,2,1,8,9,41,2]
    print("Sorted arr:", sorted(arr[:]))
    print("Original arr:", arr)
    print("Third smallest value:", nsmallest(3,arr)[-1])
    print("Fourth largest value:", nlargest(4,arr)[-1])

def priorityQueue_usage():
    """
    The queue module provides a thread-safe FIFO implementation, since this is not relevant in competitive
    programming, the reason to mention the module is due to its priority queue implementation, where the processing
    order of the elements of the queue can be based in specifics characteristics of that elements.
    """
    from functools import total_ordering

    @total_ordering
    class Item:
        def __init__(self, priority):
            self.priority = priority
        
        def __eq__(self, other):
            if isinstance(other, Item):
                return self.priority == other.priority
            return NotImplemented

        def __lt__(self, other):
            if isinstance(other, Item):
                return self.priority < other.priority
            return NotImplemented
        
    pq = queue.PriorityQueue()
    pq.put(Item(1))
    pq.put(Item(3))
    pq.put(Item(2))
    item = pq.get()
    print("Getting the first time:")
    print("Item Priority:", item.priority)
    
# endregion Data Structures






# region Algorithms
    
# The following modules have several modules for implementing algorithms using the appropriate style depending on the task.
# reduce function has a C version in the standard library, and itertools is entirely a C extension for Python, so the methods we 
# are going to show are reliably fast.
from functools import reduce
from itertools import product, permutations, accumulate, combinations,combinations_with_replacement

def accumulative_effect():
    """
    Accumulative effect may be useful in many situations, for example when converting an 
    embbeded lists [1,[2,3],[[4,[5]],6]] in just on list [1,2,3,4,5,6]. 
    """
    # We can implement the accumulative technique by ourselves, we omit validations
    def accumulate_x_with_f(f,x):

        it = iter(x) # Getting the iterator object of an iterable
        value = next(it) # Getting the initial value,
        for item in it:
            value = f(value,item)
        return value
    
    print(accumulate_x_with_f(lambda x,y:x+y, (1,2,3,4))) # prints 10

    # That is basically what does the Python 'reduce' version from module functools, but
    # it turns out that there is a faster execution since there is a C version for 'reduce',
    # so it is a good idea to use it

    print(reduce(lambda x,y:x+y,(1,2,3,4))) # prints 10

    # If you want a lazy accumulative effect, we can use 'accumulate' from itertools
    # 'accumulate' returns an iterable that yields accumulated values in each step
    for i in accumulate((1,2,3,4),lambda x,y:x+y**2, initial=0):
        print(i, end=" ") # prints 1 5 14 30

def combinatorics():
    """
    itertools has good tools for working with combinatoric problems, as we'll see.
    """
    # Cartesian product:
    print(list(product(range(2),"abc"))) # [(0, 'a'), (0, 'b'), (0, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]
    print(list(product("ab", repeat=3))) # [('a', 'a', 'a'), ('a', 'a', 'b'), ('a', 'b', 'a'), ('a', 'b', 'b'), ('b', 'a', 'a'), 
                                         # ('b', 'a', 'b'), ('b', 'b', 'a'), ('b', 'b', 'b')]
    
    # Permutations:
    print(list(permutations("abc"))) # [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
    print(list(permutations("abc",2))) # [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]

    # Combinations:
    list(combinations("abcd",2)) # [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]

    # Combinations with replacement
    list(combinations_with_replacement("abca",3)) # [('a', 'a'), ('a', 'b'), ('a', 'c'), ('a', 'a'), 
                                                  # ('b', 'b'), ('b', 'c'), ('b', 'a'), ('c', 'c'), ('c', 'a'), ('a', 'a')]

def binary_search():
    """
    Using insort we can add elements to a list mantaining it in sorted order. Also bisect is an iterative implementation
    of binary search algorithm. Note that bisect returns the index where the value must be inserted to keep the array sorted, 
    so if we want to find out if x is in the array, we must check if x == arr[bisect(arr,x) - 1]
    """
    l = [1,2]
    print("Value   List")
    print("_____   ____")
    for i in (7,5,3,9,0):
        insort(l,i)
        print(f"{i:5}", l)

    print()
    l = [2,4,6,8]
    print("Sorted array:",l)
    print("Where to put 5:", bisect(l,5)) # Prints 2
    l.insert(2,5) # Now l = [2,4,5,6,8]
    assert 5 == l[bisect(l,5)-1] # True

# endregion Algorithms

if __name__ == '__main__':
    ...