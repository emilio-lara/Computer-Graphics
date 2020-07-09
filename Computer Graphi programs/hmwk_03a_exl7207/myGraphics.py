# Lara, Emilio.
# exl7207
# 2019-03-04

#----------------------------------------------------------------------
# This code was originally created by Prof. Farhad Kamangar.
# It has been significantly modified and updated by Brian A. Dalio for
# use in CSE 4303 / CSE 5365 in the 2019 Spring semester.

#----------------------------------------------------------------------
import CohenSutherland
class cl_world :
  def __init__( self, objects = [], canvases = [] ) :
    self.canvases = canvases


  def add_canvas( self, canvas ) :
    self.canvases.append( canvas )
    canvas.world = self

  def reset( self ) :
    for canvas in self.canvases :
      canvas.delete( 'all' )

  def create_graphic_objects( self, canvas,Tv,faces ) :
    Clip= CohenSutherland
    p1=[400,25]
    p2 =[350,75]
    l1=[50,50]
    l2=[450,50]
    test =Clip.line_intersection((p1,p2), (l1,l2))
    print(test)
    # Define bonderies dimentions
    x_right=float(canvas.cget("width"))*.90
    x_left=float(canvas.cget("width"))*.10
    y_bottom=float(canvas.cget("height"))*.90
    y_top=float(canvas.cget("height"))*.10

    # Creating box
    right_line= canvas.create_line(x_right,y_top,x_right,y_bottom)
    left_line= canvas.create_line(x_left,y_top,x_left,y_bottom)
    top_line = canvas.create_line(x_left,y_top,x_right,y_top)
    bottom_line = canvas.create_line(x_left,y_bottom,x_right,y_bottom)
    
    for f in faces :
      
      x1=Tv[f[0]][0]
      y1=Tv[f[0]][1]
      x2=Tv[f[1]][0]
      y2=Tv[f[1]][1]
      p1=[x1,y1]
      p2=[x2,y2]
      if (y_top <= y1 or y_top <= y2) :# top check    
        if (y_bottom >= y1 or y_bottom >= y2) :# bottom check
          if (x_left <= x1 or x_left <= x2) : # left check
            if (x_right >= x1 or x_right >= x2) : # right check
              v1=canvas.create_line(x1,y1,x2,y2)

      x1=Tv[f[1]][0]
      y1=Tv[f[1]][1]
      x2=Tv[f[2]][0]
      y2=Tv[f[2]][1]
      if (y_top <= y1 or y_top <= y2 ):# top check
        if (y_bottom >= y1 or y_bottom >= y2) :# bottom check
          if (x_left <= x1 or x_left <= x2) :# left check
            if (x_right >= x1 or x_right >= x2) : # right check
              v2=canvas.create_line(x1,y1,x2,y2)

      x1=Tv[f[2]][0]
      y1=Tv[f[2]][1]
      x2=Tv[f[0]][0]
      y2=Tv[f[0]][1]
      if( y_top <= y1 or y_top <= y2 ):# top check
        if (y_bottom >= y1 or y_bottom >= y2) : # bottom check
          if (x_left <= x1 or x_left <= x2) :# left check
            if (x_right >= x1 or x_right >= x2) : # right check
              v3=canvas.create_line(x1,y1,x2,y2)
      



    


#----------------------------------------------------------------------
