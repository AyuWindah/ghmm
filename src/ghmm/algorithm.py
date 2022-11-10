import numpy as np
import numpy.typing as npt
from scipy.stats import norm

def Frames(O: npt.NDArray, mu: npt.NDArray, sigma: npt.NDArray):
    (T, ) = O.shape
    (N, ) = mu.shape

    frames = np.empty((T, N))
    for i in range(T):
        frames[i] = norm.pdf(O[i], mu, sigma)
    
    return frames

def Forward(A: npt.NDArray, frames: npt.NDArray, pi: npt.NDArray):
    (T, N) = frames.shape
    alpha = np.empty((T, N))
    alpha[0] = pi * frames[0]
    for t in range(1, T):
        alpha[t] = np.matmul(
            alpha[t-1], 
            A * frames[t]
        )
    return alpha
