import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    stack = [ tmp ]
    screen = new_screen()
        
    for command in commands:
        if command == 'line':
            temp = []
            add_edge( points, command[1], commands[2], args[3], args[4], args[5], args[6] )
            matrix_mult( stack[len(stack) - 1], temp )
            draw_lines( temp, screen, color )
        elif command == 'circle':
            temp = []
            add_circle( points, command[1], command[2], 0, command[3], .01 )
            matrix_mult( stack[len(stack) - 1], temp )
            draw_lines( temp, screen, color )
        elif command == 'bezier':
            temp = []
            add_curve( points, command[1], command[2], command[3], command[4], command[5], command[6], command[7], command[8], .01, 'bezier' )
            matrix_mult( stack[len(stack) - 1], temp )
            draw_lines( temp, screen, color )
        elif command == 'hermite':
            temp = []
            add_curve( points, command[1], command[2], command[3], command[4], command[5], command[6], command[7], command[8], .01, 'hermite' )
            matrix_mult( stack[len(stack) - 1], temp )
            draw_lines( temp, screen, color )
        elif command == 'sphere':
            temp = []
            add_sphere( temp, command[1], command[2], 0, command[3], 7 )
            matrix_mult( stack[len(stack) - 1], temp )
            draw_polygons( temp, screen, color )
        elif command == 'torus':
            temp = []
            add_torus(temp, command[1], command[2], 0, command[3], command[4],5)
            matrix_mult( stack[len(stack) - 1], temp )
            draw_polygons( temp, screen, [255, 0 ,0] )
        elif command == 'box':
            temp = []
            add_box( temp, command[1], command[2], command[3], command[4], command[5], command[6])
            matrix_mult( stack[len(stack) - 1], temp )
            draw_polygons( temp, screen, color )
        elif command == 'scale':
            s = make_scale( command[1], command[2], command[3] )
            matrix_mult( s, stack[len(stack) - 1] )
        elif command == 'translate':
            t = make_translate( command[1], command[2], command[3] )
            matrix_mult( t, stack[len(stack) - 1]  )
        elif command == 'display':
            display(screen)
        elif command == 'save':
            save_extension(screen, command[1])
        elif command == 'push':
            stack.append(stack[len(stack) - 1])
        elif command == 'pop':
            stack.pop()
        elif command != '#':
            print 'Invalid command: ' + command
        elif command == 'quit':
            return
        else:
            angle = command[2] * ( math.pi / 180 )
            if command[1] == 'x':
                r = make_rotX( angle )
            elif command[1] == 'y':
                r = make_rotY( angle )
            elif command[1]  == 'z':
                r = make_rotZ( angle )
            matrix_mult( r, stack[len(stack) - 1] )
        


            
