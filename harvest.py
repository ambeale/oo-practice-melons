############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType("musk", "1998", "green", True, True, "Muskmelon")
    muskmelon.add_pairing("mint")
    all_melon_types.append(muskmelon)


    casaba = MelonType("cas", "2003", "orange", False, False, "Casaba")
    casaba.add_pairing("strawberies")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)

    crenshaw = MelonType("cren", "1996", "green", False, False, "Crenshaw")
    crenshaw.add_pairing("proscuitto")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType("yw", "2013", "yellow", False, True, "Yellow Watermelon")
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print("{melon} pairs with".format(melon = melon.name))
        for pair in melon.pairings:
            print("- {pair}".format(pair = pair))
        print("")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_codes = {}
    
    for melon in melon_types:
        melon_codes[melon.code] = melon

    return melon_codes    


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field_num,
                    harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_num = field_num
        self.harvested_by = harvested_by

    def is_sellable(self):
        return (self.shape_rating > 5) and (self.color_rating > 5) and (self.field_num != 3)


def make_melons(melon_codes):
    """Returns a list of Melon objects."""

    melons = []

    melon_1 = Melon(melon_codes["yw"], 8, 7, 2, "Sheila")
    melon_2 = Melon(melon_codes["yw"], 3, 4, 2, "Sheila")
    melon_3 = Melon(melon_codes["yw"], 9, 8, 3, "Sheila")
    melon_4 = Melon(melon_codes["cas"], 10, 6, 35, "Sheila")
    melon_5 = Melon(melon_codes["cren"], 8, 9, 35, "Michael")
    melon_6 = Melon(melon_codes["cren"], 8, 2, 35, "Michael")
    melon_7 = Melon(melon_codes["cren"], 2, 3, 4, "Michael")
    melon_8 = Melon(melon_codes["musk"], 6, 7, 4, "Michael")
    melon_9 = Melon(melon_codes["yw"], 7, 10, 3, "Sheila")

    melons.extend([melon_1, melon_2, melon_3, melon_4, melon_5, melon_6,
                    melon_7, melon_8, melon_9])

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        sellable = melon.is_sellable()

        if sellable:
            print("Harvested by {} from Field #{} - CAN BE SOLD".format(melon.harvested_by,melon.field_num))
        else:
            print("Harvested by {} from Field #{} - NOT SELLABLE".format(melon.harvested_by,melon.field_num))


all_melons = make_melon_types()

melon_lookup = make_melon_type_lookup(all_melons)

melons = make_melons(melon_lookup)
#print(melons[0].melon_type.first_harvest)

get_sellability_report(melons)
