#Pract 3B
#supervised learning
import numpy as np
import time
np.set_printoptions(precision=2)
x=np.zeros((3,))
weights=np.zeros((3,))
desired=np.zeros((3,))
actual=np.zeros((3,))
for i in range(0,3):
    x[i]=float(input("Initial inputs:"))

for i in range(0,3):
    weights[i]=float(input("Initial weights:"))

for i in range(0,3):
    desired[i]=float(input("Desired output:"))

a=float(input("Enter learning rate:"))
actual=x*weights
print("actual",actual)
print("desired",desired)

while True:
    if np.array_equal(desired,actual):
        break #no change
    else:
        for i in range(0,3):
            weights[i]=weights[i]+a*(desired[i]-actual[i])

    actual=x*weights
    print("weights",weights)
    print("actual",actual)
    print("desired",desired)
print("*"*30)
print("Final output")
print("Corrected weights",weights)
print("actual",actual)
print("desired",desired)