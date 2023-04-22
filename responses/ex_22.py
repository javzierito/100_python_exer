from pprint import pprint
d = {
    "a": 1,
    "b": 2,
    "c": 3,
}
for k,v in dict(d).items():
    d[k] = list(range(1+(v-1)*10, 11+(v-1)*10))

pprint(d)