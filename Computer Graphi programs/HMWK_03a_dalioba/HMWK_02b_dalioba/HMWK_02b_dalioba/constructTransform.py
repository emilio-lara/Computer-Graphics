# Dalio, Brian A.
# dalioba
# 2019-02-25

#---------#---------#---------#---------#---------#--------#
def constructTransform( w, v, width, height ) :
    ##################################################
    # Put your Python code for computing fx, fy, gx, gy, sx, sy,
    # ax, and ay here.
    #
    # Return ax, ay, sx, and sy as a tuple.
    ##################################################

#---------#---------#---------#---------#---------#--------#
def _main() :
  w      = ( -1.0, -2.0, 4.0, 5.0 )
  v      = ( 0.15, 0.15, 0.85, 0.85 )
  width  = 500
  height = 400

  values = constructTransform( w, v, width, height )
  ax, ay, sx, sy = values

  print( f'Values          : {values}' )
  print( f'Test transform  : ax {ax}, ay {ay}, sx {sx}, sy {sy}' )

#---------#
if __name__ == '__main__' :
  _main()

#---------#---------#---------#---------#---------#--------#