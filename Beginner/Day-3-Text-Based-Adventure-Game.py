from Beginner.Modules import py_art

print(py_art.treasure)

print('''             
*********************************************************************************************************
You're a fearless explorer on a quest for the legendary Pearl of Revia, a treasure lost to time. Destiny 
leads you to Skagos, a rugged island teeming with fierce creatures and flesh-eating inhabitants. Legends 
claim the pearl resides here, holding the power to change fate. As you tread through untamed wilderness, 
overcoming challenges and unraveling mysteries, the allure of the pearl beckons, promising a chance to 
rewrite history. Will you conquer this perilous journey, seizing the pearl and shaping your legacy amidst 
the echoes of Skagos?
**********************************************************************************************************\n
''')

print("Are you ready to start your journey, explorer?")
start = input("[yes / no]\n")

if start.lower() == 'yes':
    print(
        "\nI've heard much about your adventures and am delighted to guide you on this quest. I believe you are here \nto find the renowned Pearl of Revia and bask in its glory. Your path takes you south, my friend, to the \nTemple of Doom – the last known abode of the Pearl. Seek the clues within, for they shall lead you closer \nto your destiny.\n")

    head_south = input("Do you wish to head south? [yes / no]\n")

    if head_south.lower() == 'no':
        print(
            "You encounter the cannibal inhabitants of the island. Unfortunately, you do not survive their encounter.")
    elif head_south.lower() == 'yes':
        print("\nAfter an hour of relentless trekking, you finally arrive at the Temple of Doom.")
        inspect = input("Would you like to examine the temple's outer perimeter before venturing in? [yes / no]\n")

        if inspect.lower() == 'no':
            print(
                "As you approach the temple's entrance, you trigger a trap. An arrow pierces your chest, ending your journey.")
        elif inspect.lower() == 'yes':
            print(
                "\nAs you cautiously explore the outer reaches of the temple, you detect and disarm a series of intricate traps. \nWith the path cleared, you enter the ancient structure.")
            print("A deafening rumble emanates from the heart of the temple.")
            head_towards_sound = input("Do you dare to venture towards the sound? [yes / no]\n")

            if head_towards_sound.lower() == 'yes':
                print(
                    "\nAs you advance towards the source of the commotion, you realize it's a massive creature charging your way.")
                fight = input("Do you stand your ground and face the wild creature? [yes / no]\n")

                if fight.lower() == 'yes':
                    print(
                        "\nThe thunderous noise was the roar of a legendary Direwolf. Alas, your bravery is in vain, for the \nformidable beast swiftly claims victory.")
                elif fight.lower() == 'no':
                    print(
                        "\nOpting for caution, you retreat from the approaching creature and head in the opposite direction. \nYou notice an eerie glow illuminating a chamber down the darkened hallway.")
                    print(
                        "\nUpon entering the chamber, you spot and successfully disarm a series of concealed traps. Your determination \nand skill have paid off, for you now stand in the presence of the coveted Pearl of Revia. \nCongratulations, valiant adventurer!")
else:
    print("Your indecision leads you astray. The island's perils claim another adventurer.")
