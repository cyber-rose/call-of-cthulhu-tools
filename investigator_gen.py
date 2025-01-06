# the main file for the program

### Investigator class - a helper class
# meant to parallel the investigator sheet, defaults to 1920s era investigator
# TODO: Consider making some of the existing functions into class methods
class Investigator:
    def __init__(self, strength, con, siz, dex, app, intelligence, power, edu, luck = None, investigator_name = "", age = None):
        # Values MUST be integers
        # Base characteristics (strength, constitution, size, dexterity, appearance, intelligence, power, education)
        self.strength = strength
        self.con = con
        self.siz = siz
        self.dex = dex
        self.app = app
        self.intelligence = intelligence
        self.power = power
        self.edu = edu

        self.name = investigator_name
        self.luck = luck
        self.age = age
        self.modify_characteristics_by_age()

    # Modify the base characteristics according to the age that has been set
    def modify_characteristics_by_age(self):
        if (self.age == None):
            # Don't modify characteristics if the new age is the same as the current age
            #print("Invalid Age.")
            return
        elif (type(self.age) is not int):
            print("Warning: current age is not an integer. Characteristics will not be modified")
            return

        print("Modifying characteristics according to given age,", self.age)
        if (self.age >= 15) and (self.age <= 19):
            deduct_choice = input("Deduct 5 points from STR or SIZ: ")
            print(deduct_choice + " and " + deduct_choice.lower())
            while (deduct_choice.lower() != 'str') and (deduct_choice.lower() != 'siz'):
                deduct_choice = input("Invalid choice. Please enter 'STR' or 'SIZ' to deduct 5 points from Strength or Size: ")
            if deduct_choice == "str":
                self.strength -= 5
            else:
                self.siz -= 5
            self.edu -= 5
            # TODO: roll TWICE to generate luck score for this age, and take the higher value
        elif (self.age >= 20) and (self.age <=39):
            self.edu_improvement_roll()
        elif (self.age >= 40) and (self.age <= 49):
            """ points_left = 5
            print("Deduct" + points_left + "points from STR, CON, or DEX. You may split this deduction across these characteristics.")
            while (points_left > 0):
                deduct_choice = input("Choose a category (STR, CON, or DEX) to deduct from: ")
                while ("str" not in deduct_choice.lower()) or ("con" not in deduct_choice.lower()) or ("dex" not in deduct_choice.lower()):
                    deduct_choice = input("Invalid choice. Please enter one category ('STR', 'CON', or 'DEX') to deduct points from: ")
                # Deduct from specified categories
                if "str" in deduct_choice.lower():
                    print("STR selected")
                    points_to_deduct = input("Points to deduct from STR: ")
                    while (not points_to_deduct.isdigit()) or (points_to_deduct < 0) or (points_to_deduct > points_left):
                        points_to_deduct = input("Invalid value. Please input a value from 0 to " + points_left +": ")
                    self.strength -= points_to_deduct
                    points_left -= points_to_deduct
                elif "con" in deduct_choice.lower():
                    print("CON selected")
                    points_to_deduct = input("Points to deduct from CON: ")
                    while (not points_to_deduct.isdigit()) or (points_to_deduct < 0) or (points_to_deduct > points_left):
                        points_to_deduct = input("Invalid value. Please input a value from 0 to " + points_left +": ")
                    self.con -= points_to_deduct
                    points_left -= points_to_deduct
                elif "dex" in deduct_choice.lower():
                    print("DEX selected")
                    points_to_deduct = input("Points to deduct from DEX: ")
                    while (not points_to_deduct.isdigit()) or (points_to_deduct < 0) or (points_to_deduct > points_left):
                        points_to_deduct = input("Invalid value. Please input a value from 0 to " + points_left +": ")
                    self.dex -= points_to_deduct
                    points_left -= points_to_deduct
                print("You have" + points_left + "points left to deduct.") """
            self.deduct_str_con_dex_by(5)
            self.app -= 5
            self.edu_improvement_roll()
            self.edu_improvement_roll()
        elif (self.age >= 50) and (self.age <= 59):
            self.deduct_str_con_dex_by(10)
            self.app -= 10
            self.edu_improvement_roll()
            self.edu_improvement_roll()
            self.edu_improvement_roll()
        elif (self.age >= 60) and (self.age <= 69):
            self.deduct_str_con_dex_by(20)
            self.app -= 15
            self.edu_improvement_roll()
            self.edu_improvement_roll()
            self.edu_improvement_roll()
            self.edu_improvement_roll()
        elif (self.age >= 70) and (self.age <= 79):
            self.deduct_str_con_dex_by(40)
            self.app -= 20
            self.edu_improvement_roll()
            self.edu_improvement_roll()
            self.edu_improvement_roll()
            self.edu_improvement_roll()
        elif (self.age >= 80) and (self.age <= 89):
            self.deduct_str_con_dex_by(80)
            self.app -= 25
            self.edu_improvement_roll()
            self.edu_improvement_roll()
            self.edu_improvement_roll()
            self.edu_improvement_roll()
        else:
            # If a player's investigators age is beyond the provided age range, the Lore Keeper (or Game Master) is responsible for choosing the appropriate modificationis to base stats
            print("Age supplied is not within the range specified by the 7th Edition Call of Cthulhu Keeper Rule Book. Please discuss your investigator age with the Keeper for your campaign. They will inform you of what characteristics to modify based on your characters age.")
            self.input("Eventually, you can use this tool to modify stats for additional, custom age ranges. This feature is not yet available. Press enter to continue.")

    # Helper function for Education improvement checks
    # TODO: fix the input integer issues
    def edu_improvement_roll(self):
        print("Make an improvement check for EDU")
        improvement_roll = int(input("Roll a percentile dice and input the value: "))
        #while (not improvement_roll.isdigit()) or (improvement_roll <= 0) or (improvement_roll > 100):
        while (improvement_roll <= 0) or (improvement_roll > 100):
            improvement_roll = int(input("Invalid value. Please input an integer from 1 to 100: "))

        if improvement_roll > self.edu:
            print("Successful EDU improvement check. Please roll a 1D10 to add to your EDU percentage points.")
            edu_increase = int(input("Value rolled: "))
            while (edu_increase <= 0) or (edu_increase > 100):
                edu_increase = int(input("Invalid value. Please input a value from 1 to 10: "))
            # EDU cannot go above 99 points
            if (self.edu + edu_increase) > 99:
                self.edu = 99
            else:
                self.edu = self.edu + edu_increase
        else:
            print("Failed EDU improvement check.")

    # Helper function for modifying base characteristics by age. 
    # Given a value of points left to deduct from STR, CON, and/or DEX, allow the user to split up the deduction of points across those characteristics.
    def deduct_str_con_dex_by(self, points_left):
        #points_left = points_to_deduct
        print("Deduct", points_left, "points from STR, CON, or DEX. You may split this deduction across these characteristics.")
        while (points_left > 0):
            deduct_choice = input("Choose a category (STR, CON, or DEX) to deduct from: ")
            while ("str" not in deduct_choice.lower()) or ("con" not in deduct_choice.lower()) or ("dex" not in deduct_choice.lower()):
                deduct_choice = input("Invalid choice. Please enter one category ('STR', 'CON', or 'DEX') to deduct points from: ")
            # Deduct from specified categories
            if "str" in deduct_choice.lower():
                print("STR selected")
                points_to_deduct = input("Points to deduct from STR: ")
                while (not points_to_deduct.isdigit()) and ((int(points_to_deduct) < 0) or (int(points_to_deduct) > points_left)):
                    points_to_deduct = input("Invalid value. Please input a value from 0 to", points_left,": ")
                self.strength -= int(points_to_deduct)
                points_left -= int(points_to_deduct)
            elif "con" in deduct_choice.lower():
                print("CON selected")
                points_to_deduct = input("Points to deduct from CON: ")
                while (not points_to_deduct.isdigit()) and ((int(points_to_deduct) < 0) or (int(points_to_deduct) > points_left)):
                    points_to_deduct = input("Invalid value. Please input a value from 0 to ", points_left, ": ")
                self.con -= int(points_to_deduct)
                points_left -= int(points_to_deduct)
            elif "dex" in deduct_choice.lower():
                print("DEX selected")
                points_to_deduct = input("Points to deduct from DEX: ")
                while (not points_to_deduct.isdigit()) and ((int(points_to_deduct) < 0) or (int(points_to_deduct) > points_left)):
                    points_to_deduct = input("Invalid value. Please input a value from 0 to", points_left,": ")
                self.dex -= int(points_to_deduct)
                points_left -= int(points_to_deduct)
            print("You have", points_left, "points left to deduct.")

    def get_sanity_points(self):
        return self.power
    
    def get_magic_points(self):
        return (self.power // 2)
    
    def get_hit_points(self):
        return ((self.con + self.siz)//10)
    
    def get_move_rate(self):
        mov = 0
        if (self.dex < self.siz) and (self.strength < self.siz):
            mov = 7
        elif (self.dex > self.siz) and (self.strength > self.siz):
            mov = 9
        else:
            mov = 8

        # Modify movement based on Age
        if self.age < 40:
            return mov
        elif self.age >= 80: 
            # The 7th edition Keeper Rule Book does not include info on how to modify movement if age is in the 90s or older. This tool will use the same MOV deduction for those ages that is deducted if age is in the 80s.
            mov -= 5
        elif self.age >= 70:
            mov -= 4
        elif self.age >= 60:
            mov -= 3
        elif self.age >= 50:
            mov -= 2
        else:
            mov -= 1
        
        return mov

    # Damage bonus is returned as a string
    def get_damage_bonus(self):
        size_strength = self.strength + self.siz

        if (size_strength >= 2) and (size_strength <= 64):
            return '-2'
        elif (size_strength >= 65) and (size_strength <= 84):
            return '-1'
        elif (size_strength >= 85) and (size_strength <= 124):
            return 'None'
        elif (size_strength >= 125) and (size_strength <= 164):
            return '+1D4'
        elif (size_strength >= 165) and (size_strength <= 204):
            return '+1D6'
        elif (size_strength >= 205) and (size_strength <= 284):
            return '+2D6'
        elif (size_strength >= 285): # Add an additional 1D6 damage bonus for each additional 80 points
            dice = 3
            while (size_strength >= 365):
                dice += 1
                size_strength -= 80
            return "+" + dice + "D6"
        else: 
            # It is not possible to have a strength and size sum to less than 2 according to the 7th edition rules of "Call of Cthulhu"
            print("Error: damage bonus is not possible. Please check your STR and SIZ values")
            return 'Not possible'

    # Get the build of a character
    def get_build(self):
        size_strength = self.strength + self.siz
        if (size_strength >= 2) and (size_strength <= 64):
            return -2
        elif (size_strength >= 65) and (size_strength <= 84):
            return -1
        elif (size_strength >= 85) and (size_strength <= 124):
            return 0
        elif (size_strength >= 125) and (size_strength <= 164):
            return 1
        elif (size_strength >= 165) and (size_strength <= 204):
            return 2
        elif (size_strength >= 205) and (size_strength <= 284):
            return 3
        elif (size_strength >= 285): # Add an additional +1 to build for each additional 80 points
            build = 4
            while (size_strength >= 365):
                dice += 1
                size_strength -= 80
            return build
        else: 
            # It is not possible to have a strength and size sum to less than 2 according to the 7th edition rules of "Call of Cthulhu"
            print("Error: Build is not possible. Please check your STR and SIZ values")
            return -3
    
    def set_luck(self, x):
        self.luck = x

    def set_age(self, a):
        # if (self.age != None) or (self.age.isdigit()):
        #     print("Warning: the current characteristic values have already been modified by age. Are you sure you would like to change this age and modify these values again?")
        #     change_confirmation = input("Type Y to confirm")
        #     if change_confirmation == "Y":
        #         print("Modifying age and current characteristics")
        #     else:
        #         print("Modification to age and current characteristics canceled.")
        #         return
        self.age = a
        self.modify_characteristics_by_age()
        

    

# Print the stats of the investigator generated. Takes an investigator class object
def print_investigator_stats(investigator):
    print("Investigator stats for " + investigator.name + ":")
    print("Age: ", investigator.age)

    print("STR: ", investigator.strength)
    print("CON: ", investigator.con)
    print("SIZ: ", investigator.siz)
    print("DEX: ", investigator.dex)
    print("APP: ", investigator.app)
    print("INT: ", investigator.intelligence)
    print("POW: ", investigator.power)
    print("EDU: ", investigator.edu)

    print("Luck: ", investigator.luck)
    print("Sanity: ", investigator.get_sanity_points())


    # print("Move Rate: ", investigator.get_move_rate())
    # print("Hit Points: ", investigator.get_hit_points())
    # print("Magic Points: ", investigator.get_magic_points())

    # print("Damage Bonus: " + investigator.get_damage_bonus())
    # print("Build: ", investigator.get_build())

    return

# Generate the base characteristics for investigators (using user given dice rolls)
def gen_base_stats_menu():
    print("You have choosen to generate the characteristics for your investigator. This will lead you through the steps to create an investigator based on the 7th edition rules.")
    print("Before begining please choose the method you would like to use to create your investigator.")
    #print("After you make your characteristic rolls, you will have an option to select additional methods or house rules to create your character. This includes: options to scrap all base stat rolls and start over, modify low rolls, or adding an extra 1D10 percentage points to distribute among characteristics.") 
    # TODO: add option to let users select where to put rolled characteristics?
    
    print("What method would you like to use to generate investigator characteristics?\n    1. Default\n    2. Point Buy Characteristics\n    3. Quick Fire Method")
    gen_method = input("Method: ")
    while (gen_method != 'q') and (gen_method != '1') and (gen_method != '2') and (gen_method != '3'):
        gen_method = input("Invalid choice. Please enter a number 1-3 to select the method or 'q' to quit:")


    if (gen_method == 'q'):
        input("Press enter to return to main menu")
        return

    # Get base characteristic values to build investigator, based on user's choice

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
    elif (gen_method == '2'):
        point_buy_char()
    else:
        quick_fire_char()

    # Create an investigator with the the base characteristics
    player_char = Investigator(base_characteristics["str"], base_characteristics["con"], base_characteristics["siz"], base_characteristics["dex"], base_characteristics["app"], base_characteristics["int"], base_characteristics["pow"], base_characteristics["edu"])
    
    # Age
    print("How old is your investigator?")
    age_is_valid = False
    input_age = input("Age: ")
    while (age_is_valid):
        if not input_age.isdigit():
            input_age = input("Invalid age. Please enter age as an integer: ")
        elif (int(input_age) <= 0) or (int(input_age) > 110):
            input_age = input("Invalid age. Please enter a realistic age for a human (i.e. from 1 to 110): ")
        else:
            age_is_valid = True

    age_num = int(input_age)
    if (1 <= age_num < 15) or (age_num >= 90):
        print("You have choosen an age outside of the typical age range (15 to 89) for Call of Cthulhu. There are no specified modifications to characteristics for these ages in the rule book. Before you proceed, please discuss this choice with your Keeper. They will determine how you should proceed / modify characteristics.")
        retry_choice = input("Would you like to input an age within the rulebook instead? (Y/N)")
        while (retry_choice != "Y") and (retry_choice != "N"):
            retry_choice = input("Y/N: ")
        
        if retry_choice.lower() == "y":
            input_age = input("Character age: ")
            while (not input_age.isdigit()) and (int(input_age) < 15) and (int(input_age) > 89):
                input_age = input("Invalid age. Please enter an age from 15 to 89:")
        age_num = int(input_age)

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

    print_investigator_stats(player_char)
    # generate the half and fifth values (?)
    # get occupation?
    # allocate edu points for skills?
    # get credit rating?
    input("Press enter to return to main menu")
    return

# Returns an investigator w/ base stats....
def point_buy_char():
    print("Point Buy Characteristics selected.")
    print("\nYou have 460 points to split among the characteristics as you desire, within the range of 15 to 90.")
    print("It is recommended that INT and SIZ be no lower than 40.")



    return

def quick_fire_char():
    print("Quick fire method selected.")

    return

# generate the half and fifth Characteristic values. This is used to determine the values for Hard and Extreme rolls
def gen_half_and_fifth():
    print("Not available at the moment")
    
    input("Press enter to return to main menu")
    return

def luck_roll():
    # input_roll = input("Luck score - roll 3D6 and enter the resulting sum: ")
    # while (not input_roll.isdigit()) and ((input_roll <= 0) or (input_roll > 18)):
    #     input_roll = input("Invalid input. Please enter the sum of 3D6 to calculate the luck score:")
    # return input_roll * 5
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