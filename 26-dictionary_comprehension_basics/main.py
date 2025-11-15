from collections import Counter, defaultdict

squares = {x: x * 2 for x in range(4)}
print(squares)
print("\n" + "=" * 45)

d = {"a": 1}
print(d.get("b", "Not found"))
print("\n" + "=" * 45)

d1, d2 = {"a": 1}, {"b": 2}
merged = {**d1, **d2}
print(merged)
print("\n" + "=" * 45)

inverted = {v: k for k, v in merged.items()}
print(inverted)
print("\n" + "=" * 45)

print(Counter("banana"))
print("\n" + "=" * 45)

print("Defaultdict for missing keys:")
d = defaultdict(int)
d["x"] += 1
print(d["x"], d["y"], d["z"])
print("\n" + "=" * 45)

d = {"a": 3, "b": 1, "c": 2}
sorted = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted)
print("\n" + "=" * 45)
