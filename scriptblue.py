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
        moveaway={(0,0):randint(1,4),(1,0):randint(1,3),(1,1):randint(2,3),(0,1):randint(2,4),(-1,1):randint(3,4),(-1,0):(1,3,4)[randint(0,2)],(-1,-1):(1,4)[randint(0,1)],(0,-1):(1,2,4)[randint(0,2)],(1,-1):randint(1,2)}
        path={(0,-1):2,(1,-1):3,(1,0):3,(1,1):4,(0,1):4,(-1,1):1,(-1,0):1,(-1,-1):2}
        dontnot={(-2,0):1,(-2,-1):1,(-2,-2):2,(-1,-2):2,(0,-2):2,(1,-2):2,(2,-2):3,(2,-1):3,(2,0):3,(2,1):3,(2,2):4,(1,2):4,(0,2):4,(-1,2):4,(-2,2):1,(-2,1):1}

        pos=robot.GetPosition()
        bpos=robot.GetInitialSignal().split()
        if len(robot.GetYourSignal())==0:
                robot.setSignal('0 '+robot.GetInitialSignal().split()[-1])
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
                #print('blue found base, ',robot.GetElixir(),'\n')
                #print(int(robot.GetElixir()))
                robot.DeployVirus(robot.GetVirus())
                for i in range(len(census)):
                        if census[i]=='enemy-base':
                                where=[(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(1,-1),(1,1),(-1,1)]
                                enemybase=(pos[0]+where[i][0],pos[1]+where[i][1])
                                s1=robot.GetYourSignal()
                                s=str(enemybase[0])+' '+str(enemybase[1])+' ebase '+s1
                                robot.setSignal(s)
                                #print(robot.GetYourSignal())
                                moveto=(enemybase[0]-pos[0],enemybase[1]-pos[1])
                                tup=(pos[0]-enemybase[0],pos[1]-enemybase[1])
                                if robot.GetElixir()>100:
                                        return dirn[moveto]
                                else:
                                        return path[tup]
        elif 'enemy' in census and 'ebase' not in robot.GetCurrentBaseSignal().split():
                #print('blue found enemy, ',int(robot.GetVirus()),'\n')
                #print(int(robot.GetElixir())) 
                if 'innerguard1' in robot.GetInitialSignal().split() or 'outerguard2' in robot.GetInitialSignal().split() or 'outerguard1' in robot.GetInitialSignal().split() or 'innerguard2' in robot.GetInitialSignal().split():
                        robot.DeployVirus(min(robot.GetVirus(),1200))
                        init=robot.GetYourSignal()
                        robot.setSignal('Danger '+init)
                        moveto=(sign(bpos[0]-pos[0]),sign(bpos[1]-pos[1]))
                        return dirn[moveto]
                        
                elif abs(int(bpos[0])-pos[0])+abs(int(bpos[1])-pos[1])<4:
                        robot.DeployVirus(min(robot.GetVirus(),1200))
                elif robot.GetVirus()>12000:
                        robot.DeployVirus(2400)
                elif robot.GetVirus()>6000:
                        robot.DeployVirus(1800)
                elif robot.GetVirus()>3000:
                        robot.DeployVirus(1200)
                else:
                        robot.DeployVirus(min(robot.GetVirus(),600))
                for i in range(len(census)):
                        if census[i]=='enemy' and robot.GetElixir()>100 and robot.GetVirus()>800:
                                where=[(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(1,-1),(1,1),(-1,1)]
                                enemy=(pos[0]+where[i][0],pos[1]+where[i][1])
                                return dirn[where[i]]
                        elif census[i]=='enemy':
                                where=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(-1,-1),(1,-1)]
                                enemy=(pos[0]-where[i][0],pos[1]-where[i][1])
                                return dirn[where[i]]
        if 'enemy' not in census and 'Danger' in robot.GetYourSignal().split():
                new=robot.GetYourSignal()[7:]
                robot.setSignal(new)
                
     
        else:
                if 'innerguard1' in robot.GetInitialSignal().split():
                        path1={(0,-1):4,(1,-1):4,(1,0):1,(1,1):1,(0,1):2,(-1,1):2,(-1,0):3,(-1,-1):3}
                        pos=robot.GetPosition()
                        bpos=robot.GetInitialSignal().split()[0:2]
                        tup=(pos[0]-int(bpos[0]),pos[1]-int(bpos[1]))
                        if tup in path1.keys():
                                return path1[tup]
                        else:
                                moveto=(sign(pos[0]-int(bpos[0])),sign(pos[1]-int(bpos[1])))
                                return moveaway[moveto]
                if 'outerguard1' in robot.GetInitialSignal().split():
                        path1={(-2,0):3,(-2,-1):3,(-2,-2):3,(-1,-2):4,(0,-2):4,(1,-2):4,(2,-2):4,(2,-1):1,(2,0):1,(2,1):1,(2,2):1,(1,2):2,(0,2):2,(-1,2):2,(-2,2):2,(-2,1):3}
                        pos=robot.GetPosition()
                        bpos=robot.GetInitialSignal().split()[0:2]
                        tup=(pos[0]-int(bpos[0]),pos[1]-int(bpos[1]))
                
                        if tup in path1.keys():
                                return path1[tup]
                        else:
                                moveto=(sign(pos[0]-int(bpos[0])),sign(pos[1]-int(bpos[1])))
                                return moveaway[moveto]
                if 'outerguard2' in robot.GetInitialSignal().split():
                        path1={(-2,0):1,(-2,-1):1,(-2,-2):2,(-1,-2):2,(0,-2):2,(1,-2):2,(2,-2):3,(2,-1):3,(2,0):3,(2,1):3,(2,2):4,(1,2):4,(0,2):4,(-1,2):4,(-2,2):1,(-2,1):1}
                        pos=robot.GetPosition()
                        bpos=robot.GetInitialSignal().split()[0:2]
                        tup=(pos[0]-int(bpos[0]),pos[1]-int(bpos[1]))
                
                        if tup in path1.keys():
                                return path1[tup]
                        else:
                                moveto=(sign(pos[0]-int(bpos[0])),sign(pos[1]-int(bpos[1])))
                                return moveaway[moveto]
                elif 'innerguard2' in robot.GetInitialSignal().split():
                        path1={(0,-1):2,(1,-1):3,(1,0):3,(1,1):4,(0,1):4,(-1,1):1,(-1,0):1,(-1,-1):2}
                        pos=robot.GetPosition()
                        bpos=robot.GetInitialSignal().split()[0:2]
                        tup=(pos[0]-int(bpos[0]),pos[1]-int(bpos[1]))
                
                        if tup in path1.keys():
                                return path1[tup]
                        else:
                                moveto=(sign(pos[0]-int(bpos[0])),sign(pos[1]-int(bpos[1])))
                                return moveaway[moveto]
                        
                if 'farmerU' in robot.GetInitialSignal().split():
                        coord=(pos[0]-1,pos[1]-1,X-2-pos[0],Y-2-pos[1])
                        count=coord.count(0)
                        if count==0:
                                m=min(coord)
                                for i in range(4):
                                        if coord[i]==m:
                                                return (4,1,2,3)[i]
                        elif count==1:
                                d=[3,4,1,2]
                                for i in range(4):
                                        if coord[i]==0:
                                                return d[i]
                        elif count==2:
                                if coord[0]==0:
                                        if coord[1]==0:
                                                return 3
                                        else:
                                                return 2
                                else:
                                        if coord[1]==0:
                                                return 4
                                        else:
                                                return 1
                elif 'farmerD' in robot.GetInitialSignal().split():
                        coord=(pos[0],pos[1],X-1-pos[0],Y-1-pos[1])
                        count=coord.count(0)
                        if count==0:
                                m=min(coord)
                                for i in range(4):
                                        if coord[i]==m:
                                                return (4,1,2,3)[i]
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


                else:
                        
                        
                        pos=robot.GetPosition()
                        bpos=robot.GetInitialSignal().split()[0:2]
                        dist=abs(int(bpos[0])-pos[0])+abs(int(bpos[1])-pos[1])
                        if 'Danger' in robot.GetCurrentBaseSignal().split():
                                moveto=(sign(int(bpos[0])-pos[0]),sign(int(bpos[1])-pos[1]))
                                return dirn[moveto]
                        if 'ebase' in robot.GetCurrentBaseSignal().split():
                                ebase=(int(robot.GetCurrentBaseSignal().split()[1]),int(robot.GetCurrentBaseSignal().split()[2]))
                                moveto=(sign(ebase[0]-pos[0]),sign(ebase[1]-pos[1]))
                                return dirn[moveto]
                        
                        
                                        
                        else:
                                
                                d=int(robot.GetYourSignal().split()[0])
                                movepos=(int(robot.GetInitialSignal().split()[2]),int(robot.GetInitialSignal().split()[3]))
                                moveto=(sign(movepos[0]-pos[0]),sign(movepos[1]-pos[1]))
                                
                                
                                if (abs(movepos[0]-pos[0])>0 or abs(movepos[1]-pos[1])>0) and d==0:
                                
                                        return dirn[moveto]
                                elif abs(movepos[0]-pos[0])+abs(movepos[1]-pos[1])<(X+Y)/2:
                                        if d==0:
                                                robot.setSignal('1 '+robot.GetInitialSignal().split()[-1])

                                        coords=(-moveto[0],-moveto[1])
                                        if (pos[0])*(pos[1])*(X-1-pos[0])*(Y-1-pos[1])!=0:
                                                return moveaway[coords]
                                        else:
                                                robot.setSignal('0 '+robot.GetInitialSignal().split()[-1])
                                                return dirn[moveto]
                                else:
                                        robot.setSignal('0 '+robot.GetInitialSignal().split()[-1])
                                        return dirn[moveto]
                                        

def ActBase(base):
        bpos=base.GetPosition()
        s=str(bpos[0])+' '+str(bpos[1])
        X=base.GetDimensionX()
        Y=base.GetDimensionY()
        #m=X//2-1
        #n=Y//2-1
        m=bpos[0]
        n=bpos[1]
        listofbots=[]
        for ch in base.GetListOfSignals():
                listofbots.append(ch.split()[-1])

        
        while base.GetElixir() > 150:
                
                a=' '+str(m+randint(-2,2))+' '+str(n+randint(-2,2))
                
                if base.GetElixir()==500:
                        base.create_robot(s+' farmerU')
                if base.GetElixir()==450:
                        base.create_robot(s+' farmerD')
                if base.GetElixir()==400:
                        base.create_robot(s+' innerguard1')
                if base.GetElixir()==350:
                        base.create_robot(s+' innerguard2')
                if base.GetElixir()==300:
                        base.create_robot(s+' outerguard1')
                if base.GetElixir()==250:
                        base.create_robot(s+' outerguard2')
                base.create_robot(s+a+' pawn')
                if base.GetElixir()==150:
                        return
        
        if base.GetElixir()>50 and 'innerguard1' not in listofbots:
                base.create_robot(s+' innerguard1')
        elif base.GetElixir()>50 and 'innerguard2' not in listofbots:
                base.create_robot(s+' innerguard2')
        elif base.GetElixir()>50 and 'outerguard1' not in listofbots:
                base.create_robot(s+' outerguard1')
        elif base.GetElixir()>50 and 'outerguard2' not in listofbots:
                base.create_robot(s+' outerguard2')
        
                

        count3=0
        for ch in base.GetListOfSignals(): #1
                                        #  4 2
                if 'ebase' in ch.split() and 'ebase' not in base.GetYourSignal().split(): # 3

                        s=ch.split()[0]+' '+ch.split()[1]
                        #print('ebase '+s)
                        a=base.GetYourSignal()
                        s=s+a
                        base.SetYourSignal('ebase '+s)

                if 'Danger' in ch.split():
                        count3=1
        if count3==1 and 'Danger' not in base.GetYourSignal().split():
                s1=base.GetYourSignal()
                base.SetYourSignal(s1+' Danger')

        
        census=[0,0,0,0,0,0,0,0]
        if bpos[0]<X:
                census[3]=base.investigate_right()
                if bpos[1]<Y:
                        census[6]=base.investigate_se()
                if bpos[1]>0:
                        census[5]=base.investigate_ne()
        if bpos[0]>0:
                census[2]=base.investigate_left()
                if bpos[1]<Y:
                        census[7]=base.investigate_sw()
                if bpos[1]>0:
                        census[4]=base.investigate_nw()
        if bpos[1]<Y:
                census[1]=base.investigate_down()
        if bpos[1]>0:
                census[0]=base.investigate_up()
        if 'enemy' in census:
                base.DeployVirus(min(base.GetVirus(),2400))
                if 'Danger' not in base.GetYourSignal().split():
                        s1=base.GetYourSignal()
                        base.SetYourSignal(s1+' Danger')
        if (count3==0 and 'enemy' not in census) and 'Danger' in base.GetYourSignal().split():
                s2=base.GetYourSignal()[0:len(base.GetYourSignal())-6]
                base.SetYourSignal(s2)


                
                
        return
