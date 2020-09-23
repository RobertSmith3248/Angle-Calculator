import math
#https://github.com/RobertSmith3248/Angle-Calculator.git
#distance formula then law of cosines

#must input numbers without separation
    #i.e. 1 1 2 1 1 2 instead of (1,1), (2,1), (1,2)

Ax, Ay, Bx, By, Cx, Cy=input("Enter x and y coordinates for the vertices: ").split()
print("x-value for point A: ", Ax)
print("y-value for point A: ", Ay)
print("x-value for point B: ", Bx)
print("y-value for point B: ", By)
print("x-value for point C: ", Cx)
print("y-value for point C: ", Cy)

A=(float(Ax),float(Ay))
B=(float(Bx),float(By))
C=(float(Cx),float(Cy))

#distance squared
#ordered pair[1st number]
def LengthSquared(D, E):
    xDiff = D[0] - E[0]
    yDiff = D[1] - E[1]
    return (xDiff*xDiff)+(yDiff*yDiff)

#Lengths squared
a2 = LengthSquared (A, B)
b2 = LengthSquared (B, C)
c2 = LengthSquared (A, C)

#lengths
a=math.sqrt(a2)
b=math.sqrt(b2)
c=math.sqrt(c2)

#law of cosines for angles
alpha1=math.acos((b2+c2-a2)/(2*b*c))
beta1=math.acos((a2+c2-b2)/(2*a*c))
gamma1=math.acos((a2+b2-c2)/(2*a*b))

#radians to degrees
alpha=alpha1*180/math.pi
beta=beta1*180/math.pi
gamma=gamma1*180/math.pi

alpha=round(alpha, 2)
beta=round(beta, 2)
gamma=round(gamma, 2)

print(alpha, beta, gamma)
