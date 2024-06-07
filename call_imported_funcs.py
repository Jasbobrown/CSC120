import short1_thing
a = input()
b = short1_thing.foo(a)
print(b)
c, d = input(), input()
e = short1_thing.bar(a, c, d)
print(e)
print(short1_thing.baz(b, e))