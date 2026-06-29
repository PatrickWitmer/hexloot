# HexLoot

## A Path of Exile 2 Loot Filter, but better.

### App to read a Path of Exile 2 loot filter, and dynamically change the filter audio cues, color themes and dynamic adjustments, we can use ideas like filtering dynamically by level rangers, or base type I am looking for with audio cue and themes, etc. Or referencing a trade api to get a filter for valuable items in the market.

#### Example Filter File:
# Show
# 	Class "Body Armour"
#   SetTextColor 255 255 255
#   PlayAlertSound 1

# ==============================
#           Parse the Filter
# ==============================


def parse_filter(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

            print("File Content:")
            for line in lines:
                print(line)

    except Exception as e:
        print(f"Error: {e}")
