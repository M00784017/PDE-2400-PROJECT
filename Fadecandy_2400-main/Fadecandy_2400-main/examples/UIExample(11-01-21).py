value = input("welcome to the menue. options are listed below: /n/t 1.Roll /n/t 2.Scroll /n Type your choice")
print("The value you input is:", value)
print(f'it is of type{type(value)}.')
def func1(val):
    return val**val
def func2(val):
    return val**val
def func3(val):
    return val**val
while True:
   if value.isdigit()==True:
       
        value=int(value)
        break
    
else:
        
    print("invalid input, please provide an integer:")

#print("The converted is :", value)
#print(f'it is of type {type(value)}.')
    
if value==1:
    func1(val)
elif value==2:
    func2(value)
elif value==3:
    func3(value)


