#This code was written by Japneet on 3rd March 2022, Thank you for reading

sum=0
while(True):
    print("Welcome to Kiryana Store")
    userinput=input("Enter the price of item or press q to quit\n")
    if userinput!='q':
        sum=sum+int(userinput)
        print(f"Your order total so far:₹{sum}")
    else:
        print(f"Your Total bill is ₹{sum}. Thank You for Shopping with us🥳. Come again!")
        break




