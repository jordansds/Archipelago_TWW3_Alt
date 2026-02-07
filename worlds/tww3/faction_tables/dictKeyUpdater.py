from enum import Enum
from BaseClasses import ItemClassification as IC
import pprint

#import bretonnia as brt
import highElves as hef

dictionary = hef.progBuildings
newDictionary = {}

newKey = 31300
for key, value in dictionary.items():
    newDictionary.update({newKey: value})
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