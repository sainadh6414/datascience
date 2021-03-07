import numpy as np

# intialize the array
a = np.array([1, 2, 3], dtype='int32')
print(a)

# intialize the array with float values
b = np.array([[9.0, 8.0, 7.0, 4.0],
              [6.0, 5.0, 4.0, 5.0],
              [6.0, 5.0, 4.0, 5.0]])

print('2x3 matrix', b)

# Get Dimension - ndim: n-dimension
print('get dimension', b.ndim)

# Get shape of an array (rows, coulumns)
print('shape of an array', a.shape, b.shape)

# Get Type using dtype
print('a.dtype', a.dtype)

# Get size using itemsize
print('a.itemsize', a.itemsize)

# Get total size
print('a.nbytes', a.nbytes)

# Accessing elements
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 1, 0, 11, 12, 13]])
print('big array', a)
print('\n Accessing elements[row, column], first row and fifth element a[0,5]', a[0, 5])

# Access a specific row
print('a[0, :]', a[0,:])

# Access a specific column
print('Access a specific column a[:,0]', a[:, 0])
print('Access a specific column a[:,2]', a[:, 2])
print('dimension', a.ndim)

# Get more elements [row_number, startindex:endindex:stepsize]
print('a[0, 2:5:1]', a[0, 1:5:1]);

# Change value
a[1, 5] = 20
print('change value at a[1,5]', a)

a[:, 2] = 123
print('change a whole column value a[:,2]=123', a)

a[:, 2] = [12, 13]
print('change a column cell value a[:,2]=[12, 13]', a)

mulDimArray = [[
    [1, 2, 3],
    [4, 5, 6]
],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]

mulDimArray = np.array(mulDimArray)
print('multi dim array', mulDimArray)
print('dimension', mulDimArray.ndim)

# Get specific element in the mul dim array
print('specific element in the mul dim array- firstSet->2nd Row->3rd element, mulDimArray[0, 1, 2]',
      mulDimArray[0, 1, 2])

# Use colons to specify the rows or columns
print('\n Get specific rows or columns using : ')
print('multiDimArray[:,1,:] gets the second rows from all dimensions', mulDimArray[:, 1,:])

# replace elements
print('\n replace elements in a specifc row')
mulDimArray[:, 1,:] = [[9, 9, 9], [8, 8, 8]]
print('mulDimArray[:,1,:]=[[9,9,9], [8,8,8]] => ', mulDimArray)

# Initialize different arrays
print('\n Initialize different arrays')

print('\n All zeros: ', np.zeros((2, 3)))
print('\n All Ones: ', np.ones((2, 3), dtype='int32'))
print('\n Any other number: ', np.full((2, 3), 99, dtype='float32'))
print('\n np.full_like: ', np.full_like(mulDimArray, 4))
print('\n Init random float numbers', np.random.rand(4, 2, 3))
print('\n Init random integer numbers', np.random.randint(4, size=(3, 3)))
print('\n Identity matrix or square matrix', np.identity(5))
print('\n Repeat the array over the rows (axis=0) or columns if the (axis=1)')
arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis=0)
print(r1)

# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 9 0 1
# 1 0 0 0 1
# 1 1 1 1 1
print('1 1 1 1 1 \n' + 
      '1 0 0 0 1 \n' + 
      '1 0 9 0 1 \n' + 
      '1 0 0 0 1 \n' + 
      '1 1 1 1 1')
fiveByFiveArray = np.ones((5, 5), dtype='int32')
fiveByFiveArray[1, (1, 2, 3)] = 0
fiveByFiveArray[2, (1, 2, 3)] = [0, 9, 0]
fiveByFiveArray[3, (1, 2, 3)] = 0
print('fiveByFiveArray\n', fiveByFiveArray)

# much better way
print('1 1 1 1 1 \n' + 
      '1 0 0 0 1 \n' + 
      '1 0 9 0 1 \n' + 
      '1 0 0 0 1 \n' + 
      '1 1 1 1 1')
output = np.ones((5, 5), dtype='int32')
z = np.zeros((3, 3), dtype='int32')
z[1, 1] = 9
output[1:4, 1:4] = z
print('output\n', output)

# Copy arrays
print('z.copy() references are not carried over\n', z.copy())

# Math capabilities
print('\nMath capabilities\n')
a = np.array([1, 2, 3, 4])
print('a', a)
print('a + 2', a + 2)
print('a - 2', a - 2)
print('a * 2', a * 2)
print('a / 2', a / 2)

b = np.array([1, 0, 1, 0])
print('a', a)
print('b', b)
print('a + b', a + b)

print('a ** 2', a ** 2)

print('take Sin value np.sin(a)', np.sin(a))

# Linear Algebra
print('\nLinear Algebra\n')

a = np.ones((2, 3))
print('a', a)

b = np.full((3, 2), 2)
print('b', b)

print('np.matmul(a,b)\n', np.matmul(a, b))

print('\n==> Statistics \n')
stats = np.array([[1, 2, 3], [4, 5, 6]])
print('stats\n', stats)
print('np.min(stats)', np.min(stats))
print('np.max(stats)', np.max(stats))
print('get min of the first row and second row, np.main(stats, axis=1)', np.min(stats, axis=1))

# Reorganizing

print('\n==>ReOrganizing\n')
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print('before', before)
print('before.reshape((8,2))', before.reshape((8, 1)))

print('\n==>Vertical Stacking\n')
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
print('np.vstack([v1,v2])\n', np.vstack([v1, v2]))

print('\n==>Horizontal Stacking\n')
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
print('np.hstack([v2,v1])\n', np.hstack([v2, v1]))

print('\nGenerate array from input text file\n')
print("filedata = np.genfromtxt('data.txt', delimiter=',')")
print("filedata.astype('int32')")

print('\n ==> Advanced Indexing and Boolean Masking\n')
idx = np.array([[1, 2, 3], [4, 5, 6]])
print('idx > 5\n', idx > 5)
print('idx[idx > 5]', idx[idx > 5])

print('\n==>Index a list a[[rowlist],[collist]]\n')
a = np.array([1, 2, 3, 4, 5])
print('a', a)
print('a[[0,2,4]]', a[[0, 2, 4]])

print('np.any(idx > 5, axis=0)', np.any(idx > 5, axis=0))
print('(a > 2) && (a <=5)', ((a > 2) & (a <= 5)))

# ====> Great Learning Course
print('np.cos(np.pi)', np.cos(np.pi))
print('np.sqrt(1.21)', np.sqrt(1.21))
print('np.log(np.exp(5.2))', np.log(np.exp(5.2)))

vec = np.array([1, 2, 3])
print('vec', vec)

mat = np.array([[1, 2, 1], [4, 5, 9], [1, 8, 9]])
print('mat', mat)
print('transpose', mat.T)

print('\nOther ways to create arrays\n')
arangeArray = np.arange(0, 15)
print('arangeArray', arangeArray)

arangeArray = np.arange(3, 21, 6)
print('arangeArray with 6 step from 3 to 21', arangeArray)

# Both start and end index are inclusive and gives out 25 equally spaced values
linSpaceArr = np.linspace(0, 5, 25)
print('linSpaceArr', linSpaceArr)

print('reshape the linspace array into 5x5 matrix')
print('reshape\n', linSpaceArr.reshape(5, 5))

# Fill array with all zeros
print('All zeros \n', np.zeros([5, 3]))

# Fill array with all ones
print('All Ones \n', np.ones([5, 3]))

# Identity matrix
print('Identity matrix\n', np.eye(5))

# Add, subtract or mul arrays
arr1 = np.arange(1, 6)
arr2 = np.arange(3, 8)
print('arr1\n', arr1)
print('arr2\n', arr2)
print('arr1 + arr2 \n', arr1 + arr2)
print('arr1 - arr2 \n', arr1 - arr2)
print('arr1 * arr2 \n', arr1 * arr2)
print('1/arr1 \n', 1 / arr1)
print('np.sqrt(arr2)\n', np.sqrt(arr2))

#  Matrix multiplication
arr1 = np.ones([3, 3])
arr2 = np.arange(1, 4)

print('arr1\n', arr1)
print('arr2\n', arr2)
product = np.matmul(arr1, arr2)
print('np.matmul(arr1, arr2)', product)

# Linear Algebra
print('Linear Algebra\n')
# print('np.linalg.solve(arr1, product)', np.linalg.solve(arr1, product))

# Calculate unique values in an array
uniq = np.array(['blue', 'red', 'oramge', 'purple', 'purple', 'orange', 'Red', '6'])
print('uniq\n', uniq)
print('np.unique(uniq)', np.unique(uniq))

# Generate random values
random_arr1 = np.random.rand(5, 5)
print('random_arr\n', random_arr1)

random_arr2 = np.random.randn(5, 5)
print('np.random.randn(5, 5)\n', random_arr2)

# Mean, Standard Deviation
print(np.mean(random_arr1), 'np.mean(random_arr1)')
print('np.std(random_arr2)', np.std(random_arr2))

print(np.linspace(10, 20, 3))

# Accessing numpy array values
rand_vec = np.random.randn(19)
print('rand_vec\n', rand_vec)
print('rand_vec[6]', rand_vec[6])

# Accesing multiple entriees
print('rand_vec[4:9]', rand_vec[4:9])

# Accesing multiple non consecutive entries
non_consecutive = np.arange(0, 15, 3)
print('non_consecutive\n', non_consecutive)
print(rand_vec[non_consecutive])

# Accesing matrices
rand_mat = np.linspace(0, 5, 25).reshape(5, 5)
print('rand_mat\n', rand_mat)
print('rand_mat[1][2]\n', rand_mat[1][2])
print('rand_mat[1, 2]\n', rand_mat[1, 2])
print('rand_mat[0:2, 1:3]\n', rand_mat[0:2, 1:3])

# Changing the values in an arrray
print('rand_vec\n', rand_vec)
rand_vec[3:5] = 4
print('rand_vec\n', rand_vec)

rand_vec[3:5] = [1, 2]
print('rand_vec\n', rand_vec)

rand_mat[1:3, 3:5] = 0
print('rand_mat[1:3, 3:5]=0', rand_mat)

# Memory references
sub_mat = rand_mat[0:2, 0:3]
print(sub_mat)

sub_mat[:] = 3
print(sub_mat)
print(rand_mat)

# Use the copy function
sub_mat2 = rand_mat[0:2, 0:3].copy()
sub_mat2[:] = 5
print(sub_mat2)
print(rand_mat)

# Logicals
rand_vec = np.random.randn(15)
print('rand_vec\n', rand_vec)
print('rand_vec>0', rand_vec > 0)
print('rand_vec[rand_vec>0]', rand_vec[rand_vec > 0])

# Logicals on an array
print('rand_mat\n', rand_mat)
print('rand_mat[rand_mat>0]\n', rand_mat[rand_mat > 0])

# Assign items of a matrix using logicals
print('rand_vec\n', rand_vec)
rand_vec[rand_vec > 0.5] = -5
print('rand_vec changed\n', rand_vec)

# Save numpy arrays to hard drive and load them
print('===> Save numpy arrays to hard drive and load them \n')

# Save one array to file
print('==> Save one array to file \n')
np.save('saved_file_name', rand_mat)

# Save more than one 
np.savez('zipped_file_name', rand_vec=rand_vec, rand_mat=rand_mat)

# load the saved numpy array
print('load the saved numpy array\n')

loaded_vec = np.load('saved_file_name.npy')
loaded_zip = np.load('zipped_file_name.npz')

print('loaded_vec\n', loaded_vec)
print('loaded_zip\n', loaded_zip)

print('loaded_zip[rand_mat]\n', loaded_zip['rand_mat'])
print('loaded_zip[rand_vec]\n', loaded_zip['rand_vec'])

# Save numpy array as text file
np.savetxt('text_file_name.txt', rand_mat, delimiter=',')

# load the saved text file
rand_mat_txt = np.loadtxt('text_file_name.txt', delimiter = ',')
print('rand_mat_txt\n', rand_mat_txt)
