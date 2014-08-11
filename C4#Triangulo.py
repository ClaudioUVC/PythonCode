#perimetro
def perimetrotriangulo(a,b,c):
    return a+b+c
#area
def areatriangulo(a,b,c):
    s = (perimetrotriangulo(a,b,c))/2
    return s*(s-a)*(s-b)*(s-c)

#valido
def triangulovalido(a,b,c):
    if a>0 and b>0 and c>0:
        if ((a+b)>c) and ((b+c)>a) and ((c+a)>b):
            return True
        else:
            return False
    else:
        return False

#tipo
def tipotriangulo (a,b,c):
    if a==b and b==c:
        print "Equilatero."
    else:
        if a==b or b==c or c==a:
            print "Isosceles."
        else:
            print "Escaleno."

#rectangulo
def triangulorectangulo(a,b,c):
    if (min(a,b,c))%3 == 0:
        if (max(a,b,c))%5 == 0:
            if (a>b and a<c) or (a>c and a<b):
                if a%4==0:
                    return True
                else:
                    return False
            else:
                if (b>a and b<c) or (b>c and b<a):
                    if b%4==0:
                        return True
                    else:
                        return False
                else:
                    if (c>a and c<b) or (c>b and c<a):
                        if c%4==0:
                            return True
                    else:
                        return False
        else:
            return False
    else:
        if (min(a,b,c))%5 == 0:
            if (max(a,b,c))%13 == 0:
                if (a>b and a<c) or (a>c and a<b):
                    if a%12==0:
                        return True
                    else:
                        return False
                else:
                    if (b>a and b<c) or (b>c and b<a):
                        if b%12==0:
                            return True
                        else:
                            return False
                    else:
                        if (c>a and c<b) or (c>b and c<a):
                            if c%12==0:
                                return True
                        else:
                            return False
            else:
                return False
        else:
            return False
