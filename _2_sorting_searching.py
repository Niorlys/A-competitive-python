# region Sort algorithms
from random import randint
"""
Some sorting algorithms are good samples of the Divide-Conquer paradigm, which involves three steps
when solving a problem with input an array A of n elements:

1- Divide: In this step we use certain criteria to partition the array A in at least two sub-arrays.
2- Conquer: For each sub-array, there is a sub-problem, so this step is about solving all those sub-problems.
3- Combine: Finally, we combine (somehow) the solutions for the sub-problems we sloved in step 2.
"""

# Divide-Conque in action

def quick_sort(arr):
    """
    1- Dividing:Given a pivot, we partition the array in two sides such that l<=arr[p] for l in arr[:p+1] 
       and r>arr[p] for r in arr[p+1:].
    2- Conquering: For the new subarrays, we apply recursively the same original routine.
    3- Combining: This step is not necessary (Why?)
    """
    
    def partition(a, left, right):
        """
        Main step, for us i-left is the numbers of elements such that e<=pivot,
        and the difference j-i is the numbers of elements that e>pivot.
        """
        pivot_index = randint(left, right)
        a[pivot_index], a[right] = a[right], a[pivot_index]
        pivot = a[right]
        i = left-1
        for j in range(left,right):
            if a[j] <= pivot:
                i = i+1
                a[i], a[j] = a[j], a[i]
        a[i+1], a[right] = a[right], a[i+1] # Setting the pivot in the right position
        return i+1 # The index of the partition boundary 
    
    def perform_quick_sort(a, left, right):
        if left >= right: return

        p = partition(a, left, right)
        perform_quick_sort(a, left, p)
        perform_quick_sort(a,p+1, right)
    
    perform_quick_sort(arr,0,len(arr)-1)


# Another Divide-Conquer classic sample
def merge_sort(arr):
    # Simple implementation of merge sort
    def merge(left,right):
        i = j = 0
        merged = []
        while i < len(left)  and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged
        
    def sort(i,j):
        if i == j:
            return [arr[i]]
        mid = (i+j)//2
        sorted_right = sort(i, mid)
        sorted_left = sort(mid+1,j)
        return merge(sorted_right, sorted_left)
    
    _sorted = sort(0, len(arr) - 1)
    return _sorted

def counting_sort(arr, max):
    # Sort in O(n)
    pivot = [0 for _ in range(max + 1)]

    for item in arr:
        pivot[item] += 1

    _sorted = []

    for i in range(max + 1):
        _sorted.extend([i for _ in range(pivot[i])])

    return _sorted

# merge_sort in action
"""
Consider an array of n different integers. Given the idexes i,j, we say that there is an inversion
if arr[i] > arr[j] and i < j. The goal is to count the number of inversions in the array.
"""
def solution_inversions():
    """
    We use a modified merge sort to count the number of inversions. The idea behind is as follows:Let be A an array , and let be
    L and R the sorted versions of the left and right halves of A. Then, an element l in L forms an inversion with an element r in R
    if in the "merge" subroutine element r is copied first, and the total of inversions for r is the current number of elements in L.
    This is because the subroutine populates the array from left to right in sorted order, so if r is copied first, then all elements
    in L are greater than r. The time complexity of this algorithm is O(n log n).
    """
    n = int(input())
    arr = list(map(int, input().split()))

    def merge_count_inv(left,right):
        i = j = inversions = 0
        merged = []
        while i < len(left)  and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inversions += len(left) - i
        
        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged, inversions

    def sort_count_inv(i,j):
        if i == j:
            return [arr[i]], 0
        mid = (i+j)//2
        sorted_right, inversions_right = sort_count_inv(i, mid)
        sorted_left, inversions_left =sort_count_inv(mid+1,j)
        _sorted, inversions = merge_count_inv(sorted_right, sorted_left)
        return _sorted, inversions + inversions_right + inversions_left

    _, inversions = sort_count_inv(0, n - 1)
    print(inversions)

# sorting in action
"""
Instersecctions of Intervals:
Given a set of intervals, determine the maximum number of intersected intervals. For example, for the following instance
|----------|
         |-----------|
    |------------|
                      |------|

there is a maximum of three intersected intrevals.
"""
def solution_intersected_intervals():
    """
    The idea is to give a credit of +1 to left extremes, and -1 to right extremes. Thus, each time we enter to an interval
    our credit increases by 1, and when we go out our credit decreases by 1. So the maximum number of intersected intervals
    is the maximum credit we got.
    """
    n = int(input()) 
    extremes = []
    for _ in range(n):
        a,b = map(int, input().split())
        extremes.append((a,1))
        extremes.append((b,-1))
    extremes.sort()

    count = max_intersected = 0
    for _, credit in extremes:
        count= count + credit
        if count > max_intersected:
            max_intersected = count

    print(max_intersected)


"""
Restaurant Customers: https://cses.fi/problemset/task/1619/
This is just a version of Instersecctions of Intervals.
"""
def solution_restaurant_customers():
    from sys import stdin
    input = stdin.readline

    n = int(input())
    extremes = list()
    for _ in range(n):
        a, b = map(int, input().split())
        extremes.append((a, 1))
        extremes.append((b, -1))
    extremes.sort()

    max_n = count = 0
    for _,credit in extremes:
        count  = count + credit
        if count>max_n:
            max_n = count
    print(max_n)

# Another sample of divide and conquer paradigm:

# endregion Sort algorithms






# region Search Algorithms
from bisect import bisect
def binary_search_smallest_value(is_good,hi):
    """ 
    Finds in O(Tc * log(hi)) the smallest integer v such that is_good(v) is True, where Tc is the time of the condition is_good. 
    The idea behind is as follows:

    We are going to reach the optimal value making jumps of lengths hi-1, hi//2, hi//4,...,1. On each jump, if the
    reached value in the new position is good, we keep our previous position, and then make a new halved jump.
    We keep doing the same until reaching a not good value, in such a case we update our position until reching a
    good value. Note that the solution is always asured since it is guaranteed a jump length of 1, so if we are in
    a bad position, adding 1 in each jump will take us up to the optimal solution.
    """
    x = -1
    while hi >= 1:
        while not is_good(x + hi): x += hi
        hi //= 2
    return x+1

def binary_search_smallest_value_arr(is_good,hi,arr_length):
    """ 
    Array version of binary_search_smallest_value. Here we assume that condition is_good makes computations
    involving an array of length arr_length.
    NOTE: In this case, if the returned value is arr_length, then it means that there is not value in the array
    satisfying is_good condition.
    """
    x = -1
    while hi >= 1:
        while x+ hi < arr_length and not is_good(x + hi): x += hi
        hi //= 2
    return x+1

# binary_search_smallest_value in action

"""
Doing tasks with concurrent machines:
We must complete k tasks using n machines. Each machine i comes with a specific processing time p_i representing the duration 
it takes to complete one task. We need to determine the minimal time required to finish all k tasks.
Input:
The first line contains an integer: k, the number of tasks.
The next line contains n integers: p_1, p_2,..., p_n

Output:
The minimal time required to process all tasks using the machines.
"""
def solution_tasks_in_concurrent_machines():
    """
    The time for complete all task is an integer, and the property P of all task being completed for certain time t is inductive
    on t, so we can use the binary_search_smallest_value procedure to find the minimal t value that makes P true. Thus, 
    a value t is good if all task are completed at time t. Since for each t, the number of tasks processed by the machine i is
    t//p_i, then t is good if Sum(t//p_i) >= k.

    Recall that binary_search_smallest_value requires an upper bound, in our case we take as upper bound the total time
    it takes to the slower machine to complete all tasks.
    """
    k = int(input())
    p = list(map(int, input().split()))
    upper_bound = max(p) * k
    def is_good(t):
        return sum((t//p_i for p_i in p))>= k
        
    print(binary_search_smallest_value(is_good,upper_bound))

def get_active_left(i, mask,mark_return=True):
    """
    This is an implementation of path compression technique to search the maximum active index j to the left
    of a given index i. An index is active if mask[i] == i. The amortized running time for this method is O(1).
    Args:
       i: The index to search the maximum active index to the left.
       mask: The array of indexes to search. Must start in the form mask[i] = i for all i.
       mark_return: This parameter avoid infinity recursion when marking the found value.
    """
    if i == -1:
        return i
    if i != mask[i]:
        mask[i] = get_active_left(mask[i], mask, mark_return=False)

    active_left = mask[i]
    if active_left != -1 and mark_return:
        # We mark the found value as non-active
        mask[active_left] = get_active_left(active_left-1, mask, mark_return=False)

    return active_left
        

# get_active_left in action

"""
Concert Tickets: https://cses.fi/problemset/task/1091/
"""
def solution_concert_tickets():
    """ This solution passes all tests.
    We must give an answer for each customer in input order, so we choose to sort the tickets prices. The idea here
    is search the customer's price in tickets using bisect, and then get the maximum active index for the tickets array.
    The value with that index will give us the maximum price available that the customer can pay.
    """
    input()
    tickets = sorted(map(int,input().split()))
    _mask = list(range(len(tickets)))

    for t in map(int,input().split()):
        i = get_active_left(bisect(tickets, t) - 1, _mask) # We get the maximum left updated index
        if i == -1:
            print(-1)
        else:
            print(tickets[i])
 

# endregion Search Algorithms

if __name__ == '__main__':
    ...