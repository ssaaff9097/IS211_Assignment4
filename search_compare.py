import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = + 1

    return found


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found


def binary_search_iterative(a_list,item):
    first = 0

    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found 
    
    
def binary_search_recursive(a_list,item):
    if len(a_list) == 0:
        return False, time.time() 
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True, time.time() 
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)
            

def main():
    """Main entry point"""
    sizes = [500, 1000, 5000]
    target = 99999999
    num_trials = 100

    for the_size in sizes:
        print(f"\nBenchmarking search algorithms for list size {the_size},,,")

        for the_size in sizes: 
            sequential_total_time = 0
            ordered_sequential_total_time = 0
            binary_iterative_total_time = 0
            binary_recursive_total_time = 0 

    
        for i in range(num_trials):
            mylist = get_me_random_list(the_size)
            # sorting is not needed for sequential search.
            mylist = sorted(mylist)

            start = time.time()
            sequential_search(mylist, target)
            sequential_total_time += time.time() - start


            start = time.time()
            ordered_sequential_search(mylist, target)
            ordered_sequential_total_time += time.time() - start

            start = time.time()
            binary_search_iterative(mylist, target)
            binary_iterative_total_time += time.time() - start 

            start + time.time()
            binary_search_recursive(mylist, target)
            binary_recursive_total_time += time.time() - start

        
            avg_sequential_time = sequential_total_time / 100
            avg_ordered_sequential_time = ordered_sequential_total_time / 100 
            avg_binary_iterative_time = binary_iterative_total_time / 100
            avg_binary_recursive_time = binary_recursive_total_time / 100

    
            print(f"Sequential search took {avg_sequential_time:10.7f} seconds to ru, on average for a list of {the_size} elements")
            print(f"Ordered sequential time took {avg_ordered_sequential_time:10.7f} seconds to run, on average for a list of {the_size} elements")
            print(f"Binary Search Iterative took {avg_binary_iterative_time:10.7f} seconds to run, on average for a list of {the_size} elements")
            print(f"Binary Search Recursive took {avg_binary_recursive_time:10.7f} seconds to run, on average for a list of {the_size} elements") 
