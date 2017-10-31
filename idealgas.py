import numpy as np
import random as rd


size = 100
steps = 1000
n = 5
dT = 0.1


#start particles
grid = [np.random.rand(n,2)*size]
griv = [np.random.rand(n,2)*10]
print(type(grid[0]))

for i in range(steps):
	r_new = grid[i] + griv[i][:] * dT
	v_new = griv
	for j in range(n):
		for k in range(2):
			if r_new[j,k] >= 100:
				r_new[j,k] -= 2*(r_new[j,k]-100)
				v_new[j,k] *= -1
			elif r_new[j,k] <= 0:
				r_new[j,k] *= -1
				v_new[j,k] *= -1
	
	grid.append(r_new)
	griv.append(v_new)
	
	
	




