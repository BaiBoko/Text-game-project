from random import randint
name = input("What is your name?: ")
biome1 = ("Forest biome")
biome2 = ("Snowing biome")
biome3 = ("Desert biome")
random_biome = (biome1, biome2,  biome3)

print("Given the biomes, select where you would like to drop: " + str(biome1) + ", " + str(biome2) + ", " + str(biome3))
print()
print("Warning: the following biomes have different methods of survival."
      " The choices you make would determine your capabilities of surviving!")
print()
select_biome = input("Please enter a biome: Forest/Snow/Desert: ")

# selecting Forest biome
if select_biome == "Forest":
    print("You have selected the Forest biome!")
    print()
    print("Your starting gear is: Canteen, Knife, Matchbox with 5 matches")
    print("Landing there you start to realise that there are not many food sources and is quite cold!"
          " Although your hydration is excellent you need to find something to eat and find shelter before nightfall!")
    print("What would you prioritize first: Food / Shelter / Scouting the area?")
    first_night = input("Food / Shelter / Scouting: ")
# decision N1
if first_night == "Food":
    print("Good decision. As you look around you see three things: A lake, bunch of trees and a nice lawn. Where would you search first?")
    food_search = input("Lake / Trees / Lawn: ")
    if food_search == "Lake":
        print("Wasting your time a little bit as you haven't crafted anything to catch the fish with. Please select another option!")
        food_search1 = input("Trees / Lawn: ")
        if food_search1 == "Trees":
            print("You find a beehive filled with honey. This looks like a very good source of food. You don't see any bees flying around but that there is a 20% chance that there are. Do you take the chance?")
            risk = input("Yes / No: ")
            if risk == "Yes":
                chance = randint(1, 100)
                if chance >= 20:
                    print("Jackpot! You are set for the night!")
                else:
                    print("You died!")
            elif risk == "No":
                print("You still need to find food!")
        elif food_search1 == "Lawn":
            print("A beautiful lawn with many rabbit holes. You don't have the tools yet but perhaps setting some traps around could work later on.")
            print("For now there are many grasshoppers you can eat but there are not a sustainable source. Will you continue on Scouting or get settled for a shelter?")





