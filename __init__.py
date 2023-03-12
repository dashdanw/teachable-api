
some_list = [1,2,3,4,5]

def some_list_generator():
    for i in range(len(some_list)):
        yield some_list.pop()


for list_item in some_list_generator:
    print(list_item)
