import yaml

with open('practice_file.yaml', 'r+') as file:
    data = yaml.safe_load(file)
    print(data)
