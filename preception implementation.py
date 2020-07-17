
import math

b = 0.1
w = [0.5,0.5,0.5,0.5]
lr = 0.01

x = [1,2,3]
y = 1.5

def sum():
    s =  x[0] * w[0] + x[1] * w[1] + x[2] * w[2] + b * w[3]
    return s

def activation():
    s =  sum()
    soft = 1 / (1 + math.exp(-s))
    return soft 
    

a = activation()
error = y - a

print("Error: ",error)
print("activation:",a)

w[0] = w[0] + error * lr * x[0]
w[1] = w[1] + error * lr * x[1]
w[2] = w[2] + error * lr * x[2]
w[3] = w[3] + error * lr * b

print(w[0],w[1],w[2],w[3])

