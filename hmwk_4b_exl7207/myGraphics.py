# Lara, Emilio.
# exl7207
# 2019-05-2

#----------------------------------------------------------------------
# This code was originally created by Prof. Farhad Kamangar.
# It has been significantly modified and updated by Brian A. Dalio for
# use in CSE 4303 / CSE 5365 in the 2018 Fall semester.

#----------------------------------------------------------------------
from CohenSutherland import clipLine
class cl_world :
  def __init__( self, objects = [], canvases = [] ) :
    self.objects = objects
    self.canvases = canvases

  def add_canvas( self, canvas ) :
    self.canvases.append( canvas )
    canvas.world = self

  def reset( self ) :
    self.objects = []
    for canvas in self.canvases :
      canvas.delete( 'all' )

  def create_graphic_objects( self, canvas, modelData,doClip,perspective,euler,resolution) :
      p = perspective
      e = euler
      patches=[]
      pointList=[]
    
      patches= modelData.getPatches()

      height = int(canvas.cget("height"))
      width = int(canvas.cget("width"))
      w = modelData.getWindow()
      v = modelData.getViewport()
      vxMin = v[0] * width
      vxMax = v[2] * width
      vyMin = v[1] * height
      vyMax = v[3] * height
      portal = (vxMin,vyMin,vxMax,vyMax)
      print(f'Portal       :({vxMin:,.2f},{vyMin:.2f},{vxMax:.2f},{vyMax:.2f})')

      for v1Num,v2Num,v3Num in modelData.getFaces():
        v1 = modelData.getTransformedVertex(v1Num,p,e)
        v2 = modelData.getTransformedVertex(v2Num,p,e)
        v3 = modelData.getTransformedVertex(v3Num,p,e)
        if doClip:
          for (vax,vay,_),(vbx,vby,_) in [(v1,v2),(v2,v3),(v3,v1)]:
            doDraw,vax,vay,vbx,vby = clipLine(vax,vay,vbx,vby,portal)
            if doDraw:
              canvas.create_line(vax,vay,vbx,vby)
        else:
          canvas.create_line(*v1[:-1], *v2[:-1],*v3[:-1],*v1[:-1])



          
      if(len(patches)!=0):
        listPatch=[]
        for patch in patches:
          for vNum in patch:
            Tuple=modelData.getTransformedVertex(vNum,p,e)
            listPatch.append(Tuple);
          pointList=modelData.resolveBézierPatch(listPatch)
          for row in range(0,resolution-1):
            rowStart = row * resolution

            for col in range(0,resolution-1):
              here = rowStart + col
              there = here + resolution

            
              triangleA =(pointList[here], pointList[there], pointList[there+1])
              (v1,v2,v3)=triangleA
              self.drawTriangle( canvas,v1,v2,v3, portal, doClip)
              
              triangleB =(pointList[there+1],pointList[here+1],pointList[here])
              (v1,v2,v3)=triangleB
              self.drawTriangle( canvas,v1,v2,v3, portal, doClip)
                                                   
  def redisplay( self, canvas, event ) :
    pass
  
  def drawTriangle(self, canvas,v1,v2,v3, portal, doClip):
    if doClip:
          for (vax,vay,_),(vbx,vby,_) in [(v1,v2),(v2,v3),(v3,v1)]:
            doDraw,vax,vay,vbx,vby = clipLine(vax,vay,vbx,vby,portal)
            if doDraw:
              canvas.create_line(vax,vay,vbx,vby)
    else:
      canvas.create_line(*v1[:-1], *v2[:-1],*v3[:-1],*v1[:-1])









          

#----------------------------------------------------------------------
