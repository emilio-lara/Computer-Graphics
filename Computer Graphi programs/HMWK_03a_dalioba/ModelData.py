# Lara, Emilio.
# exl7207
# 2019-03-4

import sys
import constructTransform
class ModelData() :
  def __init__( self, inputFile = None ) :
    self.m_Vertices = []
    self.m_Faces    = []
    self.m_Window   = []
    self.m_Viewport = []

    self.m_minX     = float( '+inf' )
    self.m_maxX     = float( '-inf' )
    self.m_minY     = float( '+inf' )
    self.m_maxY     = float( '-inf' )
    self.m_minZ     = float( '+inf' )
    self.m_maxZ     = float( '-inf' )

    if inputFile is not None :
      # File name was given.  Read the data from the file.
      self.loadFile( inputFile )
  def specifyTransform(self,ax,ay,sx,sy):
    ax,ay,sx,sy = constructTransform.

  def loadFile( self, inputFile ) :
    wcount=0
    scount=0
    
    with open( inputFile, 'r' ) as fp :
      
      lines = fp.read().replace('\r', '' ).split( '\n' )

    for ( index, line ) in enumerate( lines, start = 1 ) :
      line = line.strip()
      if ( line == '' or line[ 0 ] == '#' ) :
        continue

      if ( line[ 0 ] == 'v' ) :
        try :
          ( _, x, y, z ) = line.split()
          x = float( x )
          y = float( y )
          z = float( z )

          self.m_minX = min( self.m_minX, x )
          self.m_maxX = max( self.m_maxX, x )
          self.m_minY = min( self.m_minY, y )
          self.m_maxY = max( self.m_maxY, y )
          self.m_minZ = min( self.m_minZ, z )
          self.m_maxZ = max( self.m_maxZ, z )

          self.m_Vertices.append( ( x, y, z ) )

        except :
          print( 'Line %d is a malformed vertex spec.' % index )

      elif ( line[ 0 ] == 'f' ) :
        try :
          ( _, v1, v2, v3 ) = line.split()
          v1 = int( v1 )-1
          v2 = int( v2 )-1
          v3 = int( v3 )-1
          self.m_Faces.append( ( v1, v2, v3 ) )

        except :
          print( 'Line %d is a malformed face spec.' % index )


      elif (line[0]== 'w') :
        try:
          (_,w1,w2,w3,w4) = line.split()
          w1 = float(w1)
          w2 = float(w2)
          w3 = float(w3)
          w4 = float(w4)
          self.m_Window=((w1,w2,w3,w4))
          wcount +=1

          if(wcount >= 2):
            print('Line %d is a duplicate window spec.' % index)

        except:
          print( 'Line %d is a malformed window spec.' % index )
      elif (line[0]== 's') :
        try:
          (_,s1,s2,s3,s4) = line.split()
          s1 = float(s1)
          s2 = float(s2)
          s3 = float(s3)
          s4 = float(s4)
          self.m_Viewport=((s1,s2,s3,s4))
          scount +=1
          
          if(scount >= 2):
            print('Line %d is a duplicate viewport spec.' % index)

          

        except:
          print( 'Line %d is a malformed viewport spec.' % index )
          
      else :
          print( 'Line %d \'%s\' is unrecognized.' % ( index, line ) )

  def getCenter( self ) :
    return (
      ( self.m_minX + self.m_maxX ) / 2.0,
      ( self.m_minY + self.m_maxY ) / 2.0,
      ( self.m_minZ + self.m_maxZ ) / 2.0 )

  def getFaces( self )    : return self.m_Faces
  def getVertices( self ) : return self.m_Vertices
  def getViewport( self ) : return self.m_Viewport
  def getWindow( self )   : return self.m_Window

#---------#---------#---------#---------#---------#--------#
def _main() :
  # Get the file name to load.
  fName = sys.argv[1]

  # Create a ModelData object to hold the model data from
  # the supplied file name.
  model = ModelData( fName )

  # Now that it's loaded, print out a few statistics about
  # the model data that we just loaded.
  print( f'{fName}: {len( model.getVertices() )} vert%s, {len( model.getFaces() )} face%s' % (
    'ex' if len( model.getVertices() ) == 1 else 'ices',
    '' if len( model.getFaces() ) == 1 else 's' ))

  print( 'First 3 vertices:' )
  for v in model.getVertices()[0:3] :
    print( f'     {v}' )

  print( 'First 3 faces:' )
  for f in model.getFaces()[0:3] :
    print( f'     {f}' )

  print( f'Window line    : {model.getWindow()}' )
  print( f'Viewport line  : {model.getViewport()}' )

  print( f'Center         : {model.getCenter()}' )

#---------#
if __name__ == '__main__' :
  _main()

#---------#---------#---------#---------#---------#--------#
