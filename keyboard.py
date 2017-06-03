from OpenGL.GL import *
from OpenGL.GLU import *

def draw_black_key(pos_x, pos_y, pos_z):
    """
    Draws a black key
    """
    glColor3f(0.1, 0.1, 0.1)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 15)
    glPushMatrix()

    # Key Dimensions
    len_x = 0.25 + pos_x
    len_y = 0.3 + pos_y
    len_z = 1.7 + pos_z
    offset_z = 0.15
    glBegin(GL_QUADS)

    # Front
    glVertex4d(pos_x, pos_y, pos_z, 1.0)
    glVertex4d(pos_x, len_y, pos_z, 1.0)
    glVertex4d(len_x, len_y, pos_z, 1.0)
    glVertex4d(len_x, pos_y, pos_z, 1.0)

    # Back
    glVertex4d(pos_x, pos_y, len_z, 1.0)
    glVertex4d(pos_x, len_y, len_z - offset_z, 1.0)
    glVertex4d(len_x, len_y, len_z - offset_z, 1.0)
    glVertex4d(len_x, pos_y, len_z, 1.0)

    # Side L
    glVertex4d(pos_x, pos_y, pos_z, 1.0)
    glVertex4d(pos_x, pos_y, len_z, 1.0)
    glVertex4d(pos_x, len_y, len_z - offset_z, 1.0)
    glVertex4d(pos_x, len_y, pos_z, 1.0)

    # Side R
    glVertex4d(len_x, pos_y, pos_z, 1.0)
    glVertex4d(len_x, pos_y, len_z, 1.0)
    glVertex4d(len_x, len_y, len_z - offset_z, 1.0)
    glVertex4d(len_x, len_y, pos_z, 1.0)

    # Bottom
    glVertex4d(pos_x, pos_y, pos_z, 1.0)
    glVertex4d(len_x, pos_y, pos_z, 1.0)
    glVertex4d(len_x, pos_y, len_z, 1.0)
    glVertex4d(pos_x, pos_y, len_z, 1.0)

    # Top
    glVertex4d(pos_x, len_y, pos_z, 1.0)
    glVertex4d(len_x, len_y, pos_z, 1.0)
    glVertex4d(len_x, len_y, len_z - offset_z, 1.0)
    glVertex4d(pos_x, len_y, len_z - offset_z, 1.0)

    glEnd()
    glPopMatrix()

def draw_white_key(pos_x, pos_y, pos_z):
    """
    Draws a white key
    """
    # key dimensions
    len_x = 0.4 + pos_x
    len_y = 0.5 + pos_y
    len_z = 2.5 + pos_z

    glColor3f(0.95, 0.95, 0.95)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 5);
    glPushMatrix()

    glBegin(GL_QUADS)
    # Front
    glVertex4d(pos_x, pos_y, pos_z, 1.0)
    glVertex4d(pos_x, len_y, pos_z, 1.0)
    glVertex4d(len_x, len_y, pos_z, 1.0)
    glVertex4d(len_x, pos_y, pos_z, 1.0)

    # Back
    glVertex4d(pos_x, pos_y, len_z, 1.0)
    glVertex4d(pos_x, len_y, len_z, 1.0)
    glVertex4d(len_x, len_y, len_z, 1.0)
    glVertex4d(len_x, pos_y, len_z, 1.0)

    # Side L
    glVertex4d(pos_x, pos_y, pos_z, 1.0)
    glVertex4d(pos_x, pos_y, len_z, 1.0)
    glVertex4d(pos_x, len_y, len_z, 1.0)
    glVertex4d(pos_x, len_y, pos_z, 1.0)

    # Side R
    glVertex4d(len_x, pos_y, pos_z, 1.0)
    glVertex4d(len_x, pos_y, len_z, 1.0)
    glVertex4d(len_x, len_y, len_z, 1.0)
    glVertex4d(len_x, len_y, pos_z, 1.0)

    # Bottom
    glVertex4d(pos_x, pos_y, pos_z, 1.0)
    glVertex4d(len_x, pos_y, pos_z, 1.0)
    glVertex4d(len_x, pos_y, len_z, 1.0)
    glVertex4d(pos_x, pos_y, len_z, 1.0)

    # Top
    glVertex4d(pos_x, len_y, pos_z, 1.0)
    glVertex4d(len_x, len_y, pos_z, 1.0)
    glVertex4d(len_x, len_y, len_z, 1.0)
    glVertex4d(pos_x, len_y, len_z, 1.0)

    glEnd()
    glPopMatrix()

def draw_keyboard():
    """
    Draws keyboard
    """
    black_offset_large = 0.8
    black_offset_small = 0.45
    num_octaves = 5

    def draw_white_keybed(start_pos):
        """
        Draws white keybed
        """
        for i in range(8):
            draw_white_key(i * 0.42 + start_pos, 0, 0)

    def draw_black_keybed(start_pos):
        """
        Draws black keybed
        """
        draw_black_key(start_pos, 0.5, 0)
        draw_black_key(black_offset_small + start_pos, 0.5, 0)
        draw_black_key(black_offset_small + black_offset_large + start_pos, 0.5, 0)
        draw_black_key(black_offset_small * 2 + black_offset_large + start_pos, 0.5, 0)
        draw_black_key(black_offset_small * 3 + black_offset_large + start_pos, 0.5, 0)

    octave_white = 7 * 0.42
    octave_black = black_offset_small * 3  + black_offset_large * 2

    start_pos_white = octave_white * num_octaves//2
    start_pos_black = octave_black * num_octaves//2

    # draw outlier keys
    draw_white_key(0 - start_pos_white - 0.42 * 2, 0, 0)
    draw_black_key(0.28 - start_pos_white - 0.42 * 2, 0.5, 0)
    draw_white_key(0 - start_pos_white - 0.42, 0, 0)

    for i in range(num_octaves):
        draw_white_keybed(octave_white * i - start_pos_white)
        draw_black_keybed(octave_black * i + 0.28 - start_pos_black)

