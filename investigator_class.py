# Helper function to integer user input within a range of values.
def get_int_input(min_val, max_val, input_message = "Input: "):
    """Get user input as an integer within a (inclusive) range of values [min_val,max_val]. Prompts the user for input with input_message string.
    Returns the inputted integer if possible."""
    try:
        user_input = int(input(input_message))
        while (user_input < min_val) or (user_input > max_val):
            user_input = int(input(("Invalid input. Please input an integer from " + str(min_val) + " to " + str(max_val) + ": ")))
        return user_input
    except ValueError:
        print("Value Error: Input must be an integer.")
        return get_int_input(min_val, max_val, input_message)



### Investigator class - a helper class
# meant to parallel the investigator sheet, defaults to 1920s era investigator
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
        #self.modify_characteristics_by_age()

    # return string representation of character sheet
    def __str__(self):
        investigator_str = f"Investigator Name: {self.name}\nAge: {self.age}\nSTR: {self.strength}\nCon: {self.con}\nSIZ: {self.siz}\nDEX: {self.dex}\nAPP: {self.app}\nINT: {self.intelligence}\nPOW: {self.power}\nEDU: {self.edu}\nLuck: {self.luck}\nSanity: {self.get_sanity_points()}\n"
        investigator_str = investigator_str + f"Move Rate: {self.get_move_rate()}\nHit Points: {self.get_hit_points()}\nMagic Points: {self.get_magic_points()}\nDamage Bonus: {self.get_damage_bonus()}\nBuild: {self.get_build()}"
        return investigator_str

    # Modify the base characteristics according to the age that has been set
    def modify_characteristics_by_age(self):
        if (self.age == None):
            # Don't modify characteristics if the new age is the same as the current age
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
            # If a player's investigators age is beyond the provided age range, the Lore Keeper (or Game Master) is responsible for choosing the appropriate modifications to base stats
            print("Age supplied is not within the range specified by the 7th Edition Call of Cthulhu Keeper Rule Book. Please discuss your investigator age with the Keeper for your campaign. They will inform you of what characteristics to modify based on your characters age.")
            input("Eventually, you can use this tool to modify stats for additional, custom age ranges. This feature is not yet available. \nPress enter to continue.")

    # Helper function for Education improvement checks
    # TODO: fix the input integer issues
    def edu_improvement_roll(self):
        print("Make an improvement check for EDU")
        improvement_roll = get_int_input(1, 100, "Roll a percentile dice and input the value: ")
        if improvement_roll > self.edu:
            print("Successful EDU improvement check. Please roll a 1D10 to add to your EDU percentage points.")
            edu_increase = get_int_input(1, 10,"Value rolled: ")
            
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
            while ((deduct_choice.lower() != "str") and (deduct_choice.lower() != "con") and (deduct_choice.lower() != "dex")):
                deduct_choice = input("Invalid choice. Please enter one category ('STR', 'CON', or 'DEX') to deduct points from: ")
            # Deduct from specified categories
            if deduct_choice.lower() == 'str':
                print("STR selected")
                points_to_deduct = get_int_input(0, points_left, "Points to deduct from STR: ")
                self.strength -= points_to_deduct
                points_left -= points_to_deduct
            elif deduct_choice.lower() == 'con':
                print("CON selected")
                points_to_deduct = get_int_input(0, points_left,"Points to deduct from CON: ")
                self.con -= points_to_deduct
                points_left -= points_to_deduct
            elif deduct_choice.lower() == 'dex':
                print("DEX selected")
                points_to_deduct = get_int_input(0, points_left,"Points to deduct from DEX: ")
                self.dex -= points_to_deduct
                points_left -= points_to_deduct
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
        elif 80 <= self.age <=90:
            mov -= 5
        elif self.age >= 70:
            mov -= 4
        elif self.age >= 60:
            mov -= 3
        elif self.age >= 50:
            mov -= 2
        else:
            mov -= 1
        # The 7th edition Keeper Rule Book does not include info on how to modify movement for ages beyond 40s to 80s.

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
                build += 1
                size_strength -= 80
            return build
        else: 
            # It is not possible to have a strength and size sum to less than 2 according to the 7th edition rules of "Call of Cthulhu"
            print("Error: Build is not possible. Please check your STR and SIZ values")
            return -3
    
    def set_luck(self, x):
        self.luck = x

    def set_age(self, a):
        """ Sets the Investigator's age to a value 'a' and modifies the characteristics by age."""
        self.age = a
        self.modify_characteristics_by_age()

    # TODO: add a to_dict function to help with testing the investigator class methods
        

if __name__ == '__main__':
    pass