import dynamixel_classes_for_windows as dyna 
import kbhit

dxl = dyna.Dynamixel("COM9",57600)
kb = kbhit.KBHit()

def fin():
    dxl.disable_torque(2)
    dxl.close_port()
    kb.set_normal_term()

# ID 2 先端上下　MIN:3000  MAX:16800 EXTENDED_POSITION
min_2=-6000
max_2=2000

dxl.enable_torque(1)
dxl.set_mode_ex_position(2)
dxl.enable_torque(2)
now_goal2=int(0)
dxl.write_position(2,now_goal2) 

"""
elif c==97: #A
    now_goal2=now_goal2+50
elif c==115: #S
    now_goal2=now_goal2-50
"""
try:
    while 1:
        if kb.kbhit():
            c = ord(kb.getch())
            if c==72 :#UP
                now_goal2=now_goal2+50
            elif c==80 : #DOWN
                now_goal2=now_goal2-50
            elif c==27: #ESC
                break

            now_goal2=max(min_2,min(now_goal2,max_2))

            dxl.write_position(2,now_goal2) 

    fin()

except KeyboardInterrupt:
    fin()
