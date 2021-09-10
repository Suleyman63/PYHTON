import json

# with open('data.json', 'r') as f:
#    content = json.load(f)
#    print(content)

    #for friend in content['friends']:
     #   print(friend['name'])


   # for friend in content['friend']:
    #    del friend['age']
     #   print(content)


# with open('data.json', 'r') as f, open('data.json', 'w') as f2:
#     content = json.load(f)
#     for friend in content['friend']:
#         del friend['name']
        
#         json.dump(content, f2)
       


try:
    with open('data.json', 'r') as f:
        content = f.readlines()
        for x in content:
            print(x)
except FileNotFoundError:
        print('dosya bulunamadi')