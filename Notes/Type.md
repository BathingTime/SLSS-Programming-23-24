In Python, data can be grouped in categories called Types.

|Name|Example|
|---|---|
|boolean/bool|`True`,`False`|
|integer/int|`1`,`-1`,`0`|
|float|`1.5`,`-1.5`,`1.0`|
|string|`'hello'`|
|list|`[1,2,3]`|

An example of using these types of data:

```Python
fave_food='tempura'# string

my_age=17.5# float
```
# Type Conversion

In Python, there are some *special functions* that allow us to change the type of something.

```Python
intro_str='My age is'# string

my_age=17# int

# Aside:
'My name is'+'Slim Shady.'# —> 'My name isSlim Shady.'

# print(intro_str+my_age) —> This breaks.
```

We can use the following *built in* functions to convert into different types.

```Python
int()
float()
str()
list()
```

We can fix the example above in this way:

```Python
intro_str='My age is'

my_age=17

print(intro_str+str(my_age))# —> 'My age is17'
print(intro_str+' '+str(my_age))# —> 'My age is 17'
print(f'{intro_str} {my_age}')# –> 'My age is 17'
```