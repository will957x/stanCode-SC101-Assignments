"""
File: Draw Line
Name: Will
-------------------------
TODO: Draws Lines
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 50

# Global variables
window = GWindow()
point1 = 0  # stores first click as GOval
point2 = 0  # stores second click as GOval


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(event):
    global point1
    global point2
    if point1 == 0:  # enter if nothing stored in point 1
        point1 = GOval(SIZE / 2, SIZE / 2, x=event.x, y=event.y)
        point1.filled = True
        point1.color = 'black'
        point1.fill_color = 'white'
        window.add(point1, x=event.x - point1.width / 2, y=event.y - point1.height / 2)
        window.remove(point2)
        print("point 1: " + str(point1))
    elif point2 == 0:  # enter if nothing stored in point 2
        point2 = GOval(SIZE / 2, SIZE / 2, x=event.x, y=event.y)
        point2.filled = True
        point2.color = 'black'
        point2.fill_color = 'white'
        window.add(point2, x=event.x - point2.width / 2, y=event.y - point2.height / 2)
        window.remove(point1)
        line = GLine(point1.x + (point1.width) / 2, point1.y + (point1.height) / 2, point2.x + (point2.width) / 2,
                     point2.y + (point2.height) / 2)
        window.add(line)
        window.remove(point2)
        print("point 2: " + str(point2))
        point1 = 0
        point2 = 0


if __name__ == "__main__":
    main()
