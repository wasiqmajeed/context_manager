import yaml

# The review to be added to the yaml file
new_review = {'comment': 'This shop has amazing products and great deals',
              'name':  'Wasiq Wani',
              'rating': 5
              }

with open('practice_file.yaml', 'r+') as file:
    data = yaml.safe_load(file)

    # Adding a new review for the shop in yaml
    data["electronic_store"]['customer_reviews'].append(new_review)

    # Updating the price of Lenovo laptop to 549.99
    data["electronic_store"]['departments']['laptops']['stock'][1]['price'] = 549.99

    #  Adding the address of the shop
    data['electronic_store']['address'] = 'Kazimierza Brokla 2, 00-032 Warszawa'


with open('practice_file.yaml', 'w') as file:
    yaml.dump(data, file)

