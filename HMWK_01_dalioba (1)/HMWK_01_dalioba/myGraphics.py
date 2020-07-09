# Dalio, Brian A.
# dalioba
# 2019-01-22

#----------------------------------------------------------------------
# This code was originally created by Prof. Farhad Kamangar.
# It has been significantly modified and updated by Brian A. Dalio for
# use in CSE 4303 / CSE 5365 in the 2019 Spring semester.

#----------------------------------------------------------------------
class cl_world :
  def __init__( self, objects = [], canvases = [] ) :
    self.canvases = canvases

  def add_canvas( self, canvas ) :
    self.canvases.append( canvas )
    canvas.world = self

  def reset( self ) :
    for canvas in self.canvases :
      canvas.delete( 'all' )

  def create_graphic_objects( self, canvas ) :
    # 1. Create a line that goes from the upper left to
    #    the lower right of the canvas.
    canvas.create_line(
      0, 0, canvas.cget( 'width' ), canvas.cget( 'height' ) )

    # 2. Create a line that goes from the lower left to
    #    the upper right of the canvas.
    canvas.create_line(
      canvas.cget( 'width' ), 0, 0, canvas.cget( 'height' ) )

    # 3. Create an oval that is centered on the canvas
    #    and is 50% as wide and 50% as high as the canvas.
    canvas.create_oval(
      int( 0.25 * int( canvas.cget( 'width' ) ) ),
      int( 0.25 * int( canvas.cget( 'height' ) ) ),
      int( 0.75 * int( canvas.cget( 'width' ) ) ),
      int( 0.75 * int( canvas.cget( 'height' ) ) ) )

#----------------------------------------------------------------------
