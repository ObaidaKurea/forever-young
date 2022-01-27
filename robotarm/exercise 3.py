from RobotArm import RobotArm
            
            
robotArm = RobotArm('exercise 3')
for q in range(1,5):
    robotArm.grab();
    robotArm.moveRight();
    robotArm.drop();
    robotArm.moveLeft();
               
robotArm.wait()

from RobotArm import RobotArm
            
             


robotArm.wait()