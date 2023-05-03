
# Network programming 

# Build a program that asks trivia questions 

# Server: any computer listening to incoming network connections 

# Request: a incoming connection that asks for some resource from the server 

# - Images, Video, Music 
# - Text 
# - JSON
# - HTML 

# Types of Requests 
# - GET - read operation 
# visiting, downloading a file, etc
# - PUT - write operation (requires security)
# login, deleting 

# Headers
# sent with request and the response 

# - status codes 
#   - 200: ok, everything went fine 
#   - 400: resource cannot be delivered 
#   - 500: bad code on the server 
# - IP address 
# - system information (geolocation)

## urllib

# Requests 

# API - Application Programmer's Interface 
# API's can return data 
# 

# URL 

# ?, &


import requests 
import random 

def main(): 
    response = requests.get("https://opentdb.com/api.php?amount=10")
    data = response.json()
    results = data['results']
    print(response.status_code)

    for r in results: 
        print(r['question'])
        possibles = [r["correct_answer"], r["incorrect_answers"]]
        random.shuffle(possibles)
        print("Make your selection:")
        for i, p in enumerate(possibles): 
            print(f"{i} {p}")

        selection = int(input(": "))
        if possibles[selection] == r["correct_answer"]: 
            print("You are correct")
        else: 
            print(f"You need to study more. The correct answer is: {r['correct_answer']}")

main()
