####
#
# simple-shape.py
#
# Author martin.mcbride@axlesoft.com
# Copyright schoolcoders.com 2016
# MIT licence
#
####

from cairobase import save

def draw(ctx):
    #Draw the triangle
    ctx.move_to(0, 0)
    ctx.line_to(5, 1)
    ctx.line_to(3, 3)
    ctx.close_path()

    #Draw the shape
    ctx.stroke()

save(draw, 'simple-shape.png')
