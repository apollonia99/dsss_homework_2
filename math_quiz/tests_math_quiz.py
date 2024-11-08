import unittest
from math_quiz import random_num, chose_operator, calculate_solution


class TestMathGame(unittest.TestCase):

    def test_random_num(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_num(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_chose_operator(self):
        '''
        test if the chosen operator is part of the predefined ones
        '''
        valid_operators = ['+', '-', '*']

        for _ in range(1000):
            rand_operator = chose_operator()
            self.assertTrue(rand_operator in valid_operators)

    def test_calculate_solution(self):
        #test for the expected outcome
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3, 3, '-', '3 - 3', 0),
                (2, 4, '*', '2 * 4', 8),
                (5, 6, '-', '5 - 6', -1)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = calculate_solution(num1, num2, operator)
                self.assertTrue(problem == expected_problem) #check if the equation is defined right
                self.assertTrue(answer == expected_answer) # check if the calculation works right


if __name__ == "__main__":
    unittest.main()
