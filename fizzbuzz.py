for i in range(1,100):
    output = "fizz"*(i%3==0)+"buzz"*(i%5==0)
    output += str(i)*(len(output)==0)
    print(output)