import matplotlib.pyplot as plt

# Given data
data = [{'date': '2023-01-01', 'region': 'North', 'sales': 1500, 'product': 'Widget'},
        {'date': '2023-01-02', 'region': 'South', 'sales': 2000, 'product': 'Gadget'},
        {'date': '2023-01-03', 'region': 'North', 'sales': 1700, 'product': 'Widget'},
        {'date': '2023-01-04', 'region': 'East', 'sales': 1300, 'product': 'Gizmo'}]

# Group data by product
products = {}
for item in data:
    products[item['product']] = (item['sales'], item['region'])

# Create lists of sales and regions for plotting
sales_list = [product[0] for product in products.values()]
regions_list = [product[1] for product in products.values()]

# Extract unique regions
unique_regions = set()
for region in regions_list:
    unique_regions.add(region)

# Plot pie chart
plt.pie(sales_list, labels=unique_regions, autopct='%1.1f%%')
plt.title('Sales by Region and Product')
plt.show()