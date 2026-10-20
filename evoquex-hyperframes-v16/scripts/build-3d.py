import bpy, math
from pathlib import Path
from mathutils import Vector

ROOT=Path(__file__).resolve().parent.parent
(ROOT/'assets/3d').mkdir(parents=True,exist_ok=True)
(ROOT/'resources').mkdir(parents=True,exist_ok=True)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
scene=bpy.context.scene
scene.render.engine='BLENDER_EEVEE_NEXT'
scene.render.resolution_x=480
scene.render.resolution_y=854
scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG'
scene.render.filepath=str(ROOT/'assets/3d/frame-')
scene.render.film_transparent=False
scene.world.use_nodes=True
scene.world.node_tree.nodes['Background'].inputs['Color'].default_value=(.005,.012,.029,1)
scene.world.node_tree.nodes['Background'].inputs['Strength'].default_value=.4
scene.eevee.taa_render_samples=8
scene.view_settings.view_transform='Standard'
scene.render.film_transparent=False
scene.render.image_settings.color_mode='RGBA'

def mat(name,color,metal=0,rough=.35,emission=None):
 m=bpy.data.materials.new(name);m.diffuse_color=(*color,1);m.use_nodes=True
 bs=m.node_tree.nodes.get('Principled BSDF');bs.inputs['Base Color'].default_value=(*color,1);bs.inputs['Metallic'].default_value=metal;bs.inputs['Roughness'].default_value=rough
 if emission:
  bs.inputs['Emission Color'].default_value=(*emission,1);bs.inputs['Emission Strength'].default_value=1.4
 return m
dark=mat('black titanium',(.018,.027,.048),.72,.23)
steel=mat('silver edge',(.34,.46,.65),.78,.19)
blue=mat('electric blue',(.025,.35,.95),.4,.2,(.04,.38,1))
cyan=mat('neon cyan',(.11,.76,1),.25,.24,(.04,.62,1))
white=mat('soft white',(.8,.9,1),.15,.25,(.25,.45,.8))
back=mat('background',(.015,.028,.06),0,1)

def cube(name,loc,scale,material,bevel=0):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name=name;o.dimensions=scale;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.data.materials.append(material)
 if bevel:
  mod=o.modifiers.new('machined radius','BEVEL');mod.width=bevel;mod.segments=5
  o.modifiers.new('weighted normals','WEIGHTED_NORMAL')
 return o
def cylinder(name,loc,r,depth,material,rotation=None):
 bpy.ops.mesh.primitive_cylinder_add(vertices=64,radius=r,depth=depth,location=loc);o=bpy.context.object;o.name=name;o.data.materials.append(material)
 if rotation:o.rotation_euler=rotation
 return o
def torus(name,loc,major,minor,material):
 bpy.ops.mesh.primitive_torus_add(major_segments=96,minor_segments=12,location=loc,major_radius=major,minor_radius=minor)
 o=bpy.context.object;o.name=name;o.data.materials.append(material);o.rotation_euler=(math.pi/2,0,0)
 return o

# Portrait phone is a genuine 3D mesh with a recessed, image-textured screen.
rig=bpy.data.objects.new('PHONE / animated rig',None);bpy.context.collection.objects.link(rig)
body=cube('titanium handset',(-.85,0,.1),(2.0,.17,3.84),steel,.19);body.parent=rig
bezel=cube('front black glass',(-.85,-.104,.1),(1.87,.035,3.69),dark,.16);bezel.parent=rig
mesh=bpy.data.meshes.new('full-frame screen UV')
mesh.from_pydata([(-.86,0,-1.65),(.86,0,-1.65),(.86,0,1.65),(-.86,0,1.65)],[],[(0,1,2,3)])
mesh.update();screen=bpy.data.objects.new('campaign video surface',mesh);bpy.context.collection.objects.link(screen)
screen.location=(-.85,-.128,.1);screen.parent=rig
uv=mesh.uv_layers.new(name='full portrait')
for loop,coord in zip(mesh.polygons[0].loop_indices,[(0,0),(1,0),(1,1),(0,1)]):uv.data[loop].uv=coord
image=bpy.data.images.load(str(ROOT/'assets/campanha-loop.mp4'))
image.source='MOVIE'
im=bpy.data.materials.new('Danny campaign video on phone');im.use_nodes=True
nt=im.node_tree;nt.nodes.clear();tex=nt.nodes.new('ShaderNodeTexImage');tex.image=image;tex.image_user.frame_duration=210;tex.image_user.use_auto_refresh=True;em=nt.nodes.new('ShaderNodeEmission');em.inputs['Strength'].default_value=1;out=nt.nodes.new('ShaderNodeOutputMaterial');nt.links.new(tex.outputs['Color'],em.inputs['Color']);nt.links.new(em.outputs[0],out.inputs['Surface']);screen.data.materials.clear();screen.data.materials.append(im)
speaker=cube('speaker',(-.85,-.143,1.86),(.34,.016,.035),steel,.015);speaker.parent=rig
button=cube('side button',(.176,0,.97),(.04,.09,.43),steel,.018);button.parent=rig
rig.rotation_euler=(math.radians(-8),math.radians(-17),math.radians(-8))
for f,loc,rot in [(1,(-.25,.2,-.2),(-8,-17,-8)),(60,(-.44,.05,.1),(-6,-11,-6)),(155,(-.62,.1,.05),(-8,8,-7)),(210,(-.7,.4,-.04),(-8,13,-8))]:
 rig.location=loc;rig.rotation_euler=[math.radians(v) for v in rot];rig.keyframe_insert('location',frame=f);rig.keyframe_insert('rotation_euler',frame=f)

target=bpy.data.objects.new('TARGET / receiver',None);bpy.context.collection.objects.link(target)
for idx,(r,material) in enumerate([(.94,steel),(.70,cyan),(.48,steel),(.25,blue)]):
 o=torus('target ring %s'%idx,(1.2,.35,-.1),r,.028 if idx else .045,material);o.parent=target
c=cylinder('target centre',(1.2,.34,-.1),.105,.05,cyan,(math.pi/2,0,0));c.parent=target
for f,scale,rot in [(1,.65,-28),(90,1,0),(165,1.04,12),(210,1.05,18)]:
 target.scale=(scale,)*3;target.rotation_euler[1]=math.radians(rot);target.keyframe_insert('scale',frame=f);target.keyframe_insert('rotation_euler',frame=f)

arrow=bpy.data.objects.new('ARROW / flight',None);bpy.context.collection.objects.link(arrow)
shaft=cylinder('arrow shaft',(0,0,0),.052,2.3,cyan,(0,math.pi/2,0));shaft.parent=arrow
bpy.ops.mesh.primitive_cone_add(vertices=48,radius1=.18,radius2=0,depth=.54,location=(1.39,0,0),rotation=(0,math.pi/2,0));head=bpy.context.object;head.name='arrowhead';head.data.materials.append(blue);head.parent=arrow
for f,loc in [(1,(-5,-2,.3)),(74,(-3.4,-1,.3)),(125,(-2.4,-.3,-.05)),(165,(-.19,.15,-.1)),(170,(-.13,.15,-.1)),(210,(-.13,.15,-.1))]:
 arrow.location=loc;arrow.keyframe_insert('location',frame=f)

# Broad studio lighting and a dark blue world give the mockup dimensionality.
bpy.ops.object.light_add(type='AREA',location=(-3,-5,7));bpy.context.object.data.energy=900;bpy.context.object.data.shape='DISK';bpy.context.object.data.size=8
bpy.ops.object.light_add(type='AREA',location=(4,2,5));bpy.context.object.data.energy=1500;bpy.context.object.data.color=(.12,.55,1);bpy.context.object.data.size=6
bpy.ops.object.camera_add(location=(0,-12,4));cam=bpy.context.object;scene.camera=cam
direction=Vector((0,0,0))-cam.location;cam.rotation_euler=direction.to_track_quat('-Z','Y').to_euler();cam.data.type='ORTHO';cam.data.ortho_scale=8.25
scene.render.image_settings.file_format='PNG'
scene.frame_start=1;scene.frame_end=210;scene.render.fps=30
scene.render.filepath=str(ROOT/'assets/3d/frame-')
bpy.ops.wm.save_as_mainfile(filepath=str(ROOT/'resources/phone-arrow-target.blend'))
for f in range(1,211,6):
 scene.frame_set(f)
 scene.render.filepath=str(ROOT/'assets/3d/shot-%04d.png')%f
 bpy.ops.render.render(write_still=True)
