import matplotlib.pyplot as plt


b = 1 # parametro de impacto

posin1 = (-10, b) 
posin2 = (0, 0)
velin1 = (.1,0)
velin2 = (0,0)
dT = 0.1
tmax = 100
m = (1,5)# particle masses
k = 1. # 1/4piE0 * q1 * q2

def force(r1, r2):
	(x,y) = (r2[0] - r1[0], r2[1] - r1[1])
	faux = -k /pow(x*x + y*y, 3)
	return (faux * x, faux * y)

def vverlet2d(r1, r2, v1, v2, a1, a2, dT):
    vaux1 = (v1[0]+1./2*(a1[0])*dT, v1[1]+1./2*(a1[1])*dT)
    vaux2 = (v2[0]+1./2*(a2[0])*dT, v2[1]+1./2*(a2[1])*dT)
    r_n1  = (r1[0] + vaux1[0]*dT, r1[1] + vaux1[1]*dT)
    r_n2  = (r2[0] + vaux2[0]*dT, r2[1] + vaux2[1]*dT)
    a_n1  = (force(r_n1, r_n2)[0]/m[0],force(r_n1, r_n2)[1]/m[0])
    a_n2  = (force(r_n2, r_n1)[0]/m[1], force(r_n2, r_n1)[1]/m[1])
    v_n1  = (vaux1[0] + 1./2*(a_n1[0])*dT, vaux1[1] + 1./2*(a_n1[1])*dT)   
    v_n2  = (vaux2[0] + 1./2*(a_n2[0])*dT, vaux2[1] + 1./2*(a_n2[1])*dT)   
    return ((r_n1, r_n2), (v_n1, v_n2), (a_n1, a_n2))


r1 = [posin1]
r2 = [posin2]
v1 = [velin1]
v2 = [velin2]
a1 = [(force(r1[0],r2[0])[0]/m[0],force(r1[0],r2[0])[1]/m[0])]
a2 = [(force(r2[0],r1[0])[0]/m[1],force(r2[0],r1[0])[1]/m[1])]

for i in range(0,int(tmax/dT)):
	nois = vverlet2d(r1[i], r2[i], v1[i], v2[i], a1[i], a2[i], dT)
	r1.append(nois[0][0])
	r2.append(nois[0][1])
	v1.append(nois[1][0])
	v2.append(nois[1][1])
	a1.append(nois[2][0])
	a2.append(nois[2][1])

for i in range(0, 100):
	print(r1[i])	
	
plt.scatter(*zip(*r1), marker='.')
plt.scatter(*zip(*r2), marker='.')
plt.show()
