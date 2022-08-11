

def Karatsuba(x, y):
    if len(x)==1 or len(y)==1:
        #print(x, y)
        return str(int(x)*int(y))
    else:
        x1 = x[:int(len(x)/2)]
        x2 = x[int(len(x)/2):]
        y1 = y[:int(len(y)/2)]
        y2 = y[int(len(y)/2):]
        third = str((int(x1)+int(x2))*(int(y1)+int(y2)))
        #print(x1,"\n", x2,"\n", y1, "\n", y2,"\n", third)
       # print(len(y1))
        p3 = Karatsuba(x1, y1)
        p1 = Karatsuba(x2, y2)
        p2 = Karatsuba(str(int(x1)+int(x2)), str(int(y1)+int(y2)))
        print(p1, p2, p3)
        val = int(p1+'0'*len(x))+int(p3)+ int(str(int(p2)-int(p1)-int(p3))+'0'*int(len(x)/2))
        print(val)
        return str(val)



X = 345345
y = 142325
print(Karatsuba('11116', '22223'))