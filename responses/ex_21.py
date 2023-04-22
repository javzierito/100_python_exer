d = {"a": 1, "b": 2, "c": 3}
for k, v in dict(d).items():
    if v > 1:
       d.pop(k)
print(d) 
