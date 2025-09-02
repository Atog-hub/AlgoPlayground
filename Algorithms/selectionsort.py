import pygame as pg
import config as conf
import random

selection_sort_text = [
    "Selection Sort Pseudocode:",
    "",
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


def start_selection_sort():
    global selection_array, selection_i, selection_j, selection_min_idx
    global selection_sort_running, selection_sorted_indices, selection_highlight_indices, selection_scroll_offset

    min_val = 50
    max_val = 400

    # Step between each value for visual balance
    step = (max_val - min_val) // conf.NUM_BARS

    # Create evenly spaced values
    selection_array = [min_val + i * step for i in range(conf.NUM_BARS)]
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
    PSEUDO_AREA_HEIGHT = conf.HEIGHT - PSEUDO_START_Y

    # Calculate animation width and left margin for centering
    animation_width = len(selection_array) * conf.BAR_WIDTH
    left_margin = (conf.WIDTH - animation_width) // 2
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

        x = left_margin + idx * conf.BAR_WIDTH
        y = animation_top + ANIMATION_HEIGHT - bar_height  # bars grow upwards
        pg.draw.rect(conf.SCREEN, color, (x, y, conf.BAR_WIDTH - 2, bar_height))  # small gap between bars

    # Draw pseudocode background area
    pseudo_area_rect = pg.Rect(10, PSEUDO_START_Y, conf.WIDTH - 20, PSEUDO_AREA_HEIGHT)
    pg.draw.rect(conf.SCREEN, (240, 240, 240), pseudo_area_rect)

    # Create a surface for the pseudocode area and fill background
    pseudo_surface = pg.Surface((conf.WIDTH - 20, PSEUDO_AREA_HEIGHT))
    pseudo_surface.fill((240, 240, 240))

    # Draw pseudocode text on pseudo_surface with scroll offset
    y = -selection_scroll_offset  # offset for scrolling text
    line_height = 28
    for line in selection_sort_text:
        if -line_height < y < PSEUDO_AREA_HEIGHT:
            rendered_line = conf.font.render(line, True, (0, 0, 0))
            pseudo_surface.blit(rendered_line, (10, y))
        y += line_height

    # Blit the clipped pseudocode surface onto the main screen
    conf.SCREEN.blit(pseudo_surface, (10, PSEUDO_START_Y))

    # Draw back button
    conf.back_btn.draw(conf.SCREEN)


