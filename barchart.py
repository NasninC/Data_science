import matplotlib.pyplot as plt



products = ['Product A', 'Product B', 'Product C', 'Product D']
inventory = [45, 88, 21, 63]

plt.figure(figsize=(8, 5))

plt.bar(
    products,
    inventory,
    color='teal',
    edgecolor='black',
    width=0.6
)

plt.title('Current Stock Inventory Level', fontsize=14)
plt.xlabel('Product Catalog', fontsize=12)
plt.ylabel('Units Available', fontsize=12)

plt.show()
