class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        calculated_value = init
        for iteration in range (iterations):
            calculated_value = calculated_value - (learning_rate * ( 2 * calculated_value) )

        return round(calculated_value, 5)

