import torch
#Exercise 1
#1.Create tensors
#Create a 2D tensor with dimension 3 x 4 includes elements are 7
array = torch.ones(3,4)*7
print(array)

#Create a 1D tensor includes even numbers from 0 to 10
even = torch.tensor([x for x in range (0,11) if x % 2 ==0])
even1 = torch.arange(0, 12, 2)
print(even)
print(even1)

#Create a tensor by randomizing with normal distribution
ran_tensor = torch.randn(2,3)
print(ran_tensor)

#2. 
A = torch.arange(12).reshape(3,4)
print(A)
row0 = A[0]
print(row0)

col3 = A[:,3]
print(col3)

ele12 = A[1,2]
print(ele12)

sub_tensor = A[0:2,2:]
print(sub_tensor)


#Exercise 2: tensor operations
B = torch.tensor([[1,2], [3,4]])
C = torch.tensor([[5], [6]])

total = B + C
print('total B and C',total)

element_wise = B*B
print('elemetn wise:\n', element_wise)

B_dot_C = B.matmul(C)
print('B multiple C:\n', B_dot_C)

B_new = B.reshape(1,1,2,2)
print('B new:\n', B_new)
B_new1 =B.view(1,1,2,2)
print('B new by view:\n', B_new1)

#Exercise 3
D = torch.rand(6)
D16 = D.view(1,6)
D23 = D.reshape(2, 3)

print('Compare\n', D, '\n', D16, '\n', D23)
print('Is GPU available', torch.cuda.is_available())
