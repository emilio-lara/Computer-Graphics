# Lara, Emilio.
# exl7207
# 2019-03-04

#---------#---------#---------#---------#---------#--------#
def constructTransform( w, v, width, height ) :
  vxmax = max(v[0],v[2])
  vxmin = min(v[0],v[2])
  vymax = max(v[1],v[3])
  vymin = min(v[1],v[3])

  wxmax = max(w[0],w[2])
  wxmin = min(w[0],w[2])
  wymax = max(w[1],w[3])
  wymin = min(w[1],w[3])

  fx = -(wxmin)
  fy = -(wymin)

  gx = width*vxmin
  gy = height*vymin

  sx =(width*(vxmax-vxmin))/ (wxmax-wxmin)
  sy =(height*(vymax-vymin))/(wymax-wymin)

  ax = fx*sx+gx
  ay = fy*sy+gy

  return(ax,ay,sx,sy)
  

#---------#---------#---------#---------#---------#--------#
def _main() :
  w      = ( -1.0, -2.0, 4.0, 5.0 )
  v      = ( 0.15, 0.15, 0.85, 0.85)
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
