acronyms = {"lol": "laugh out loud", "brb": "be right back", "idk": "I don't know", "gt": "get lost"}

print(f"gt:  stands for  {acronyms["gt"]}")

del  acronyms["gt"]

print(acronyms)

gt= acronyms.get("gt")  #this wont crash if a key is not found and will return NONE
print(gt)  #none it also works in an if statement

for item, value in acronyms.items():
    print(f"acronyms are {item} stands for {value}")

if gt:
    print("value of gt was found")
else:
    print("gt was not found")
    
    
menuOptions= {
    "breakfast": ["pancakes", "omelette", "fruit salad"],
    "lunch": ["burger", "salad", "soup"],
    "dinner": ["steak", "pasta", "stir fry"]
}

print(f"Today's breakfast options are: {menuOptions['breakfast']}") 

for key, value in menuOptions.items():
    print(f"{key.capitalize()}: {', '.join(value)}") # prints the list as a comma-separated string
    print(f"{key.capitalize()}: {value}") # prints the list as is
    print(f"{key.capitalize()}: {value [0]}") # prints first item in the list