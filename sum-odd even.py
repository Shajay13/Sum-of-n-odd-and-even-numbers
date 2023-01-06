'''
Write a function that takes n as the parameter and finds 
a) Sum of  first n odd terms
b) Sum of first n even terms 
c) generate n random numbers from 1 to 20    '''

def oddeven(n):
    import random
    o,e=0,0
    for i in range(n*2+1):
        if i%2==0:
            e+=i
        else:
            o+=i
    print('Sum of  first',n,'odd terms: ',o)   #(a)
    print('Sum of  first',n,'even terms: ',e)  #(b)
    l=[]
    for i in range(n):
        l.append(random.randrange(1,20)) #(c)
    print(n,'random numbers from 1 to 20: ',l)
n=int(input('Enter the number'))
oddeven(n)


