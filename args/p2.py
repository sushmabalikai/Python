def function_1(*args):
    if(len(args)==3):
        print("The name of student is",args[0],"The age is",args[1],"and rollno is",args[2])
    else:
        print("The name of student is",args[0],"The age is",args[1])
list=['harry',22]
function_1(*list)        
