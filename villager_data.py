"""Functions to parse a file containing villager data."""

def all_species(filename):
    """Return a set of unique species in the given file.
    
    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()
    file_data = open(filename)
    for line in file_data:
        each_species = line.split("|")
        species.add(each_species[1])
       
    return species
        

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species 

    Return:
        - list[str]: a list of names
    """

    villagers = []

    file_data = open(filename)
    for line in file_data:
        each_species = line.split("|")
        if(search_string == "All"): 
            villagers.append(each_species[0])
        else:
            if search_string == each_species[1]:
                villagers.append(each_species[0])

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    file_data = open(filename)
    for line in file_data:
        each_species = line.split("|")
        if (each_species[3] == "Fitness"):
            fitness.append(each_species[0])
        if (each_species[3] == "Nature"):
            nature.append(each_species[0])
        if (each_species[3] == "Education"):
            education.append(each_species[0])
        if (each_species[3] == "Music"):
            music.append(each_species[0])
        if (each_species[3] == "Fashion"):
            fashion.append(each_species[0])
        if (each_species[3] == "Play"):
            play.append(each_species[0])

    return [fitness, nature, education, music, fashion, play]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """
    all_data = []
    file_data = open(filename)
    for line in file_data:
        each_species = line.split("|")
        all_data.append(tuple(each_species))

    return all_data



def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code

all_species("villagers.csv")