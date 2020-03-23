while True:
    c=input ('Input operation: /, *, +, - ')
    if c=='0':
        break
    if c in ('/', '*', '+','-' ):
        a=float(input ('Input a '))
        b=float(input ('Input b '))

        if c=='*':
            print (a*b)
        elif c=='+':
            print (a+b)
        elif c=='-':
            print (a-b)
        if c=='/':
            if b==0:
                print ('Zero division error')
            else:
                print (a/b)
    else:
        print ('Bad operation')
