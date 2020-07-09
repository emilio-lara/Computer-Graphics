# Lara, Emilio.
# exl7207
# 2019-02-14

import sys

class ModelData() :
  def __init__( self, inputFile = None ) :
    self.m_Vertices = []
    self.m_Faces    = []

    if inputFile is not None :
      # File name was given.  Read the data from the file.
      self.loadFile( inputFile )

  def loadFile( self, inputFile ) :
    with open( inputFile, 'r' ) as fp :
      lines = fp.read().replace('\r', '' ).split( '\n' )
    
    for ( index, line ) in enumerate( lines, start = 1 ) :
      line = line.split()
      if(len(line)!=0):
        
        if(line[0]=='v' and len(line)==4): # checking for vertex spec
          internal_list = []
          for item in line[1:]:# for loop will input a new list into self.m_Vertices = []
            
            try :
              floatVar = float( item )
              
              internal_list.append(floatVar)

            except :
              print("Line ",index,"is a malformed vertex spec")
              break
          if(len(internal_list)==3):
            self.m_Vertices.append(internal_list)
          
            
        if(line[0]=='f' and len(line)==4): # checking for faces spec
          internal_list = []
          for item in line[1:]: # for loop will input a new list into self.m_Faces    = []
            try :
              intVar = int( item )-1
              internal_list.append(intVar)

            except :
              print("Line ",index,"is a malformed face spec")
              break
          if(len(internal_list)==3):# internal list is valit with 
            self.m_Faces.append(internal_list)
          
        if(line[0][0]!='#' and line[0] != 'v' and line[0] and line[0] !='f'): # print error of unrecognized values
          print("Line ",index,"'", " ".join(line),"'","unrecognized")
        if(line[0]=='f' and len(line)!=4): # print error of malformed faces
          print("Line ",index,"is a malformed face spec")
        if(line[0]=='v' and len(line)!=4):# print error of malformed vertex
          print("Line ",index,"is a malformed vertex spec")
        
        


  def getFaces( self )    : return self.m_Faces
  def getVertices( self ) : return self.m_Vertices

#model = ModelData()
#model.loadFile("pyramid-centered.txt")



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

#---------#
if __name__ == '__main__' :
  _main()

#---------#---------#---------#---------#---------#--------#

