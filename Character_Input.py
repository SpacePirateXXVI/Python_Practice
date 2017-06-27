while True:
    name = input("What is your name?: ").strip().title()
    age = input("What is your age?: ").strip()
    century  = (100-int(age)) + 2016

    
    
    output = "Your name is {} and you are {} years old. You will be 100 in the year {} " .format(name, age,century)
    print (output)

    num = input("Give me a number, please: ").strip()
    lego = int(num) * "Give me a number, please" "\n"
    print (lego)

