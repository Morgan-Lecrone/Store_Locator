"""
Lab06
This program will use quickselect to find the optimum location for a new store based on its proximity to other businesses.
Class: CSCI 141
Author: Morgan Lecrone
"""
import tools
import time


def median(lst):
    """
    This function finds the median of a list using quickselect.
    :param lst: The list to find the median of.
    :return: The median of the list.
    """
    if len(lst) % 2 == 1:
        return quick_select(lst, len(lst) // 2)
    else:
        k = len(lst) // 2
        a = quick_select(lst, k)
        b = quick_select(lst, k - 1)
        return (a + b) / 2

def quick_select(lst, k):
    """
    This function selects the kth element in a list if it were ordered.
    :param lst: The list to find the element in.
    :param k: The index of the element to be returned in lst if it were sorted..
    :return: The kth element in of lst if it were sorted.
    """
    if len(lst) != 0:
        pivot = lst[len(lst) // 2]
        smaller_list = []
        larger_list = []
        count = 0
        for e in lst:
            if e == pivot:
                count += 1
            elif e < pivot:
                smaller_list.append(e)
            elif e > pivot:
                larger_list.append(e)
        m = len(smaller_list)
        if k >= m and k < m + count:
            return pivot
        if m > k:
            return quick_select(smaller_list, k)
        else:
            return quick_select(larger_list, k - m - count)

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