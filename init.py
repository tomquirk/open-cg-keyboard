from keyboard import *
from OpenGL.GLUT import *
from time import *
from math import *

# global storage of various params
hWindow = 0
bFill = 0
bRotation = 1
RotX = 0
RotY = 0
RotZ = 0
CamPhi = 60
CamTheta = 0
CamRange = 15

def InitGL(width, height):
    """
    Initialises the GL scene by enabling various features
    """
    glClearColor(0.37, 0.37, 0.44, 1)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_COLOR_MATERIAL)

    ResizeGLScene(width, height)

def ResizeGLScene(width, height):
    """
    Function for making appropriate adjustments for window resizing
    """

    # prevent a divide-by-zero error if the window is too small
    if height == 0:
        height = 1

    # reset the current viewport and recalculate the perspective transformation
    # for the projection matrix
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
    """
    Draws the scene
    """
    global Theta
    global CamPhi, CamTheta, CamRange
    global LightPhi, LightTheta, LightRange

    # clear the screen and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # reset the matrix stack with the identity matrix
    glLoadIdentity()

    # CAMERA
    r_xz = CamRange*cos(CamPhi*pi/180)
    x = r_xz*sin(CamTheta*pi/180)
    y = CamRange*sin(CamPhi*pi/180)
    z = r_xz*cos(CamTheta*pi/180)

    gluLookAt(x, y, z,
              0, 0, 0,
	          0, 1, 0
             )

    # LIGHTING

    yellow_tinge = GLfloat_3(1, 0.97, 0.91)
    white = GLfloat_3(1, 1, 1)

    glLightfv(GL_LIGHT0, GL_AMBIENT, GLfloat_3(.25, .25, .25))
    glLightfv(GL_LIGHT0, GL_POSITION, GLfloat_3(0, 10, 0))

    glLightfv(GL_LIGHT1, GL_DIFFUSE, yellow_tinge)
    glLightfv(GL_LIGHT1, GL_SPECULAR, white)
    glLightfv(GL_LIGHT1, GL_POSITION, GLfloat_4(-13, 5, 3, 3))

    glLightfv(GL_LIGHT2, GL_DIFFUSE, yellow_tinge)
    glLightfv(GL_LIGHT2, GL_SPECULAR, white)
    glLightfv(GL_LIGHT2, GL_POSITION, GLfloat_4(13, 5, 3, 3))

    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1, 1, 1, 1])
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glEnable(GL_LIGHT2)

    glEnable(GL_LIGHTING)

    # Draw the keyboard
    draw_keyboard()

    glutSwapBuffers()

    sleep(0.01)


def KeyPressed(key, x, y):
    """
    Process a keypress
    """
    global bFill, CamPhi, CamTheta, CamRange, bRotation

    key = ord(key)

    if key == 27:
        glutDestroyWindow(hWindow)
        sys.exit()
    elif key == ord('S') or key == ord('s'):
        CamPhi -= 1
        if CamPhi < -90:
            CamPhi = -90
    elif key == ord('W') or key == ord('w'):
        CamPhi += 1
        if CamPhi > 90:
            CamPhi = 90
    elif key == ord('A') or key == ord('a'):
        CamTheta -= 1
        if CamTheta < 0:
            CamTheta += 360
    elif key == ord('D') or key == ord('d'):
        CamTheta += 1
        if CamTheta > 360:
            CamTheta -= 360
    elif key == ord('E') or key == ord('e'):
        CamRange -= 1
    elif key == ord('Q') or key == ord('q'):
        CamRange += 1
    elif key == ord('F') or key == ord('f'):
        if bFill == 0:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
            bFill = 1
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
            bFill = 0
    elif key == ord('R') or key == ord('r'):
        if bRotation == 0:
            bRotation = 1
        else:
            bRotation = 0
    else:
        return

def main():
    """
    Runs the application
    """
    global hWindow

    # initialise GLUT
    glutInit("")
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE | GLUT_MULTISAMPLE)
    glutInitWindowSize(760, 480)
    glutInitWindowPosition(0, 0)

    hWindow = glutCreateWindow(b"COSC3000: Tom Quirk")

    # setup the display function callback
    glutDisplayFunc(DrawGLScene)

    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ResizeGLScene)
    glutKeyboardFunc(KeyPressed)

    # call our init function
    InitGL(1920, 1080)

    # enter the window's main loop to set things rolling
    glutMainLoop()


# Tell people how to exit, then start the program...
print("Program Controls\n\n\
      Esc - Exit the program\n\
      A-D - Camera: Rotate around object (theta)\n\
      W-S - Camera: Rotate around object (phi)\n\
      Q-E - Camera: Zoom\n\
      F - Toggle Shadding/Wire-frame\n\
      R - Toggle Rotation on/off\n\
      ")

if __name__ == "__main__":
    main()
