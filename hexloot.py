# HexLoot

## A Path of Exile 2 Loot Filter, but better.

### App to read a Path of Exile 2 loot filter, and dynamically change the filter audio cues, color themes and dynamic adjustments, we can use ideas like filtering dynamically by level rangers, or base type I am looking for with audio cue and themes, etc. Or referencing a trade api to get a filter for valuable items in the market.

#### Example Filter File:
# Show
# 	Class "Body Armour"
#   SetTextColor 255 255 255
#   PlayAlertSound 1

# HexLoot

## A Path of Exile 2 Loot Filter, but better.

### App to read a Path of Exile 2 loot filter, and dynamically change the filter audio cues, color themes and dynamic adjustments, we can use ideas like filtering dynamically by level rangers, or base type I am looking for with audio cue and themes, etc. Or referencing a trade api to get a filter for valuable items in the market.

#### Example Filter File:
# Show
# 	Class "Body Armour"
#   SetTextColor 255 255 255
#   PlayAlertSound 1

# First Step


def parse_filter(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    rules = []  # Empy list to store all parsed rules.
    current_rule = []  # A temporary list to build the current rule line by line.

    for line in lines:
        line = line.strip()
        if line.startswith("Show") or line.startswith("Hide"):
            if current_rule:
                rules.append(current_rule)
            current_rule = [line]
        elif current_rule:
            current_rule.append(line)

    if current_rule:
        rules.append(current_rule)

    return rules


def categorize_rules(parsed_rules):
    categories = {}
    for rule in parsed_rules:
        for line in rule:
            if line.startswith("Class"):
                category = line.split('"')[1]  # Extract the class name
                if category not in categories:
                    categories[category] = []
                categories[category].append(rule)
                break
    return categories


# Parse filter file
filter_path = "filters/test.filter"  # Replace with your filter path
filter_path2 = "filters/Cyberion_POE2_V14b.filter"  # Replace with your filter path
filter_path3 = "filters/neversink.filter"  # Replace with your filter path
parsed_rules = parse_filter(filter_path3)
for rule in parsed_rules[:5]:  # Print the first 5 rules
    print(rule)
    print("-" * 20)


# Categorize rules
categories = categorize_rules(parsed_rules)
for category, rules in categories.items():
    print(f"Category: {category}, Rules: {len(rules)}")
