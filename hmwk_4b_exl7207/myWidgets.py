# Lara, Emilio.
# exl7207
# 2019-05-02
#----------------------------------------------------------------------
# This code was originally created by Prof. Farhad Kamangar.
# It has been significantly modified and updated by Brian A. Dalio for
# use in CSE 4303 / CSE 5365 in the 2018 Fall semester.

#----------------------------------------------------------------------
import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog
import math

#----------------------------------------------------------------------
from ModelData           import ModelData
from constructTransform  import constructTransform

#----------------------------------------------------------------------
class cl_widgets :
  def __init__( self, ob_root_window, ob_world = [] ) :
    self.ob_root_window = ob_root_window
    self.ob_world = ob_world

    self.m_ModelData = None
    
    
    self.Clip = tk.BooleanVar()
    self.Clip.set(False)

    self.Perspective = tk.BooleanVar()
    self.Perspective.set(False)

    self.Euler = tk.BooleanVar()
    self.Euler.set(False)
    
    self.m_resolution = 4
    self.m_distance = 1.0
    self.m_roll = 0.0
    self.m_pitch = 0.0
    self.m_yaw = 0.0

    self.menu = cl_menu( self )

    self.toolbar = cl_toolbar( self )

    self.statusBar_frame = cl_statusBar_frame( self.ob_root_window )
    self.statusBar_frame.pack( side = tk.BOTTOM, fill = tk.X )
    self.statusBar_frame.set( 'This is the status bar' )

    self.ob_canvas_frame = cl_canvas_frame( self )
    self.ob_world.add_canvas( self.ob_canvas_frame.canvas )

#----------------------------------------------------------------------
class cl_canvas_frame :
  def __init__( self, master ) :
    self.master = master
    self.canvas = tk.Canvas(
      master.ob_root_window, width=1, height=1, bg='teal' )

    self.canvas.pack( expand=tk.YES, fill=tk.BOTH )
    self.canvas.bind( '<Configure>',       self.canvas_resized_callback )
    self.canvas.bind( '<Key>',             self.key_callback )

    self.canvas.bind( '<ButtonPress-1>',   lambda e : self.btn_callback( 'LMB', 'press', e ) )
    self.canvas.bind( '<ButtonRelease-1>', lambda e : self.btn_callback( 'LMB', 'release', e ) )
    self.canvas.bind( '<B1-Motion>',       lambda e : self.btn_callback( 'LMB', 'motion', e ) )
    self.canvas.bind( '<ButtonPress-2>',   lambda e : self.btn_callback( 'MMB', 'press', e ) )
    self.canvas.bind( '<ButtonRelease-2>', lambda e : self.btn_callback( 'MMB', 'release', e ) )
    self.canvas.bind( '<B2-Motion>',       lambda e : self.btn_callback( 'MMB', 'motion', e ) )
    self.canvas.bind( '<ButtonPress-3>',   lambda e : self.btn_callback( 'RMB', 'press', e ) )
    self.canvas.bind( '<ButtonRelease-3>', lambda e : self.btn_callback( 'RMB', 'release', e ) )
    self.canvas.bind( '<B3-Motion>',       lambda e : self.btn_callback( 'RMB', 'motion', e ) )

    self.canvas.bind( '<Up>',              lambda e : self.arrow_callback( 'Up', False, e ) )
    self.canvas.bind( '<Down>',            lambda e : self.arrow_callback( 'Down', False, e ) )
    self.canvas.bind( '<Right>',           lambda e : self.arrow_callback( 'Right', False, e ) )
    self.canvas.bind( '<Left>',            lambda e : self.arrow_callback( 'Left', False, e ) )
    self.canvas.bind( '<Shift-Up>',        lambda e : self.arrow_callback( 'Up', True, e ) )
    self.canvas.bind( '<Shift-Down>',      lambda e : self.arrow_callback( 'Down', True, e ) )
    self.canvas.bind( '<Shift-Right>',     lambda e : self.arrow_callback( 'Right', True, e ) )
    self.canvas.bind( '<Shift-Left>',      lambda e : self.arrow_callback( 'Left', True, e ) )

  def arrow_callback( self, arrow, shift, event ) :
    shiftValue = 'Shift-' if shift else ''
    self.master.statusBar_frame.set( f'{shiftValue}{arrow} arrow pressed.' )

  def btn_callback( self, btn, action, event ) :
    if action == 'press' :
      self.master.statusBar_frame.set( f'{btn} pressed. ({event.x}, {event.y})' )
      self.x = event.x
      self.y = event.y
      self.canvas.focus_set()

    elif action == 'release' :
      self.master.statusBar_frame.set( f'{btn} released. ({event.x}, {event.y})' )
      self.x = None
      self.y = None

    elif action == 'motion' :
      self.master.statusBar_frame.set( f'{btn} dragged. ({event.x}, {event.y})' )
      self.x = event.x
      self.y = event.y

    else :
      self.master.statusBar_frame.set( f'Unknown {btn} action {action}.' )

  def key_callback( self, event ) :
    msg = f'{event.char!r} ({ord( event.char )})' \
      if len( event.char ) > 0 else '<non-printing char>'

    self.master.statusBar_frame.set(
      f'{msg} pressed at ({event.x},{event.y})' )

  def canvas_resized_callback( self, event ) :
    self.canvas.config( width = event.width-4, height = event.height-4 )

    self.master.statusBar_frame.pack( side = tk.BOTTOM, fill = tk.X )
    self.master.statusBar_frame.set(
      f'Canvas width, height ({self.canvas.cget( "width" )}, ' +
      f'{self.canvas.cget( "height" )})' )

    self.canvas.pack()

#----------------------------------------------------------------------
class cl_statusBar_frame( tk.Frame ) :
  def __init__( self, master ) :
    tk.Frame.__init__( self, master )
    self.label = tk.Label( self, bd = 1, relief = tk.SUNKEN, anchor = tk.W )
    self.label.pack( fill = tk.X )

  def set( self, formatStr, *args ) :
    self.label.config( text = 'exl7207: ' + ( formatStr % args ) )
    self.label.update_idletasks()

  def clear( self ) :
    self.label.config( text='' )
    self.label.update_idletasks()

#----------------------------------------------------------------------
class cl_menu :
  def __init__( self, master ) :
    self.master = master
    self.menu = tk.Menu( master.ob_root_window )
    master.ob_root_window.config( menu = self.menu )

    dummy = tk.Menu( self.menu )
    self.menu.add_cascade( label = 'File', menu = dummy )
    dummy.add_command( label = 'New', command = lambda : self.menu_callback( 'file>new' ) )
    dummy.add_command( label = 'Open...', command = lambda : self.menu_callback( 'file>open' ) )
    dummy.add_separator()
    dummy.add_command( label = 'Exit', command = lambda : self.menu_callback( 'file>exit' ) )

    dummy = tk.Menu( self.menu )
    self.menu.add_cascade( label = 'Settings', menu = dummy )
    dummy.add_checkbutton(label ='Clip',variable = self.master.Clip,
                          command = lambda : self.menu_callback( 'Clip on' ))
    dummy.add_checkbutton(label ='Perspective',variable = self.master.Perspective,
                          command = lambda : self.menu_callback( 'Perspective on' ))
    dummy.add_checkbutton(label ='Euler',variable = self.master.Euler,
                          command = lambda : self.menu_callback( 'Euler on' ))

    dummy = tk.Menu( self.menu )
    self.menu.add_cascade( label = 'Help', menu = dummy )
    dummy.add_command( label = 'About...', command = lambda : self.menu_callback( 'help>about' ) )

  def menu_callback( self, which = None ) :
    item = 'menu' if which is None else which
    self.master.statusBar_frame.set( f'{item!r} callback' )

#----------------------------------------------------------------------
class cl_toolbar :
  def __init__( self, master ) :
    self.master = master
    self.toolbar = tk.Frame( master.ob_root_window )

    dummy = tk.Button( self.toolbar, text = 'Resolution', width = 16, command = self.resolution_callback )
    dummy.pack( side = tk.LEFT, padx = 2, pady = 2 )
    
    dummy = tk.Button( self.toolbar, text = 'Distance', width = 16, command = self.distance_callback )
    dummy.pack( side = tk.LEFT, padx = 2, pady = 2 )
    

    dummy = tk.Button( self.toolbar, text = 'φ', width = 8, command = self.Roll_callback )
    dummy.pack( side = tk.LEFT, padx = 2, pady = 2 )

    dummy = tk.Button( self.toolbar, text = 'θ', width = 8, command = self.Pitch_callback )
    dummy.pack( side = tk.LEFT, padx = 2, pady = 2 )

    dummy = tk.Button( self.toolbar, text = 'ψ', width = 8, command = self.Yaw_callback )
    dummy.pack( side = tk.LEFT, padx = 2, pady = 2 )
    
    
    dummy = tk.Button( self.toolbar, text = 'Reset', width = 16, command = self.reset_callback )
    dummy.pack( side = tk.LEFT, padx = 2, pady = 2 )

    dummy = tk.Button( self.toolbar, text = 'Load', width = 16, command = self.load_callback )
    dummy.pack( side = tk.LEFT, padx = 2, pady = 2 )

    dummy = tk.Button( self.toolbar, text = 'Draw', width = 16, command = self.draw_callback )
    dummy.pack( side = tk.LEFT, padx = 2, pady = 2 )

    self.toolbar.pack( side = tk.TOP, fill = tk.X )

  def resolution_callback(self):
    f = simpledialog.askinteger(
      'View Resolution', 'Resolution?',
      initialvalue = self.master.m_resolution, minvalue = 4)
    if f is None:
      msg = f'[Resolution was cancelled, reamins{self.master.m_resolution}]'
    else:
      self.master.m_resolution = f
      msg = f'Resolution is now {f}'
    self.master.statusBar_frame.set(msg)

  def distance_callback(self):
    f = simpledialog.askfloat(
      'View Distance', 'Distance?',
      initialvalue = self.master.m_distance, minvalue = 1.0)
    if f is None:
      msg = f'[Distance was cancelled, reamins{self.master.m_distance}]'
    else:
      self.master.m_distance = f
      msg = f'Distence is now {f}'
    self.master.statusBar_frame.set(msg)
  def Roll_callback(self):
    f = simpledialog.askfloat(
      'View Angle', 'φ?',
      initialvalue = self.master.m_roll, minvalue = 0.0)
    if f is None:
      msg = f'[φ was cancelled, reamins{self.master.m_roll}]'
    else:
      self.master.m_roll = f
      msg = f'φ {f}'
      self.master.statusBar_frame.set(msg)
    
    
  def Pitch_callback(self):
    f = simpledialog.askfloat(
      'View Angle', 'θ?',
      initialvalue = self.master.m_pitch, minvalue = 0.0)
    if f is None:
      msg = f'[θ was cancelled, reamins{self.master.m_roll}]'
    else:
      self.master.m_pitch = f
      msg = f'θ is now {f}'
      self.master.statusBar_frame.set(msg)
  def Yaw_callback(self):
    f = simpledialog.askfloat(
      'View Angle', 'ψ?',
      initialvalue = self.master.m_yaw, minvalue = 0.0)
      
    if f is None:
      msg = f'[ψ was cancelled, reamins{self.master.m_yaw}]'
    else:
      self.master.m_yaw = f
      msg = f'ψ  {f}'
      self.master.statusBar_frame.set(msg)
  
  def reset_callback( self ) :
    self.master.ob_world.reset()
    self.master.statusBar_frame.set( 'Reset callback' )

  def load_callback( self ) :
    fName = tk.filedialog.askopenfilename( filetypes = [ ( "allfiles", "*" ) ] )
    if ( len( fName ) == 0 ) :
        self.master.statusBar_frame.set( "%s", "[Load was cancelled]" )

    else :
      self.master.m_ModelData = ModelData( fName )

      print( f'---Load {fName!r}' )
      print(  'Window line   :', self.master.m_ModelData.getWindow() )
      print(  'Viewport line :', self.master.m_ModelData.getViewport() )
      print(  'Bounding box  :', self.master.m_ModelData.getBoundingBox() )

      self.master.statusBar_frame.set( 'Load callback' )

  def draw_callback( self ) :
    if self.master.m_ModelData is None :
      self.master.statusBar_frame.set( 'No model loaded.' )
      return
    clip       = self.master.Clip.get()==1
    perpective = self.master.Perspective.get()==1
    euler      = self.master.Euler.get()==1
    
    roll       = self.master.m_roll
    pitch      = self.master.m_pitch
    yaw        = self.master.m_yaw
    distance   = self.master.m_distance
    resolution = self.master.m_resolution

    phi   = (roll  * math.pi)/180
    theta = (pitch * math.pi)/180
    psi   = (yaw   * math.pi)/180

    print(phi)
    print(theta)
    print(psi)

    print(resolution)
    
  

    width  = int( self.master.ob_canvas_frame.canvas.cget( "width" ) )
    height = int( self.master.ob_canvas_frame.canvas.cget( "height" ) )


    w = self.master.m_ModelData.getWindow()
    v = self.master.m_ModelData.getViewport()

    ( ax, ay, sx, sy ) = constructTransform( w, v, width, height )
    
    self.master.m_ModelData.specifyEuler(phi,theta,psi)
    self.master.m_ModelData.specifyTransform( ax, ay, sx, sy,distance,resolution)

    print(  '---Draw' )
    print( f'Canvas size   : ({width}, {height})' )
    print( f'Transform     : ax {ax:.3f} ay {ay:.3f} sx {sx:.3f} sy {sy:.3f}' )

    self.master.ob_world.create_graphic_objects( self.master.ob_canvas_frame.canvas,
                                                 self.master.m_ModelData,clip,perpective,euler,resolution)
    
    vxMin = v[0] * width
    vxMax = v[2] * width
    vyMin = v[1] * height
    vyMax = v[3] * height
    self.master.ob_canvas_frame.canvas.create_line(
      vxMin, vyMin, vxMin, vyMax, vxMax, vyMax, vxMax, vyMin, vxMin, vyMin )
    
    r= str(int(resolution))
    d= str(float(distance))
    p=str(float(roll))
    t=str(float(pitch))
    ps=str(float(yaw))
    dg='\u02da'

    self.master.statusBar_frame.set( 'resolution   '+r+',  '+'distance  '+d+',  '+'φ   '+p+dg+'  '+'θ   '+t+dg+'  '+'ψ  '+ps+dg )

#----------------------------------------------------------------------
