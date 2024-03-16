import yaml

# The review to be added to the yaml file
new_review = {'comment': 'This shop has amazing products and great deals',
              'name':  'Wasiq Wani',
              'rating': 5
              }

with open('practice_file.yaml', 'r+') as file:
    data = yaml.safe_load(file)
    # data["electronic_store"]['customer_reviews'].append(new_review) # Adding a new review for the shop in yaml file
    # data["electronic_store"]['departments']['laptops']['stock'][1]['price'] = 549.99  # Updating the price of Lenovo
    # laptop to 549.99


with open('practice_file.yaml', 'w') as file:
    yaml.dump(data, file)

