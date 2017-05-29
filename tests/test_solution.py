from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        import numpy as np
        x = np.ones((5, 5))

        result = solution(x)
        print(result)
        self.assertNotEqual(result, None)

        self.assertEqual(result[0][0], 1.)
        self.assertEqual(result[1][1], 0.)
        self.assertEqual(result[2][2], 0.)
        self.assertEqual(result[3][3], 0.)
        self.assertEqual(result[4][4], 1.)
