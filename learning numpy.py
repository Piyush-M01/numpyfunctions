import numpy as np
lst=[2,5,6,7,8]
print(np.array(lst))
print()
print(np.array([lst,lst]))
print()
#creating a diagonal matrix
print(10*np.eye(4))

print(np.zeros(shape=(4,6)))

print(np.arange(10))
print(np.arange(-5,10))
print(np.arange(-5,10,3))
print(np.arange(100,10,-5))

#to divide the matrix in values ranging from x to y with number of steps
print(np.linspace(5,20,4))

#generating random values
print(np.random.rand(2,3))
print(np.random.rand())
print(np.random.rand(2,2,3))
print(np.random.randint(2,10))
print(np.random.randint(2,3,3))

arr=np.arange(5,20)
print(arr[4])
print(arr[5:10])
print(arr[1:])
print(arr[:8])
print(np.cos(arr),np.tan(arr),np.sum(arr),np.mean(arr))

#stacking the arrays
a=np.random.rand(3,3)
b=np.random.rand(3,3)
 #horizontal
c=np.hstack((a,b))
print(a)
print(b)
print("merged matrix : ",c)

 #vertical
d=np.vstack((a,b))
#print(a)
#print(b)
print("merged matrix : ",d)

#addition of elements of array in :
print("addition row-wise and column-wise")
 #horizontal way
print(np.sum(a,axis=1))
 #vertical way
print(np.sum(a,axis=0))

print(np.cumsum(a))
print(np.cumproduct(a))

#removing the repeated number
print(np.unique(a))

#np.min(a) --min value
#np.max(a) --max value

#getting array value and its index
ar=np.arange(20,25)
for index,item in enumerate(ar):
    print(index,item)