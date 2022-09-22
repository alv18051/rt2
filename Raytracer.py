from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 1024
height = 1024

# Materiales

snow = Material(diffuse = (0.8, 0.8, 0.8), spec = 16, matType= OPAQUE)
wood = Material(diffuse = (0.5, 0.2, 0), spec = 8, matType= OPAQUE)

mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
mirror2 = Material(diffuse = (0.5, 0.8, 0.9), spec = 64, matType = REFLECTIVE)

water = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.01, matType = TRANSPARENT)
diamond = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 2.45, matType = TRANSPARENT)


rtx = Raytracer(width, height)

rtx.envMap = Texture("map.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1), intensity = 0.8 ))


rtx.scene.append( Sphere(V3(0,0,-10), 1, mirror)  )
rtx.scene.append( Sphere(V3(3,0,-10), 1, mirror2)  )

rtx.scene.append( Sphere(V3(0,3,-10), 1, water)  )
rtx.scene.append( Sphere(V3(4,3,-10), 1, diamond)  )

rtx.scene.append( Sphere(V3(-3,0,-10),1, snow)  )
rtx.scene.append( Sphere(V3(-3,-3,-10), 1, wood)  )


rtx.glRender()

rtx.glFinish("output.bmp")