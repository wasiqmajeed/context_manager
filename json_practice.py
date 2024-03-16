import json

with open("practice_file.json", "r") as f:
    data = json.load(f)
    # Append a new phone to data
    data['electronic_store']['departments']['smartphones']['brands'].append('Nokia')

    # Delete the laptop at the 4th index of the list
    del data['electronic_store']['departments']['laptops']['brands'][4]

    phones = data['electronic_store']['departments']['smartphones']['brands']
    with open('phones_for_sale.json', 'w') as f1:  # Add the phones for sale to a new JSON file
        json.dump(phones, f1, indent=1)

# Opening the file in write mode and adding changes
with open('practice_file.json', 'w') as f:
    json.dump(data, f, indent=2)


