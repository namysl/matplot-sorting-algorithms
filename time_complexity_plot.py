import time
import random

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

import sorting_algorithms


def create_new_list(len_list, case="average"):
    """Depending on the chosen case,
    the function creates a specified list of elements"""
    new_list = []

    if case == "best":
        new_list = list(range(0, len_list))

    elif case == "worst":
        new_list = list(range(0, len_list))
        new_list.reverse()

    elif case == "average":
        for _ in range(0, len_list):
            new_list.append(random.randint(-10000, 10000))

    return new_list


def generate_axis(new_list, algorithm):
    """Measures time, calculates the mean of 10 repeats,
     then returns the axis for the plot"""
    x = []
    y = []
    time_sum = 0

    for i in range(1, len(new_list) + 1):
        for _ in range(0, 10):
            start = time.time()

            chosen_algorithm = getattr(sorting_algorithms, algorithm)
            chosen_algorithm(new_list[0:i])

            end = time.time()
            time_sum += end - start

        x.append(i)
        y.append(time_sum / len(new_list))

    return x, y


def draw_plot(axis, algorithm):
    figure(figsize=(8, 6))
    plt.plot(axis[0], axis[1], linewidth=1.0)
    plt.title(algorithm)
    plt.xlabel('number of elements in a list')
    plt.ylabel('time')
    plt.grid(True)
    plt.show()


def show_chosen_case(len_list, case, algorithm):
    """Creates a single plot of a chosen case"""
    created_list = create_new_list(len_list, case)
    xy = generate_axis(created_list, algorithm)
    draw_plot(xy, algorithm)


def show_every_case(len_list, algorithm):
    """Creates a plot of every case of an algorithm"""
    list_best = create_new_list(len_list, 'best')
    
    xy1 = generate_axis(list_best, algorithm)

    list_average = create_new_list(len_list, 'average')
    xy2 = generate_axis(list_average, algorithm)

    list_worst = create_new_list(len_list, 'worst')
    xy3 = generate_axis(list_worst, algorithm)

    figure(figsize=(8, 6))
    plt.plot(xy1[0], xy1[1], linewidth=1.0, label='best')
    plt.plot(xy2[0], xy2[1], linewidth=1.0, label='average')
    plt.plot(xy3[0], xy3[1], linewidth=1.0, label='worst')

    plt.title(algorithm)
    plt.xlabel('number of elements in a list')
    plt.ylabel('time')
    plt.grid(True)
    plt.legend(prop={"size": 10})
    plt.show()


def compare_algorithms(len_list, case, algo1, algo2):
    """Creates a plot of two algorithms"""
    list_algo1 = create_new_list(len_list, case)
    xy1 = generate_axis(list_algo1, algo1)

    list_algo2 = create_new_list(len_list, case)
    xy2 = generate_axis(list_algo2, algo2)

    figure(figsize=(8, 6))
    plt.plot(xy1[0], xy1[1], linewidth=1.0, label=algo1)
    plt.plot(xy2[0], xy2[1], linewidth=1.0, label=algo2)

    plt.title(case+" case")
    plt.xlabel('number of elements in a list')
    plt.ylabel('time')
    plt.grid(True)
    plt.legend(prop={"size": 10})
    plt.show()
    
    
# show_chosen_case(200, 'worst', 'selection_sort')
# show_every_case(200, 'selection_sort')
# compare_algorithms(200, 'worst', 'bubble_sort', 'insertion_sort')
