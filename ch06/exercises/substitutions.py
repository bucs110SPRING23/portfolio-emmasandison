import json

file1 = open("subs.json", "r")
file2 = open("news.txt", "r")

data = {
    "trump": "master of evil",
    "arrested": "taken to the dungeon", 
    "protest": "cat",
    "pence": "wicked witch of the west", 
    "law": "demon", 
    "new york": "wonder world", 
    "manhattan": "mount olympus"
}

json_string = json.dumps(data)
print(json_string, type(json_string))
json_data = json.loads(json_string)

for k, v in json_data.items(): 
    print(k, v)

file3 = open("betternews.txt", "w")
file3.write(json_string)

file1.close()
file2.close()

print(file3.read())

file3.close()

print("\n")


