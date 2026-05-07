import random
import math

N = 100000
inside = 0

for _ in range(N):
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1:
        inside += 1

pi_estimate = 4 * inside / N
print(pi_estimate)