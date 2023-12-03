class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        n1 = []
        n2 = []
        c1 = 0
        c2 = 0
        for i in num1:
            n1.append(dict[i])
        for j in num2:
            n2.append(dict[j])
        n1 = n1[::-1]
        n2 = n2[::-1]
        for k in range(len(n1)):
            c1+= (10**k ) * n1[k] 
        for l in range(len(n2)):
            c2+= (10**l ) * n2[l] 
        return str(c1*c2)