import os
import sys
import io
from contextlib import redirect_stdout

class SolutionTestCases:
    def __init__(self, problem_name, input_func, output_func, num_cases):
        """
        Initializes the SolutionTestCases.

        :param problem_name: The name of the problem (used for directory structure)
        :param input_func: A function to generate input data
        :param output_func: A function to generate output data based on input data
        :param num_cases: Number of test cases to generate
        """
        self.problem_name = problem_name
        self.input_func = input_func
        self.output_func = output_func
        self.num_cases = num_cases

        self.base_dir = os.path.join('tests', 'testcases', problem_name)

        self.inputs_dir = os.path.join(self.base_dir, 'inputs')
        self.outputs_dir = os.path.join(self.base_dir, 'outputs')
        os.makedirs(self.inputs_dir, exist_ok=True)
        os.makedirs(self.outputs_dir, exist_ok=True)


    def generate_test_cases(self):
        """
        Generates test cases and writes them to files.
        """
        for i in range(1, self.num_cases + 1):
            input_data = self.input_func()
            output_data = self.output_func(input_data)

            input_file_path = os.path.join(self.inputs_dir, f'input{i}.inp')
            output_file_path = os.path.join(self.outputs_dir, f'output{i}.out')

            with open(input_file_path, 'w') as input_file:
                input_file.write(input_data)
            
            with open(output_file_path, 'w') as output_file:
                output_file.write(output_data)

            print(f'Generated test case {i}: {input_file_path}, {output_file_path}')

    def test_solution(self, solution_func):
        """
        Tests a given solution function against all generated test cases.

        :param solution_func: The solution function to be tested
        """
        all_passed = True
        for i in range(1, self.num_cases + 1):
            input_file_path = os.path.join(self.inputs_dir, f'input{i}.inp')
            output_file_path = os.path.join(self.outputs_dir, f'output{i}.out')

            with open(input_file_path, 'r') as input_file:
                input_data = input_file.read()

            with open(output_file_path, 'r') as output_file:
                expected_output = output_file.read()

            # Redirect input and capture output
            sys.stdin = io.StringIO(input_data)
            captured_output = io.StringIO()
            with redirect_stdout(captured_output):
                solution_func()

            actual_output = captured_output.getvalue()

            # Reset sys.stdin to its original state
            sys.stdin = sys.__stdin__

            if actual_output.strip() == expected_output.strip():
                print(f'Test {i} passed.')
            else:
                print(f'Test {i} failed.')
                print(f'Input:\n{input_data}')
                print(f'Expected Output:\n{expected_output}')
                print(f'Actual Output:\n{actual_output}')
                all_passed = False

        if all_passed:
            print('All tests passed.')
        else:
            print('Some tests failed.')

# Example usage:
if __name__ == '__main__':
    def generate_input():
        return "3\n1 2 3\n"

    def generate_output(input_data):
        numbers = list(map(int, input_data.split()[1:]))
        return f'{sum(numbers)}\n'

    # Define a solution function to be tested
    def solution():
        n = int(input())
        arr = list(map(int, input().split()))
        print(sum(arr))

    test_case = SolutionTestCases('example_problem', generate_input, generate_output, 5)

    # Generate test cases
    test_case.generate_test_cases()

    # Test the solution function
    test_case.test_solution(solution)