import random
def hilelizar(n):
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    for i in range(n):
        x=random.randint(1,6)
        if(x==1):
            a+=1
        elif(x==2):
            b+=1
        elif (x == 3):
            c+= 1
        elif (x == 4):
            d+= 1
        elif (x == 5):
            e+= 1
        else:
            f+=1
    print("a sayısı" ,a/6)
    print("b sayısı", b/ 6)
    print("c sayısı", c / 6)
    print("d sayısı", d/ 6)
    print("e sayısı", e/ 6)
    print("f sayısı", f/6)
hilelizar(360)