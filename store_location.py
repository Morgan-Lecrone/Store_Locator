"""
Lab06
This program will use insertion sort to find the optimum location for a new store based on its proximity to other businesses.
Class: CSCI 141
Author: Morgan Lecrone
"""
import insertion_sort
import tools
import time


def median(lst):
    """
    This function finds the median of a list using insertion sort.
    :param lst: The list of values to find the median of.
    :return: The median of the list.
    """
    lst = insertion_sort.insertion_sort(lst)
    if len(lst) % 2 == 1:
        return lst[len(lst) // 2]
    else:
        a = len(lst) // 2
        b = a - 1
        return (lst[a] + lst[b]) / 2

def main():
    """
    This function reads a file inputted by the user.  Then, it finds the median of the data in the file, and the
    sum of the distances from the median.  Then it prints the new store location (median), sum of distances to
    the new store, and the amount of time elapsed during the calculation.
    """
    file = input("Enter data file: ")
    distances = tools.read_file(file)
    initial_time = time.perf_counter()
    med = median(distances)
    sum = tools.sum_distances(distances, med)
    final_time = time.perf_counter() - initial_time
    print("Optimum new store location: " + str(med))
    print("Sum of distances to the new store: " + str(sum))
    print("\nelapsed time: " + str(final_time))


if __name__ == '__main__':
    main()