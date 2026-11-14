def foo(a,b, *args, **kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1,2,3,4,5, six=6,seven=7)


def foo(a_list):
    a_list = [200,300,400]
    a_list.append(4)
    a_list[0] = -100

my_list = [1,2,3]
foo(my_list)
print(my_list)
