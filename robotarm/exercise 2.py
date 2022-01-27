from shutil import move
from RobotArm import RobotArm
            
             
robotArm = RobotArm('exercise 2')
robotArm.grab()
for x in range (1,11):  
    robotArm.moveRight()
robotArm.drop()                       
for q in range (1,6):
    robotArm.moveLeft()
robotArm.grab()
for w in range(5,11):
    robotArm.moveRight()
robotArm.drop() 
for l in range (9,11):
    robotArm.moveLeft()
robotArm.grab()
for g in range(9,11):
    robotArm.moveRight()
robotArm.drop()

robotArm.wait()



