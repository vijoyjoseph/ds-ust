allow = {'hra':.4,'da':.3,'ta':.2}
print(u"\u2661")

try:
    n1 = int(input('Enter no 1 ')) 
    n2 = int(input('Enter no 2 '))
    res = n1/n2
    print(n1,'/',n2,'=',res)

except ZeroDivisionError as e:
    print('Err',e)