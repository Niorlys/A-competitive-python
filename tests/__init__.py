from util.generate_solution_test_data import SolutionTestSession, Generator, Callable

class BaseTest:
    def assert_solution(self,input_generator:Generator, output_func:Callable, solution:Callable, output_generator=False):
        problem_name=solution.__name__[len('solution_'):] # Using naming convention, see _1_introduction.py
        session = SolutionTestSession(problem_name, input_generator, output_func,output_generator)

        session.generate_test_cases()

        assert session.test_solution(solution) == SolutionTestSession.ALL_PASSED
