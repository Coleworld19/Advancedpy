#Excercise1
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

def a_places(place):
    print(place.strip())
    if place.lower() == " ":
        return False
    else:
         return True
    
new_places_list = list(filter(a_places, places))
print(places)



#Exercise2
author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
#Here i know i need a function to access the last names

print(author.sort())
print(author)

#Exercise3
# map(func,iterable(list,dict,tuple,set))
#map (lambda x:(9/5)*x + 32, places)
