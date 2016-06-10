####
#
# cairobase.py
#
# Author martin.mcbride@axlesoft.com
# Copyright schoolcoders.com 2016
# MIT licence
#
####

import cairo

def save(draw, filename, width=500, height=500, fill=(1, 1, 1),
                scale=25):
    surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context (surface)
    ctx.rectangle(0, 0, width, height)
    ctx.set_source_rgb(*fill)
    ctx.fill()
    ctx.translate(width/2, height/2)
    ctx.scale(scale, -scale)
    xr = width/scale
    yr = height/scale
    ctx.set_source_rgb(.8, .8, 1)
    ctx.set_line_width(.1)
    for n in range(int(-xr/2), int(xr/2)):
        if n:
            ctx.move_to(n, -yr/2)        
            ctx.line_to(n, yr/2)        
            ctx.stroke()
    for n in range(int(-yr/2), int(yr/2)):
        if n:
            ctx.move_to(-xr/2, n)        
            ctx.line_to(xr/2, n)        
            ctx.stroke()
    ctx.set_source_rgb(.4, .4, 1)
    ctx.move_to(0, -yr/2)        
    ctx.line_to(0, yr/2)        
    ctx.stroke()
    ctx.move_to(-xr/2, 0)        
    ctx.line_to(xr/2, 0)        
    ctx.stroke()
    ctx.set_source_rgb(0,0,0)
    ctx.set_line_width(.1)
    draw(ctx)
    surface.write_to_png(filename)

if __name__=='__main__':
    save(lambda x: 0, 'grid.png')
