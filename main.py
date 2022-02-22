import vgamepad as vg
import os,sys,time
from windowcapture import WindowCapture
from detection import Detection
from vcontroller import vController
from ircbot import RigBot

if len(sys.argv) != 3:
    print("Correct usage: ./main.py RiggersNicknameonIRC modelname.jpg")
    exit()
rigger = str(sys.argv[1])

os.chdir(os.path.dirname(os.path.abspath(__file__)))

homedata = int(0)
awaydata = int(0)

wincap = WindowCapture('Windowed Projector (Preview)')

detector = Detection(sys.argv[2])

c1 = vController(0)
c2 = vController(1)

print("Plug in your controllers now, and have PES open on the main menu.")

homepassword = input("Home manager?")
awaypassword = input("Away manager?")

ircbot = RigBot("#4chancup", "Telerig", rigger, homepassword, awaypassword, "irc.implyingrigged.info")
ircbot.start()

c1.reset()
#menu over to coach
"""c1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
c1.update()
time.sleep(0.5)
c1.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
c1.update()
time.sleep(10)"""
c1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
c1.update()
time.sleep(0.35)
c1.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
c1.update()
time.sleep(0.95)
c1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
c1.update()
time.sleep(0.35)
c1.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
c1.update()
time.sleep(1.5)
c1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
c2.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
c1.update()
c2.update()
time.sleep(0.35)
c1.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
c1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
c2.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
c2.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
c1.update()
c2.update()
time.sleep(0.25)
c1.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
c2.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
c1.update()
c2.update()
time.sleep(0.75)
c1.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
c1.update()
time.sleep(0.35)
c1.reset()
wincap.start()
detector.start()
c1.start()
c2.start()  

while True:
        #try:
            wincap.get_screenshot()
            detector.update(wincap.screenshot)
            homedata = ircbot.retrievehomeinput()
            awaydata = ircbot.retrieveawayinput()
            #print(homedata, awaydata)
            #print(detector.confidence)
            if detector.confidence > 0.90 and (homedata != 0 or awaydata != 0):
                c1.stop()
                c2.stop()
                c1.autoinput(homedata)
                c2.autoinput(awaydata)
                c1.start()
                c2.start()
        #except KeyboardInterrupt:
            #try:
            #    homepassword = input("Home manager?")
            #    awaypassword = input("Away manager?")
            #    ircbot.updatehomenickname(homepassword)
            #    ircbot.updateawaynickname(awaypassword)
            #except KeyboardInterrupt:
            #    ircbot.die()
            #    c1.stop()
            #    c2.stop()
            #    wincap.stop()
            #    detector.stop()
            #    ircbot.stop()
            #    quit()


