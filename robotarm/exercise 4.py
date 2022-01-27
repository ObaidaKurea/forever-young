from sys import builtin_module_names
from turtle import color
from RobotArm import RobotArm
            
            
robotArm = RobotArm('exercise 4')
robotArm.grab()
for q in range(0,2):
    robotArm.moveRight()
robotArm.drop()
for w in range(0,2):
    robotArm.moveLeft()
robotArm.grab()
for e in range(0,2):
    robotArm.moveRight()
robotArm.drop()
for r in range(0,2):
    robotArm.moveLeft()
robotArm.grab()
for e in range(0,2):
    robotArm.moveRight()
robotArm.drop()
robotArm.grab()
for f in range(0,1):
    robotArm.moveLeft()
robotArm.drop()
for g in range(0,1):
    robotArm.moveRight()
robotArm.grab()
for y in range(0,1):
    robotArm.moveLeft()
robotArm.drop()
for m in range(0,1):
    robotArm.moveRight()
robotArm.grab()
for n in range(0,1):
    robotArm.moveLeft()
robotArm.drop()




               
robotArm.wait()

from RobotArm import RobotArm
            
             


robotArm.wait()