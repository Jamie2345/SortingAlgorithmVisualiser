'''
    HOW EACH SORTING ALGORITHM WORKS
    --------------------------------

        BUBBLE SORT
        -----------

        Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

        Example:

            First Pass:
            ( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
            ( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
            ( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
            ( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.
            Second Pass:
            ( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
            ( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
            ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
            ( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
            Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.
            Third Pass:
            ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
            ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
            ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
            ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )

        Time Complexity
        ---------------

        Best	            O(n)
        Worst	            O(n2)
        Average	            O(n2)
        Space Complexity    O(1)
        Stability	        Yes



        INSERTION SORT
        --------------

        Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.

        To sort an array of size n in ascending order:
        1: Iterate from arr[1] to arr[n] over the array.
        2: Compare the current element (key) to its predecessor.
        3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

        Example:

            12, 11, 13, 5, 6
            Let us loop for i = 1 (second element of the array) to 4 (last element of the array)
            i = 1. Since 11 is smaller than 12, move 12 and insert 11 before 12
            11, 12, 13, 5, 6
            i = 2. 13 will remain at its position as all elements in A[0..I-1] are smaller than 13
            11, 12, 13, 5, 6
            i = 3. 5 will move to the beginning and all other elements from 11 to 13 will move one position ahead of their current position.
            5, 11, 12, 13, 6
            i = 4. 6 will move to position after 5, and elements from 11 to 13 will move one position ahead of their current position.
            5, 6, 11, 12, 13

        Time Complexity
        ---------------

        Best	            O(n)
        Worst	            O(n2)
        Average	            O(n2)
        Space Complexity    O(1)
        Stability	        Yes



        SELECTION SORT
        --------------

        Selection sort is the most conceptually simple of all the sorting algorithms. It works by selecting the smallest (or largest, if you want to sort from big to small) element of the array and placing it at the head of the array.

        Time Complexity
        ---------------

        Best	            O(n2)
        Worst	            O(n2)
        Average	            O(n2)
        Space Complexity    O(1)
        Stability	        No



        Merge Sort
        ----------

        A merge sort uses a technique called divide and conquer. The list is repeatedly divided into two until all the elements are separated individually. Pairs of elements are then compared, placed into order and combined. The process is then repeated until the list is recompiled as a whole.

        Time Complexity
        ---------------

        Best	            O(n*log n)
        Worst	            O(n*log n)
        Average	            O(n*log n)
        Space Complexity	O(n)
        Stability	Yes



        Quick Sort
        ----------

        Quicksort is a highly efficient sorting technique that divides a large data array into smaller ones. A vast array is divided into two arrays, one containing values smaller than the provided value, say pivot, on which the partition is based. The other contains values greater than the pivot value.

        How Does Quick Sort Work?

        To sort an array, you will follow the steps below:

        1) You will make any index value in the array as a pivot.
        2) Then you will partition the array according to the pivot.
        3) Then you will recursively quicksort the left partition
        4) After that, you will recursively quicksort the correct partition.

        Let's have a closer look at the partition bit of this algorithm:

        1) You will pick any pivot, let's say the highest index value.
        2) You will take two variables to point left and right of the list, excluding pivot.
        3) The left will point to the lower index, and the right will point to the higher index.
        4) Now you will move all elements which are greater than pivot to the right.
        5) Then you will move all elements smaller than the pivot to the left partition.

        Time Complexity
        ---------------

        Best	            O(n*log n)
        Worst	            O(n2)
        Average	            O(n*log n)
        Space Complexity	O(log n)
        Stability	        No



        Cocktail Shaker Sort
        --------------------

        Cocktail Shaker Sort (also known as bidirectional bubble sort) The algorithm extends bubble sort by operating in two directions. While it improves on bubble sort by more quickly moving items to the beginning of the list, it provides only marginal performance improvements.

        Time Complexity
        ---------------

        Best	            O(n)
        Worst	            O(n2)
        Average	            O(n2)
        Space Complexity    O(1)
        Stability	        Yes

'''







# code

import pygame
import random
import time

# Initialising pygame
pygame.init()

# Settings

list_size = 100  # amount of items in the list  if blocks don't show up you have added too many
delay = 0  # slow down algorithms if you want (delay is in milliseconds)

use_random_numbers_in_list = False    # if false you will have numbers 1 -> len(lst) elif true you will have x random numbers in range(min_v, max_v) where x is list length

# min and max value if you are using random numbers
min_v = 0
max_v = 700


# class for pygame window settings and colours
class DrawInfo:

    # colours
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    grey = (128, 128, 128)

    # colours used in program
    background_colour = (255, 255, 255)
    text_colour = (0, 0, 0)
    block_colour = (0, 0, 0)
    current_node_colour = (255, 0, 0)
    end_colour = (0, 255, 0)   # what colour to highlight the blocks once sorted

    background = background_colour

    side_pad = 10    # gap on sides of blocks
    top_pad = 150  # gap between top text and blocks

    SMALL_FONT = pygame.font.SysFont("comicsans", 15)
    FONT = pygame.font.SysFont("comicsans", 20)
    LARGE_FONT = pygame.font.SysFont("comicsans", 35)

    nodes_visited = 0
    comparisons = 0

    current_algorithm = 'Bubble Sort'
    ascending_or_descending = 'Ascending'

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sorting Algorithms Visualiser")

        self.set_list(lst)

    # work out useful info about list and where to draw blocks and how big to draw them
    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        # set height and width of blocks to represent the numbers
        self.block_width = round((self.width - self.side_pad) - len(self.lst)) / len(self.lst)
        self.block_height = int((self.height - self.top_pad) / (self.max_val - self.min_val))   # will multiply by real value to make block height proportional to value (greater val taller block)

        # co-ordinates of where to start adding blocks and text
        self.start_x = self.side_pad // 2
        self.start_y = self.top_pad // 2


def draw(drawinfo, index, sorting, end=False, custom_colour=None):   # index of the element that is being moved in the sort
    if sorting:
        drawinfo.nodes_visited += 1

    drawinfo.window.fill(drawinfo.background)

    sort_details = drawinfo.LARGE_FONT.render(f"{drawinfo.current_algorithm} - {drawinfo.ascending_or_descending}", 1, drawinfo.green)
    drawinfo.window.blit(sort_details, ((drawinfo.width / 2 - sort_details.get_width() / 2), -5))
    # Writing Text On Screen
    controls = drawinfo.FONT.render("R - Reset | Space - Start Sorting | A - Ascending | D - Descending", 1, drawinfo.text_colour)
    drawinfo.window.blit(controls, ((drawinfo.width / 2 - controls.get_width() / 2), 50))

    sorts = drawinfo.FONT.render("B - Bubble Sort | I - Insertion Sort | S - Selection Sort | M - Merge Sort | Q - Quick Sort | C - Cocktail Shaker Sort", 1, drawinfo.text_colour)
    drawinfo.window.blit(sorts, ((drawinfo.width / 2 - sorts.get_width() / 2), 80))

    sort_stats = drawinfo.SMALL_FONT.render(f"{drawinfo.comparisons} comparisons, {drawinfo.nodes_visited} array accesses, {delay} ms delay", 1, drawinfo.text_colour)
    drawinfo.window.blit(sort_stats, ((drawinfo.width / 2 - sort_stats.get_width() / 2), 110))

    # Calling Func To Draw Blocks

    draw_lst(drawinfo, index, sorting, end, custom_colour)

    pygame.display.update()  # update screen


def draw_lst(drawinfo, index, sorting, end, custom_colour=None):
    if custom_colour is None:
        custom_colour = drawinfo.current_node_colour

    lst = drawinfo.lst

    for i, val in enumerate(lst):
        x = (drawinfo.start_x + i * drawinfo.block_width) + i   # add a + i if you want spaces in between blocks
        y = drawinfo.height - (val - drawinfo.min_val) * drawinfo.block_height

        if end:
            if i <= index:
                colour = drawinfo.end_colour  # make block colour end colour
            else:
                colour = drawinfo.block_colour  # make block colour normal colour

        else:
            if i == index and sorting:    # and sorting because otherwise index 0 would stay red
                colour = custom_colour
            else:
                colour = drawinfo.block_colour

        pygame.draw.rect(drawinfo.window, colour, (x, y, drawinfo.block_width, (drawinfo.block_height * val)))


def generate_list(min_value, max_value, list_size, random_numbers):
    lst = []

    if random_numbers:  # for loop adding x amount of numbers with random values between min and max
        for i in range(list_size):
            if random_numbers:
                lst.append(random.randint(min_value, max_value))
    else:  # if you just want x numbers in range 1-x
        for i in range(list_size):
            lst.append(i)

        # shuffle list so it is random order

        for j in range(len(lst) - 1, 0, -1):
            rand = random.randint(0, j)
            lst[j], lst[rand] = lst[rand], lst[j]



    return lst

"""

    for i in range(len(lst)):
        for j in range(1, len(lst)):
            if lst[i] < lst[j]:
                lst[i], lst[j] == lst[j], lst[i]

"""


def bubble_sort(ascending, index, lst):

    if index > 0:
        if (lst[index] < lst[index - 1] and ascending) or (lst[index] > lst[index - 1] and not ascending):
            lst[index - 1], lst[index] = lst[index], lst[index - 1]

    if delay > 0:
        time.sleep(delay / 1000)

    return lst


def insertion_sort(ascending, index, insertion_index, lst):

    if index > 0:
        if insertion_index > 0:
            if (lst[insertion_index] < lst[insertion_index - 1] and ascending) or (lst[insertion_index] > lst[insertion_index - 1] and not ascending):
                lst[insertion_index], lst[insertion_index - 1] = lst[insertion_index - 1], lst[insertion_index]
                insertion_index -= 1
            else:
                index += 1
                insertion_index = index
        else:
            index += 1
            insertion_index = index

    if delay > 0:
        time.sleep(delay / 1000)

    return lst, index, insertion_index


# Turns out you can use a generator for the sorting algorithms so ive used a generator here instead of having index variables in main loop like i did for bubble and insertion sort
def selection_sort(drawinfo, ascending):
    lst = drawinfo.lst

    for i in range(len(lst)):
        min_or_max = None
        min_or_max_index = None
        for j in range(i, len(lst)):
            if min_or_max is None:
                min_or_max = lst[j]
                min_or_max_index = j

            if (lst[j] < min_or_max and ascending) or (lst[j] > min_or_max and not ascending):
                min_or_max = lst[j]
                min_or_max_index = j

            drawinfo.comparisons += 1
            draw(drawinfo, j, True)
            yield True

        lst[min_or_max_index], lst[i] = lst[i], lst[min_or_max_index]
        draw(drawinfo, i, True, custom_colour=drawinfo.green)  # Because block is in correct place make green or whatever custom colour you want
        yield True

    return lst


# merge sort coded iteratively because drawing it wouldn't work if it was coded recursively (copied from https://www.studytonight.com/python-programs/python-program-for-iterative-merge-sort because I had no clue how to code merge iteratively) I just added the draw() functions into it)
def merge_lists(temp, From, mid, to, drawinfo, ascending):
    S = drawinfo.lst

    a = From
    b = From
    c = mid + 1

    while b <= mid and c <= to:
        if (S[b] < S[c] and ascending) or (S[b] > S[c] and not ascending):
            temp[a] = S[b]
            b = b + 1
        else:
            temp[a] = S[c]
            c = c + 1
        drawinfo.comparisons += 1
        a = a + 1

    # remaining elements
    while b < len(S) and b <= mid:
        temp[a] = S[b]
        a = a + 1
        b = b + 1

    # copy back

    for b in range(From, to + 1):
        S[b] = temp[b]
        draw(drawinfo, b, True)


def merge_sort(drawinfo, ascending):
    S = drawinfo.lst

    low = 0
    high = len(S) - 1

    # sort list
    temp = S.copy()

    d = 1
    while d <= high - low:

        for b in range(low, high, 2 * d):
            From = b
            mid = b + d - 1
            to = min(b + 2 * d - 1, high)
            merge_lists(temp, From, mid, to, drawinfo, ascending)
            yield True

        d = 2 * d

# quicksort


def partition(drawinfo, low, high, ascending):
    array = drawinfo.lst

    i = (low - 1)
    x = array[high]

    for j in range(low, high):
        if (array[j] <= x and ascending) or (array[j] >= x and not ascending):
            i = i + 1
            array[i], array[j] = array[j], array[i]
            drawinfo.comparisons += 1
            draw(drawinfo, i, sorting=True)
        draw(drawinfo, j, sorting=True)


    array[i + 1], array[high] = array[high], array[i + 1]
    draw(drawinfo, i, sorting=True)
    return i + 1


# low  --> Starting index,
# high  --> Ending index
def quick_sort(drawinfo, low, high, ascending):
    #  auxiliary stack
    size = high - low + 1
    stack = [0] * (size)

    top = -1

    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop high and low
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        # sorted array
        p = partition(drawinfo, low, high, ascending)
        yield True

        # push left side to stack
        if p - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

        #  push right side to stack
        if p + 1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high

# Python program for implementation of Cocktail Sort


def cocktail_sort(drawinfo, ascending):
    alist = drawinfo.lst

    upper = len(alist) - 1
    lower = 0

    no_swap = False
    while not no_swap and upper - lower > 1:
        no_swap = True
        for j in range(lower, upper):
            if (alist[j + 1] < alist[j] and ascending) or (alist[j + 1] > alist[j] and not ascending):
                alist[j + 1], alist[j] = alist[j], alist[j + 1]
                no_swap = False
            drawinfo.comparisons += 1
            draw(drawinfo, j, sorting=True)
            yield True
        upper = upper - 1

        for j in range(upper, lower, -1):
            if (alist[j - 1] > alist[j] and ascending) or (alist[j - 1] < alist[j] and not ascending):
                alist[j - 1], alist[j] = alist[j], alist[j - 1]
                no_swap = False
            drawinfo.comparisons += 1
            draw(drawinfo, j, sorting=True)
            yield True
        lower = lower + 1



def main():

    run = True
    clock = pygame.time.Clock()

    lst = generate_list(min_v, max_v, list_size=list_size, random_numbers=use_random_numbers_in_list)   # make random numbers false if you just want 1-len(list) as values instead
    drawinfo = DrawInfo(1600, 1000, lst)   # width of screen and lst

    sorting = False

    bubble = True
    insertion = False
    selection = False
    merge = False
    quick = False
    cocktail = False

    ascending = True   # if this is false sort descending there isn't a need for another variable

    index = 0
    insertion_sort_index = 1
    loop_count = 0  # used for bubble sort because there are two loops

    end = False   # doesn't stop program this refers to the colour animation at the end of sorting

    pre_sorted = sorted(drawinfo.lst)   # just to stop bubble sort from continuing if it has been sorted

    generator = None  # I coded selection sort using a generator because it is simpler to use a generator than to have index variables but I am too lazy to recode bubble and insertion to use a generator

    while run:
        clock.tick(144)

        if sorting:
            if bubble:
                if loop_count < len(lst) and index < len(lst) and lst != pre_sorted:
                    lst = bubble_sort(ascending, index, lst)

                    index += 1
                    if index == len(lst) - loop_count:
                        loop_count += 1
                        index = 0
                    drawinfo.comparisons += 1
                else:
                    sorting = False
                    index = 0
                    loop_count = 0
                    end = True

            if insertion:
                if index < 1:
                    index = 1
                if index < len(lst) and lst != pre_sorted:
                    i = insertion_sort(ascending, index, insertion_sort_index, lst)
                    lst = i[0]
                    index = i[1]
                    insertion_sort_index = i[2]
                    drawinfo.comparisons += 1
                else:
                    sorting = False
                    index = 0
                    insertion_sort_index = 1
                    end = True

            if selection or merge or quick or cocktail:
                if delay > 0:
                    time.sleep(delay / 1000)
                try:
                    next(generator)
                except StopIteration:
                    sorting = False
                    end = True

        if end:
            if index < len(lst):
                draw(drawinfo, index, sorting, end)
                index += 1

            else:
                index = 0
                end = False
        else:
            if insertion:
                draw(drawinfo, insertion_sort_index, sorting)
            elif bubble:
                draw(drawinfo, index, sorting)
            elif (selection or merge or quick or cocktail) and not sorting:   # and not sorting because I have this line written in the generator which runs when sorting
                draw(drawinfo, index, sorting, end)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # code to make x button to end program work
                run = False

            # do a certain thing if a certain key if pressed
            if event.type == pygame.KEYDOWN:
                # reset list
                if event.key == pygame.K_r and not end:
                    drawinfo.nodes_visited, drawinfo.comparisons = 0, 0
                    sorting = False
                    index = 0
                    lst = generate_list(min_v, max_v, list_size, random_numbers=use_random_numbers_in_list)
                    drawinfo.set_list(lst)
                    pre_sorted = sorted(drawinfo.lst)

                    if selection:
                        generator = selection_sort(drawinfo, ascending)
                    elif merge:
                        generator = merge_sort(drawinfo, ascending)
                    elif quick:
                        generator = quick_sort(drawinfo, low=0, high=len(drawinfo.lst)-1, ascending=ascending)
                    elif cocktail:
                        generator = cocktail_sort(drawinfo, ascending)


                # Toggle different sorting algorithms
                elif event.key == pygame.K_SPACE and not sorting and end is False and drawinfo.lst != pre_sorted:
                    sorting = True

                # ascending or descending
                elif event.key == pygame.K_a and not sorting and end is False:
                    ascending = True
                    drawinfo.ascending_or_descending = 'Ascending'
                    if selection:
                        generator = selection_sort(drawinfo, ascending)
                    elif merge:
                        generator = merge_sort(drawinfo, ascending)
                    elif quick:
                        generator = quick_sort(drawinfo, low=0, high=len(drawinfo.lst) - 1, ascending=ascending)
                    elif cocktail:
                        generator = cocktail_sort(drawinfo, ascending)

                elif event.key == pygame.K_d and not sorting and end is False:
                    ascending = False
                    drawinfo.ascending_or_descending = 'Descending'
                    if selection:
                        generator = selection_sort(drawinfo, ascending)
                    elif merge:
                        generator = merge_sort(drawinfo, ascending)
                    elif quick:
                        generator = quick_sort(drawinfo, low=0, high=len(drawinfo.lst) - 1, ascending=ascending)
                    elif cocktail:
                        generator = cocktail_sort(drawinfo, ascending)

                elif event.key == pygame.K_b and not sorting and end is False:
                    quick = False
                    merge = False
                    insertion = False
                    selection = False
                    cocktail = False
                    bubble = True
                    drawinfo.current_algorithm = 'Bubble Sort'

                elif event.key == pygame.K_i and not sorting and end is False:
                    quick = False
                    bubble = False
                    merge = False
                    selection = False
                    cocktail = False
                    insertion = True
                    drawinfo.current_algorithm = 'Insertion Sort'

                elif event.key == pygame.K_s and not sorting and end is False:
                    quick = False
                    bubble = False
                    insertion = False
                    merge = False
                    cocktail = False
                    selection = True
                    generator = selection_sort(drawinfo, ascending)
                    drawinfo.current_algorithm = 'Selection Sort'

                elif event.key == pygame.K_m and not sorting and end is False:
                    quick = False
                    bubble = False
                    selection = False
                    insertion = False
                    cocktail = False
                    merge = True
                    generator = merge_sort(drawinfo, ascending)
                    drawinfo.current_algorithm = 'Merge Sort'

                elif event.key == pygame.K_q and not sorting and end is False:
                    bubble = False
                    selection = False
                    insertion = False
                    merge = False
                    cocktail = False
                    quick = True
                    generator = quick_sort(drawinfo, low=0, high=len(drawinfo.lst)-1, ascending=ascending)
                    drawinfo.current_algorithm = 'Quick Sort'

                elif event.key == pygame.K_c and not sorting and end is False:
                    bubble = False
                    selection = False
                    insertion = False
                    merge = False
                    quick = False
                    cocktail = True
                    generator = cocktail_sort(drawinfo, ascending)
                    drawinfo.current_algorithm = 'Cocktail Shaker Sort'

    pygame.quit()


if __name__ == '__main__':
    main()






