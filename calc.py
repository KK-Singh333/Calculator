def log():
    a=float(input("Enter the number "))
    e=2.718281828459045
    n=int(input("Enter number of digits upto which you accurately want the result(upper limit is 14) "))
    i=1
    c=0
    f=1
    while(c<=n):
        if(f==1):
            while((e**i)<a):
                i=i+(0.1**c)
        else:
            while((e**i)>a):
                i=i-(0.1**c)
        f=f*(-1)
        c+=1
    return(round(i,n))
a=0
b=""
print("Key for operations:-\nUse b to solve quadratic\nUse + for addition\nUse - for substraction\nUse * for multiplication\nUse / for division\nUse t to calculate tan of any angle(in radians)\nUse p to find square root\nUse l to find natural log of any number\nType o to reset\nType 'stop' to stop entering\n(Enter another number along with operator e.g. +9 and dont use any operator with log, tan and square root)\nAt each input you can either enter an operator followed by number or function followed by number")

while(b!="stop"):
    b=input().lower()
    if b:
        if(b == "stop"):
            break
        elif(b == "b"):
            x,y,z=input("Enter values of a,b,c separated by single space ").split(" ")
            x=float(x)
            y=float(y)
            z=float(z)
            print("Values of x are "+str((-y+((y**2)-4*x*z)**0.5)/(2*x))+" and "+str((-y-((y**2)-4*x*z)**0.5)/(2*x)))
        if(b[0] in "+"):
            a=a+float(b[1::1])
        elif(b[0] in "-"):
            a=a-float(b[1::1])
        elif(b[0] in "x" or b[0] in "X" or b[0] in "*"):
            a*=float(b[1::1])
        elif(b[0] in "l"):
            a=(log())
        elif(b[0] in "/"):
            a/=float(b[1::1])
        elif(b[0] == "o"):
            a=0
        elif(b[0] == "p"):
            a=float(b[1::1])**(0.5)
        elif(b[0]=='t'):
            a=(float(b[1::1])+(float(b[1::1])**3)/3+((2/15)*(float(b[1::1])**5)))
    else:
        print("You didn't type anything")
    
        
    
    print(".......\n"+str(a)+"\n.......")
print(str(a)+"\n.......")
