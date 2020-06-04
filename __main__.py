import lihzahrd
from lihzahrd.timer import Timer

with Timer("Parse sample world"):
    world = lihzahrd.World.create_from_file("The_Gateway_To_A_New_Future.wld")

breakpoint()
