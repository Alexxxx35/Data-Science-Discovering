import numpy as np

a= np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# print(a)
b= np.array([[1.0,2.0,3.0],[4.0,5.0,6.0]])
# print(b)
c= np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(c)
# print(a.ndim)
# print(b.ndim)

# print(a.shape)
# print(b.shape)

# print(a.dtype)

# print(a.itemsize) #size of ele inside list

# print(a.size) #length list
# print(a.size * a.itemsize) #get total size

# print(a.nbytes) #equivalence
# print(b.nbytes)

# print(a.shape)

#access to specific ele => fourth ele of first list inside main list
# print(a[0,-4])
# print(a[0,3])

#access to specific row
# print(a[0,:3])

#access to specific col
# print(a[1,3:6])

#access to ele with index [startindex:endindex:stepsize]
# print(a[1,0:-1:2])

#replace value of an ele inside an array
# a[1,5]=20
# a[0:,3]=5
# print(a)

# print(c[:,1,:])
# print(c[0,1,:])
# print(c[:1,1,:])
# print(c[1,0])
# print(c[:,0,:])
# print(c[:,1,1])
# c[:,1,1]=[5,5]
# print(c[:,1,1])
# print(c)


#initializing different types of arrays
full_array=np.zeros((2,3,4),dtype=int)
# print(full_array)

#random generation
random_matrice=np.random.rand(3,2)
c_matrice=np.random.random_sample(c.shape)
random_array_integers=np.random.randint(1,6, size=(3,3))
# print(random_matrice)
# print(c_matrice)
# print(random_array_integers)

#repeat array
arr=np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=0)
# print(r1)

#matrices
z=np.zeros((3,3))
z[1,1]=9
# print(z)
var=np.ones((5,5))
# var[2,2]=7 =>middle of matrix=7
var[1:4,1:4]=z
# print(var)

#operations
# print(var+2)
# print(var*5)
# print(var/2)
# print(var**2)
# print(np.cos(var))

#reorganize array
np_array_2d = np.arange(0, 6).reshape([3,2])
# np_array_2dv2 = np.arange(0, 6).reshape([2,3])
#### =>respect meta values
# print(np_array_2d)
# print(np_array_2dv2)
sum_=np.sum(np_array_2d, axis = 1)
sum_2=np.sum(np_array_2d, axis = 0)
# print(sum_)
# print(sum_2)
############ axis=0 :l'axe est horizontal axis=1: l'axe est vertical ############


#idem pour les concaténations
arr_to_concat1=([[1, 1, 1],[1, 1, 1]])
arr_to_concat2=([[9, 9, 9],[9, 9, 9]])
# print(arr_to_concat1)
# print(arr_to_concat2)
concat=np.concatenate([arr_to_concat1,arr_to_concat2],axis=0)
concat2=np.concatenate([arr_to_concat1,arr_to_concat2],axis=1)
# print(concat)
# print(concat2)
#### One Dimensional numpy arrays only have one axis => axis=0

x=np.ones((2,3))
# print(x)
y=np.full((3,2),2)
# # print(y)
# print(np.matmul(x,y))

#statistics
stats= np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(stats)
#find minus and maximum
# print(np.min(stats,axis=0))
# print(np.max(stats,axis=0))

#stacking
# print(np.vstack([arr_to_concat1,arr_to_concat2,arr_to_concat2]))

#take data from file
data_from_file=np.genfromtxt('data_test.txt',delimiter=',')
data_from_file=data_from_file.astype('int32')
# print(data_from_file)
data_bigger_than_index=data_from_file[data_from_file>50]
# print(data_bigger_than_index)

filtered_data=data_bigger_than_index[[0,2,5]]
# print(filtered_data)

#Boolean masking
advanced_index=np.any(data_from_file> 50, axis=0)
advanced_index_3_all=np.any(data_from_file> 50, axis=1)
# print(advanced_index)
# print(advanced_index_3_all)

advanced_filtred_index=((data_from_file>50)&(data_from_file<100))
# print(advanced_filtred_index)
####~ => NOT
reverse_advanced_filtred_index=(~((data_from_file>50)&(data_from_file<100)))
# print(reverse_advanced_filtred_index)
#-------------------------------------------------------------------------------
integers=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
print(integers)
print(integers[2:4,0:2])
print(integers[[0,1,2,3],[1,2,3,4]])
print(integers[[0,4,5],3:5])