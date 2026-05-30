import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        x = 1/(1 + np.e**(-z))
        return np.round(x, 5)

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        for index, element in enumerate(z):
            if element < 0:
                z[index] = 0.0
            else:
                z[index] = np.round(z[index], 5)
        return z
