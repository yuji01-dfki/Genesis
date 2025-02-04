import genesis as gs
import mujoco as mj
gs.init(backend=gs.gpu)

scene = gs.Scene(
  show_viewer=False,
  viewer_options=gs.options.ViewerOptions(
    res=(640, 480),
    max_FPS=30,
    camera_fov = 40,
  ),
  vis_options=gs.options.VisOptions(
    show_world_frame=True,
    ambient_light=(0.5, 0.5, 0.5),
 ),
  renderer=gs.renderers.Rasterizer(),
)

plane = scene.add_entity(
    morph=gs.morphs.Plane(),
)

cam = scene.add_camera(
  res= (640, 480),
  pos=(0, 10, 10),
  lookat=(0, 0, 0),
  fov=40,
  GUI=False,
)

arter = scene.add_entity(
  gs.morphs.URDF(file = "/workspace/genesis/assets/urdf/arter/arter.urdf",
                 pos = (0, 0, 1),),
  visualize_contact=True,
)
 
scene.build()

cam.start_recording()

for i in range(1000):
  scene.step()
  cam.render()
  rgb, depth, seg, normal = cam.render(depth=True, segmentation=True, normal=True)
  

cam.stop_recording(save_to_filename="arter.mp4", fps=60)