import json

t = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
t1 = json.dumps([1,2,3,{'4': 5, '6': 7}], separators=(',',':'))
t2 = json.dumps([1,2,3,{'4': 5, '6': 7}])

#print t1

d = json.JSONDecoder(t1)

print d

