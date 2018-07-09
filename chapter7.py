from numpy import *

# x = int(raw_input("Enter Sigmoid X\n"))

def sigmoid(x):
	return 1./(1+exp(-x))

# print "Sigmoid is",sigmoid(x)


Wxh= 0.5
Whh= -1.0
Why= -0.7
hbias= -1.0
ybias=0.0

x0 = 9
x1 = 4
x2 = -2

z0 = Wxh * x0 + hbias
h0 = sigmoid(z0)
y0 = Why*h0+ybias
t0 = 0.1
E0 = 0.5*((t0 - y0)**2)

z1 = (Wxh*x1) + (Whh * h0) + hbias
h1 = sigmoid(z1)
y1 = Why * h1 + ybias
t1 = -0.1
E1 = 0.5*((t1 - y1)**2)

z2 = (Wxh * x2) + (Whh * h1) + hbias
h2 = sigmoid(z1)
y2 = Why * h2 + ybias
t2 = -0.2
E2 = 0.5*((t2 - y2)**2)

Err = E0 + E1 + E2



print(h2)





Wxh=-0.1
Whh=0.5
Why=0.25
hbias=0.4
ybias=0.0

x0 = 18.
x1 = 9.
x2 = -8.

z0 = Wxh * x0 + hbias
h0 = sigmoid(z0)
y0 = Why*h0+ybias
t0 = 0.1
E0 = 0.5*((t0 - y0)**2)

z1 = (Wxh*x1) + (Whh * h0) + hbias
h1 = sigmoid(z1)
y1 = Why * h1 + ybias
t1 = -0.1
E1 = 0.5*((t1 - y1)**2)

z2 = (Wxh * x2) + (Whh * h1) + hbias
h2 = sigmoid(z1)
y2 = Why * h2 + ybias
t2 = -0.2
E2 = 0.5*((t2 - y2)**2)

Err = E0 + E1 + E2



print(Err)