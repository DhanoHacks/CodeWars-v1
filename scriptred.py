from random import randint
'''
 1
4 2
 3
'''


def ActRobot(robot):#up down left right nw ne se sw
               
        path={(0,-1):2,(1,-1):3,(1,0):3,(1,1):4,(0,1):4,(-1,1):1,(-1,0):1,(-1,-1):2}

        pos=robot.GetPosition()
        bpos=robot.GetInitialSignal().split()
        bpos[0]=int(bpos[0])
        bpos[1]=int(bpos[1])
        census=[0,0,0,0,0,0,0,0]
        if pos[0]<39:
                census[3]=robot.investigate_right()
                if pos[1]<39:
                        census[6]=robot.investigate_se()
                if pos[1]>0:
                        census[5]=robot.investigate_ne()
        if pos[0]>0:
                census[2]=(robot.investigate_left())
                if pos[1]<39:
                        census[7]=robot.investigate_sw()
                if pos[1]>0:
                        census[4]=robot.investigate_nw()
        if pos[1]<39:
                census[1]=robot.investigate_down()
        if pos[1]>0:
                census[0]=robot.investigate_up()
        if 'enemy-base' in census:
                print(int(robot.GetElixir())) 
                robot.DeployVirus(robot.GetVirus())
                for i in range(len(census)):
                        if census[i]=='enemy-base':
                                where=[(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(1,-1),(1,1),(-1,1)]
                                enemybase=(pos[0]+where[i][0],pos[1]+where[i][1])
                                robot.setSignal(str(pos[0]+where[i][0])+' '+str(pos[1]+where[i][1]))
                                tup=(pos[0]-enemybase[0],pos[1]-enemybase[1])
                                return path[tup]
        elif 'enemy' in census:
                print(int(robot.GetElixir())) 
                if abs(bpos[0]-pos[0])<10 and abs(bpos[1]-pos[1])<10:
                        robot.DeployVirus(min(robot.GetVirus()/4,4000))
                else:
                        robot.DeployVirus(min(robot.GetVirus()/5,2000))

        if pos[0]==0:
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
                elif 'leftl' in robot.GetInitialSignal().split() or 'leftu' in robot.GetInitialSignal().split() or 'leftd' in robot.GetInitialSignal().split():
                        pos=robot.GetPosition()
                        bpos=robot.GetInitialSignal().split()[0:2]
                        if pos[0]-int(bpos[0])==0 and pos[1]-int(bpos[1])==0:
                                d={'l':4,'u':1,'d':3}
                                return d[robot.GetInitialSignal().split()[2][4]]
                        else:
                                return 4
                elif 'rightl' in robot.GetInitialSignal().split() or 'rightu' in robot.GetInitialSignal().split() or 'rightd' in robot.GetInitialSignal().split():
                        pos=robot.GetPosition()
                        bpos=robot.GetInitialSignal().split()[0:2]
                        if pos[0]-int(bpos[0])==0 and pos[1]-int(bpos[1])==0:
                                d={'l':2,'u':1,'d':3}
                                return d[robot.GetInitialSignal().split()[2][5]]
                        else:
                                return 2
                else:
                        pos=robot.GetPosition()
                        bpos=robot.GetInitialSignal().split()[0:2]
                        dist=abs(int(bpos[0])-pos[0])+abs(int(bpos[1])-pos[1])
                        if 'right' in robot.GetInitialSignal().split() and dist<20:
                                d={'up':(1,2),'down':(2,3)}
                                return d[robot.GetInitialSignal().split()[3]][randint(0,1)]
                        elif 'left' in robot.GetInitialSignal().split() and dist<20:
                                d={'up':(1,4),'down':(4,3)}
                                return d[robot.GetInitialSignal().split()[3]][randint(0,1)]
                        else:
                                return randint(1,4)

def ActBase(base):
        bpos=base.GetPosition()
        if bpos[1]/bpos[0]>1:
                a=' right'
        elif bpos[1]/bpos[0]<1:
                a=' left'
        s=str(bpos[0])+' '+str(bpos[1])

        
        while base.GetElixir() > 50:
                if base.GetElixir() > 300:
                        if base.GetElixir()%100==0:
                                base.create_robot(s+a+' up')
                        else:
                                base.create_robot(s+a+' down')
                if base.GetElixir()==300:
                        base.create_robot(s+a+'u')
                if base.GetElixir()==250:
                        base.create_robot(s+a+'d')
                if base.GetElixir()==200:
                        base.create_robot(s+a+'l')
                if base.GetElixir()==150:
                        base.create_robot(s+' upg')
                if base.GetElixir()==100:
                        base.create_robot(s+' downg')
                
                
        return
