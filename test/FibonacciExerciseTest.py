import unittest

from src import FibonacciExercise


class TestFibonacci(unittest.TestCase):

    # Comprueba que se calcule correctamente la sencuencia de fibonacci
    def test_calculate_fibonacci(self):
        actual_fibonacci_numbers = FibonacciExercise.calculate_fibonacci()

        # Calcular que toda la secuencia de fibonacci sea correcta
        expected_fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        self.assertEqual(expected_fibonacci_numbers, actual_fibonacci_numbers,
                         "La secuencia Fibonacci dada no es correcta")

        # Comprobar que el tercer numero de la secuencia sel el correcto (3)
        self.assertEqual(3, actual_fibonacci_numbers[4],
                         "El numero 3 de la secuencia no es correcto")


if __name__ == '__main__':
    unittest.main()
