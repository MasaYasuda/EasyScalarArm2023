import dynamixel_classes_for_windows as dyna 
import kbhit

dxl = dyna.Dynamixel("COM9",57600,1)
kb = kbhit.KBHit()

dxl.set_mode_position()
dxl.set_min_max_position(0,4095)
dxl.enable_torque()
now_goal=2048

while 1:
    if kb.kbhit():
        c = ord(kb.getch())
        if c==72: #UP
            now_goal=now_goal+50
        elif c==80: #DOWN
            now_goal=now_goal-50
        elif c==27: #ESC
            break

        now_goal=max(0,min(now_goal,4095))
        dxl.write_position(now_goal)   

dxl.disable_torque()
dxl.close_port()
kb.set_normal_term()
