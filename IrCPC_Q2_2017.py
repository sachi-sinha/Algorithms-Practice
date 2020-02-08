"""
Solution to Question 2 of Problem Set 2017 of Irish Collegiate Programming Contest
Variables Used:
    l : List of powers of ten till 3.
    choice : Number of inputs that user chooses
    k : List of all numbers input
    g : A number that has been input
"""
from collections import Counter
l = [1000,100,10,1]
choice = int(input("Enter the number of Inputs: "))
k = []
for i in range(choice):
    g = int(input("Enter number: "))
    k.append(g)
for u in k:
  p = [] #p records the number from the list l that divides the number
  n = int(u) #number from the list of inputs
  for i in range(len(l)):
    if n >= l[i]:
        q = int(n/l[i])
        n = n - l[i]*q
        for k in range(q):
          p.append(l[i])

  c=Counter(p) #to count the number of occurences of each number from the list l in the list p


#for loop below breaks the number into its place value components
  for i in range(len(c)):
    var_t=c[1000]*1000
    var_h=c[100]*100
    var_t=c[10]*10
    var_o=c[1]*1
  #var_h
  if var_h>=100 and var_h<400:
    h=int((var_h)/100)
    ans_h = "C"*h
  elif var_h>=400 and var_h<500:
    ans_h = "CD"
  elif var_h>=500 and var_h<900:
    h=int((var_h-500)/100)
    ans_h = "D"+ "C"*h
  elif var_h>=900:
    ans_h = "CM"
  else:
    ans_h=""
 #var_t
  if var_t>=10 and var_t<40:
    t=int((var_t)/10)
    ans_t = "X"*t
  elif var_t>=40 and var_t<50:
    ans_t = "XL"
  elif var_t>=50 and var_t<90:
    t=int((var_t-50)/10)
    ans_t = "L"+ "X"*t
  elif var_t>=90:
    ans_t = "XC"
  else:
    ans_t=""

 #var_o
  if var_o>=0 and var_o<4:
    o=int((var_o))
    ans_o = "I"*o
  elif var_o>=4 and var_o<5:
    ans_o = "IV"
  elif var_o>=5 and var_o<9:
    o=int((var_o-5))
    ans_o = "V"+ "I"*o
  elif var_o>=9:
    ans_o = "IX"
  else:
    ans_o=""

  ans = c[1000]*'M'+ ans_h + ans_t + ans_o
  print(ans)
