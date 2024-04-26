# Author: Dhaval Patel. Codebasics YouTube Channel

import re
def get_str_from_food_dict(food_dict: dict):
    """
    This function takes a dictionary of food items and returns a string of the food items and their quantities.
    """
    food_str = ""
    for food, quantity in food_dict.items():
        food_str += f"{food}: {quantity}\n"
    return food_str
#def get_str_from_food_dict(food_dict:dict):
    #result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    #return result


def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(0)
        return extracted_string

    return ""
