from typing import Optional
from BaseClasses import MultiWorld
from .. import Helpers


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(world: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    if category_name == "G1":
        if Helpers.get_option_value(world, player, "NumGames") >= 1:
            return True
        return False
    if category_name == "G2":
        if Helpers.get_option_value(world, player, "NumGames") >= 2:
            return True
        return False
    if category_name == "G3":
        if Helpers.get_option_value(world, player, "NumGames") >= 3:
            return True
        return False
    if category_name == "G4":
        if Helpers.get_option_value(world, player, "NumGames") >= 4:
            return True
        return False
    if category_name == "G5":
        if Helpers.get_option_value(world, player, "NumGames") >= 5:
            return True
        return False
    return None
