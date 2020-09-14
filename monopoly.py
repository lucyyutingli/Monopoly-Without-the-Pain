#Imports! ---------------------------------------------------------------------------------------------
import pyfiglet #for ascii art
import random #for dice rolls
from collections import defaultdict #for determining roll order


# Classes and hard-coded information -------------------------------------------------------------------
# Player class that keeps track of a player's name, money, propeties, and held cards
class Player:
    def __init__(self):
        self.dict = {"name": "None", "money": 1500, "owned_props": {}, "cards":[], "location": board_one[0], "last_corner_space": "Go"}

# Property class that keeps track of all of a properties rent and ownership. Names aren't needed here since we won't be doing any trading in this version, and they are 
# encapsulated within variable names.
class Colored_Properties:
    def __init__(self, color, init_cost, rent, house_cost, hotel_cost):
        self.color = color
        self.init_cost = init_cost # Initial cost of the property
        self.rent = rent #Order is as follows [Rent, One House Rent, Two House Rent, Three House Rent, Four House Rent, Hotel Rent]
        self.house_cost = house_cost # Cost of a house
        self.hotel_cost = hotel_cost #Cost of a hotel
        self.dict = {"owner": "None", "current houses": 0}

class Railroads:
    def __init__():
        self.cost = 200
        self.rent = 25
        self.owner = "None"

class Utilities:
    def __init__():
        self.cost = 150
        self.owner = "None"


# Initizliaing all properties. Names will be replaced with characater numbers to bring down run time and memory required.
# Remember the following:
#   - Monopoly rents are double the normal rent
#   - Mortgages are half the intial cost


# Browns
med_ave = Colored_Properties("1", 60, [2, 10, 30, 90, 160, 250], 50, 50)
bal_ave = Colored_Properties("1", 60, [4, 20, 60, 180, 320, 450], 50, 50)

# Light blues
ori_ave = Colored_Properties("2", 100, [6, 30, 90, 270, 400, 550], 50, 50)
ver_ave = Colored_Properties("2", 100, [6, 30, 90, 270, 400, 550], 50, 50)
conn_ave = Colored_Properties("2", 120, [8, 40, 100, 300, 450, 600], 50, 50)

# Pinks
stch_pl = Colored_Properties("3", 140, [10, 50, 150, 250, 625, 750], 100, 100)
st_ave = Colored_Properties("3", 140, [10, 50, 150, 250, 625, 750], 100, 100)
vir_ave = Colored_Properties("3", 160, [12, 60, 180, 500, 700, 900], 100, 100)

# Oranges
stjm_pl = Colored_Properties("4", 180, [14, 70, 200, 550, 750, 950], 100, 100)
ten_ave = Colored_Properties("4", 180, [14, 70, 200, 550, 750, 950], 100, 100)
ny_ave = Colored_Properties("4", 200, [16, 80, 220, 600, 800, 1000], 100, 100)

# Reds
ken_ave = Colored_Properties("5", 220, [18, 90, 250, 700, 875, 1050], 110, 150)
in_ave = Colored_Properties("5", 220, [18, 90, 250, 700, 875, 1050], 110, 150)
ill_ave = Colored_Properties("5", 240, [20, 100, 300, 750, 925, 1100], 120, 150)

# Yellows
at_ave = Colored_Properties("6", 260, [22, 110, 330, 800, 975, 1150], 130, 150)
ven_ave = Colored_Properties("6", 260, [22, 110, 330, 800, 975, 1150], 130, 150)
mar_gar = Colored_Properties("6", 280, [24, 120, 360, 850, 1025, 1200], 150, 150)

# Greens
pac_ave = Colored_Properties("7", 300, [26, 130, 390, 900, 1100, 1275], 200, 200)
nc_ave = Colored_Properties("7", 300, [26, 130, 390, 900, 1100, 1275], 200, 200)
penn_ave = Colored_Properties("7", 320, [150, 450, 1000, 1200, 1400], 200, 200)

# Dark blues
pa_pl = Colored_Properties("8", 350, [35, 175, 500, 1100, 1300, 1500], 200, 200)
bw = Colored_Properties("8", 400, [50, 200, 600, 1400, 1700, 2000], 200, 200)

# Railroads
read_rail = Railroads()
penn_rail = Railroads()
bo_rail = Railroads()
sl_rail = Railroads()

# Utilities
ec = Utilities()
ww = Utilities()


# Breaking up the board into 4 arrays. There is no possible way you cannot hard-code the Monopoly board, because it never changes. 
# First quarter of the board starting with Go. 
board_one = ["Go", ]

# Body -------------------------------------------------------------------------------------------------

banner = pyfiglet.figlet_format("WELCOME TO MONOPOLY (without the pain)")
print(banner)

players_entered = False
player_list = []

# Getting player(s) information (and a bit of cheeky flaming)
while (players_entered == False):
    try:
        playernum = int(input("How many players are playing? (Supports 2-4 players): "))
    except ValueError:
        print("Hey, no letters allowed. This is an integer only zone! Try again.")
    if playernum == 1:
        print("Look, I get it, you wanna play by yourself, but that's not how this game works! This isn't Solitaire! " 
                "Where's the fun in playing by yourself anyways? Sounds awfully lonely. Try again.\n")

    elif playernum == 2:
        name1 = input("Please type in player 1's name: ")
        name2 = input("Plase type in player 2's name: ")
        players_entered = True

        player1 = Player()
        player2 = Player()

        player1.dict["name"] = name1
        player2.dict["name"] = name2


        player_list.extend([player1, player2])

    elif playernum == 3:
        name1 = input("Please type in player 1's name: ")
        name2 = input("Please type in player 2's name: ")
        name3 = input("Please type in player 3's name: ")
        players_entered = True

        player1 = Player()
        player2 = Player()
        player3 = Player()

        player1.dict["name"] = name1
        player2.dict["name"] = name2
        player3.dict["name"] = name3

        player_list.extend([player1, player2, player3])

    elif playernum == 4:
        name1 = input("Please type in player 1's name: ")
        name2 = input("Please type in player 2's name: ")
        name3 = input("Please type in player 3's name: ")
        name4 = input("Please type in player 4's name: ")
        players_entered = True

        player1 = Player()
        player2 = Player()
        player3 = Player()
        player4 = Player()

        player1.dict["name"] = name1
        player2.dict["name"] = name2
        player3.dict["name"] = name3
        player4.dict["name"] = name4

        player_list.extend([player1, player2, player3, player4])

        players_entered = True

    else:
        print("Surprise surprise, you put in an unsupported number of players and found this cheeky message! Congrats. Try again.\n")

print ("\nThank you, the game will now begin. May the (RNG) odds be ever in your favor. \n")

# Determining player order. This whole section seems a little more complicated than it needs to be right now, I will probably come back to it later.
print("Determining turn order...\n")

player_rolls = []

for i in player_list:
    roll = random.randint(2,12)
    player_rolls.append((roll, i))

#Check to see if any of the rolls are the same

print("Original rolls listed:")
for i in player_rolls:
    print("{} got a roll of {}. ".format(i[1].dict["name"], i[0]))

print("\n")
 
player_roll_dict = defaultdict(list) 

final_roll_order = []
for i in player_rolls:    
    player_roll_dict[i[0]].append(i[1])

sorted(player_roll_dict.keys())


unique = 0
while(unique!= playernum):
    for i in player_roll_dict:
        if len(player_roll_dict.get(i)) > 1:
            print("The following players got a duplicate roll of {}: {}. Resolving between the players...".format(i,player_roll_dict.get(i)))

            reroll_list = []
            for j in (player_roll_dict.get(i)):
                reroll_list.append(random.randint(2,12), j)

            reroll_list.sort()
            final_roll_order.extend(reroll_list)
            unique += len(reroll_list)
        else:
            final_roll_order.append(player_roll_dict.get(i)[0])
            unique += 1


# Final player order
print("The player order will be as follows: ")
for i in final_roll_order:
    print(i.dict["name"])


players_in = playernum 

#while (players_in > 1):
    #for i in player_list:




