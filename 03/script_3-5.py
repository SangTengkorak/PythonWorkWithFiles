import csv


def write_to_csv_list():
    with open('products.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Category", "Name", "Quantity", "Price"])
        writer.writerow([41, "Furnishings", "Office Chair", 10, 85])
        writer.writerow([20, "Office Supplies", "Pens", 30, 10])
        writer.writerow([13, "House Keeping", "Bed Sheet (Double)", 15, 20])


def write_to_csv_dictionary():
    with open('maintenance-products.csv', 'w') as file:
        headers = ['id', 'name', 'quantity', 'price']
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        item = {'id': 65, 'name': 'ladder', 'quantity': 33, 'price': 50}
        writer.writerow(item)


def append_to_csv_dictionary():
    with open('products.csv', 'a') as file:
        headers = ['id', 'category', 'name', 'quantity', 'price']
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        item = {'id': 65, 'category': 'maintenance',
                'name': 'ladder', 'quantity': 33, 'price': 50}
        writer.writerow(item)


if __name__ == "__main__":
    # write_to_csv_list()
    # write_to_csv_dictionary()
    append_to_csv_dictionary()
