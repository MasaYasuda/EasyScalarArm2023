import dynamixel_classes_for_ubuntu as dyna 
import kbhit

dxl1 = dyna.Dynamixel("COM9",57600,1)
dxl2 = dyna.Dynamixel("COM9",57600,2)
dxl3 = dyna.Dynamixel("COM9",57600,3)
kb = kbhit.KBHit()

# ID 1 土台左右　MIN: 400  MAX:1400 MODE:POSITON
min_1=400
max_1=1400
# ID 2 先端上下　MIN:3000  MAX:16800 EXTENDED_POSITION
min_2=3000
max_2=16800
# ID 3 先端左右　MIN:1350  MAX:2750 MODE:POSITION
min_3=1650
max_3=2750

dxl1.set_mode_position()
dxl2.set_mode_ex_position()
dxl3.set_mode_position()

dxl1.set_min_max_position(min_1,max_1)
dxl2.set_min_max_position(min_2,max_2)
dxl3.set_min_max_position(min_3,max_3)
dxl1.enable_torque()
dxl2.enable_torque()
dxl3.enable_torque()

now_goal1=(int)((min_1,max_1)/2)
now_goal2=(int)((min_2,max_2)/2)
now_goal3=(int)((min_3,max_3)/2)

while 1:
    if kb.kbhit():
        c = ord(kb.getch())
        if c==122: #Z
            now_goal1=now_goal1+25
        elif c==120: #X
            now_goal1=now_goal1-25
        elif c==97: #A
            now_goal2=now_goal2+50
        elif c==115: #S
            now_goal2=now_goal2-50
        elif c==113: #Q
            now_goal3=now_goal3+25
        elif c==119: #W
            now_goal3=now_goal3-25
        elif c==27: #ESC
            break

        now_goal1=max(min_1,min(now_goal1,max_1))
        now_goal2=max(min_2,min(now_goal2,max_2))
        now_goal3=max(min_3,min(now_goal3,max_3))

        dxl1.write_position(now_goal1)   
        dxl2.write_position(now_goal2)   
        dxl3.write_position(now_goal3)   

dxl1.disable_torque()
dxl2.disable_torque()
dxl3.disable_torque()

dxl1.close_port()
dxl2.close_port()
dxl3.close_port()

kb.set_normal_term()
