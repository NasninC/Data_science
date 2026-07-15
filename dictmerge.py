item1 = input("Enter key-value pairs for first dictionary (e.g., a 1 b 2): ").split()
item2 = input("Enter key-value pairs for second dictionary (e.g., b 3 c 4): ").split()
dict1 = {item1[i]: item1[i + 1] for i in range(0, len(item1), 2)}
dict2 = {item2[i]: item2[i + 1] for i in range(0, len(item2), 2)}
merged = dict1.copy()
merged.update(dict2)
print("Merged dictionary:", merged)
