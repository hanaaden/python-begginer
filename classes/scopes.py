#local scope
def func():
    x=100
    print(x)
    
func()

#enclosing scope
def out_func():
    x=900
    def ins_func():
        print(x)
    ins_func()
out_func()

#global scope
y=90
def myfunc():
    print(y)
myfunc()
print(y)
