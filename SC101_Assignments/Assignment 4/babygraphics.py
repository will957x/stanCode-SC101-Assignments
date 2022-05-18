"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """

    x_coordinate = GRAPH_MARGIN_SIZE + (
            year_index * ((CANVAS_WIDTH - GRAPH_MARGIN_SIZE - GRAPH_MARGIN_SIZE) / (len(YEARS))))
    return int(x_coordinate)


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)  # top horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)  # bottom horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT, width=LINE_WIDTH)  # left vertical line
    canvas.create_line(CANVAS_WIDTH - GRAPH_MARGIN_SIZE, 0, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT,
                       width=LINE_WIDTH)  # right vertical line

    for i in range(len(YEARS)):
        x_coord = get_x_coordinate(CANVAS_WIDTH, i)  # unnecessary but added for conforming to milestone guidelines
        canvas.create_line(x_coord, 0, x_coord, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(TEXT_DX + x_coord, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=str(YEARS[i]), anchor=tkinter.NW)

    # alternative method for getting x coordinate without using get_x_coordinate()
    # canvas_divided = (CANVAS_WIDTH-GRAPH_MARGIN_SIZE-GRAPH_MARGIN_SIZE)/(len(YEARS))
    # name_col = 0
    # for i in range(len(YEARS)):
    #     canvas.create_line(GRAPH_MARGIN_SIZE+(name_col*canvas_divided), GRAPH_MARGIN_SIZE,
    #                        GRAPH_MARGIN_SIZE+(name_col*canvas_divided), CANVAS_HEIGHT, width=LINE_WIDTH)
    #     canvas.create_text(TEXT_DX+GRAPH_MARGIN_SIZE+(name_col*canvas_divided),
    #                        CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=str(YEARS[i]), anchor=tkinter.NW)
    #     name_col += 1

def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #
    canvas_divided = int((CANVAS_WIDTH - GRAPH_MARGIN_SIZE - GRAPH_MARGIN_SIZE) / (len(YEARS)))  # 80
    x1 = GRAPH_MARGIN_SIZE
    y1 = 0
    count = 0
    for i in range(len(lookup_names)):
        if lookup_names[i] in name_data:
            # print(lookup_names[i])  # test to see what returns
            name = lookup_names[i]  #
            # print(name_data[name])  # check to see what name_data contains
            # print(f' length of {name}s rank is {len(name_data[name])}')  # check length
            for year in range(len(YEARS)):
                curr_year = YEARS[year]
                x2 = TEXT_DX + GRAPH_MARGIN_SIZE + (year * canvas_divided)
                if str(curr_year) in name_data[name]:
                    # print(curr_year)  # checking current year
                    graph_prop = int((CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / 1000 * int(
                        name_data[name][str(curr_year)]) + GRAPH_MARGIN_SIZE)  # converts rank to y coordinate
                    canvas.create_text(TEXT_DX + GRAPH_MARGIN_SIZE + (year * canvas_divided), graph_prop,
                                       text=str(name) + " " + str(name_data[name][str(curr_year)]), anchor=tkinter.SW)
                    y2 = graph_prop
                    if count == 0:  # base case for found year
                        y1 = graph_prop
                    count += 1
                if str(curr_year) not in name_data[name]:
                    # print(f'No {year1} is not in {key_list}')
                    canvas.create_text(TEXT_DX + GRAPH_MARGIN_SIZE + (year * canvas_divided),
                                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       text=str(name) + " *", anchor=tkinter.SW)
                    if count == 0:  # base case for no year
                        y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    count += 1
                if count > 1:  # only update x & y on second run and onwards
                    canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=str(COLORS[i]))
                    x1 = x2
                    y1 = y2
            # Reset for next name
            count = 0
            x1 = GRAPH_MARGIN_SIZE
            y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
