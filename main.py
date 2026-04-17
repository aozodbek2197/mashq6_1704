# 1-mashq
d = {"a": 1, "b": 2}
rev = {v: k for k, v in d.items()}
print(rev)
# 2-mashq
a = [1, 2, 3]
b = [2, 3, 4]
print(set(a) & set(b))
# 3-mashq
names = ["Ali", "Vali"]
d = {name: len(name) for name in names}
print(d)
# 4-mashq
lst = [[1, 2], [3, 4]]
flat = [x for sub in lst for x in sub]
print(flat)
# 5-mashq
d = {"a": 10, "b": 5, "c": 20}
print(max(d.values()))
