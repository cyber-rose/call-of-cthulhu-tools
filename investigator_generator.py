from investigator_class import Investigator, get_int_input

# the main file for the program

# Generate the base characteristics for investigators (using user given dice rolls)
def gen_base_stats_menu():
    print("You have chosen to generate the characteristics for your investigator. This will lead you through the steps to create an investigator based on the 7th edition rules.")
    print("Before beginning please choose the method you would like to use to create your investigator.")
    #print("After you make your characteristic rolls, you will have an option to select additional methods or house rules to create your character. This includes: options to scrap all base stat rolls and start over, modify low rolls, or adding an extra 1D10 percentage points to distribute among characteristics.") 
    print("What method would you like to use to generate investigator characteristics?\n    1. Default\n    2. Point Buy Characteristics\n    3. Quick Fire Method")
    gen_method = input("Method: ")
    while (gen_method != 'q') and (gen_method != '1') and (gen_method != '2') and (gen_method != '3'):
        gen_method = input("Invalid choice. Please enter a number 1-3 to select the method or 'q' to quit:")

    if (gen_method == 'q'):
        input("Press enter to return to main menu")
        return

    # Store base characteristic values in a dict before creating a character
    base_characteristics = {
        "str" : 0,
        "con" : 0,
        "siz" : 0,
        "dex" : 0,
        "app" : 0,
        "int" : 0,
        "pow" : 0,
        "edu" : 0,
    }

    if (gen_method == '1'):
        print("Default method selected.")
        # get the rolled dice from the users
        # allow users to pick where they put each value (show the users their vals before they continue)
        default_char_method(base_characteristics)

    elif (gen_method == '2'):
        point_buy_char(base_characteristics)
    else:
        quick_fire_char()

    # Create an investigator with the the base characteristics
    player_char = Investigator(base_characteristics["str"], base_characteristics["con"], base_characteristics["siz"], base_characteristics["dex"], base_characteristics["app"], base_characteristics["int"], base_characteristics["pow"], base_characteristics["edu"])
    
    # Age
    print("How old is your investigator?")
    # age_is_valid = False
    # input_age = input("Age: ")
    # while (age_is_valid):
    #     if not input_age.isdigit():
    #         input_age = input("Invalid age. Please enter age as an integer: ")
    #     elif (int(input_age) <= 0) or (int(input_age) > 110):
    #         input_age = input("Invalid age. Please enter a realistic age for a human (i.e. from 1 to 110): ")
    #     else:
    #         age_is_valid = True
    # age_num = int(input_age)
    age_num = get_int_input(1,110, "Age:")

    if (1 <= age_num < 15) or (age_num >= 90):
        print("You have chosen an age outside of the typical age range (15 to 89) for Call of Cthulhu. There are no specified modifications to characteristics for these ages in the rule book. Before you proceed, please discuss this choice with your Keeper. They will determine how you should proceed / modify characteristics.")
        retry_choice = input("Would you like to input an age within the specified range (15 to 89) instead? (Y/N)")
        while (retry_choice.lower() != "y") and (retry_choice.lower() != "n"):
            retry_choice = input("Y/N: ")
        if retry_choice.lower() == "y":
            input_age = get_int_input(15, 89,"Investigator age: ")
            age_num = input_age

    player_char.set_age(age_num)
    
    # Luck
    luck_score = luck_roll()
    player_char.set_luck(luck_score)
    if (15 <= player_char.age <=20):
        print("Age is within 15-19. Make a second roll for luck.")
        luck_score_2 = luck_roll()
        print(luck_score)
        print(luck_score_2)
        if luck_score_2 > luck_score:
            player_char.set_luck(luck_score_2)

    print(player_char)
    # generate the half and fifth values (?)
    # get occupation?
    # allocate edu points for skills?
    # get credit rating?
    input("Press enter to return to main menu")
    return

# Default method to generate characteristics. Gets user input and returns a dictionary for investigator base stats
# Takes a dictionary and modifies that dictionary on return
def default_char_method(base_characteristics):
    print("Strength Characteristic")
    str_roll = get_int_input(3, 18, "STR - Roll 3D6 to generate STR value: ")
    base_characteristics["str"] = str_roll * 5

    print("Constitution Characteristic")
    con_roll = get_int_input(3, 18, "CON - Roll 3D6 to generate CON value: ")
    base_characteristics["con"] = con_roll * 5

    print("Dexterity Characteristic")
    dex_roll = get_int_input(3, 18, "DEX - Roll 3D6 to generate DEX value: ")
    base_characteristics["dex"] = dex_roll * 5

    print("Appearance Characteristic")
    app_roll = get_int_input(3, 18, "APP - Roll 3D6 to generate APP value: ")
    base_characteristics["app"] = app_roll * 5

    print("Power Characteristic")
    pow_roll = get_int_input(3, 18, "POW - Roll 3D6 to generate POW value: ")
    base_characteristics["pow"] = pow_roll * 5

    print("Size Characteristic") # Recommended (total) minimum value: 40
    siz_roll = 6 + get_int_input(2, 12, "SIZ - Roll 2D6 to generate SIZ value: ")
    base_characteristics["siz"] = siz_roll * 5

    print("Intelligence Characteristic") # Recommended minimum value: 40
    int_roll = 6 + get_int_input(2, 12, "INT - Roll 2D6 to generate INT value: ")
    base_characteristics["int"] = int_roll * 5

    print("Education Characteristic")
    edu_roll = 6 + get_int_input(2, 12, "EDU - Roll 2D6 to generate EDU value: ")
    base_characteristics["edu"] = edu_roll * 5


# Returns a dictionary for investigator base stats
def point_buy_char(base_characteristics):
    print("Point Buy Characteristics selected.")
    print("\nYou have 460 points to split among the characteristics as you desire, within the range of 15 to 90.")
    print("It is recommended that INT and SIZ be no lower than 40.")

    points = 460
    is_valid_split = False # Points must be split so each characteristic is within the range of 15 to 90
    while (not is_valid_split):
        print(f"---CURRENT STATS---\nSTR: {base_characteristics["str"]}\nCon: {base_characteristics["con"]}\nSIZ: {base_characteristics["siz"]}\nDEX: {base_characteristics["dex"]}\nAPP: {base_characteristics["app"]}\nINT: {base_characteristics["int"]}\nPOW: {base_characteristics["pow"]}\nEDU: {base_characteristics["edu"]}")
        
        # modify points left (add OR remove points from characteristic to put in another category)
        characteristic_choice = input("Modify characteristic (STR, CON, SIZ, DEX, APP, INT, POW, or EDU): ")
        points_choice = 0 # Amount to modify characteristics by
        if (characteristic_choice.lower() == 'str'):
            points_choice = get_int_input(-base_characteristics["str"], points, "STR - Modify characteristic: ")
            base_characteristics["str"] += points_choice
        elif (characteristic_choice.lower() == 'con'):
            points_choice = get_int_input(-base_characteristics["con"], points,"CON - Modify characteristic: ")
            base_characteristics["con"] += points_choice
        elif (characteristic_choice.lower() == 'siz'):
            points_choice = get_int_input(-base_characteristics["siz"], points,"SIZ - Modify characteristic: ")
            base_characteristics["siz"] += points_choice
        elif (characteristic_choice.lower() == 'dex'):
            points_choice = get_int_input(-base_characteristics["dex"], points,"DEX - Modify characteristic: ")
            base_characteristics["dex"] += points_choice
        elif (characteristic_choice.lower() == 'app'):
            points_choice = get_int_input(-base_characteristics["app"], points,"APP - Modify characteristic: ")
            base_characteristics["app"] += points_choice
        elif (characteristic_choice.lower() == 'int'):
            points_choice = get_int_input(-base_characteristics["int"], points,"INT - Modify characteristic: ")
            base_characteristics["int"] += points_choice
        elif (characteristic_choice.lower() == 'pow'):
            points_choice = get_int_input(-base_characteristics["pow"], points,"POW - Modify characteristic: ")
            base_characteristics["pow"] += points_choice
        elif (characteristic_choice.lower() == 'edu'):
            points_choice = get_int_input(-base_characteristics["edu"], points,"EDU - Modify characteristic: ")
            base_characteristics["edu"] += points_choice
        else:
            print("Invalid choice. Please input a characteristic abbreviation (STR, CON, SIZ, DEX, APP, INT, POW, or EDU).")

        points -= points_choice
        print("You have", points,"left to spend.")

        # Confirm validity of investigator's base characteristics
        if (points == 0):
            if (15 <= base_characteristics["str"] <=90) and (15 <= base_characteristics["con"] <=90) and (15 <= base_characteristics["siz"] <=90) and (15 <= base_characteristics["dex"] <=90) and (15 <= base_characteristics["app"] <=90) and (15 <= base_characteristics["int"] <=90) and (15 <= base_characteristics["pow"] <=90) and (15 <= base_characteristics["edu"] <=90):
                is_valid_split = True
            else:
                print("Characteristic values must be within the range of 15 to 90. Please reallocate characteristic points.")

    return base_characteristics

def quick_fire_char():
    print("Quick fire method selected.")
    return

# generate the half and fifth Characteristic values. This is used to determine the values for Hard and Extreme rolls
def gen_half_and_fifth():
    print("Not available.")
    
    input("Press enter to return to main menu")
    return

def luck_roll():
    try:
        input_roll = int(input("Luck score - roll 3D6 and enter the resulting sum: "))
        while ((input_roll < 3) or (input_roll > 18)):
            input_roll = int(input("Invalid input. Please enter the sum of 3D6 to calculate the luck score:"))
        return input_roll * 5
    except ValueError:
        print("Value Error. Please try again.")
        return luck_roll()

# TODO: add a function to generate the skill points they have to spend based off their occupation

# TODO later: add a feature to generate base characteristics using randomly generated rolls

# show the main menu to allow user choice
def show_main_menu():
    print("What would you like to do? \n1) Generate Investigator Characteristics \n2) Generate Half and Fifth Characteristic Values\n3) Quit\n")
    user_response = input("Please select a number: ")
    return user_response

# Main function loop
if __name__ == '__main__':
    print("")
    user_choice = str(show_main_menu())
    while(user_choice != '3'):
        if (user_choice == '1'):  # Generate Characteristics
            gen_base_stats_menu()
        elif (user_choice == '2'): # Generate half and fifth characteristic values, based on user-submitted characteristics
            gen_half_and_fifth()
        else:
            print("Invalid choice. Please input a number 1-3")
        user_choice = str(show_main_menu())

    print("Goodbye!")