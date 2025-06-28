# local scope
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

def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "non local spam"
    def do_global():
        global spam
        spam = "this is global spam"
    spam = "this is testing"
    do_nonlocal()
    print("after local assigmet: " , spam)
    do_local()
    print("after non local assigmet: " , spam)
    do_global()
    print("after global assigmet: " , spam)

scope_test()
print("in global scope:", spam)
        