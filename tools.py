def read_file(file_name):
    """
    This function reads a file of businesses and their locations and returns a list of the locations.
    :param file_name: The name of the file to be read.
    :return: A list of the locations of the businesses.
    """
    file = open("test/" + file_name)
    numbers = []
    for line in file:
        split = line.split(" ")
        numbers.append(float(split[1]))
    return numbers

def sum_distances(lst, best_location):
    """
    This function adds up the distances of each business to the best new store location.
    :param lst: The list of business locations.
    :param best_location: The best location for the new store.
    :return: The sum of the distances of each business from the best new store location.
    """
    sum = 0
    for i in lst:
        sum += abs(i - best_location)
    return sum
