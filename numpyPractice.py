import numpy as np
### create array using numpy
arr=np.array([1,2,3,4,5])
# print(type(arr))
## Output: <class 'numpy.ndarray'>

# print(arr.shape)
## Output: (5,)

arr2=arr.reshape(1,5)
# print(arr2)

## Output : [[1 2 3 4 5]]



arr2=arr.reshape(5,1)
# print(arr2)
## Output : [[1]
#  [2]
#  [3]
#  [4]
#  [5]]

# arr2=arr.reshape(1,4)
# print(arr2)
## Output : Traceback (most recent call last):
#   File "/home/deq/Projects/python practice/numpyPractice.py", line 15, in <module>
#     arr2=arr.reshape(1,4)
# ValueError: cannot reshape array of size 5 into shape (1,4)

### 2D ARRAY
arr2=np.array([[1,2,3,4,5],[1,8,8,8,7]])
# print(arr2.shape)
## Output : (2, 5)
# print(arr2.dtype) #Output: int64

a=np.arange(0,10,2)
# print(a)
## Output [0 2 4 6 8]
# print(a.reshape(5,1))
## Output [[0]
#          [2]
#          [4]
#          [6]
#          [8]]

# b=np.ones((3,4))
# print(b)
#Output [[1. 1. 1. 1.]
#        [1. 1. 1. 1.]
#        [1. 1. 1. 1.]]


###Identity Matrix

b=np.eye(3)
# print(b)
#Output [[1. 0. 0.]
#        [0. 1. 0.]
#        [0. 0. 1.]]

# print(b.ndim) #Output 2

# print(b.dtype) #Output float64

# print(b.itemsize)  # Output 8


###* Numpy Vectorized Operation

arr1=np.array([1,2,3,4,5])
arr2=np.array([10,20,30,40,50])

##Element Wise addition
# print("addition",arr1+arr2)
##Output : addition [11 22 33 44 55]

## Element wise subtraction
# print("Substraction",arr1-arr2)
##Output : Subtraction [ -9 -18 -27 -36 -45]

##Element Wise multiplication
# print("Multiplicatin",arr1*arr2)
##Output : Multiplicatin [ 10  40  90 160 250]

## Element wise Division
# print("Division",arr2/arr1)
##Output : Division [10. 10. 10. 10. 10.]


### Universal Functions

arr=np.array([1,2,3,4,5,6,])

##square root
print(np.sqrt(arr))
##Output: [1.         1.41421356 1.73205081 2.         2.23606798 2.44948974]

##Exponential
print(np.exp(arr))
##Output:[  2.71828183   7.3890561   20.08553692  54.59815003 148.4131591     403.42879349]

## Sine
print(np.sin(arr))
##Output: [ 0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427 -0.2794155 ]


## natural log
print(np.log(arr))
##Output:[0.   0.69314718 1.09861229 1.38629436 1.60943791 1.79175947]



