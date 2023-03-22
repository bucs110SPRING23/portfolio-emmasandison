import json

def main(): 
    text_fptr = open("news.txt", "r").read().lower() # read entire article in
    sub_fptr = open("subs.json", "r")
    subs = json.load(sub_fptr)
    print(subs, type(subs))

    for k, v in subs.items(): 
        text_fptr = text_fptr.replace(k, v)
    
    fptr = open("betternews.txt", "w")
    fptr.write(text_fptr)
    fptr.close()

main()


