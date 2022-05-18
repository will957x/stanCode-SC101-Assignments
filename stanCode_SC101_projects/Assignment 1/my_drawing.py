"""
File: My Drawing
Name: Depicts an incomplete Baymax using various campy tools, mainly using GOval & GLine
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine, GArc, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    window = GWindow(width=800, height=1000, title="Drawing1")
    # body
    body = GOval(350, 400, x=200, y=240)
    body.filled = True
    body.fill_color = 'lemonchiffon'
    window.add(body)
    #face
    face = GOval(150, 100, x=300, y=180)
    face.filled = True
    face.fill_color = 'lemonchiffon'
    window.add(face)
    #eyes
    eye1 = GOval(25, 25, x=350, y=200)
    eye2 = GOval(25, 25, x=400, y=200)
    eye_line = GArc(100, 100, 400, 20)
    eye1.filled = True
    eye2.filled = True
    window.add(eye1)
    window.add(eye2)
    window.add(eye_line)
    # blush
    blush1 = GOval(25, 25, x=330, y=225)
    blush2 = GOval(25, 25, x=415, y=225)
    blush1.filled = True
    blush1.fill_color = 'pink'
    blush2.filled = True
    blush2.fill_color = 'pink'
    window.add(blush1)
    window.add(blush2)

if __name__ == '__main__':
    main()
