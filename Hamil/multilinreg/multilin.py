import pandas as pd 
import numpy as np
from numpy.linalg import inv

#Read Dataset from Excel file using Pandas and store number of columns in the dataset in a variable ‘colums’
data = pd.read_excel('Bradley/multilinreg/ENB2012_data.xlsx') 
colums = (len(data.columns)) #10
# Computing max and min values in each column and store them in list
max= [data[c].max() for c in data.columns] # [0.98, 808.5, 416.5, 220.5, 7.0, 5, 0.4, 5, 43.1, 48.03]
min= [data[c].min() for c in data.columns]# [0.62, 514.5, 245.0, 110.25, 3.5, 2, 0.0, 0, 6.01, 10.9]
#-------------
# Now, Normalize the dataset using the formula: xnew = (x - xmin)/(xmax - xmin)
i=0
for c in data.columns:
    while(i<len(data.columns)): 
        data[c]=(data[c]-min[i])/(max[i]-min[i])
        i=i+1
        break
#-------------
# Now, split the dataset and store the features and target values in different list. 
# Here, I have stored the features in x_train list and the target values in y1,y2 lists.
arr = data.values #matrix of 1's
x_train=[]
y1=[]
y2=[]
a=data.shape #(768, 10)
for i in range(a[0]): #a[0] = 768                     
    x_train.append((arr[i][:-2]).tolist()) #i [X1,...,X8]
    y2.append(arr[i][-1]) #i [Y2]
    y1.append(arr[i][-2]) #i [Y1]
#-------------
# Concatenate the x_train list with matrix of 1ˢ and compute the coefficient matrix using the normal equation given above (Y=XC). 
# I have used numpy built-in functions for matrix operations
m=np.ones((768,1)) # a 768x1 vector of ones

b=np.matrix(x_train) # X

b=np.concatenate((m,b),axis=1) #why?    

d=b.T # X transpose 

e=np.linalg.inv(np.matmul(d,b)) # (X^T X)^-1

y1=np.matrix(y1) 
y1=y1.T

y2=np.matrix(y2)
y2=y2.T

f=np.matmul(e,d) # (X^T X)^-1 X^T

c1=np.matmul(f,y1) # (X^T X)^-1 X^T y1
c2=np.matmul(f,y2) # (X^T X)^-1 X^T y2
#-------------
# Input the test data and thereby store it in a list, x_test. 
# Predict the target variable using the test data and the coefficient matrix and thereby stored the result in Y1, Y2 .
    # x_test=[[1],]
    # for j in range (8): #8 independent variables
    #     inp=[float(input("Enter Value:"))]
    #     x_test.append(inp) 

x_test = [[1], [0.62], [808.50], [367.50], [220.58], [3.50], [5], [0.40], [5]]
# [[22.91143953]]
# [[23.06167597]]


for i in range(8):
    x_test[i+1][0]=(x_test[i+1][0]-min[i])/(max[i]-min[i]) #normalize x_test

x_test=np.matrix(x_test)

Y1=np.matmul(c1.T,x_test) # Y1= XC
Y2=np.matmul(c2.T,x_test) # Y2= XC
#-------------
# Print the predicted output. 
# As the value stored in Y1, Y2 is normalized I denormalized it after prediction as per the following equation, y^ = y^norm*(max y - min y) + min y
print(Y1*(max[-2]-min[-2])+min[-2])
print((Y2*(max[-1]-min[-1]))+min[-1])

# Enter Value:0.62
# Enter Value:808.50
# Enter Value:367.50
# Enter Value:220.50
# Enter Value:3.50
# Enter Value:5
# Enter Value:0.40
# Enter Value:5
# [[22.91870857]]
# [[23.06842293]]