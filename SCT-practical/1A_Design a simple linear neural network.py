x=float(input("\nEnter input x="))
b=float(input("\nEnter input b="))
w=float(input("\nEnter input w="))
net=(b+x*w)
print("\t***OUTPUT***\n")
print("\nnet=",net)
if(net<0):
    out=0
elif(net>=0)&(net<=1):
    out=net
else:
    out=1
print("output=",out)	