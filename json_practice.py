import json


with open("practice_file.json", "r") as f:
    data = json.load(f)
    data['electronic_store']['departments']['smartphones']['brands'].append('Nokia')
    print(data)

    # print(phones)
    # with open('phones_for_sale.json', 'w') as f1: # Add the phones for sale to a new JSON file
    #     json.dump(phones, f1, indent=1)

# Add new phone to the list of phones in "practice_file.json"
with open('practice_file.json', 'w') as f:
    json.dump(data, f, indent=2)


