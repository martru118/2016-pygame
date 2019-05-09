# -------------------------------------------------------------------------------
# Name:    adventure_game.py
# Purpose:
# This final project will give you an opportunity to demonstrate your understanding of the concepts acquired in this
# course.  Your job will be to create a graphical adventure game based on course content.
# You will utilize all concepts from variables and control structures, and data structures.
# You will work as an individual. The project is worth 20% of your final mark and is due: June 15th 11:59pm.
#
#
# Author:  Truong.M
#
# Created: 15/06/2016
# -------------------------------------------------------------------------------


def open_file(datafile):
    """
    Opens a file for reading
    :param datafile: file
    :return:
    """
    return open(datafile, 'r')  # returns a file object


def write_save(save_data):  # writes a save point for the player
    """
    An in-game save point for the user. This function will write a save file to track the user's progress in the game.
    Game is saved by default after each stage completion
    :param save_data: list
    :return: file
    """
    save_file = open("game_savefile.txt",'w')   # opens the save file for writing

    print "Saving game..."   # tells user that their game is saving

    save_str = " ".join(save_data)  # put list as string
    save_file.write(save_str)   # write string onto save file

    save_file.close()


def levers_room():  # Puzzle in the levers room of the castle stage
    """
    This is the color-matching puzzle in the potion room
    :return: bool
    """
    from random import randint

    puzzle1 = open_file("levers_room.txt").read()
    print puzzle1

    for tries in range(3):   # The player will have three tries to align the levers in the correct positions
        pull_lever1 = input("What position to put Lever 1 to?: ")
        lever1 = randint(1, 2)
        pull_lever2 = input("What position to put Lever 2 to?: ")
        lever2 = randint(1, 2)
        pull_lever3 = input("What position to put Lever 3 to?: ")
        lever3 = randint(1, 2)
        pull_lever4 = input("What position to put Lever 4 to?: ")
        lever4 = randint(1, 2)
        pull_lever5 = input("What position to put Lever 5 to?: ")
        lever5 = randint(1, 2)
        if (pull_lever1 != lever1) or (pull_lever2 != lever2) or (pull_lever3 != lever3) or (pull_lever4 != lever4) or (pull_lever5 != lever5):
            if tries < 2:
                print "Wrong configuration! Try again!\n"
            elif tries == 2:
                print False, ", the correct configuration was:", lever1, lever2, lever3, lever4, lever5
        else:
            return True


def castle_past():   # The past
    """
    You have been transported back in time to mid-Medieval times.
    You are in a castle for this stage (sorry, no dragons)
    :return:
    """
    room_list = []
    room = ["You are in a Holding Cell.\nThe door is unlocked as you are placed on house arrest.", None, None, None, 1]
    room_list.append(room)
    room = ["You are now in the Eastern Back Hall of the castle\nYour Holding Cell is to the east.", 2, 0, None, 10]
    room_list.append(room)
    room = ["You are in the Eastern Central Hall of the castle.", 3, 17, 1, 12]
    room_list.append(room)
    room = ["You are now in the Eastern Corridor of the castle.", None, 18, 2, 4]
    room_list.append(room)
    room = ["You are now in the Eastern Main Hall of the castle.\nThere is a room to the south.", None, 3, 13, 5]
    room_list.append(room)
    room = ["You are now in the Entrance Hall of the castle.", None, 4, 24, 6]
    room_list.append(room)
    room = ["You are now in the Western Main Hall of the castle.\nThere is a room to the south.", None, 5, 14, 7]
    room_list.append(room)
    room = ["You are now in the North Western Corridor.\nThere is a gift shop to the west.", None, 6, 8, 20]
    room_list.append(room)
    room = ["You are now in the Western Central Hall of the castle.", 7, 15, 9, 21]
    room_list.append(room)
    room = ["You are now in the Western Back Hall of the castle.", 8, 16, None, None]
    room_list.append(room)
    room = ["You are now inside the armory.\nYou wear some clothes that fit in to this era.", None, 1, None, None]
    room_list.append(room)
    room = ["You are now in the Potion Room.", 12, 2, None, None]
    room_list.append(room)
    room = ["You are now in the Feast Room.\nThis room doubles as a kitchen.\nThere is a room to the south.", None, 2, 11, 24]
    room_list.append(room)
    room = ["You are now in the Meeting Room, where all of the castle's employees gather.", 4, 3, None, 5]
    room_list.append(room)
    room = ["You are now in the Monarchs' Room, the Living Room of the Royal Family.", 6, 5, 24, 7]
    room_list.append(room)
    room = ["You are now in the Construction Room.\nThis room is under construction.", None, None, None, 8]
    room_list.append(room)
    room = ["You are now in the Lever Room.\nThere are five levers for you to pull.", None, None, None, 9]
    room_list.append(room)
    room = ["You are now in the castle's chapel.\nThere is no mass today.", None, None, None, 2]
    room_list.append(room)
    room = ["You are now in the Smithery, where they make things.", 19, None, None, 3]
    room_list.append(room)
    room = ["You are in the Garderobes.\nSomeone left a lock pick.", None, None, 18, 3]
    room_list.append(room)
    room = ["You are now in the Souvenir Shop.\nThings seem overpriced.", None, 7, 21, None]
    room_list.append(room)
    room = ["You are now in the Multi-Purpose Room.\nIt is set up for an event.", 20, 8, 22, None]
    room_list.append(room)
    room = ["You are now in the Refinery, where they upgrade things.", 21, 8, None, None]
    room_list.append(room)
    room = ["You are now in the Treasure Room.\nThere is a treasure chest.", None, 9, None, None]
    room_list.append(room)
    room = ["You are now in the Throne Room.\nThis is where the King and Queen are.", 5, None, None, None]
    room_list.append(room)
    room = ["\nWith thy time piece retrieved, thee enter thy time machine.", None, None, None, None]
    room_list.append(room)
    current_room = 0
    print room_list[current_room][0]
    save_list = []
    save_list.append(room_list[current_room][0])
    potion_effect = False
    potion_steps = 0
    treasure_key = False
    levers_key = False
    time_piece1 = False
    cloak = False
    lock_pick = False

    done = False  # This stage is not done yet
    while done == False:
        direction = raw_input("Which direction? ")
        save_list.append(direction)
        if direction.lower() == "north" or direction.lower() == "n":
            next_room = room_list[current_room][1]
            if next_room == None:
                print "You can't go that way!\n"
                save_list.append("You can't go that way!\n")
                print room_list[current_room][0]
                save_list.append(room_list[current_room][0])
            else:
                current_room = next_room
                print "\n", room_list[next_room][0]
                save_list.append("\n"+room_list[next_room][0])
                if room_list[next_room][0] == "You are in the Garderobes.\nSomeone left a lock pick.":
                    lockpick = raw_input("Take the lock pick? (Yes/No): ")
                    if lockpick.lower() == "yes" or lockpick.lower() == "y":
                        print "You take the lock pick"
                        save_list.append("You take the lock pick")
                        lock_pick = True
                        room_list[19][0] = "You are now in the Garderobes (a medieval-era washroom)."

                if potion_effect == True:
                    potion_steps -= 1
                    if potion_steps == 0:
                        print "Your potion effect wore off!"
                        potion_effect = False
                        save_list.append("Your potion effect wore off!")
                if (potion_effect and cloak) == False:
                    if time_piece1 == True:
                        if room_list[next_room][0] == room_list[1:10][0]:
                            print "You have been caught stealing and you have been sent back to your holding cell."
                            save_list.append(
                                "You have been caught stealing and you have been sent back to your holding cell.")
                            lock_pick = False
                            treasure_key = False
                            time_piece1 = False
                            levers_key = False
                            current_room = 0
                            print room_list[current_room][0]
                            save_list.append(room_list[current_room][0])

        elif direction.lower() == "east" or direction.lower() == "e":
            next_room = room_list[current_room][2]
            if next_room == None:
                print "You can't go that way!\n"
                save_list.append("You can't go that way!\n")
                print room_list[current_room][0]
                save_list.append(room_list[current_room][0])
            else:
                current_room = next_room
                print "\n", room_list[next_room][0]
                save_list.append("\n" + room_list[next_room][0])
                if levers_key == True:
                    if room_list[next_room][0] == "You are now in the Lever Room.\nThere are five levers for you to pull.":
                        if levers_room() == False:
                            print "You can use the lock pick in the Garderobes to open the Treasure Room."
                            save_list.append("You can use the lock pick in the Garderobes to open the Treasure Room.")
                        else:
                            print "A door opens behind you."
                            room_list[9][4] = 23
                            save_list.append("A door opens behind you.")

                if time_piece1 == True:
                    room_list[0][2] = 25
                    if room_list[next_room][0] == "\nWith thy time piece retrieved, thee enter thy time machine.":
                        potion_effect = False
                        done = True
                        write_save(save_list)

                if room_list[next_room][0] == room_list[17][0]:
                    if potion_effect == True:
                        potion_steps *= 2
                        print "Your potion effect has doubled! Your potion now lasts", potion_steps, "steps."
                        save_list.append("Your potion effect has doubled!")
                if potion_effect == True:
                    potion_steps -= 1
                    if potion_steps == 0:
                        print "Your potion effect wore off!"
                        potion_effect = False
                        save_list.append("Your potion effect wore off!")
                if (potion_effect and cloak) == False:
                    if time_piece1 == True:
                        if room_list[next_room][0] == room_list[1:10][0]:
                            print "You have been caught stealing and you have been sent back to your holding cell."
                            save_list.append(
                                "You have been caught stealing and you have been sent back to your holding cell.")
                            lock_pick = False
                            treasure_key = False
                            time_piece1 = False
                            levers_key = False
                            current_room = 0
                            print room_list[current_room][0]
                            save_list.append(room_list[current_room][0])

        elif direction.lower() == "south" or direction.lower() == "s":
            next_room = room_list[current_room][3]
            if next_room == None:
                print "You can't go that way!\n"
                save_list.append("You can't go that way!\n")
                print room_list[current_room][0]
                save_list.append(room_list[current_room][0])
            else:
                current_room = next_room
                print "\n", room_list[next_room][0]
                save_list.append("\n" + room_list[next_room][0])
                if room_list[next_room][0] == "You are now in the Meeting Room, where all of the castle's employees gather.":
                    attend = raw_input("There is a meeting going on right now.\nAttend the meeting (Yes/No)?: ")
                    if attend.lower() == "yes" or attend.lower() == "y":
                        print "You attend the meeting.\nThey are talking about construction and building more rooms."
                        print "They are now talking about the newly built Levers Room and the improved security features of that room."
                        print "After the meeting, everyone leaves."
                        room_list[14][0] = "You are now in the Meeting Room, where all of the castle's employees gather.\nThere's nobody here."
                        print "You take a key. It leads to the Lever Room."
                        levers_key = True
                        save_list.append("You attend the meeting.")
                if room_list[next_room][0] == "You are now in the Refinery, where they upgrade things.":
                    if potion_effect == True:
                        upgrade_refinery = raw_input("Do you want to upgrade your potion? (Yes/No): ")
                        if upgrade_refinery.lower() == ("yes" or "y") and potion_steps >= 1:
                            potion_steps *= 2
                            print "Your potion effect has doubled! Your potion now lasts", potion_steps, "steps."
                            save_list.append("You upgraded your potion!")
                    else:
                        print "You need something to upgrade."
                        save_list.append("You need something to upgrade.")
                if potion_effect == True:
                    potion_steps -= 1
                    if potion_steps == 0:
                        print "Your potion effect wore off!"
                        potion_effect = False
                        save_list.append("Your potion effect wore off!")
                if room_list[next_room][0] == "You are now in the Potion Room.":
                    if potion_effect == False:
                        print "There is a potion on the table."
                        save_list.append("There is a potion on the table.")
                        potion_drink = raw_input("Drink the potion? (Yes/No): ")
                        if potion_drink.lower() == "yes" or potion_drink.lower() == "y":
                            print "You decide to drink the potion.\nYou turn invisible for a limited amount of steps."
                            save_list.append("You decide to drink the potion.\nYou turn invisible for a limited amount of steps.")
                            potion_effect = True
                            potion_steps = 15
                if (potion_effect and cloak) == False:
                    if time_piece1 == True:
                        if room_list[next_room][0] == room_list[1:10][0]:
                            print "You have been caught stealing and you have been sent back to your holding cell."
                            save_list.append(
                                "You have been caught stealing and you have been sent back to your holding cell.")
                            lock_pick = False
                            treasure_key = False
                            time_piece1 = False
                            levers_key = False
                            current_room = 0
                            print room_list[current_room][0]
                            save_list.append(room_list[current_room][0])

        elif direction.lower() == "west" or direction.lower() == "w":
            next_room = room_list[current_room][4]
            if next_room == None:
                print "You can't go that way!\n"
                save_list.append("You can't go that way!\n")
                print room_list[current_room][0]
                save_list.append(room_list[current_room][0])
            else:
                current_room = next_room
                print "\n", room_list[next_room][0]
                save_list.append("\n" + room_list[next_room][0])
                if lock_pick == True:
                    room_list[9][4] = 23
                    if room_list[next_room][0] == "You are now in the Treasure Room.\nThere is a treasure chest.":
                        print "You need a key or a lock pick to open the treasure chest."
                        save_list.append("You need a key or a lock pick to open the treasure chest.")
                        if treasure_key == True or lock_pick == True:
                            treasure = raw_input("Open the treasure chest? (Yes/No): ")
                            if treasure.lower() == "yes" or treasure.lower() == "y":
                                print "You open the treasure chest. You take your time piece."
                                save_list.append("You open the treasure chest. You take your time piece.")
                                room_list[23][0] = "You are now in the Treasure Room./nThe treasure chest is empty."
                                time_piece1 = True
                if room_list[next_room][0] == "You are now in the Souvenir Shop.\nThings seem overpriced.":
                    print "You take a key."
                    save_list.append("You take a key.")
                    treasure_key = True
                    room_list[20][0] = "You are now in the Souvenir Shop."
                if room_list[next_room][0] == "You are now inside the armory.\nYou wear some clothes that fit in to this era.":
                    cloak = True
                    room_list[10][0] = "You are now inside the armoury.\nThere's a knight's armour being repaired."

                if potion_effect == True:
                    potion_steps -= 1
                    if potion_steps == 0:
                        print "Your potion effect wore off!"
                        potion_effect = False
                        save_list.append("Your potion effect wore off!")
                if (potion_effect and cloak) == False:
                    if time_piece1 == True:
                        if room_list[next_room][0] == room_list[1:10][0]:
                            print "You have been caught stealing and you have been sent back to your holding cell."
                            save_list.append("You have been caught stealing and you have been sent back to your holding cell.")
                            lock_pick = False
                            treasure_key = False
                            time_piece1 = False
                            levers_key = False
                            current_room = 0
                            print room_list[current_room][0]
                            save_list.append(room_list[current_room][0])
        else:
            print "Please enter either 'north', 'east', 'south', or 'west'."


def control_room():
    """
    This is the puzzle inside of the control room in the starship
    :return: bool
    """

    puzzle2 = open_file("control_room.txt").read()
    print puzzle2

    colours_list = ["White", "Red", "Blue", "Green"]    # the possible variety of button colours

    correlation = False     # there is no correct correlation of the button colours
    while correlation == False:     # user will have to keep guessing the colors until the colour correlation is correct
        button1 = input("How many times do you want to push button 1?: ")
        colour_red = colours_list[1]
        button2 = input("How many times do you want to push button 2?: ")
        colour_blue = colours_list[2]
        button3 = input("How many times do you want to push button 3?: ")
        colour_green = colours_list[3]
        button4 = input("How many times do you want to push button 4?: ")
        colour_white = colours_list[0]
        button5 = input("How many times do you want to push button 5?: ")
        button6 = input("How many times do you want to push button 6?: ")
        button7 = input("How many times do you want to push button 7?: ")
        button8 = input("How many times do you want to push button 8?: ")

        try:    # if the user enters a number between 0 and 3
            if colours_list[button1] != colours_list[button8] != colour_red:
                print "Wrong correlation! Please try again!"
            elif colours_list[button2] != colours_list[button7] != colour_blue:
                print "Wrong correlation! Please try again!"
            elif colours_list[button3] != colours_list[button5] != colour_green:
                print "Wrong correlation! Please try again!"
            elif colours_list[button4] != colours_list[button6] != colour_white:
                print "Wrong correlation! Please try again!"
            else:
                correlation = True  # when the button's colours do match
                return correlation
        except IndexError:   # in case the user enters a number greater than 3 and less than 0
            print "Please enter a number between 0 and 3."


def starship_future():  # The future
    """
    You have travelled into the future to retrieve your next time piece. It is inside someone's starship.
    :return:
    """
    room_list = []  # List of rooms in this stage
    room = ["You have have arrived in the Cargo Cell of someone's starship.\nYou realize are an intruder.\nThere's a room to the north",1, 3, None, 2]
    room_list.append(room)
    room = ["You are now in the Broom Closet.\nThere is the janitor's key.", None, None, 0, None]
    room_list.append(room)
    room = ["West Stairs (Cargo Area)\nUse 'n' to go upstairs and 'e' to leave.", 8, 0, None, None]
    room_list.append(room)
    room = ["East Stairs (Cargo Area)\nUse 'n' to go upstairs and 'w' to leave.", 8, None, None, 0]
    room_list.append(room)
    room = ["West Stairs (Lounge Floor)\nUse 'n' to go upstairs and 's' to go downstairs; use 'e' to leave.", 12, 8, 0, None]
    room_list.append(room)
    room = ["East Stairs (Lounge Floor)\nUse 'n' to go upstairs and 's' to go downstairs; use 'w' to leave.", 13, None, 0, 8]
    room_list.append(room)
    room = ["West Stairs (Top Floor)\nUse 's' to go downstairs and 'n' to leave.", 12, None, 8, None]
    room_list.append(room)
    room = ["East Stairs (Top Floor)\nUse 's' to go downstairs and 'n' to leave.", 13, None, 8, None]
    room_list.append(room)
    room = ["You are now in the starship's Lounge Area.\nThere is some pretty cool furniture.", None, 5, 10, 4]
    room_list.append(room)
    room = ["Using your key card, you enter the cockpit\nThe pilot appears to be sleeping.", None, None, 8, None]
    room_list.append(room)
    room = ["You are now in the Mess.\nSome snacks are laid out on a table.\nA Washroom is to the west", 8, None, None, 11]
    room_list.append(room)
    room = ["You are now in the Lounge Floor Washroom.\nYou activate a cleaning robot.", 8, 10, None, None]
    room_list.append(room)
    room = ["You are now in the Top Floor West Hall.\nThere is a room to the west and north.", None, None, 6, None]
    room_list.append(room)
    room = ["You are now in the Top Floor East Hall.\nThere are rooms to the east and north.", None, 19, 7, None]
    room_list.append(room)
    room = ["Using your key card, you enter the Master Bedroom.\nThat is a huge bed!\nThere is a room to the north.", 15, 12, None, None]
    room_list.append(room)
    room = ["You are now in the Captain's Office.\nA computer displays information about a planet.\nThere is a key.", None, None, 14, None]
    room_list.append(room)
    room = ["You are now in the Control Room.\nYou see eight buttons on a control panel.", None, None, 12, None]
    room_list.append(room)
    room = ["You are now in the Storage Room.\nYou take your time piece.", None, None, 13, None]
    room_list.append(room)
    room = ["You are now in the Supplies Room.\nIt is just used for supplying the Mess.", None, None, 19, None]
    room_list.append(room)
    room = ["You are now in the Top Floor Washroom.\nYou activate a cleaning robot.", 18, None, None, 13]
    room_list.append(room)
    room = ["\nWith the second time piece retrieved, you enter your time machine.", None, None, None, None]
    room_list.append(room)
    current_room = 0
    print room_list[current_room][0]
    save_list = []
    save_list.append(room_list[current_room][0])
    key_in_broomcloset = False  # found in Broom Closet
    key_for_controlroom = False     # found in Captain's Office
    cleanbot_loungefloor = False    # found in the lounge floor Washroom
    cleanbot_topfloor = False   # found in the top floor Washroom
    time_piece2 = False     # found in the Storage Room
    done = False
    while done == False:  # While this stage is not done yet
        direction = raw_input("Which direction? ")
        save_list.append(direction)
        if direction.lower() == "north" or direction.lower() == "n":
            next_room = room_list[current_room][1]
            if next_room == None:
                print "You can't go that way!\n"
                save_list.append("You can't go that way!\n")
                print room_list[current_room][0]
                save_list.append(room_list[current_room][0])
            else:
                current_room = next_room
                print "\n", room_list[next_room][0]
                save_list.append("\n" + room_list[next_room][0])
                if room_list[next_room][0] == "You are now in the Broom Closet.\nThere is the janitor's key.":
                    janitors_key = raw_input("Take the janitor's key? (Yes/No): ")
                    if janitors_key.lower() == "yes" or janitors_key.lower() == "y":
                        print "You take the janitor's key."
                        save_list.append("You take the janitor's key.")
                        key_in_broomcloset = True
                        room_list[1][0] = "You are now in the Broom Closet."
                if key_in_broomcloset == True:
                    room_list[8][1] = 9
                if room_list[next_room][0] == "You are now in the Captain's Office.\nA computer displays information about a planet.\nThere is a key.":
                    captains_key = raw_input("Take the captain's key? (Yes/No): ")
                    if captains_key.lower() == "yes" or captains_key.lower() == "y":
                        print "You take the Captain's Key (don't worry, he has spare keys)."
                        save_list.append("You take the Captain's Key (don't worry, he has spare keys).")
                        key_for_controlroom = True
                        room_list[15][0] = "You are now in the Captain's Office.\nA computer displays information about a planet."
                if key_for_controlroom == True:
                    room_list[12][1] = 16
                    if room_list[next_room][0] == "You are now in the Control Room.\nYou see eight buttons on a control panel.":
                        if control_room() == True:
                            print "You have now unlocked the Storage Room!"
                            room_list[13][1] = 17
                if room_list[next_room][0] == "You are now in the Storage Room.\nYou take your time piece.":
                    time_piece2 = True
                    print "Don't forget to activate the cleaning robots in the washrooms!"
                    room_list[17][0] = "You are now in the Storage Room.\nDon't forget to activate the cleaning robots!"
        elif direction.lower() == "east" or direction.lower() == "e":
            next_room = room_list[current_room][2]
            if next_room == None:
                print "You can't go that way!\n"
                save_list.append("You can't go that way!\n")
                print room_list[current_room][0]
                save_list.append(room_list[current_room][0])
            else:
                current_room = next_room
                print "\n", room_list[next_room][0]
                save_list.append("\n" + room_list[next_room][0])
                if room_list[next_room][0] == "You are now in the Top Floor Washroom.\nYou activate a cleaning robot.":
                    cleanbot_topfloor = True
                    room_list[19][0] = "You are now in the Top Floor Washroom.\nA cleaning robot cleans the floor."
        elif direction.lower() == "south" or direction.lower() == "s":
            next_room = room_list[current_room][3]
            if next_room == None:
                print "You can't go that way!\n"
                save_list.append("You can't go that way!\n")
                print room_list[current_room][0]
                save_list.append(room_list[current_room][0])
            else:
                current_room = next_room
                print "\n", room_list[next_room][0]
                if (time_piece2 and cleanbot_loungefloor and cleanbot_topfloor) == True:
                    room_list[0][3] = 20
                    if room_list[next_room][0] == "\nWith the second time piece retrieved, you enter your time machine.":
                        write_save(save_list)
                        done = True
        elif direction.lower() == "west" or direction.lower() == "w":
            next_room = room_list[current_room][4]
            if next_room == None:
                print "You can't go that way!\n"
                save_list.append("You can't go that way!\n")
                print room_list[current_room][0]
                save_list.append(room_list[current_room][0])
            else:
                current_room = next_room
                print "\n", room_list[next_room][0]
                save_list.append("\n" + room_list[next_room][0])
                if room_list[next_room][0] == "You are now in the Lounge Floor Washroom.\nYou activate a cleaning robot.":
                    cleanbot_loungefloor = True
                    room_list[11][0] = "You are now in the Lounge Room Washroom.\nA cleaning robot cleans the floor."
                elif key_in_broomcloset == True:
                    room_list[12][4] = 14
        else:
            print "Please enter either 'north', 'east', 'south', or 'west'."


def safe_storageroom(key_numbers):   # safe puzzle inside storage room
    """
    This is the safe puzzle for the modern house stage.
    :param key_numbers: list
    :return: bool
    """
    from random import randint

    puzzle3 = open_file("safe_storageroom.txt").read()
    print puzzle3

    print "The numbers on the keys are:", key_numbers  # this will be a list containing the numbers on the keys

    for tries in range(10):     # user will be given nine tries
        lock1 = input("You turn the dial right three times.\nWhat number do you stop at?: ")
        password1 = randint(0, 4)
        lock2 = input("You turn the dial left one full turn.\nWhat number do you stop at?: ")
        password2 = randint(0, 4)
        lock3 = input("You turn the dial right.\nWhat number do you stop at?: ")
        password3 = randint(0, 4)
        lock4 = input("You turn the dial left two times.\nWhat number do you stop at?: ")
        password4 = randint(0, 4)
        lock5 = input("You turn the dial right one full turn.\nWhat number do you stop at?: ")
        password5 = randint(0, 4)
        # start cracking the code
        if tries <= 8:   # on tries 1 to 8
            if lock1 != key_numbers[password1]:
                print "Wrong password! Try again! You have", 10-tries, "tries left!\n"
            elif lock2 != key_numbers[password2]:
                print "Wrong password! Try again! You have", 10-tries, "tries left!\n"
            elif lock3 != key_numbers[password3]:
                print "Wrong password! Try again! You have", 10-tries, "tries left!\n"
            elif lock4 != key_numbers[password4]:
                print "Wrong password! Try again! You have", 10-tries, "tries left!\n"
            elif lock5 != key_numbers[password5]:
                print "Wrong password! Try again! You have", 10-tries, "tries left!\n"
            else:   # if the password combination is correct
                print "You've opened the safe and you take your time piece."
                return True
        else:   # on the ninth try
            print "TRYING TO OPEN THIS SAFE ONE MORE TIME WILL TRIGGER THE ALARM TO SOUND!"
            last_chance = raw_input("DO YOU WISH TO STOP OPENING THIS SAFE? (YES/NO): ")
            if last_chance.upper() == "YES" or last_chance.upper() == "Y":
                print "You stop opening the safe!"
                print "...\n...\n...\n"
                print "There is an alternative however!"
                cheat_code  = raw_input("Do you wish to steal the safe? (Yes/No): ")
                if cheat_code.lower() == "yes" or cheat_code.lower() == "y":
                    break   # a cheat for the user when they give up
            else:
                print "Despite the warning, you try to open the safe once more."
                if lock1 != key_numbers[password1]:
                    print "YOU JUST TRIGGERED THE ALARM!\n"
                    return False
                elif lock2 != key_numbers[password2]:
                    print "YOU JUST TRIGGERED THE ALARM!\n"
                    return False
                elif lock3 != key_numbers[password3]:
                    print "YOU JUST TRIGGERED THE ALARM!\n"
                    return False
                elif lock4 != key_numbers[password4]:
                    print "YOU JUST TRIGGERED THE ALARM!\n"
                    return False
                elif lock5 != key_numbers[password5]:
                    print "YOU JUST TRIGGERED THE ALARM!\n"
                    return False
                else:  # if the password combination is correct
                    print "You've opened the safe and you take your time piece."
                    return True

    # after the break command
    print "You decide to steal the safe with the time piece inside."
    return True


def house_present():  # The present
    """
    The setting is modern day but in another place. The time is the same as what is displayed on your computer
    :return:
    """
    room_list = []
    room = ["You have arrived in Front of someone's House. The entrance is to the north.", 1, None, None, None]
    room_list.append(room)
    room = ["You are now in the Entrance of the house.\nIt seems like nobody's home.\nEnter through the north and enter the Garage through the west.", 3, None, 0, 2]
    room_list.append(room)
    room = ["You are now in the Garage.\nYou find a key.", 3, 1, None, None]
    room_list.append(room)
    room = ["You are now in the Living Room.", 6, 9, 1, 4]
    room_list.append(room)
    room = ["You are now in the first floor Washroom. There is a room to the north.", None, 3, None, None]
    room_list.append(room)
    room = ["You use a key to enter the Utilities Room.\nYou find a key.", None, None, 4, None]
    room_list.append(room)
    room = ["You are now in the Dining Room.\nThere is a shopping list on the table.", None, 7, 3, None]
    room_list.append(room)
    room = ["You are now in the Kitchen.\nThere is a box of pizza on the counter.", None, None, None, 6]
    room_list.append(room)
    room = ["You unlock the back door to enter the Backyard.\nLeave through the east or west.", None, 0, 6, 0]
    room_list.append(room)
    room = ["Stairs (First Floor)\nEnter 'n' to go upstairs and 's' to go downstairs. Leave through the west.", 12, None, 19, 3]
    room_list.append(room)
    room = ["Stairs (Second Floor)\nEnter 's' to go downstairs and leave through the west.", None, None, 3, 12]
    room_list.append(room)
    room = ["Stairs (Basement)\nEnter 'n' to go upstairs and leave though the west.", 3, None, None, 17]
    room_list.append(room)
    room = ["You are now in the Second Floor Hallway.", 13, 10, 15, 17]
    room_list.append(room)
    room = ["You are now in the Master Bedroom. There is a room to the west.", None, None, 12, 14]
    room_list.append(room)
    room = ["You use a key to enter the Multi-Purpose Room.\nYou find a key.", None, 13, None, None]
    room_list.append(room)
    room = ["You are now in an Empty Room.", 12, None, None, None]
    room_list.append(room)
    room = ["You use a key to enter the Storage Room.", None, 15, None, None]
    room_list.append(room)
    room = ["You are now in the second floor Washroom. There is a door to the north.", 18, 12, None, None]
    room_list.append(room)
    room = ["You are now in the Closet.\nYou find a key.", None, 12, 17, None]
    room_list.append(room)
    room = ["You are now in the Basement.\nThere is the person's Home Office to the south.", None, 11, None, None]
    room_list.append(room)
    room = ["You use a key to open the person's Home Office.\nThere are computers everywhere.\nYou find a key.", 19, None, None, None]
    room_list.append(room)
    room = ["\nWith the third time piece retrieved, you enter your time machine.", None, None, None, None]
    room_list.append(room)
    current_room = 0
    print room_list[current_room][0]
    save_list = []  # save data
    save_list.append(room_list[current_room][0])    # append room info to save data

    garage_key_for_utilities = False    # key found in the Garage and is used to open the Utilities Room
    utilities_key_for_homeoffice = False    # key found in the Utilities Room used to open the Home Office
    homeoffice_key_for_multipurpose = False     # key found in the Home Office used to open the Multi-Purpose Room
    multipurpose_key_for_closet = False     # key found in Multi-Purpose Room used for opening the Closet
    closet_key_for_storage = False  # key found in the Closet used for opening the Storage Room
    keynumbers_list = []    # used for the safe puzzle, a list containing the numbers on the keys
    time_piece3 = False
    steps = 0   # added challenge of finishing this stage in a limited number of steps.

    done = False  # This stage is not done yet
    while done == False:
        direction = raw_input("Which direction? ")
        save_list.append(direction)
        if direction.lower() == "north" or direction.lower() == "n":
            next_room = room_list[current_room][1]
            if next_room == None:
                print "You can't go that way!\n"
                save_list.append("You can't go that way!\n")
                print room_list[current_room][0]
                save_list.append(room_list[current_room][0])
            else:
                current_room = next_room
                print "\n", room_list[next_room][0]
                save_list.append("\n" + room_list[next_room][0])
                steps += 1  # each direction you go, the step count will increase by 1
                if steps == 30:  # first warning when the step count is at 30
                    print "You hear a car pull up.\nYou must hurry up and leave the house."
                    save_list.append("You hear a car pull up.\nYou must hurry up and leave the house.")
                elif steps == 40:  # final warning when the step count is at 40
                    print "The homeowner comes into the house and you are caught.\nTry this stage again!"
                    save_list.append("The homeowner comes into the house and you are caught.\nTry this stage again!")
                    current_room = 0  # restarts the stage
                    garage_key_for_utilities = False  # all items obtained in this stage will be removed.
                    utilities_key_for_homeoffice = False
                    homeoffice_key_for_multipurpose = False
                    multipurpose_key_for_closet = False
                    closet_key_for_storage = False
                    time_piece3 = False
                    steps = 0
                    print room_list[current_room][0]
                    save_list.append(room_list[current_room][0])

                if garage_key_for_utilities == True:
                    room_list[4][1] = 5
                    if room_list[next_room][0] == "You use a key to enter the Utilities Room.\nYou find a key.":
                        utilities_key = raw_input("Take the key? (Yes/No): ")
                        if utilities_key.lower() == "yes" or utilities_key.lower() == "y":
                            print "You take the key.\nThere is the number 20 on it."
                            save_list.append("You take the key.\nThere is the number 20 on it.")
                            utilities_key_for_homeoffice = True
                            keynumbers_list.append(20)
                            room_list[5][0] = "You use a key to enter the Utilities Room.\nThere is a washing machine here."

                if multipurpose_key_for_closet == True:
                    room_list[17][1] = 18
                    if room_list[next_room][0] == "You are now in the Closet.\nYou find a key.":
                        closet_key = raw_input("Take the key? (Yes/No): ")
                        if closet_key.lower() == "yes" or closet_key.lower() == "y":
                            closet_key_for_storage = True
                            print "You take the key.\nThere is the number 16 on it."
                            save_list.append("You take the key.\nThere is the number 16 on it.")
                            keynumbers_list.append(16)
                            room_list[18][0] = "You are now in the closet.\nThere is some nice clothing.\nLeave through the east."

                if time_piece3 == True:
                    room_list[6][1] = 8
                    if room_list[next_room][0] == "You are now in the Dining Room.\nThere is a shopping list on the table.":
                        print "There is the backyard to the north."
                        save_list.append("There is the backyard to the north.")

        elif direction.lower() == "east" or direction.lower() == "e":
            next_room = room_list[current_room][2]
            if next_room == None:
                print "You can't go that way!\n"
                save_list.append("You can't go that way!\n")
                print room_list[current_room][0]
                save_list.append(room_list[current_room][0])
            else:
                current_room = next_room
                print "\n", room_list[next_room][0]
                save_list.append("\n" + room_list[next_room][0])
                steps += 1  # each direction you go, the step count will increase by 1
                if steps == 30:  # first warning when the step count is at 30
                    print "You hear a car pull up.\nYou must hurry up and leave the house."
                    save_list.append("You hear a car pull up.\nYou must hurry up and leave the house.")
                elif steps == 40:  # final warning when the step count is at 40
                    print "The homeowner comes into the house and you are caught.\nTry this stage again!"
                    save_list.append("The homeowner comes into the house and you are caught.\nTry this stage again!")
                    current_room = 0  # restarts the stage
                    garage_key_for_utilities = False  # all items obtained in this stage will be removed.
                    utilities_key_for_homeoffice = False
                    homeoffice_key_for_multipurpose = False
                    multipurpose_key_for_closet = False
                    closet_key_for_storage = False
                    time_piece3 = False
                    steps = 0
                    print room_list[current_room][0]
                    save_list.append(room_list[current_room][0])

        elif direction.lower() == "south" or direction.lower() == "s":
            next_room = room_list[current_room][3]
            if next_room == None:
                print "You can't go that way!\n"
                save_list.append("You can't go that way!\n")
                print room_list[current_room][0]
                save_list.append(room_list[current_room][0])
            else:
                current_room = next_room
                print "\n", room_list[next_room][0]
                save_list.append("\n" + room_list[next_room][0])
                steps += 1  # each direction you go, the step count will increase by 1
                if steps == 30:  # first warning when the step count is at 30
                    print "You hear a car pull up.\nYou must hurry up and leave the house."
                    save_list.append("You hear a car pull up.\nYou must hurry up and leave the house.")
                elif steps == 40:  # final warning when the step count is at 40
                    print "The homeowner comes into the house and you are caught.\nTry this stage again!"
                    save_list.append("The homeowner comes into the house and you are caught.\nTry this stage again!")
                    current_room = 0  # restarts the stage
                    garage_key_for_utilities = False  # all items obtained in this stage will be removed.
                    utilities_key_for_homeoffice = False
                    homeoffice_key_for_multipurpose = False
                    multipurpose_key_for_closet = False
                    closet_key_for_storage = False
                    time_piece3 = False
                    steps = 0
                    print room_list[current_room][0]
                    save_list.append(room_list[current_room][0])

                if utilities_key_for_homeoffice == True:
                    room_list[19][3] = 20
                    if room_list[next_room][0] == "You use a key to open the person's Home Office.\nThere are computers everywhere.\nYou find a key.":
                        homeoffice_key = raw_input("Take the key? (Yes/No): ")
                        if homeoffice_key.lower() == "yes" or homeoffice_key.lower() == "y":
                            print "You take the key.\nThere is the number 14 on it."
                            save_list.append("You take the key.\nThere is the number 14 on it.")
                            homeoffice_key_for_multipurpose = True
                            keynumbers_list.append(14)
                            room_list[20][0] = "You use a key to open the person's Home Office.\nThere are computers everywhere."

                if closet_key_for_storage == True:
                    if room_list[next_room][0] == "You are now in an Empty Room.":
                        print "There is a room to the west."
                        save_list.append("There is a room to the west.")
                        room_list[15][4] = 16

                if time_piece3 == True:
                    room_list[0][3] = 21
                    if room_list[next_room][0] == "\nWith the third time piece retrieved, you enter your time machine.":
                        steps -= 1   # this room does not increase step count
                        done = True     # stage finished
                        write_save(save_list)

        elif direction.lower() == "west" or direction.lower() == "w":
            next_room = room_list[current_room][4]
            if next_room == None:
                print "You can't go that way!\n"
                save_list.append("You can't go that way!\n")
                print room_list[current_room][0]
                save_list.append(room_list[current_room][0])
            else:
                current_room = next_room
                print "\n", room_list[next_room][0]
                save_list.append("\n" + room_list[next_room][0])
                steps += 1  # each direction you go, the step count will increase by 1
                if steps == 30:  # first warning when the step count is at 30
                    print "You hear a car pull up.\nYou must hurry up and leave the house."
                    save_list.append("You hear a car pull up.\nYou must hurry up and leave the house.")
                elif steps == 40:  # final warning when the step count is at 40
                    print "The homeowner comes into the house and you are caught.\nTry this stage again!"
                    save_list.append("The homeowner comes into the house and you are caught.\nTry this stage again!")
                    current_room = 0  # restarts the stage
                    garage_key_for_utilities = False  # all items obtained in this stage will be removed.
                    utilities_key_for_homeoffice = False
                    homeoffice_key_for_multipurpose = False
                    multipurpose_key_for_closet = False
                    closet_key_for_storage = False
                    time_piece3 = False
                    steps = 0
                    print room_list[current_room][0]
                    save_list.append(room_list[current_room][0])

                if room_list[next_room][0] == "You are now in the Garage.\nYou find a key.":
                    garage_key  = raw_input("Take the key? (Yes/No): ")
                    if garage_key.lower() == "yes" or garage_key.lower() == "y":
                        print "You take the key.\nThere is the number 5 on it."
                        save_list.append("You take the key.\nThere is the number 5 on it.")
                        garage_key_for_utilities = True
                        keynumbers_list.append(5)
                        room_list[2][0] = "You are now in the Garage.\nThe Living Room is to the north."

                if homeoffice_key_for_multipurpose == True:
                    room_list[13][4] = 14
                    if room_list[next_room][0] == "You use a key to enter the Multi-Purpose Room.\nYou find a key.":
                        multipurposeroom_key = raw_input("Take the key? (Yes/No): ")
                        if multipurposeroom_key.lower() == "yes" or multipurposeroom_key.lower() == "y":
                            multipurpose_key_for_closet = True
                            print "You take the key.\nThere is the number 18 on it."
                            save_list.append("You take the key.\nThere is the number 18 on it.")
                            keynumbers_list.append(18)
                            room_list[14][0] = "You use a key to enter the Multi-Purpose Room.\nThis room is connected to the Bedroom."

                if closet_key_for_storage == True:
                    room_list[15][4] = 16
                    if room_list[next_room][0] == "You use a key to enter the Storage Room.":
                        if safe_storageroom(keynumbers_list) == True:
                            time_piece3 = True
                            room_list[16][0] = "You use a key to enter the Storage Room.\nThere are filing cabinets here."
                        else:
                            print "YOU'VE JUST EXPOSED YOURSELF!\nTHE HOMEOWNER KNOWS WHERE YOU ARE AND WHAT HAPPENED!\nPLEASE TRY THIS STAGE AGAIN!"
                            save_list.append("YOU'VE JUST EXPOSED YOURSELF!\nTHE HOMEOWNER KNOWS WHERE YOU ARE AND WHAT HAPPENED!\nPLEASE TRY THIS STAGE AGAIN!")
                            current_room = 0
                            garage_key_for_utilities = False
                            utilities_key_for_homeoffice = False
                            homeoffice_key_for_multipurpose = False
                            multipurpose_key_for_closet = False
                            closet_key_for_storage = False
                            time_piece3 = False
                            steps = 0
                            print room_list[current_room][0]
                            save_list.append(room_list[current_room][0])

                if time_piece3 == True:
                    room_list[6][1] = 8
                    if room_list[next_room][0] == "You are now in the Dining Room.\nThere is a shopping list on the table.":
                        print "There is the backyard to the north."
                        save_list.append("There is a backyard to the north.")

        else:   # when the user does not type 'n', 'e', 's', or 'w'
            print "Please enter either 'north', 'east', 'south', or 'west'."


def rooms_timemachine():     # while you are going back home with today's date
    """
    You are in the space-time continuum on your way to modern day.
    One last part of your time machine is in the machine itself.
    :return:
    """
    import datetime
    print "It is currently:", datetime.datetime.now()

    room_list = []
    room = ["You are in the cockpit of your time machine. There is a door to the north", 1, None, None, None]
    room_list.append(room)
    room = ["You are now in the Lower Main Hall of your time machine.\nThere is an unlocked room to your east.", 2, 4, 0, None]
    room_list.append(room)
    room = ["You are now in the Central Main Hall of your time machine.", 3, None, 1, None]
    room_list.append(room)
    room = ["You are now in the Upper main hall of your time machine.", None, None, 2, None]
    room_list.append(room)
    room = ["You are now in Room 1.\nIt is an empty room.\nYou see a button.", None, None, None, 1]
    room_list.append(room)
    room = ["You are now in Room 2.\nIt is the bedroom.\nYou press a button.", None, 3, None, None]
    room_list.append(room)
    room = ["You are now in Room 3.\nIt is the snack bar.\nYou press a button.", None, None, None, 2]
    room_list.append(room)
    room = ["You are now in Room 4.\nIt is the closet.\nYou press a button.", None, 1, None, None]
    room_list.append(room)
    room = ["You are now in Room 5.\nIt is the electrical room.\nYou press a button.", None, None, None, 3]
    room_list.append(room)
    room = ["You are now in Room 6.\nIt is the study room.\nYou press a button.", None, 2, None, None]
    room_list.append(room)
    room = ["You are now in Room 10.\nIt is the backroom.\nThere is a cardboard box.", None, None, 3, None]
    room_list.append(room)
    current_room = 0
    room1_button = False
    room2_button = False
    room3_button = False
    room4_button = False
    room5_button = False
    room6_button = False
    print room_list[current_room][0]
    done = False  # This stage is not done yet
    while done == False:
        direction = raw_input("Which direction? ")

        if direction.lower() == "north" or direction.lower() == "n":
            next_room = room_list[current_room][1]
            if next_room == None:
                print "You can't go that way!\n"
                print room_list[current_room][0]
            else:
                current_room = next_room
                print "\n", room_list[next_room][0]

                if room6_button == True:
                    room_list[3][1] = 10
                    if room_list[next_room][0] == "You are now in Room 10.\nIt is the backroom.\nThere is a cardboard box.":
                        cardboard_box = raw_input("Open the box? (Yes/No): ")
                        if cardboard_box.lower() == "yes" or cardboard_box.lower() == "y":
                            print "You open the box."
                            done = True

        elif direction.lower() == "east" or direction.lower() == "e":
            next_room = room_list[current_room][2]
            if next_room == None:
                print "You can't go that way!\n"
                print room_list[current_room][0]
            else:
                current_room = next_room
                print "\n", room_list[next_room][0]

                if room_list[next_room][0] == "You are now in Room 1.\nIt is an empty room.\nYou see a button.":
                    press_button = raw_input("Press the button? (Yes/No): ")
                    if press_button.lower() == "yes" or press_button.lower() == "y":
                        room1_button = True
                        print "You have activated the button."

                if room2_button == True:
                    room_list[2][2] = 6
                    if room_list[next_room][0] == "You are now in Room 3.\nIt is the snack bar.\nYou press a button.":
                        room3_button = True

                if room4_button == True:
                    room_list[3][2] = 8
                    if room_list[next_room][0] == "You are now in Room 5.\nIt is the electrical room.\nYou press a button.":
                        room5_button = True

        elif direction.lower() == "south" or direction.lower() == "s":
            next_room = room_list[current_room][3]
            if next_room == None:
                print "You can't go that way!\n"
                print room_list[current_room][0]
            else:
                current_room = next_room
                print "\n", room_list[next_room][0]

        elif direction.lower() == "west" or direction.lower() == "w":
            next_room = room_list[current_room][4]
            if next_room == None:
                print "You can't go that way!\n"
                print room_list[current_room][0]
            else:
                current_room = next_room
                print "\n", room_list[next_room][0]
                if room1_button == True:
                    room_list[3][4] = 5
                    if room_list[next_room][0] == "You are now in Room 2.\nIt is the bedroom.\nYou press a button.":
                        room2_button = True
                if room3_button == True:
                    room_list[1][4] = 7
                    if room_list[next_room][0] == "You are now in Room 4.\nIt is the closet.\nYou press a button.":
                        room4_button = True
                if room5_button == True:
                    room_list[2][4] = 9
                    if room_list[next_room][0] == "You are now in Room 6.\nIt is the study room.\nYou press a button.":
                        room6_button = True
                        room_list[3][0] = "You are now in the Upper main hall of your time machine.\nThere is a room to the north."
        else:
            print "Please enter either 'north', 'east', 'south', or 'west'."


def readlines_file(game_story):
    """
    Reads the story from the file
    :param game_story: file
    :return:
    """
    for intro in range(33):     # will read the beginning of the game's storyline
        print game_story.readline().strip()
    castle_past()   # which is the first stage: a castle in the 14th century

    for story1 in range(18):
        print game_story.readline().strip()
    starship_future()

    for story2 in range(12):
        print game_story.readline().strip()
    house_present()

    for ending1 in range(10):
        print game_story.readline().strip()
    rooms_timemachine()

    for ending2 in range(13):
        print game_story.readline().strip()


def main():
    """
    An adventure game. Game data will be read from a txt file
    :return:
    """
    print "***  Welcome to Stranded in Time!    ***"   # title card
    action = raw_input("Would you like to start a 'new game' or 'load a save file' or 'quit'?: ")     # determines what the user wants to do
    if action.lower() == 'new game':
        new_game = open_file("adventure_game.txt")
        readlines_file(new_game)
    elif action.lower() == 'load a save file':
        print "There is no point of loading a save file if you can't choose to save halfway in the game and to choose where to start off at!"
    elif action.lower() == 'quit':
        quit()

main()
