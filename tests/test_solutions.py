from random import sample, randint

from . import BaseTest
from _2_sorting_searching import (
    solution_inversions,
    solution_intersected_intervals,
)

class TestSortingSearching(BaseTest):
    def test_solution_inversions(self):
        def input_generator():
            _input = "{}\n{}"
            yield _input.format(100000," ".join(map(str,range(100000,0,-1))))
            for i in range(9):
                n = randint(10,1000)
                yield _input.format(n," ".join(map(str,sample(range(n), n))))

        def output_func(inp):
            n, arr = inp.split('\n')
            arr = list(map(int, arr.split()))
            n = int(n)
            if n == 100000:
                return "4999950000"
            inversion_count = 0
            
            for i in range(n):
                for j in range(i + 1, n):
                    if arr[i] > arr[j]:
                        inversion_count += 1                 
            return str(inversion_count)
        
        self.assert_solution(input_generator,output_func, solution_inversions)

    def test_solution_intersected_intervals(self):
        def input_generator():
           yield "4\n1 2\n1 6\n4 9\n5 12"
           yield "5\n12 45\n10 78\n54 77\n11 69\n21 87"
           yield "2\n1 2\n3 4"

        def output_func():
            yield "3"
            yield "4"
            yield "1"

        self.assert_solution(input_generator,output_func,solution_intersected_intervals,True)