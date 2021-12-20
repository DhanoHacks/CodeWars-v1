from random import randint


def ActRobot(robot):
        if robot.GetVirus() > 1000:
                robot.DeployVirus(200)
        
        return randint(1,4)


