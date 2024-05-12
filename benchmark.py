import time
import statistics

class Benchmark:
    """
    A class for benchmarking the performance of functions.

    This class provides a simple way to benchmark one or more functions
    by executing them a specified number of times and recording their
    execution times.
    """
    def __init__(self, iterations:int=100) -> None:
        self.iterations = iterations

    def benchmark(self, *functions:tuple, args:tuple=(), kwargs:dict={}) -> None:
        """
        Benchmarks the given functions with the specified arguments and keyword arguments.

        This method runs each of the provided functions for a number of iterations
        set during the class initialization. It records the execution time for each
        iteration and stores it in the results dictionary. At the end you will receive
        an statistic report about the performance of the benchmarked functions.

        Parameters:
            functions (tuple): A tuple of functions to be benchmarked.
            args (tuple): A tuple of arguments to be passed to the functions.
            kwargs (dict): A dictionary of keyword arguments to be passed to the functions.

        Note:
            All functions must be able to accept the provided args and kwargs.
        """
        results = dict()
        for function in functions:
            execution_times = []
            for _ in range(self.iterations):
                start_time = time.time()
                function(*args, **kwargs)
                end_time = time.time()
                execution_times.append(end_time - start_time)
            results[function.__name__] = execution_times

        self._report(results)

    def _report(self, results:dict) -> None:
        """
        Creates a report for the benchmarking results.

        Parameters:
            results (dict): The records of execution times for benchmarked functions.
        """
        function_name_padding = max(len(function_name) for function_name in results.keys())
        print(f"{'Function':<{function_name_padding}} {'Average':>10} {'Median':>10} {'Maximum':>10} {'Minimum':>10}")
        print('-' * (44+function_name_padding))

        for function_name, times in results.items():
            avg_time = statistics.mean(times)
            median_time = statistics.median(times)
            max_time = max(times)
            min_time = min(times)
            print(f"{function_name:<{function_name_padding}} {avg_time:>10.5f} {median_time:>10.5f} {max_time:>10.5f} {min_time:>10.5f}")



if __name__ == "__main__":
    # Usage example
    def sum_n_numbers_using_for(n):
        total = 0
        for i in range(1,n + 1):
            total += i
        return total

    def sum_n_numbers_using_sum_builtin(n):
        return sum(range(1,n+1))

    bench =Benchmark()
    bench.benchmark(sum_n_numbers_using_for, sum_n_numbers_using_sum_builtin , args=(10000000,), kwargs={})
