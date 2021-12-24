from random import randint
from numpy import sign
'''
 1
4 2
 3
'''


def ActRobot(robot):#up down left right nw ne se sw
        X=robot.GetDimensionX()
        Y=robot.GetDimensionY()
        dirn={(1,0):2,(1,1):(2,3)[randint(0,1)],(0,1):3,(-1,1):(3,4)[randint(0,1)],(-1,0):4,(-1,-1):(1,4)[randint(0,1)],(0,-1):1,(1,-1):(1,2)[randint(0,1)],(0,0):randint(1,4)}
        path={(0,-1):2,(1,-1):3,(1,0):3,(1,1):4,(0,1):4,(-1,1):1,(-1,0):1,(-1,-1):2}       

        pos=robot.GetPosition()
        bpos=robot.GetInitialSignal().split()
        if pos[0]==int(bpos[0]) and pos[1]==int(bpos[1]):
                robot.setSignal('0')
        bpos[0]=int(bpos[0])
        bpos[1]=int(bpos[1])
        census=[0,0,0,0,0,0,0,0]
        if pos[0]<X:
                census[3]=robot.investigate_right()
                if pos[1]<Y:
                        census[6]=robot.investigate_se()
                if pos[1]>0:
                        census[5]=robot.investigate_ne()
        if pos[0]>0:
                census[2]=(robot.investigate_left())
                if pos[1]<Y:
                        census[7]=robot.investigate_sw()
                if pos[1]>0:
                        census[4]=robot.investigate_nw()
        if pos[1]<Y:
                census[1]=robot.investigate_down()
        if pos[1]>0:
                census[0]=robot.investigate_up()
        if 'enemy-base' in census:
                #print(int(robot.GetElixir()))
                robot.DeployVirus(robot.GetVirus())
                for i in range(len(census)):
                        if census[i]=='enemy-base':
                                where=[(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(1,-1),(1,1),(-1,1)]
                                enemybase=(pos[0]+where[i][0],pos[1]+where[i][1])
                                s=str(enemybase[0])+' '+str(enemybase[1])+' ebase'
                                robot.setSignal(s)
                                #print(robot.GetYourSignal())
                                tup=(pos[0]-enemybase[0],pos[1]-enemybase[1])
                                return path[tup]
        elif 'enemy' in census:
                #print(int(robot.GetElixir())) 
                if abs(bpos[0]-pos[0])<10 and abs(bpos[1]-pos[1])<10:
                        robot.DeployVirus(min(robot.GetVirus()*0.25,4000))
                else:
                        robot.DeployVirus(min(robot.GetVirus()*0.2,2000))
        if 'farmerU' in robot.GetInitialSignal().split():
                coord=(pos[0]-1,pos[1]-1,X-2-pos[0],Y-2-pos[1])
                count=coord.count(0)
                if count==0:
                        return 1
                elif count==1:
                        d=[1,2,3,4]
                        for i in range(4):
                                if coord[i]==0:
                                        return d[i]
                elif count==2:
                          if coord[0]==0:
                                if coord[1]==0:
                                        return 2
                                else:
                                        return 1
                          else:
                                if coord[1]==0:
                                        return 3
                                else:
                                        return 4
        elif 'farmerD' in robot.GetInitialSignal().split():
                coord=(pos[0],pos[1],X-1-pos[0],Y-1-pos[1])
                count=coord.count(0)
                if count==0:
                        return 3
                elif count==1:
                        d=[1,2,3,4]
                        for i in range(4):
                                if coord[i]==0:
                                        return d[i]
                elif count==2:
                        if coord[0]==0:
                                if coord[1]==0:
                                        return 2
                                else:
                                        return 1
                        else:
                                if coord[1]==0:
                                        return 3
                                else:
                                        return 4

        elif pos[0]==0:
                return 2
        elif pos[0]==39:
                return 4
        elif pos[1]==0:      # 1
                return 3    # 4 2
        elif pos[1]==39:     # 3
                return 1     
        else:
                if 'upg' in robot.GetInitialSignal().split():
                        path1={(0,0):1,(0,-1):2,(1,-1):3,(1,0):3,(1,1):4,(0,1):4,(-1,1):1,(-1,0):1,(-1,-1):2}
                        pos=robot.GetPosition()
                        bpos=robot.GetInitialSignal().split()[0:2]
                        tup=(pos[0]-int(bpos[0]),pos[1]-int(bpos[1]))
                
                        return path1[tup]
                elif 'downg' in robot.GetInitialSignal().split():
                        path2={(0,0):3,(0,-1):2,(1,-1):3,(1,0):3,(1,1):4,(0,1):4,(-1,1):1,(-1,0):1,(-1,-1):2}
                        pos=robot.GetPosition()
                        bpos=robot.GetInitialSignal().split()[0:2]
                        tup=(pos[0]-int(bpos[0]),pos[1]-int(bpos[1]))
                
                        return path2[tup]

                else:
                        if 'base' in robot.GetYourSignal():
                                return randint(1,4)
                        d=int(robot.GetYourSignal())
                        pos=robot.GetPosition()
                        bpos=robot.GetInitialSignal().split()[0:2]
                        dist=abs(int(bpos[0])-pos[0])+abs(int(bpos[1])-pos[1])
                        if 'ebase' in robot.GetCurrentBaseSignal().split() and 'dont' not in robot.GetCurrentBaseSignal().split():
                                ebase=(int(robot.GetCurrentBaseSignal().split()[1]),int(robot.GetCurrentBaseSignal().split()[2]))
                                moveto=(sign(ebase[0]-pos[0]),sign(ebase[1]-pos[1]))
                                return dirn[moveto]
                        else:
                                moveto=(sign(int(robot.GetInitialSignal().split()[2])-pos[0]),sign(int(robot.GetInitialSignal().split()[3])-pos[1]))
                        
                        if d<=10 and moveto!=(0,0):
                                d+=1
                                d1=str(d)
                                robot.setSignal(d1)
                                return dirn[moveto]
                        else:
                                return randint(1,4)
                                        

def ActBase(base):
        bpos=base.GetPosition()
        s=str(bpos[0])+' '+str(bpos[1])
        a=' 20 20'

        
        while base.GetElixir() > 50:
                if base.GetElixir() > 250:
                        base.create_robot(s+a)
                if base.GetElixir()==250:
                        base.create_robot(s+' farmerU')
                if base.GetElixir()==200:
                        base.create_robot(s+' farmerD')
                if base.GetElixir()==150:
                        base.create_robot(s+' upg')
                if base.GetElixir()==100:
                        base.create_robot(s+' downg')
                

        count=0
        for ch in base.GetListOfSignals():
                
                if 'ebase' in ch.split():
                        count+=1
                        s=ch.split()[0]+' '+ch.split()[1]
                        #print('ebase '+s)
                        base.SetYourSignal('ebase '+s)
        if count>2:
                base.SetYourSignal('ebase '+s+' dont')

                
                
        return
