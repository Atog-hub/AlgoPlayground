import sys
import pygame as pg
import random
from button import Button
from config import back_btn
import bubblesort as bs

pg.init()

icon = pg.image.load("icon.png")
pg.display.set_icon(icon)

# -------- Constants --------
WIDTH, HEIGHT = 1024, 576
TITLE_TEXT_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 120, 215)
BLUE_HOVER = (0, 100, 180)
RED = (255, 0, 0)
RED_HOVER = (200, 0, 0)

scroll_offset = 0
NUM_BARS = 50
min_height = 50
max_height = int(HEIGHT * 0.6)
BAR_WIDTH = HEIGHT // NUM_BARS
PSEUDO_TOP_OFFSET = 60 + 250 + 20

# -------- Setup --------
SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("AlgoPlayground")

title_font = pg.font.SysFont("Arial", 50)
font = pg.font.SysFont("Arial", 24)


# -------- Globals --------
current_screen = "menu"
values = []




# Bubble sort animation state and text



















#Linear search variable and text
# Add these globals near your constants
linear_num_bars = 50
linear_scroll_offset = 0
linear_search_running = False
linear_found_index = -1
linear_current_index = 0
linear_bar_width = 0  # will set in draw function or start function



linear_array = []
linear_num_bars = 50
linear_bar_width = WIDTH // linear_num_bars
linear_target = None
linear_current_index = 0
linear_search_running = False
linear_found_index = -1
linear_scroll_offset = 0

linear_search_text = [
    "Linear Search Pseudocode:",
    "",
    "for i in range(len(array)):",
    "    if array[i] == target:",
    "        return i",
    "return -1",
    "",
    "Explanation:",
    "- Checks each element one by one.",
    "- Stops when target is found or end is reached.",
]












# Insertion sort variables and text
insertion_i = 1
insertion_j = 0
insertion_key = None
insertion_sort_running = False
insertion_scroll_offset = 0


insertion_sort_text = [
    "Insertion Sort Pseudocode:",
    "",
    "for i from 1 to n-1:",
    "    key = A[i]",
    "    j = i - 1",
    "    while j >= 0 and A[j] > key:",
    "        A[j + 1] = A[j]",
    "        j = j - 1",
    "    A[j + 1] = key",
    "",
    "Explanation:",
    "- Starts from the second element, assuming the first is sorted.",
    "- Picks the 'key' element to insert into the sorted part.",
    "- Shifts elements greater than 'key' one position to the right.",
    "- Inserts the 'key' into its correct position.",
    "- Repeats until the entire list is sorted."
]



# Selection sort variables and text
selection_array = []
selection_i = 0
selection_j = 0
selection_min_idx = 0
selection_sort_running = False
selection_sorted_indices = []
selection_highlight_indices = []
selection_scroll_offset = 0

selection_sort_text = [
    "for i from 0 to n - 1:",
    "    min_index = i",
    "    for j from i+1 to n:",
    "        if array[j] < array[min_index]:",
    "            min_index = j",
    "    swap array[i] with array[min_index]",
    "",
    "Explanation:",
    "Selection Sort divides the list into a sorted and an unsorted part.",
    "It repeatedly selects the smallest element from the unsorted part",
    "and moves it to the sorted part by swapping.",
]

# Merge sort variables and text
merge_array = []
merge_sort_running = False
merge_steps = []
merge_step_index = 0
merge_sorted_indices = []
merge_scroll_offset = 0


merge_sort_text = [
    "function mergeSort(arr):",
    "    if length of arr <= 1:",
    "        return arr",
    "    mid = len(arr) // 2",
    "    left = mergeSort(arr[:mid])",
    "    right = mergeSort(arr[mid:])",
    "    return merge(left, right)",
    "",
    "function merge(left, right):",
    "    result = []",
    "    while left and right:",
    "        if left[0] <= right[0]:",
    "            result.append(left[0])",
    "            left = left[1:]",
    "        else:",
    "            result.append(right[0])",
    "            right = right[1:]",
    "    return result + left + right",
    "",
    "--- Explanation ---",
    "Merge Sort is a divide-and-conquer algorithm.",
    "1. It splits the array into halves until each subarray",
    "   contains one element (base case).",
    "2. It then merges these sorted subarrays back together",
    "   in order, creating a fully sorted array.",
    "The merging process compares elements from each half",
    "   and builds a new sorted list.",
    "Time Complexity: O(n log n) in all cases.",
    "Space Complexity: O(n) due to auxiliary arrays."
]






# -------- Functions --------

def show_welcome_screen():
    SCREEN.fill(WHITE)
    splash = pg.image.load("lightmode_logo.png").convert_alpha()
    splash = pg.transform.smoothscale(splash, (600, 600))
    splash_rect = splash.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    SCREEN.blit(splash, splash_rect)
    pg.display.update()
    pg.time.delay(1500)
    SCREEN.fill(WHITE)
    pg.display.update()

def handle_scroll(event, text_lines, top_offset):
    global scroll_offset
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 4:
            scroll_offset = max(scroll_offset - 20,0)
        elif event.button == 5:
            max_scroll = max(0,len(text_lines) * 28 - (HEIGHT - top_offset))
            scroll_offset = min(scroll_offset + 20, max_scroll)
    return scroll_offset


def reset_values():
    global values
    step = (max_height - min_height) // NUM_BARS
    values = [min_height + (i * step) for i in range(NUM_BARS)]
    random.shuffle(values)






def start_linear_search():
    global linear_array, linear_target, linear_current_index, linear_search_running, linear_found_index

    min_val = 50
    max_val = 400
    step = (max_val - min_val) // linear_num_bars
    linear_array = [min_val + i * step for i in range(linear_num_bars)]
    random.shuffle(linear_array)

    linear_target = random.choice(linear_array)
    linear_current_index = 0
    linear_search_running = True
    linear_found_index = -1

def update_linear_search():
    global linear_current_index, linear_search_running, linear_found_index

    if linear_search_running:
        if linear_current_index < len(linear_array):
            if linear_array[linear_current_index] == linear_target:
                linear_found_index = linear_current_index
                linear_search_running = False
            else:
                linear_current_index += 1
        else:
            linear_search_running = False

def draw_linear_search():
    global linear_scroll_offset
    global linear_bar_width  # so we can calculate it dynamically

    TITLE_HEIGHT = 60
    ANIMATION_HEIGHT = 250
    PSEUDO_START_Y = TITLE_HEIGHT + ANIMATION_HEIGHT + 20
    PSEUDO_AREA_HEIGHT = HEIGHT - PSEUDO_START_Y

    SCREEN.fill(WHITE)

    title_surface = title_font.render("Linear Search", True, TITLE_TEXT_COLOR)
    SCREEN.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, 10))

    padding = 100
    available_width = WIDTH - 2 * padding
    linear_bar_width = available_width // linear_num_bars
    left_margin = padding
    animation_top = 100

    max_val = max(linear_array) if linear_array else 1
    for idx, val in enumerate(linear_array):
        bar_height = int(val / max_val * ANIMATION_HEIGHT)
        x = left_margin + idx * linear_bar_width
        y = animation_top + ANIMATION_HEIGHT - bar_height

        color = BLUE
        if idx == linear_current_index and linear_search_running:
            color = (255, 165, 0)  # orange for current check
        elif idx == linear_found_index:
            color = (0, 255, 0)  # green if found
        pg.draw.rect(SCREEN, color, (x, y, linear_bar_width - 2, bar_height))

    # Show target value
    target_text = font.render(f"Target Value: {linear_target}", True, (0, 0, 0))
    SCREEN.blit(target_text, (10, TITLE_HEIGHT))

    # Draw pseudocode area
    pseudo_surface = pg.Surface((WIDTH, PSEUDO_AREA_HEIGHT))
    pseudo_surface.fill((240, 240, 240))

    linear_search_text = [
        "Linear Search Pseudocode:",
        "",
        "for i from 0 to n-1:",
        "    if array[i] == target:",
        "        return i",
        "return -1",
        "",
        "Explanation:",
        "- Iterate through the list one by one.",
        "- Compare each element with the target value.",
        "- Stop when the target is found or end is reached.",
    ]

    line_height = 28
    for idx, line in enumerate(linear_search_text):
        y = idx * line_height - linear_scroll_offset
        if -line_height < y < PSEUDO_AREA_HEIGHT:
            rendered = font.render(line, True, (0, 0, 0))
            pseudo_surface.blit(rendered, (20, y))

    SCREEN.blit(pseudo_surface, (0, PSEUDO_START_Y))

    # Draw back button
    back_btn.draw(SCREEN)



def start_merge_sort():
    global merge_array, merge_sort_running, merge_steps, merge_step_index
    global merge_sorted_indices, merge_scroll_offset

    min_val = 50
    max_val = 400

    # Step between each value for visual balance
    step = (max_val - min_val) // NUM_BARS

    # Create evenly spaced values
    merge_array = [min_val + i * step for i in range(NUM_BARS)]
    random.shuffle(merge_array)

    merge_sort_running = True
    merge_step_index = 0
    merge_sorted_indices = []
    merge_scroll_offset = 0

    merge_steps = []
    temp = list(merge_array)
    merge_sort_recursive(temp, 0, len(temp) - 1)


def merge_sort_recursive(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort_recursive(arr, left, mid)
    merge_sort_recursive(arr, mid + 1, right)
    merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    global merge_steps

    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            merge_steps.append((k, list(arr)))
            i += 1
        else:
            arr[k] = right_part[j]
            merge_steps.append((k, list(arr)))
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        merge_steps.append((k, list(arr)))
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        merge_steps.append((k, list(arr)))
        j += 1
        k += 1


def update_merge_sort():
    global merge_array, merge_sort_running, merge_step_index, merge_steps, merge_sorted_indices

    if merge_sort_running and merge_step_index < len(merge_steps):
        idx, snapshot = merge_steps[merge_step_index]
        merge_array = snapshot
        merge_sorted_indices = list(range(idx + 1))
        merge_step_index += 1
    elif merge_sort_running:
        merge_sort_running = False
        merge_sorted_indices = list(range(len(merge_array)))


def draw_merge_sort():
    TITLE_HEIGHT = 60
    ANIMATION_HEIGHT = 250
    PSEUDO_START_Y = TITLE_HEIGHT + ANIMATION_HEIGHT + 10
    PSEUDO_AREA_HEIGHT = HEIGHT - PSEUDO_START_Y

    SCREEN.fill(WHITE)

    # Title
    title_surface = title_font.render("Merge Sort", True, TITLE_TEXT_COLOR)
    SCREEN.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, 10))

    # Bars
    BAR_WIDTH = WIDTH // NUM_BARS
    animation_width = NUM_BARS * BAR_WIDTH
    left_margin = (WIDTH - animation_width) // 2
    animation_top = TITLE_HEIGHT

    max_val = max(merge_array) if merge_array else 1
    for idx, val in enumerate(merge_array):
        bar_height = int(val / max_val * ANIMATION_HEIGHT)
        x = left_margin + idx * BAR_WIDTH
        y = animation_top + ANIMATION_HEIGHT - bar_height
        color = (0, 255, 0) if idx in merge_sorted_indices else (0, 120, 215)
        pg.draw.rect(SCREEN, color, (x, y, BAR_WIDTH - 2, bar_height))

    # Pseudocode Area
    pseudo_area_rect = pg.Rect(10, PSEUDO_START_Y, WIDTH - 20, PSEUDO_AREA_HEIGHT)
    pg.draw.rect(SCREEN, (240, 240, 240), pseudo_area_rect)

    y = PSEUDO_START_Y - merge_scroll_offset
    line_height = 28
    for line in merge_sort_text:
        line_surface = font.render(line, True, (0, 0, 0))
        SCREEN.blit(line_surface, (20, y))
        y += line_height

    back_btn.draw(SCREEN)



def start_selection_sort():
    global selection_array, selection_i, selection_j, selection_min_idx
    global selection_sort_running, selection_sorted_indices, selection_highlight_indices, selection_scroll_offset

    min_val = 50
    max_val = 400

    # Step between each value for visual balance
    step = (max_val - min_val) // NUM_BARS

    # Create evenly spaced values
    selection_array = [min_val + i * step for i in range(NUM_BARS)]
    random.shuffle(selection_array)

    selection_i = 0
    selection_j = 1
    selection_min_idx = 0
    selection_sort_running = True
    selection_sorted_indices = []
    selection_highlight_indices = []
    selection_scroll_offset = 0



def update_selection_sort():
    global selection_array, selection_i, selection_j, selection_min_idx
    global selection_sort_running, selection_sorted_indices, selection_highlight_indices, selection_scroll_offset

    if selection_i < len(selection_array) - 1:
        if selection_j < len(selection_array):
            selection_highlight_indices = [selection_i,selection_j,selection_min_idx]

            if selection_array[selection_j] < selection_array[selection_min_idx]:
                selection_min_idx = selection_j

            selection_j += 1
        else:

            selection_array[selection_i], selection_array[selection_min_idx] = selection_array[selection_min_idx], selection_array[selection_i]
            selection_sorted_indices.append(selection_i)

            selection_i += 1
            selection_j = selection_i + 1
            selection_min_idx = selection_i

    else:
        selection_sort_running = False
        selection_sorted_indices = list(range(len(selection_array)))
        selection_highlight_indices = []


def draw_selection_sort():
    TITLE_HEIGHT = 60
    ANIMATION_HEIGHT = 225
    PSEUDO_START_Y = TITLE_HEIGHT + ANIMATION_HEIGHT
    PSEUDO_AREA_HEIGHT = HEIGHT - PSEUDO_START_Y

    # Calculate animation width and left margin for centering
    animation_width = len(selection_array) * BAR_WIDTH
    left_margin = (WIDTH - animation_width) // 2
    animation_top = TITLE_HEIGHT  # start right below the title

    max_val = max(selection_array) if selection_array else 1

    # Draw bars for selection sort animation
    for idx, val in enumerate(selection_array):
        bar_height = int(val / max_val * ANIMATION_HEIGHT) - 20
        if idx in selection_sorted_indices:
            color = (0, 255, 0)  # green for sorted bars
        elif idx in selection_highlight_indices:
            color = (255, 0, 0)  # red for currently highlighted bars (min/current)
        else:
            color = (0, 120, 215)  # default blue

        x = left_margin + idx * BAR_WIDTH
        y = animation_top + ANIMATION_HEIGHT - bar_height  # bars grow upwards
        pg.draw.rect(SCREEN, color, (x, y, BAR_WIDTH - 2, bar_height))  # small gap between bars

    # Draw pseudocode background area
    pseudo_area_rect = pg.Rect(10, PSEUDO_START_Y, WIDTH - 20, PSEUDO_AREA_HEIGHT)
    pg.draw.rect(SCREEN, (240, 240, 240), pseudo_area_rect)

    # Create a surface for the pseudocode area and fill background
    pseudo_surface = pg.Surface((WIDTH - 20, PSEUDO_AREA_HEIGHT))
    pseudo_surface.fill((240, 240, 240))

    # Draw pseudocode text on pseudo_surface with scroll offset
    y = -selection_scroll_offset  # offset for scrolling text
    line_height = 28
    for line in selection_sort_text:
        if -line_height < y < PSEUDO_AREA_HEIGHT:
            rendered_line = font.render(line, True, (0, 0, 0))
            pseudo_surface.blit(rendered_line, (10, y))
        y += line_height

    # Blit the clipped pseudocode surface onto the main screen
    SCREEN.blit(pseudo_surface, (10, PSEUDO_START_Y))

    # Draw back button
    back_btn.draw(SCREEN)





def start_insertion_sort():
    reset_values()
    global insertion_i, insertion_j, insertion_key, insertion_sort_running, scroll_offset
    insertion_i = 1
    insertion_j = 0
    insertion_key = None
    insertion_sort_running = True  # Changed to True to start animation
    scroll_offset = 0
    insertion_key = values[insertion_i]  # Initialize the key at start
    insertion_j = insertion_i - 1

def update_insertion_sort():
    global insertion_i, insertion_j, insertion_key, insertion_sort_running

    if insertion_i < len(values):
        if insertion_j >= 0 and values[insertion_j] > insertion_key:
            values[insertion_j + 1] = values[insertion_j]
            insertion_j -= 1
        else:
            values[insertion_j + 1] = insertion_key
            insertion_i += 1  # Increment by 1, not by insertion_key
            if insertion_i < len(values):
                insertion_key = values[insertion_i]
                insertion_j = insertion_i - 1
            else:
                insertion_sort_running = False
    else:
        insertion_sort_running = False

def draw_insertion_sort():
    TITLE_HEIGHT = 60
    ANIMATION_HEIGHT = 250
    PSEUDO_START_Y = TITLE_HEIGHT + ANIMATION_HEIGHT + 20
    PSEUDO_AREA_HEIGHT = HEIGHT - PSEUDO_START_Y

    # Draw bars
    animation_width = len(values) * BAR_WIDTH
    left_margin = (WIDTH - animation_width) // 2
    animation_top = 125

    for index, val in enumerate(values):
        color = BLUE
        if insertion_sort_running:
            if index == insertion_i:
                color = (255, 0, 0)  # red for current key
            elif index == insertion_j:
                color = (0, 255,255 )  # orange for comparison
        elif not insertion_sort_running:
            color = (0, 200, 0)  # green when sorted

        x = left_margin + index * BAR_WIDTH
        y = animation_top + ANIMATION_HEIGHT - val
        pg.draw.rect(SCREEN, color, (x, y, BAR_WIDTH, val))

    # Draw pseudocode area
    pseudo_surface = pg.Surface((WIDTH, PSEUDO_AREA_HEIGHT))
    pseudo_surface.fill((240, 240, 240))
    for idx, line in enumerate(insertion_sort_text):
        y = idx * 28 - insertion_scroll_offset
        if 0 <= y < PSEUDO_AREA_HEIGHT:
            rendered = font.render(line, True, (0, 0, 0))
            pseudo_surface.blit(rendered, (20, y))
    SCREEN.blit(pseudo_surface, (0, PSEUDO_START_Y))

    # Draw back button
    back_btn.draw(SCREEN)




def draw_merge_sort():
    TITLE_HEIGHT = 60
    ANIMATION_HEIGHT = 250
    PSEUDO_START_Y = TITLE_HEIGHT + ANIMATION_HEIGHT + 20
    PSEUDO_AREA_HEIGHT = HEIGHT - PSEUDO_START_Y


    # Calculate animation width and left margin for centering (same as insertion sort)
    animation_width = len(merge_array) * BAR_WIDTH
    left_margin = (WIDTH - animation_width) // 2
    animation_top = TITLE_HEIGHT + 65  # same top margin as insertion sort animation (125 - 60)

    max_val = max(merge_array) if merge_array else 1

    for index, val in enumerate(merge_array):
        color = BLUE
        # Color bars green if fully sorted (or in sorted indices)
        if index in merge_sorted_indices:
            color = (0, 200, 0)  # green for sorted bars
        # Optionally you can highlight bars involved in current merge here

        bar_height = int(val / max_val * ANIMATION_HEIGHT)
        x = left_margin + index * BAR_WIDTH
        y = animation_top + ANIMATION_HEIGHT - bar_height
        pg.draw.rect(SCREEN, color, (x, y, BAR_WIDTH - 2, bar_height))  # small gap between bars

    # Draw pseudocode background and text (same style as insertion sort)
    pseudo_surface = pg.Surface((WIDTH, PSEUDO_AREA_HEIGHT))
    pseudo_surface.fill((240, 240, 240))
    for idx, line in enumerate(merge_sort_text):
        y = idx * 28 - merge_scroll_offset
        if 0 <= y < PSEUDO_AREA_HEIGHT:
            rendered = font.render(line, True, (0, 0, 0))
            pseudo_surface.blit(rendered, (20, y))
    SCREEN.blit(pseudo_surface, (0, PSEUDO_START_Y))

    # Draw back button
    back_btn.draw(SCREEN)





#binary search variables and text

def handle_back_button_events(event):
    global current_screen, bubble_sort_running
    if event.type == pg.MOUSEBUTTONDOWN:
        if back_btn.rect.collidepoint(event.pos):
            current_screen = "menu"
            bubble_sort_running = False

def draw_menu():
    SCREEN.fill(WHITE)
    title_surface = title_font.render("Algorithms", True, TITLE_TEXT_COLOR)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, 60))
    SCREEN.blit(title_surface, title_rect)

    for btn in buttons:
        btn.draw(SCREEN)

# -------- Button actions --------

def bubble_sort():
    global current_screen
    current_screen = "bubble sort"
    bs.start_bubble_sort()

#-----INSERTION SORT-------
def insertion_sort():
    global current_screen
    current_screen = "insertion sort"
    start_insertion_sort()  # Initialize insertion sort variables here



#------SELECTION SORT-----
def selection_sort():
    global current_screen
    current_screen = "selection sort"
    start_selection_sort()


def merge_sort():
    global current_screen
    current_screen = "merge sort"
    start_merge_sort()


def linear_search():
    global current_screen
    current_screen = "linear search"
    start_linear_search()  # Initialize the linear search array and variables


def binary_search():
    global current_screen
    current_screen = "binary search"
    SCREEN.fill(WHITE)
    title_surface = title_font.render("Binary Search", True, TITLE_TEXT_COLOR)
    SCREEN.blit(title_surface, title_surface.get_rect(center=(WIDTH // 2, 60)))
    pg.display.update()

def quit():
    pg.quit()
    sys.exit()

# -------- Buttons --------



bubble_btn = Button(
    text="Bubble Sort",
    x=(WIDTH - 300) // 2,
    y=150,
    width=300,
    height=50,
    color=BLUE,
    hover_color=BLUE_HOVER,
    action=bubble_sort,
)

insertion_btn = Button(
    text="Insertion Sort",
    x=(WIDTH - 300) // 2,
    y=210,
    width=300,
    height=50,
    color=BLUE,
    hover_color=BLUE_HOVER,
    action=insertion_sort,
)

selection_btn = Button(
    text="Selection Sort",
    x=(WIDTH - 300) // 2,
    y=270,
    width=300,
    height=50,
    color=BLUE,
    hover_color=BLUE_HOVER,
    action=selection_sort,
)

merge_btn = Button(
    text="Merge Sort",
    x=(WIDTH - 300) // 2,
    y=330,
    width=300,
    height=50,
    color=BLUE,
    hover_color=BLUE_HOVER,
    action=merge_sort,
)

linear_btn = Button(
    text="Linear Search",
    x=(WIDTH - 300) // 2,
    y=390,
    width=300,
    height=50,
    color=BLUE,
    hover_color=BLUE_HOVER,
    action=linear_search,
)

binary_btn = Button(
    text="Binary Search",
    x=(WIDTH - 300) // 2,
    y=450,
    width=300,
    height=50,
    color=BLUE,
    hover_color=BLUE_HOVER,
    action=binary_search,
)

quit_btn = Button(
    text="Quit",
    x=(WIDTH - 300) // 2,
    y=510,
    width=300,
    height=50,
    color=RED,
    hover_color=RED_HOVER,
    action=quit,
)

buttons = [
    bubble_btn,
    insertion_btn,
    selection_btn,
    merge_btn,
    linear_btn,
    binary_btn,
    quit_btn,
]

# -------- Main Loop --------
show_welcome_screen()



clock = pg.time.Clock()
running = True
while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

        # Handle back button clicks on sorting screens
        if current_screen != "menu":
            handle_back_button_events(event)

        # Handle main menu buttons only if on menu
        if current_screen == "menu":
            for btn in buttons:
                btn.handle_event(event)

        # Bubble sort scroll
        if current_screen == "bubble sort":
            bs.scroll_offset = handle_scroll(event,bs.bubble_sort_text, 330)

        # Insertion sort scroll
        elif current_screen == "insertion sort":
            insertion_scroll_offset = handle_scroll(event, insertion_sort_text, 250)

        elif current_screen == "selection sort":
            selection_scroll_offset = handle_scroll(event,selection_sort_text,330)

        elif current_screen == "merge sort":
            merge_scroll_offset = handle_scroll(event, merge_sort_text, 330)

        elif current_screen == "linear search":
            linear_scroll_offset = handle_scroll(event, linear_search_text, 330)

    # Screen rendering
    if current_screen == "menu":
        draw_menu()
    else:
        SCREEN.fill(WHITE)
        # Draw title at the top center for every screen except menu
        title_surface = title_font.render(current_screen.replace("-", " ").title(), True, TITLE_TEXT_COLOR)
        title_rect = title_surface.get_rect(midtop=(WIDTH // 2, 10))
        SCREEN.blit(title_surface, title_rect)

        if current_screen == "bubble sort":
            if bs.bubble_sort_running:
                bs.update_bubble_sort()
            bs.draw_bubble_sort()
        elif current_screen == "insertion sort":
            if insertion_sort_running:
                update_insertion_sort()
            draw_insertion_sort()

        elif current_screen == "selection sort":
            if selection_sort_running:
                update_selection_sort()
            draw_selection_sort()

        elif current_screen == "merge sort":
            if merge_sort_running:
                update_merge_sort()
            draw_merge_sort()

        elif current_screen == "linear search":
            if linear_search_running:
                update_linear_search()
            draw_linear_search()

        else:
            # Placeholder for other sorting screens
            back_btn.draw(SCREEN)
        back_btn.draw(SCREEN)
    pg.display.update()
    clock.tick(60)

pg.quit()
sys.exit()
