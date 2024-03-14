import json

with open("practice_file.json", "r") as f:
    data = json.load(f)
    phones = data['electronic_store']['departments']['smartphones']


    with open('phones_for_sale.json', 'w') as f1:
        json.dump(phones, f1, indent=1)

