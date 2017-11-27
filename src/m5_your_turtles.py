"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Zewei Xiang.
"""
########################################################################
# done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.delay(20)

a=rg.SimpleTurtle()
b=rg.SimpleTurtle()
a.pen=rg.Pen('red',5)
b.pen=rg.Pen('blue',10)
a.speed = 10
b.speed = 10

for j in range(8):

    for i in range(4):
        a.forward(10)
        a.pen_up()
        a.forward(10)
        a.pen_down()
    a.forward(10)
    a.left(45)

for j in range(16):
    for i in range(2):
        b.forward(20)
        b.pen_up()
        b.forward(20)
        b.pen_down()
    b.forward(10)
    b.right(22.5)


window.close_on_mouse_click()

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
