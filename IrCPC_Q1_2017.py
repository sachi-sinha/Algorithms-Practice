"""
Solution to Question 1 of Problem Set 2017 of Irish Collegiate Programming Contest
Variables Used:
    l : List of all input rows
    l2 : List of all output rows
    N : Number of rows
    M : Number of Columns
"""

""" Taking Input for the Question"""

N = int(input("Enter the number of lines: "))

M = int(input("Enter the number of columns: "))

l = []

l2 = []


for i in range(N):
    numbers = input("Enter row: ").split()
    l.append(numbers)
    ln = []
    for i in numbers:
        ln.append(0)
    l2.append(ln)

for i in l: # displaying the input
    for j in i:
        print(j,end=" ")
    print("\n")


"""
Calculating Output
Variables used:
    index : list of the positions of the mines, 'x'
"""
index = []

for i in range(len(l2)):
    for j in range(M):
         if l[i][j] == "x":
            index.append([i,j])

for i in index:
    t=i[0]
    k=i[1]
    if t==0 and k==0:
        l2[t][k+1]+=1
        l2[t+1][k]+=1
        l2[t+1][k+1]+=1

    elif t==0 and k!=0 and k!=(M-1):
        l2[t][k-1]+=1
        l2[t][k+1]+=1
        l2[t+1][k]+=1
        l2[t+1][k+1]+=1
        l2[t+1][k-1]+=1

    elif t!=0 and t!=(N-1) and k==0:
        l2[t-1][k]+=1
        l2[t-1][k+1]+=1
        l2[t][k+1]+=1
        l2[t+1][k]+=1
        l2[t+1][k+1]+=1

    elif t==(N-1) and k==(M-1):
        l2[t-1][k]+=1
        l2[t-1][k-1]+=1
        l2[t][k-1]+=1

    elif t==(N-1) and k!=(M-1) and k!=0:
        l2[t-1][k]+=1
        l2[t-1][k+1]+=1
        l2[t-1][k-1]+=1
        l2[t][k-1]+=1
        l2[t][k+1]+=1

    elif t!=(N-1) and t!=(0) and k==(M-1):
        l2[t-1][k]+=1
        l2[t-1][k-1]+=1
        l2[t][k-1]+=1
        l2[t+1][k]+=1
        l2[t+1][k-1]+=1

    else:
        l2[t-1][k]+=1
        l2[t-1][k+1]+=1
        l2[t-1][k-1]+=1
        l2[t][k-1]+=1
        l2[t][k+1]+=1
        l2[t+1][k]+=1
        l2[t+1][k+1]+=1
        l2[t+1][k-1]+=1


for i in index: # putting in the mine positions in the ouput list
    t = i[0]
    k = i[1]
    for i in range(len(l2)):
        for j in range(M):
            l2[t][k] = 'x'

for i in l2: # displaying the output
    for j in i:
        print(j,end=" ")
    print("\n")
