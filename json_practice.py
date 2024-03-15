import json

with open("practice_file.json", "r") as f:
    data = json.load(f)
    # data['electronic_store']['departments']['smartphones']['brands'].append('Nokia') # Append a new phone to data
    # del data['electronic_store']['departments']['laptops']['brands'][4]  # Delete the phone at the 4th index of the
    # list

    # print(phones)
    # with open('phones_for_sale.json', 'w') as f1: # Add the phones for sale to a new JSON file
    #     json.dump(phones, f1, indent=1)

# Opening the file in write mode and adding changes
with open('practice_file.json', 'w') as f:
    json.dump(data, f, indent=2)


