import numpy as np
import vgamepad as vg
import time
import XInput as xb
from threading import Thread, Lock

class vController:
    #threading garbage
    stopped = True
    lock = None
    #properties
    id = 0

    # constructor
    def __init__(self, id):
        self.lock = Lock()
        self.gamepad = vg.VX360Gamepad()
        self.id = id

    #def __del__(self):


    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()
        self.gamepad.reset()

    def stop(self):
        self.stopped = True
    #controller forwarding
    #spaghetti code moment to convert xinput state to vigem state
    def run(self):
        while not self.stopped:
            try:
                #print("AO")
                realid = self.id + 2
                realstate = xb.get_state(realid)
                #ButtonList = np.asarray(list(xb.get_button_values(realstate).values())).astype(int)
                #res = int("".join(str(x) for x in ButtonList), 2)
                Triggers = xb.get_trigger_values(realstate)
                Thumbs = xb.get_thumb_values(realstate)
                #self.gamepad.report.wButtons = res
                Buttons = np.asarray(list(xb.get_button_values(realstate).values()))
        
                if Buttons[0]: self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
                else: self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
                if Buttons[1]: self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
                else: self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
                if Buttons[2]: self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
                else: self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
                if Buttons[3]: self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
                else: self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
                if Buttons[4]: self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
                else: self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
                if Buttons[5]: self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
                else: self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
                if Buttons[6]: self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
                else: self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
                if Buttons[7]: self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
                else: self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
                if Buttons[8]: self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
                else: self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
                if Buttons[9]: self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
                else: self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
                if Buttons[10]: self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                else: self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                if Buttons[11]: self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                else: self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)        
                if Buttons[12]: self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                else: self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                if Buttons[13]: self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                else: self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                self.gamepad.left_trigger_float(Triggers[0])
                self.gamepad.right_trigger_float(Triggers[1])
                self.gamepad.left_joystick_float(Thumbs[0][0],Thumbs[0][1])
                self.gamepad.right_joystick_float(Thumbs[1][0],Thumbs[1][1])
            except Exception:
                print('CONTROLLER NO!')
            pass
        #print(self.gamepad.report.value())
        #print(np.asarray(list(xb.get_button_values(realstate).values())).astype(int))
        #self.gamepad.report = reportconversion(xb.get_state(realid)._fields_[1])
            self.lock.acquire()
            self.gamepad.update()
            self.lock.release()

#    def reportconversion(self):
    def autoinput(self, input):
        #self.stop()
        self.lock.acquire()
        if input == 1:
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
            self.gamepad.update()
            time.sleep(0.5)
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        if input == 2:
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
            self.gamepad.update()
            time.sleep(0.5)
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)              
        if input == 3:
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
            self.gamepad.update()
            time.sleep(0.09)
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
            self.gamepad.update()
            time.sleep(0.09)
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
            self.gamepad.update()
            time.sleep(0.09)
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)                        
        if input == 4:
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
            self.gamepad.update()
            time.sleep(0.09)
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
            self.gamepad.update()
            time.sleep(0.09)
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
            self.gamepad.update()
            time.sleep(0.09)
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)      
        if input == 5:
            self.gamepad.left_trigger(255)
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
            self.gamepad.update()
            time.sleep(0.15)
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        if input == 6:
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
            self.gamepad.left_trigger(255)
            self.gamepad.update()
            time.sleep(0.15)
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)              
        if input == 7:
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
            self.gamepad.left_trigger(255)
            self.gamepad.update()
            time.sleep(0.15)
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)         
        if input == 8:
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
            self.gamepad.left_trigger(255)                
            self.gamepad.update()
            time.sleep(0.15)
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        self.gamepad.update()
        self.lock.release()
        #self.start()                

    def press_button(self, button):
        #self.stop()
        self.lock.acquire()
        self.gamepad.press_button(button)
        self.lock.release()
        #self.start()

    def release_button(self, button):
        #self.stop()
        self.lock.acquire()
        self.gamepad.release_button(button)
        self.lock.release()
        #self.start()
    
    def update(self):
        #self.stop()
        self.lock.acquire()
        self.gamepad.update()
        self.lock.release()
        #self.start()

    def reset(self):
        #self.stop()
        self.lock.acquire()
        self.gamepad.reset()
        self.lock.release()    
        #self.start()
        