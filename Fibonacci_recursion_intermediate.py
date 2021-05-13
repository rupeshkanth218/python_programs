def fibro(limit):
    if limit<=1:
        return limit
    else:
        return (fibro(limit-1)+fibro(limit-2))
        
a=int(input("please enter the numbers"))

for i in range(0,a):
    if (i==a-1):
        print(fibro(i))
    else:
        print(fibro(i), end=",")
        