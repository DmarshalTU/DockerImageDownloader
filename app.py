import docker
import time

def pull_image(image_name):
    client = docker.from_env()
    client.images.pull(image_name)
    time.sleep(3)


c = 'hello-world'
client = docker.from_env()


# Import the necessary packages
from consolemenu import *
from consolemenu.items import *


# Create the menu
menu = ConsoleMenu("DT", "Docker Image Builder")

jp_menu = SelectionMenu(["jp44", "jp43"])
tf_menu = SelectionMenu(["tf1", "tf2"])

submenu_all = CommandItem("all",f"docker pull image all {pull_image(c)}")
submenu_x86 = CommandItem("x86", f"docker pull image x86 {pull_image(c)}")
submenu_jetson_43_tf1 = CommandItem("jetson jp43 tf1", f"docker pull image jetson {pull_image(c)}")
submenu_jetson_43_tf2 = CommandItem("jetson jp43 tf2", f"docker pull image jetson {pull_image(c)}")
submenu_jetson_44_tf1 = CommandItem("jetson jp44 tf2", f"docker pull image jetson {pull_image(c)}")
submenu_jetson_44_tf2 = CommandItem("jetson jp44 tf2", f"docker pull image jetson {pull_image(c)}")

menu.append_item(submenu_all)
menu.append_item(submenu_x86)
menu.append_item(submenu_jetson_43_tf1)
menu.append_item(submenu_jetson_43_tf2)
menu.append_item(submenu_jetson_44_tf1)
menu.append_item(submenu_jetson_44_tf2)


menu.show()
