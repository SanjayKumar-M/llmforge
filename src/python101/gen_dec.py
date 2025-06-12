#decorators  -> a func that takes another func and process it i.e extending or modifying it's behaviour without changing the actual function. As simple as that

# **args means how many arguments we gonna pass, just like rest in js. eg. def num(**args), then num(1,2,3,4...)
# **kwargs means keyword arguments, i.e  key value dict format. def person(**kwargs): i.e person(name="Sanjay",age="20") => this can be get by kwargs.get('name')

def person(**kwargs):
    name = kwargs.get('name','Guest') # here declaring guest as default value
    print(f"Hello {name}")

person(name="Sanjay")

# functools.wrap is used normally in decorator, coz this helps to preserve the metadata like func name, docstring of the original func that being wrapped

