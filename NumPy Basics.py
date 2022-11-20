import numpy as np


#assigning data
a=np.array([1,2,3])
print(a)
print(a[1])
l1=[1,2,3]
l2=['a','b','c']
b=np.array([l1,l2])
print(b)
d={1:'a',2:'b',3:'c'}
c=np.array(d)
print(c)


#get dimension
print(a.ndim)
print(b.ndim)

#get shape
print(a.shape)
print(b.shape)

#get data type
print(a.dtype)
print(b.dtype)
#to specify dtype
a.dtype='int16'
#or a=np.array([1,2,3],dtype='int16')
print(a.dtype)



a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
print(a[1,4])   


a = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(a)
print(a[0, 1, 2])

#negative indexing also works


#slicing
#[start:end:step]
#start included, end excluded   
#default of start is 0
#default of end is length of array in that dimension
#default of step is 1



#copy vs view
a=np.array([1,2,3,4,5])
b=a.copy()
c=a.view()
a[0]=6
print(a)
print(b)
print(c)

#copy doesnt change when original is modified
#view does change when original is modified
#conversely, original also changes when view is changed

#copy owns the data
#view does not own the data (just a view of the original)


#shape change
r = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
n2r = r.reshape(6,2)
m2r = r.reshape(4,3)
print(n2r)
print(m2r)
#new shape should allign with size
n3r=r.reshape(2,3,2)
print(n3r)
m3r=n2r.reshape(2,3,2)
print(m3r)

#reshaped arrays are copies of original
r[0]=100
print(n2r)
print(m3r)

#unknown dimension - one dimension is allowed to be unknown - pass -1 as dimension value
ur=r.reshape(2,2,-1)
print(ur)

#flattening array - flattening a multidimensional array - reshape(-1)
fr=m3r.reshape(-1)
print(fr)

#iteration - works as normal
for i in r:
    print(i)
for i in m2r:
    print(i)
    for j in i:
        print(j)


#joining arrays

#use concatenate(<array1>,<array2>,axis=<axis>)
#default of axis = 0
#dimensions of arrays being concatenated should be same
r1 = np.array([1, 2, 3])
r2 = np.array([4, 5, 6])
r = np.concatenate((r1, r2))
print(r)

r3 = np.array([[1, 2], [3, 4]])
r4 = np.array([[5, 6], [7, 8]])
r = np.concatenate((r3, r4), axis=1)
print(r)
r = np.concatenate((r3, r4))
print(r)
