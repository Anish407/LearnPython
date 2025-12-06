acronyms= [ "Lol", "rofl", "btw", "GTB" ]

print(acronyms[0])  # Output: Lol
acronyms.append("brb") 

newAcronym = "GTW"
if "btw" in acronyms:
   print("Found it") 
   acronyms.remove("btw") 
if newAcronym not in acronyms:
   print(f"DID Not Find {newAcronym}") ; # string interpolation

del acronyms[1] ; # another way to remove an item

for acronym in acronyms:
    print(acronym)