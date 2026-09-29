import os
import random
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import brute  # noqa: E402
import solution  # noqa: E402


def read(name):
    with open(os.path.join(HERE, "examples", name)) as f:
        return f.read()


class ExampleTest(unittest.TestCase):
    def test_examples(self):
        for case in ("1", "2"):
            with self.subTest(case=case):
                data = read(case + ".in")
                expected = read(case + ".out")
                self.assertEqual(solution.solve(data), expected)
                self.assertEqual(brute.solve(data), expected)


class EdgeCaseTest(unittest.TestCase):
    def test_single_task(self):
        self.assertEqual(solution.schedule([(7, 3, 5)]), ([1], 0))

    def test_all_identical_uses_index_order(self):
        tasks = [(0, 1, 0)] * 4
        self.assertEqual(solution.schedule(tasks), ([1, 2, 3, 4], 0 + 1 + 2 + 3))

    def test_arrival_at_finish_time_is_considered(self):
        # 1번이 [0, 2)에 실행되고, 시각 2에 도착한 급한 3번이 2번보다 먼저 실행된다.
        tasks = [(0, 2, 5), (1, 1, 5), (2, 1, 0)]
        self.assertEqual(solution.schedule(tasks), ([1, 3, 2], 0 + 0 + 2))

    def test_large_wait_sum_exceeds_32bit(self):
        n = 1000
        tasks = [(0, 10000, 0)] * n
        order, total = solution.schedule(tasks)
        self.assertEqual(order, list(range(1, n + 1)))
        self.assertEqual(total, 10000 * n * (n - 1) // 2)
        self.assertGreater(total, 2**31 - 1)


class RandomCompareTest(unittest.TestCase):
    def test_against_brute_force(self):
        rng = random.Random(20260929)
        for _ in range(500):
            n = rng.randint(1, 30)
            span = rng.choice([5, 30, 1000])
            tasks = [
                (rng.randint(0, span), rng.randint(1, 10), rng.randint(0, 3))
                for _ in range(n)
            ]
            with self.subTest(tasks=tasks):
                self.assertEqual(solution.schedule(tasks), brute.schedule(tasks))


class LargeInputTest(unittest.TestCase):
    def test_max_size_runs(self):
        rng = random.Random(1)
        n = 200_000
        tasks = [
            (rng.randint(0, 10**9), rng.randint(1, 10**4), rng.randint(0, 10**9))
            for _ in range(n)
        ]
        order, _ = solution.schedule(tasks)
        self.assertEqual(sorted(order), list(range(1, n + 1)))


if __name__ == "__main__":
    unittest.main()
