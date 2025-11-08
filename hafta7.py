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
    print("a sayısı" ,a/n)
    print("b sayısı", b/ n)
    print("c sayısı", c / n)
    print("d sayısı", d/ n)
    print("e sayısı", e/ n)
    print("f sayısı", f/n)
hilelizar(360)