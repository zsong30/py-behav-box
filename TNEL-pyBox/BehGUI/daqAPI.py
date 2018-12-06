#Python 3.7.1rc2 (v3.7.1rc2:6c06ef7dc3, Oct 13 2018, 15:44:37) [MSC v.1914 64 bit (AMD64)] on win32
#WType "help", "copyright", "credits" or "license()" for more information.
# -*- coding: utf-8 -*-
"""
Created on Nov. 30, 2018 by Mark Schatza
Communicates with layafette instruments DAQ 41510-NL
to control a behavioral box

NOTE: 1. Please Start Whisker server first
      2. Check daqAPI.py on this directory.
         be sure Devices are named properly:

         on Ephis-1 'Dev1' runs behavior box
                    'pciDAQ' runs open ephys

         on Ephis-2 'Dev2' runs behavior box
                    'Dev1' runs open ephis
"""
import nidaqmx
from nidaqmx.constants import (LineGrouping)
import time
dev = 'Dev2'

'''
Class for Digital Outputs. Can send (and maybe see what has been written. Hasn't been tested)
Also holds task information.
Must Call exampleclass.end() to correctly reset DAQ.

If using mult. lines use sendDByte function to send info sendDByte(3)
If using 1 line use sendDBit function to send info sendDBit(True)
'''
class InterfaceOut:
    def __init__(self, address):
        self.task = nidaqmx.Task()
        self.task.do_channels.add_do_chan(
            address,
            line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
        self.address = address

    def startTask(self):
        self.task.start()

    def sendDBit(self,TF):
        self.task.write(TF)
        enablePulse()

    def sendDByte(self,bits):
        self.task.write(bits)
        enablePulse()

    def rcvDI(self):
        return self.task.read()

    def end(self):
        self.task.close()
        
        


def enableSetup():
    enableAddress = dev + '/port0/line4'
    enableTask = InterfaceOut(enableAddress)
    enableTask.startTask()
    return enableTask


'''
!!! DEPRECIATED !!!!
Enable pulse for when sending bits/bytes.
(Doesn't need a global task because its just a pulse).
!! Plus it seems like making a class on port0 isn't a good idea.
'''
'''
def enablePulse():
    try:
            enable.enable()
        enable.end()
    except:
        print('woops')
    return
'''
def enablePulse():
    enable = dev + '/port0/line4'
    #print('Enable Pulse')
    sendPulse(enable,True)

def sendPulse(address,bits):
     while True:
         try:
            with nidaqmx.Task() as task:
                task.do_channels.add_do_chan(
                address,
                line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

                print(task.write(bits))
            break
         except:
            print('trying')

####################################################
##      OUTPUTS
####################################################
'''
Returns a new lever output task
'''
def leverOutputSetup():
    leverAddress = dev + '/port1/line0:1'
    levers = InterfaceOut(leverAddress)
    levers.startTask()
    return levers

'''
Returns a new left conditioning light task
'''
def conditioningLightsLeftSetup():
    conditioningLightAddress = dev + '/port1/line2'
    conditioningLight = InterfaceOut(conditioningLightAddress)
    conditioningLight.startTask()
    return conditioningLight

'''

'''
def conditioningLightsRightSetup():
    conditioningLightAddress = dev + '/port1/line3'
    conditioningLight = InterfaceOut(conditioningLightAddress)
    conditioningLight.startTask()
    return conditioningLight

'''
Returns a new food task
'''
def giveFoodSetup():
    foodAddress = dev + '/port1/line4'
    food = InterfaceOut(foodAddress)
    food.startTask()
    return food

'''
Returns a new food light task
'''
def foodLightSetup():
    foodLightAddress = dev + '/port1/line5'
    foodLight = InterfaceOut(foodLightAddress)
    foodLight.startTask()
    return foodLight


'''
Returns a new fan task
'''
def fanSetup():
    fanAddress = dev + '/port2/line2'
    fan = InterfaceOut(fanAddress)
    fan.startTask()
    return fan

'''
Returns a new cabin light task
'''
def cabinLightSetup():
    cabinLightAddress = dev + '/port2/line1'
    cabinLight = InterfaceOut(cabinLightAddress)
    cabinLight.startTask()
    return cabinLight


'''
Returns a new low tone task
'''
def lowToneSetup():
    lowToneAddress = dev + '/port2/line5:7'
    lowTone = InterfaceOut(lowToneAddress)
    lowTone.startTask()
    return lowTone

'''
Returns a new high tone Task
'''
def highToneSetup():
    highToneAddress = dev + '/port2/line5'
    highTone = InterfaceOut(highToneAddress)
    highTone.startTask()
    return highTone

####################################################
##   Inputs
####################################################

'''
Class for Digital Inputs. Can only use receive.
Also holds Task information.
Must Call exampleclass.end() to correctly reset DAQ.
'''
class InterfaceIn:
    def __init__(self, address):
        self.task = nidaqmx.Task()
        self.task.di_channels.add_di_chan(
            address,
            line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
        self.address = address

    def startTask(self):
        self.task.start()

    # Use to receive data, increase 1 to make a larger buffer size
    # Check READ_ALL_AVAILABLE in documentation for nidaqmx. Might be useful
    def rcvDI(self):
        return self.task.read()

    def end(self):
        self.task.stop()
        self.task.close()
        
class InterfaceInNEW:
    def __init__(self, address):
        self.task = nidaqmx.Task()
        self.task.di_channels.add_di_chan(
            address,
            line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
        self.address = address

    def startTask(self):
        self.task.start()

    # Use to receive data, increase 1 to make a larger buffer size
    # Check READ_ALL_AVAILABLE in documentation for nidaqmx. Might be useful
    def rcvDI(self):
        return self.task.read()

    def end(self):
        self.task.stop()
        self.task.close()

class debounce:
    def __init__(self, inputTask):
        self.REPEAT = False
        self.prev_signal = False

'''
Returns a new lever input task
'''        
def leverInputSetup():
    leftAddress = dev + '/port6/line0'
    checkPressLeft = InterfaceIn(leftAddress)
    rightAddress = dev + '/port6/line1'
    checkPressRight = InterfaceIn(rightAddress)
    checkPressLeft.startTask()
    checkPressRight.startTask()
    return checkPressLeft, checkPressRight


'''
Returns a new input task for when rat eats food
'''
def foodEatInputSetup():
    foodEatAddress = dev + '/port6/line2'
    foodEat = InterfaceIn(foodEatAddress)
    foodEat.startTask()
    return foodEat

'''
Returns left nose poke input Task
'''
def leftNoseInputSetup(): # 3
    leftNoseInputAddress = dev + '/port6/line3'
    leftNose = InterfaceIn(leftNoseInputAddress)
    leftNose.startTask()
    return leftNose

'''
Returns right nose poke input Task
'''
def rightNoseInputSetup():
    rightNoseInputAddress = dev + '/port6/line4'
    rightNose = InterfaceIn(rightNoseInputAddress)
    rightNose.startTask()
    return rightNose
