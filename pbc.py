import math
import numpy as np
import matplotlib.pyplot as plt

# DATA
size = 10
N = 10
maxTime = 200
dt = 0.1

def leonardjones(sigma, x,y):
	r = math.sqrt(x*x+y*y)
	s1 = sigma/r
	s3 = pow(s1,3)
	s6 = s3*s3
	lj = 48*(-0.5*s6+s6*s6)/pow(r,2)
	return (lj*x, lj*y)

def timeEvol(r, v, dt):

	rl = r + v*dt 
	return rl

def checkBox(r, v, pbc=True):
	# check if particle is out of box, invert vel
	# CC NAO PERIODICA
	if pbc = False:	
		for j in coord(2):
			for i in range(N):
				if r[i][j] <= 0:
					r[i][j] *= -1
					v[i][j] *= -1
				elif r[i][j] >= size:
					r[i][j] = 2*size - r[i][j]
					v[i][j] *= -1
		return r, v
	# CC PERIODICA	
	else:
		np.remainder(r+10, 10)
		return r, v		


r = np.zeros((2,2,2000))
r[:,:,0] = [[4,4],[6,6]]
print(r)




plt.scatter(r[:,0,0],r[:,1,0])
plt.xlim(0,10)
plt.ylim(0,10)
plt.show()

