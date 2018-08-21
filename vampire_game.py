from sys import exit

sunlight = False
first_mirror = False
staircase = False
dagger = False
box = False
blessed = False
holy_water_font = False
inventory = ["garlic", "torch", "bible"]




def basement():
    global sunlight


    print("""In the basement, your torchlight
    reveals: Above your head, another mirror. At the far end of the basement,
    there is the lowered altar with the lamb chained to it. Beyond that, an
    ornate but rotting coffin which holds a vampire, you presume. The door to
    the coffin, if it were to open, would open toward the staircase.""")

    while True:

        print("What do you do?")
        choice = input("> ")

        if "mirror" in choice:
            if first_mirror == False:
                print("The mirror creaks as you adjust it, but nothing happens.")
            else:
                sunlight = True
                print("""You adjust the mirror.""")
                print("""The sunlight reflecting from the mirror above hits the
basement mirror, which in turn reflects the light above the sacrificial lamb
and onto the door of the coffin.""")
        elif "inv" in choice or "inventory" in choice:
            for i in inventory:
                print(i)
        elif "drop" in choice:
            drop()
        elif "bless" in choice:
            bless()
        elif "coffin" in choice and "open" in choice:
            print("""Without hesitation, you cross the room and open the coffin.
This awakens the vampire, who upon seeing you promptly consumes your human
flesh.""")
            exit(0)
        elif "coffin" in choice:
            print("""You inspect the coffin. It gives you the creeps.""")
        elif "recite" in choice or "altar" in choice or "lamb" in choice \
        or "say" in choice or "forward" in choice or "ahead" in choice:
            print("You walk up to the altar, in front of the coffin.")

            print("""Do you remember the words you were to recite to summon the
vampire?""")
            choice = input("> ")

            if "n" in choice:
                print("Better figure that out...")
                basement()
            else:
                print("Do you want to recite them?")
                choice = input("> ")

                if "n" in choice:
                    print("Ok.")
                    basement()
                else:
                    win_condition()
        elif "up" in choice or "back" in choice:
            main_chamber()
        else:
            print("Sorry, don't know what that means, try something else.")



def win_condition():
    print("Ok, what are the words of the summoning phrase?")
    choice = input("> ")

    if "luna di sangue recurrit" in choice and sunlight:
        print("""You utter the words of the summoning incantation. You hear a
sharp inhale and a hiss from inside the coffin door. It can smell the blood of the
lamb. The coffin door's hinges grind as the vampire wakes from his sleep. As soon
as the vampire exposes himself the basement air, the sunlight reflecting from
the mirrors bursts into his face. The vampire wails dramatically, then suddenly
falls into cremated remains.

    Congratulations. One more hamlet saved, with your help.""")
        exit(0)
    elif "luna di sangue recurrit" in choice and not sunlight:
        print("""You utter the words of the summoning incantation. You hear a
sharp inhale and a hiss from inside the coffin door. It can smell the blood of the
lamb. The coffin door's hinges grind as the vampire wakes from his sleep. The vampire
steps outside his coffin, and upon seeing you next to the altar, decides to consume your flesh.

You are dead.""")
        exit(0)
    else:
        print("""You totally whiff. You're not sure if you completely forgot a word,
or if you mispronounced something. Regardless, this deeply angers the vampire residing in
the coffin in front of you. The coffin door is broken off of its hinges and sent flying
across the basement. Before you even process what has happened, you're dead. You lost. Sorry.""")
        exit(0)




def relic_box():
    global box

    if box == False:
        print("""You inspect the relic box past the altar. It is made
of sturdy wood and has a keylock. Carved into the lid is a moon with an
ambiguous expression.""")
        print("What do you do?")
        choice = input("> ")

        if "open" in choice and "key" in inventory:
            box = True
            inventory.append("dagger")
            print("""You open the relic box and find a ceremonial
dagger.""")
            main_chamber()
        elif "open" in choice and not "key" in inventory:
            print("""You try to open it, but it's clearly locked.""")
            main_chamber()
        else:
            print("Okay.")
            main_chamber()
    else:
        print("The relic box is empty.")
        main_chamber()





def altar():
    global staircase

    print("""You approach the altar. Upon it you see old blood stains.  And
chains for keeping sacrifices in position. You feel queazy. You can't tell if
you're imagining it or not, but you think you hear whispers in the drafts of
air. Sounds like \'Sanguis autem Agni dei\'.""")

    while True:
        print("What do you do?")
        choice = input("> ")

        if "inv" in choice:
            for i in inventory:
                print(i)
        elif "drop" in choice:
            drop()
        elif "bless" in choice:
            bless()
        elif "kill" in choice or "sac" in choice or "dag" in choice \
            or "lamb" in choice and ("lamb" and "dagger") in inventory:
            print("""You chain the lamb to the altar, and slit its throat.
The second the lamb's blood touches the altar, a rumbling commences and the
altar begins sinking through the floor into a chamber below.""")
            staircase = True
            main_chamber()
        else:
            print("Okay.")
            main_chamber()





def mirror1():
    global first_mirror

    if "ladder" in inventory:
        print("""You set your ladder under the mirror, climb it, and inspect
the mirror. It looks like it can be spun a quarter turn to point at the floor
in front of the altar.""")
        print("Would you like to point the mirror downward?")
        choice = input("> ")

        if "y" in choice:
            first_mirror = True
            print("""The mirror is now reflecting a shaft of sunlight down into
the chapel.""")
            main_chamber()
        else:
            print("Okay.")
            main_chamber()
    else:
        print("""The mirror is too high for you to reach. There is bright
sunlight bouncing off of it onto the ceiling of the chapel.""")
        main_chamber()





def chapel1():
    print("""Here is a smaller chapel to the side. It is filled with a dozen
pews. They face a stained glass window. It depicts a saint, beset upon by
demons with blood on their fangs. Instinctually, you reach for the holy water
font to your right in order to bless yourself, but the font is empty.""")

    while True:
        print("What do you do?")
        choice = input("> ")

        if "inv" in choice:
            for i in inventory:
                print(i)
        elif "drop" in choice:
            drop()
        elif "bless" in choice:
            bless()
        elif "back" in choice or "leave" in choice or "main" in choice:
            print("You leave the side chapel, and return to the main chapel.")
            main_chamber()
        elif "font" in choice or "holy" in choice or "water" in choice or "fill" in choice:
            font()
        else:
            print("Don't know what ya mean. Try something else.")




def font():
    global blessed
    global holy_water_font

    if "holy water bottle" not in inventory:
        print("""The holy water font is empty. Being ordained, you could
bless some water yourself.""")
        chapel1()
    else:
        if not blessed:
            print("""You fill the font with holy water, dip your fingers in it,
and make the sign of the cross.""")
            print("""As you look back to the stained glass, you are shocked to find
the content has changed. The saint now stands serene, unbothered by the demons
over his shoulder. He stands confidently, holding a bottle that says
\'Holy Water\' on it in a corporate stylized font, like Lebron with some
Gatorade.""")
            blessed = True
            holy_water_font = True
            chapel2()
        else:
            print("""The font now contains the holy water you poured into it. You
have made the sign of the cross with it, and you feel His holy protection.""")
            chapel2()

def chapel2():
    print("""You are in the side chapel. The stained glass window shows the
reassuring image of the saint unbothered by demons. The holy water font is full.
You feel comfortable in this room, but there is work to be done elsewhere.""")
    print("You return to the main chapel.")
    main_chamber()




def priest_quarters():
    print("""You're in what look to be living quarters for the resident
priest. However the room looks uninhabited. There is a blanket of dust over
everything. Or almost everything. There is a desk in one corner. There is a
bookshelf in the opposite corner. On the left there is a door to a further
room.""")

    while True:
        print("What do you do?")
        choice = input("> ")

        if "inv" in choice:
            for i in inventory:
                print(i)
        elif "drop" in choice:
            drop()
        elif "bless" in choice:
            bless()
        elif "desk" in choice:
            desk()
        elif "book" in choice or "shelf" in choice:
            bookshelf()
        elif "left" in choice or "door" in choice:
            stables()
        elif "back" in choice or "main" in choice:
            main_chamber()
        else:
            print("Not sure what that means.")

def desk():
    if "bottle" in inventory:
        print("Just a dusty desk...")
    else:
        print("""Standing in front of the desk you notice one item not covered in dust.
It's a pocket-sized bottle, and has a cross engraved into one side. You
recognize it as a bottle commonly used to carry holy water.""")

        print("Take the bottle?")
        choice = input("> ")

        if "y" in choice:
            inventory.append("bottle")
            print("You take the bottle.")
            priest_quarters()
        elif "n" in choice:
            print("You leave the bottle.")
            priest_quarters()
        else:
            print("Yes or no.")
            desk()

def bookshelf():
    if "key" not in inventory:
        print("""You inspect the bookshelf. There is one book conspicuously
not covered in dust.""")
        print("Take the book down?")
        choice = input("> ")

        if "y" in choice:
            print("You take the book down.")
            book()
        elif "n" in choice:
            print("You leave the book.")
            priest_quarters()
        else:
            print("Yes or no.")
            bookshelf()
    else:
        print("""You are at the bookshelf. Reread the book?""")
        choice = input("> ")

        if "y" in choice:
            print("You take the book down.")
            book2()
        elif "n" in choice:
            print("You leave the book.")
            priest_quarters()
        else:
            print("Yes or no.")
            bookshelf()



def book():
    inventory.append("key")
    print("""The first thing you notice is that there is a hole cut out of the
middle of the book, with a key stored inside. You pocket the key.""")
    print("""Before setting the book down, you skim some of the latin verses
contained on the remaining in tact pages. It seems that the pages are a tract
describing the best practices when dealing with vampires. From it you glean
that if you want to survive an encounter with a vampire DO: bless yourself with
holy water. DO: try to hunt them with sunlight. DO NOT: have garlic on your
person. To summon a vampire from its sleep, you must have a bible on your
person, a worthy sacrifice on an altar in front of you, and recite
"luna di sangue recurrit".""")
    print("""You put the book back on the shelf.""")
    priest_quarters()




def book2():
    print("""You refresh yourself on the important contents of the book:
DO: bless yourself with holy water. DO: try to hunt them with sunlight. DO NOT:
have garlic on your person. To summon a vampire from its sleep, you must have a
bible on your person and recite "luna di sangue recurrit".""")
    priest_quarters()




def stables():
    while True:
        if "lamb" not in inventory and not staircase:
            if "ladder" not in inventory:
                print("""You are inside a stable. The floor is dirt, and straw-strewn. A
little lamb is grazing on straw. It's small enough to hold in your arms, but
its mother is no where to be seen. In the far right corner is a water well.
To the right of the door is a ladder set against the wall.""")

                while True:
                    print("What do you do?")
                    choice = input("> ")

                    if "inv" in choice:
                        for i in inventory:
                            print(i)
                    elif "drop" in choice:
                        drop()
                    elif "bless" in choice:
                        bless()
                    elif "back" in choice or "door" in choice or "leave" in choice:
                        priest_quarters()
                    elif "ladder" in choice:
                        ladder()
                    elif "lamb" in choice:
                        lamb()
                    elif "water" in choice or "well" in choice:
                        well()
                    else:
                        print("Try something else.")
            else:
                print("""You are inside the stable. The floor is dirt, and straw-strewn. A
little lamb is grazing on straw. It's small enough to hold in your arms, but
its mother is no where to be seen. In the far right corner is a water well.""")

                while True:
                    print("What do you do?")
                    choice = input("> ")

                    if "inv" in choice:
                        for i in inventory:
                            print(i)
                    elif "drop" in choice:
                        drop()
                    elif "bless" in choice:
                        bless()
                    elif "back" in choice or "door" in choice or "leave" in choice:
                        priest_quarters()
                    elif "lamb" in choice:
                        lamb()
                    elif "water" in choice or "well" in choice:
                        well()
                    else:
                        print("Try something else.")
        else:
            if "ladder" not in inventory:
                print("""You are inside the stable. There is a well in the
far-right corner. There is a ladder to the right of the door.""")

                while True:
                    print("What do you do?")
                    choice = input("> ")

                    if "inv" in choice:
                        for i in inventory:
                            print(i)
                    elif "drop" in choice:
                        drop()
                    elif "ladder" in choice:
                        ladder()
                    elif "bless" in choice:
                        bless()
                    elif "back" in choice or "door" in choice or "leave" in choice:
                        priest_quarters()
                    elif "lamb" in choice:
                        lamb()
                    elif "water" in choice or "well" in choice:
                        well()
                    else:
                        print("Try something else.")
            else:
                print("""You are inside the stable. There is a well in the far-right
corner.""")

                while True:
                    print("What do you do?")
                    choice = input("> ")

                    if "inv" in choice:
                        for i in inventory:
                            print(i)
                    elif "drop" in choice:
                        drop()
                    elif "bless" in choice:
                        bless()
                    elif "back" in choice or "door" in choice or "leave" in choice:
                        priest_quarters()
                    elif "lamb" in choice:
                        lamb()
                    elif "water" in choice or "well" in choice:
                        well()
                    else:
                        print("Try something else.")





def ladder():
    print("The ladder's about 10ft tall. You could carry it.")

    while True:
        print("Pick up the ladder?")
        choice = input("> ")

        if "y" in choice:
            inventory.append("ladder")
            print("You take the ladder.")
            stables()
        elif "n" in choice:
            print("You leave the ladder.")
            stables()
        else:
            print("Yes or no.")



def lamb():
    print("""The lamb looks up at you with doleful eyes.
It's small enough you could carry it with you.""")

    while True:
        print("Pick up the lamb?")
        choice = input("> ")

        if "y" in choice:
            inventory.append("lamb")
            print("You carry the lamb.")
            stables()
        if "n" in choice:
            print("You leave the lamb.")
        else:
            stables()



def well():
    print("""This is a healthy looking well. There is water
brimming to the top.""")

    while True:
        print("What do you do?")
        choice = input("> ")

        if "inv" in choice:
            for i in inventory:
                print(i)
        elif "drop" in choice:
            drop()
        elif "bless" in choice:
            bless()
        elif "drink" in choice:
            print("You drink the water. It's minerally and clean.")
        elif "fill" in choice or "bottle" in choice or "take" in choice:
            fill_bottle()
        else:
            print("Ok.")
            stables()



def fill_bottle():
    if "bottle" not in inventory:
        print("You need something to carry it.")
    else:
        inventory.remove("bottle")
        inventory.append("water bottle")
        print("You have filled your bottle with water.")
        stables()



def main_chamber():

    if staircase == False:
        print("""You are in the main chamber of the church. There are doors to
your left and right. There is an altar. Past the altar is a relic box. Eight
feet above the entry door is a mirror with the sun shining onto it through a
window in the steeple.""")

        while True:

            print("""What do you do?""")
            choice = input("> ")

            if "inv" in choice:
                for i in inventory:
                    print(i)
            elif "left" in choice:
                print("You enter the door to the left.")
                if holy_water_font:
                    chapel2()
                else:
                    chapel1()
            elif "right" in choice:
                print("You enter the door to the right.")
                priest_quarters()
            elif "relic" in choice or "box" in choice:
                relic_box()
            elif "altar" in choice:
                altar()
            elif "mirror" in choice:
                mirror1()
            else:
                print("Try something else.")

    else:
        print("""You are in the main chamber of the church. There are doors
to your left and right. The altar has lowered into the basement. Before the
lowered altar is a yawning staircase to the level below. Past this is a relic
box. Eight feet above the entry door is a mirror with the sun shining onto it
through a window in the steeple.""")

        while True:
            print("What do you do?")
            choice = input("> ")

            if "inv" in choice:
                for i in inventory:
                    print(i)
            elif "left" in choice:
                print("You enter the door to the left.")
                chapel()
            elif "right" in choice:
                print("You enter the door to the right.")
                priest_quarters()
            elif "relic" in choice or "box" in choice:
                relic_box()
            elif "mirror" in choice:
                mirror1()
            elif "staircase" in choice or "down" in choice:
                basement()
            else:
                print("Try something else.")




def drop():
    print("What would you like to drop from your inventory?")
    choice = input("> ")

    if choice in inventory:
        inventory.remove(choice)
    else:
        print("No such thing in your inventory.")




def bless():
    if "water bottle" in inventory:
        inventory.remove("water bottle")
        inventory.append("holy water bottle")
        print("You bless your bottle of water.")
    else:
        print("You need a bottle of water in order to bless it.")



def start():
    print("""You are an itinerant priest, whose occupation consists of investigating
the claims of peasants troubled by occult happenings. A string of deaths have made
the folk of this hamlet wary; and they cast a suspicious eye upon the derelict
church resting in a clearing in the forest just outside their village. Passing through,
your services are requested, and you make for the abandoned church forthwith.""")
    print("""Instructions: interact with this game by naming the objects you'd
like to interact with, and sometimes an accompanying verb. You can navigate with
words like "left", "right", "back" etc. You can access your inventory at any time
by typing "inv" or "inventory". You can manage your inventory by typing "drop".""")
    main_chamber()





start()
