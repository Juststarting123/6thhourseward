#Name:Seeley Seward
#Class: 6th Hour
#Assigment: AI Playground
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import Point3
from panda3d.core import AmbientLight, DirectionalLight
from panda3d.core import TextNode

from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionNode, CollisionSphere
from direct.task import Task
import random

# Initialize the base class
class HorrorGame(ShowBase):
    def __init__(self):
        super().__init__()

        # Set the window title and background color
        self.set_window_title("3D Horror Game")
        self.set_background_color(0, 0, 0)  # Black background

        # Load the environment model
        self.environment = self.loader.load_model("models/environment")
        self.environment.reparent_to(self.render)
        self.environment.set_scale(2)
        self.environment.set_pos(-8, 42, 0)

        # Create lighting (scary atmosphere)
        ambient_light = AmbientLight("ambient_light")
        ambient_light.set_color((0.3, 0.3, 0.3, 1))
        directional_light = DirectionalLight("directional_light")
        directional_light.set_color((0.8, 0.8, 0.8, 1))

        # Attach lights to the scene
        self.lights = self.render.attach_new_node(ambient_light)
        self.render.set_light(self.lights)
        self.lights = self.render.attach_new_node(directional_light)
        self.render.set_light(self.lights)

        # Player setup (first-person perspective)
        self.player = self.loader.load_model("models/box")
        self.player.reparent_to(self.render)
        self.player.set_pos(0, 0, 0)
        self.player.set_scale(1)

        # Add player controls
        self.mouse_task = self.task_mgr.add(self.mouse_move)

        # Create the monster
        self.monster = self.loader.load_model("models/box")
        self.monster.reparent_to(self.render)
        self.monster.set_pos(random.randint(-30, 30), random.randint(-30, 30), 0)
        self.monster.set_scale(1.5)

        # Add monster AI (move towards player)
        self.monster_task = self.task_mgr.add(self.monster_move)

        # Create the collision detection
        self.collision_node = self.player.attach_new_node(CollisionNode('player'))
        self.collision_node.node().add_solid(CollisionSphere(0, 0, 0, 1))
        self.collision_node.set_collide_mask(1)

        # Create on-screen text to display instructions
        self.instruction_text = OnscreenText(text="Use WASD to move, Mouse to look around", pos=(-1.3, -0.95), scale=0.07)

    # Move the player based on mouse movement
    def mouse_move(self, task):
        if self.mouseWatcherNode.has_mouse():
            mouse_x = self.mouseWatcherNode.get_mouse().get_x()
            mouse_y = self.mouseWatcherNode.get_mouse().get_y()

            self.camera.look_at(self.player)
            self.camera.set_rotation(mouse_x * 180, mouse_y * 180, 0)

        return Task.cont

    # Monster AI to follow the player
    def monster_move(self, task):
        monster_pos = self.monster.get_pos()
        player_pos = self.player.get_pos()

        direction = player_pos - monster_pos
        direction.normalize()

        self.monster.set_pos(monster_pos + direction * 0.05)

        return Task.cont

# Run the game
app = HorrorGame()
app.run()