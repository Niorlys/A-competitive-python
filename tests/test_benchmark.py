from unittest.mock import Mock, patch
from util.benchmark import Benchmark



class TestBenchmark:
    @patch('time.time')
    @patch.object(Benchmark, '_report')
    def test_benchmark(self, mock__report, mock_time):
        f1, f2 = Mock(__name__='f1'), Mock(__name__='f2')
        mock_time.side_effect=range(1,13) # Mock time.time() to return increasing values
        benchmark = Benchmark(iterations=3)
        args=(2,)
        kwargs={'y': 3}

        benchmark.benchmark(f1, f2,args=args,kwargs=kwargs)

        expected_results = {
            'f1': [1.0, 1.0, 1.0],
            'f2': [1.0, 1.0, 1.0]
        }
        mock__report.assert_called_once_with(expected_results)
        # assert f1 calls
        f1.assert_called_with(*args,**kwargs)
        assert f1.call_count == benchmark.iterations
        # assert f2 calls
        f2.assert_called_with(*args,**kwargs)
        assert f2.call_count == benchmark.iterations