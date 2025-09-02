import pygame as pg
import random
import config as conf



# Merge sort variables and text
merge_array = []
merge_sort_running = False
merge_steps = []
merge_step_index = 0
merge_sorted_indices = []
merge_scroll_offset = 0


merge_sort_text = [
    "Merge Sort Pseudocode:",
    "",
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


def start_merge_sort():
    global merge_array, merge_sort_running, merge_steps, merge_step_index
    global merge_sorted_indices, merge_scroll_offset

    min_val = 50
    max_val = 400

    # Step between each value for visual balance
    step = (max_val - min_val) // conf.NUM_BARS

    # Create evenly spaced values
    merge_array = [min_val + i * step for i in range(conf.NUM_BARS)]
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
    PSEUDO_START_Y = TITLE_HEIGHT + ANIMATION_HEIGHT + 20
    PSEUDO_AREA_HEIGHT = conf.HEIGHT - PSEUDO_START_Y


    # Calculate animation width and left margin for centering (same as insertion sort)
    animation_width = len(merge_array) * conf.BAR_WIDTH
    left_margin = (conf.WIDTH - animation_width) // 2
    animation_top = TITLE_HEIGHT + 65  # same top margin as insertion sort animation (125 - 60)

    max_val = max(merge_array) if merge_array else 1

    for index, val in enumerate(merge_array):
        color = conf.BLUE
        # Color bars green if fully sorted (or in sorted indices)
        if index in merge_sorted_indices:
            color = (0, 200, 0)  # green for sorted bars
        # Optionally you can highlight bars involved in current merge here

        bar_height = int(val / max_val * ANIMATION_HEIGHT)
        x = left_margin + index * conf.BAR_WIDTH
        y = animation_top + ANIMATION_HEIGHT - bar_height
        pg.draw.rect(conf.SCREEN, color, (x, y, conf.BAR_WIDTH - 2, bar_height))  # small gap between bars

    # Draw pseudocode background and text (same style as insertion sort)
    pseudo_surface = pg.Surface((conf.WIDTH, PSEUDO_AREA_HEIGHT))
    pseudo_surface.fill((240, 240, 240))
    for idx, line in enumerate(merge_sort_text):
        y = idx * 28 - merge_scroll_offset
        if 0 <= y < PSEUDO_AREA_HEIGHT:
            rendered = conf.font.render(line, True, (0, 0, 0))
            pseudo_surface.blit(rendered, (20, y))
    conf.SCREEN.blit(pseudo_surface, (0, PSEUDO_START_Y))

    # Draw back button
    conf.back_btn.draw(conf.SCREEN)



