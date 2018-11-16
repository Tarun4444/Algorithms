def f():
    some_dict={1:'a',2:'b',3:'c'}
    key=1
    default_value = 2
    
    if key in some_dict:
        value = some_dict[key]
    else:
         value = default_value

    print(value)
    
    value = some_dict.get(key, default_value)

    print(value)

f()
