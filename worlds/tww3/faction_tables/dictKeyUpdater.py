from enum import Enum
import pprint
from worlds.tww3.item_types import ItemData

import warriorsOfChaos as fac

dictionary = fac.tzeentchUnits
newDictionary = {}

#    classification: ItemClassification
#    count: int
#    name: str
#    type: ItemType
#    tier: int
#    progressionGroup: str
#    readableName: str
#FIX BEASTMEN
#FIX DWARFS
newKey = 56350
for key, value in dictionary.items():
    #newDictionary.update({newKey: specialItemData(*value)})
    newDictionary.update({newKey: ItemData(*value[:4], value[4], *value[5:])})
    newKey += 1

#Thanks Gemini, you eventually wrote the correct code I wanted. This is why I don't vibecode...
class ItemDataWrapper:
    """Wraps a namedtuple to control exactly how it appears in pprint."""
    def __init__(self, nt):
        self.nt = nt

    def __repr__(self):
        # Format the internal values: clean Enums, keep others as is
        clean_values = [
            f"{v.__class__.__name__}.{v.name}" if isinstance(v, Enum) else repr(v)
            for v in self.nt
        ]
        # Join them to look like: ItemData(Value1, Value2, ...)
        return f"{type(self.nt).__name__}({', '.join(clean_values)})"

def clean_for_print(obj):
    if isinstance(obj, dict):
        return {k: clean_for_print(v) for k, v in obj.items()}
    # If it's your namedtuple, wrap it
    if isinstance(obj, tuple) and hasattr(obj, '_fields'):
        return ItemDataWrapper(obj)
    return obj

cleaned = clean_for_print(newDictionary)
pprint.pprint(cleaned, width=1) # Width=1 forces it to multi-line if you prefer

"""    name = value.readableName
    readableName = name.split("anc_")[-1].replace("_", " ").title().split(" ")
    if readableName[0] == "Magic" or readableName[0] == "Blessing":
        readableName = "Standard: " + " ".join(readableName[2:])
    elif readableName[0] == "Weapon":
        readableName = "Weapon: " + " ".join(readableName[1:])
    elif readableName[0] == "Armour":
        readableName = "Armour: " + " ".join(readableName[1:])
    elif readableName[0] == "Talisman":
        readableName = "Talisman: " + " ".join(readableName[1:])
    elif readableName[0] == "Follower":
        readableName = "Follower: " + " ".join(readableName[1:])
    elif readableName[0] == "Dread":
        readableName = "Follower: " + " ".join(readableName[2:])
    elif readableName[0] == "Cth":
        readableName = "Follower: " + " ".join(readableName[3:])
    elif readableName[0] == "Enchanted":
        readableName = "Enchanted Item: " + " ".join(readableName[2:])
    elif readableName[0] == "Arcane":
        readableName = "Arcane Item: " + " ".join(readableName[2:])
    elif readableName[0] == "Banner":
        readableName = "Banner: " + " ".join(readableName[1:])

    newDictionary.update({newKey: ItemData(value.classification, value.count, name, value.type, value.tier, value.progressionGroup, readableName)})"""