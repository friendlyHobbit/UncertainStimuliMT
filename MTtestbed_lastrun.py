#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on November 15, 2022, at 17:10
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'MTtestbed'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='H:\\git\\UncertainStimuliMT\\MTtestbed_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "WelcomeScreen" ---
welcome_txt = visual.TextStim(win=win, name='welcome_txt',
    text='Welcome, instructions go here.\n\nPress SPACE to start the experiment',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
startButton = visual.ImageStim(
    win=win,
    name='startButton', 
    image='resp_button.png', mask=None, anchor='center',
    ori=0.0, pos=(0.46, -0.3), size=(0.5, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
start_mouse = event.Mouse(win=win)
x, y = [None, None]
start_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "SetReference" ---
# Run 'Begin Experiment' code from CheckInput
def TypeCastResp(input_var):
    try:
        float(input_var)
        #print(float(input_var))
        # enable submit button
        return True
    except:
        #print("participant did not enter a number")
        # show text on screen
        return False
instrText_ref = visual.TextStim(win=win, name='instrText_ref',
    text='Please set a reference number for this stimuli.',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
SetRefStim = visual.ImageStim(
    win=win,
    name='SetRefStim', 
    image='stim/ph4.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
SetRefResp = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, -0.3),     letterHeight=0.05,
     size=(0.4, 0.1), borderWidth=2.0,
     color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=[1.0000, 1.0000, 1.0000], borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='SetRefResp',
     autoLog=True,
)
Ref_submitButton = visual.ImageStim(
    win=win,
    name='Ref_submitButton', 
    image='resp_button.png', mask=None, anchor='center',
    ori=0.0, pos=(0.46, -0.3), size=(0.5, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
ref_resp_mouse = event.Mouse(win=win)
x, y = [None, None]
ref_resp_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "Trial1" ---
intrText = visual.TextStim(win=win, name='intrText',
    text='Uncertainty is 40',
    font='Open Sans',
    pos=(0.3, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
RefStim = visual.ImageStim(
    win=win,
    name='RefStim', 
    image='stim/ph4.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.3), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
TargetStim = visual.ImageStim(
    win=win,
    name='TargetStim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
EstResp = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, -0.3),     letterHeight=0.05,
     size=(0.4, 0.1), borderWidth=2.0,
     color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=[1.0000, 1.0000, 1.0000], borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='EstResp',
     autoLog=True,
)
textboxText = visual.TextStim(win=win, name='textboxText',
    text='Enter estimate here',
    font='Open Sans',
    pos=(0.0, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
ME_submitButton = visual.ImageStim(
    win=win,
    name='ME_submitButton', 
    image='resp_button.png', mask=None, anchor='center',
    ori=0.0, pos=(0.46, -0.3), size=(0.5, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
resp_mouse = event.Mouse(win=win)
x, y = [None, None]
resp_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "RateConfidence" ---
questionTXT = visual.TextStim(win=win, name='questionTXT',
    text='How confident are you in estimating the uncertainty of the last stimulus?',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.0), units=None,
    labels=["Very unconfident", "Very confident"], ticks=(1, 2, 3, 4, 5, 6 ,7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)
submitButton = visual.ImageStim(
    win=win,
    name='submitButton', 
    image='resp_button.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.4), size=(0.5, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "StategyQ" ---
Qstrategy = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='Qstrategy',
     autoLog=True,
)
QstatTXT = visual.TextStim(win=win, name='QstatTXT',
    text='What strategy did you use to determine the uncertainty of the stimuli?',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
submitQuestionButton = visual.ImageStim(
    win=win,
    name='submitQuestionButton', 
    image='resp_button.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.4), size=(0.5, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()

# --- Initialize components for Routine "EndScreen" ---
endTXT = visual.TextStim(win=win, name='endTXT',
    text='Thank you for participating!\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "WelcomeScreen" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the start_mouse
start_mouse.x = []
start_mouse.y = []
start_mouse.leftButton = []
start_mouse.midButton = []
start_mouse.rightButton = []
start_mouse.time = []
start_mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
WelcomeScreenComponents = [welcome_txt, startButton, start_mouse]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "WelcomeScreen" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_txt* updates
    if welcome_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_txt.frameNStart = frameN  # exact frame index
        welcome_txt.tStart = t  # local t and not account for scr refresh
        welcome_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_txt, 'tStartRefresh')  # time at next scr refresh
        welcome_txt.setAutoDraw(True)
    
    # *startButton* updates
    if startButton.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        startButton.frameNStart = frameN  # exact frame index
        startButton.tStart = t  # local t and not account for scr refresh
        startButton.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startButton, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'startButton.started')
        startButton.setAutoDraw(True)
    # *start_mouse* updates
    if start_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_mouse.frameNStart = frameN  # exact frame index
        start_mouse.tStart = t  # local t and not account for scr refresh
        start_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_mouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('start_mouse.started', t)
        start_mouse.status = STARTED
        start_mouse.mouseClock.reset()
        prevButtonState = start_mouse.getPressed()  # if button is down already this ISN'T a new click
    if start_mouse.status == STARTED:  # only update if started and not finished!
        buttons = start_mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(Ref_submitButton)
                    clickableList = Ref_submitButton
                except:
                    clickableList = [Ref_submitButton]
                for obj in clickableList:
                    if obj.contains(start_mouse):
                        gotValidClick = True
                        start_mouse.clicked_name.append(obj.name)
                x, y = start_mouse.getPos()
                start_mouse.x.append(x)
                start_mouse.y.append(y)
                buttons = start_mouse.getPressed()
                start_mouse.leftButton.append(buttons[0])
                start_mouse.midButton.append(buttons[1])
                start_mouse.rightButton.append(buttons[2])
                start_mouse.time.append(start_mouse.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "WelcomeScreen" ---
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('start_mouse.x', start_mouse.x)
thisExp.addData('start_mouse.y', start_mouse.y)
thisExp.addData('start_mouse.leftButton', start_mouse.leftButton)
thisExp.addData('start_mouse.midButton', start_mouse.midButton)
thisExp.addData('start_mouse.rightButton', start_mouse.rightButton)
thisExp.addData('start_mouse.time', start_mouse.time)
thisExp.addData('start_mouse.clicked_name', start_mouse.clicked_name)
thisExp.nextEntry()
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
BigTrialLoop = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='BigTrialLoop')
thisExp.addLoop(BigTrialLoop)  # add the loop to the experiment
thisBigTrialLoop = BigTrialLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBigTrialLoop.rgb)
if thisBigTrialLoop != None:
    for paramName in thisBigTrialLoop:
        exec('{} = thisBigTrialLoop[paramName]'.format(paramName))

for thisBigTrialLoop in BigTrialLoop:
    currentLoop = BigTrialLoop
    # abbreviate parameter names if possible (e.g. rgb = thisBigTrialLoop.rgb)
    if thisBigTrialLoop != None:
        for paramName in thisBigTrialLoop:
            exec('{} = thisBigTrialLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "SetReference" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    SetRefResp.reset()
    SetRefResp.setText('')
    # setup some python lists for storing info about the ref_resp_mouse
    ref_resp_mouse.x = []
    ref_resp_mouse.y = []
    ref_resp_mouse.leftButton = []
    ref_resp_mouse.midButton = []
    ref_resp_mouse.rightButton = []
    ref_resp_mouse.time = []
    ref_resp_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    SetReferenceComponents = [instrText_ref, SetRefStim, SetRefResp, Ref_submitButton, ref_resp_mouse]
    for thisComponent in SetReferenceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SetReference" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from CheckInput
        
            
        #print("EstResp.text: ")
        #print(EstResp.text)
        #print("len(EstResp.text): ")
        #print(len(EstResp.text))
        #print(type(EstResp.text))
        
        # *instrText_ref* updates
        if instrText_ref.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrText_ref.frameNStart = frameN  # exact frame index
            instrText_ref.tStart = t  # local t and not account for scr refresh
            instrText_ref.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrText_ref, 'tStartRefresh')  # time at next scr refresh
            instrText_ref.setAutoDraw(True)
        
        # *SetRefStim* updates
        if SetRefStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SetRefStim.frameNStart = frameN  # exact frame index
            SetRefStim.tStart = t  # local t and not account for scr refresh
            SetRefStim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SetRefStim, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'SetRefStim.started')
            SetRefStim.setAutoDraw(True)
        
        # *SetRefResp* updates
        if SetRefResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SetRefResp.frameNStart = frameN  # exact frame index
            SetRefResp.tStart = t  # local t and not account for scr refresh
            SetRefResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SetRefResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'SetRefResp.started')
            SetRefResp.setAutoDraw(True)
        
        # *Ref_submitButton* updates
        if Ref_submitButton.status == NOT_STARTED and TypeCastResp(SetRefResp.text) == True:
            # keep track of start time/frame for later
            Ref_submitButton.frameNStart = frameN  # exact frame index
            Ref_submitButton.tStart = t  # local t and not account for scr refresh
            Ref_submitButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ref_submitButton, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Ref_submitButton.started')
            Ref_submitButton.setAutoDraw(True)
        # *ref_resp_mouse* updates
        if ref_resp_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ref_resp_mouse.frameNStart = frameN  # exact frame index
            ref_resp_mouse.tStart = t  # local t and not account for scr refresh
            ref_resp_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ref_resp_mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('ref_resp_mouse.started', t)
            ref_resp_mouse.status = STARTED
            ref_resp_mouse.mouseClock.reset()
            prevButtonState = ref_resp_mouse.getPressed()  # if button is down already this ISN'T a new click
        if ref_resp_mouse.status == STARTED:  # only update if started and not finished!
            buttons = ref_resp_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(Ref_submitButton)
                        clickableList = Ref_submitButton
                    except:
                        clickableList = [Ref_submitButton]
                    for obj in clickableList:
                        if obj.contains(ref_resp_mouse):
                            gotValidClick = True
                            ref_resp_mouse.clicked_name.append(obj.name)
                    x, y = ref_resp_mouse.getPos()
                    ref_resp_mouse.x.append(x)
                    ref_resp_mouse.y.append(y)
                    buttons = ref_resp_mouse.getPressed()
                    ref_resp_mouse.leftButton.append(buttons[0])
                    ref_resp_mouse.midButton.append(buttons[1])
                    ref_resp_mouse.rightButton.append(buttons[2])
                    ref_resp_mouse.time.append(ref_resp_mouse.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SetReferenceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SetReference" ---
    for thisComponent in SetReferenceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from CheckInput
    #print("TypeCastResp(EstResp.text)")
    #print(TypeCastResp(EstResp.text))
    
    if TypeCastResp(EstResp.text) == True:
        print("this is false")
    else:
        print("this is true")
    BigTrialLoop.addData('SetRefResp.text',SetRefResp.text)
    # store data for BigTrialLoop (TrialHandler)
    BigTrialLoop.addData('ref_resp_mouse.x', ref_resp_mouse.x)
    BigTrialLoop.addData('ref_resp_mouse.y', ref_resp_mouse.y)
    BigTrialLoop.addData('ref_resp_mouse.leftButton', ref_resp_mouse.leftButton)
    BigTrialLoop.addData('ref_resp_mouse.midButton', ref_resp_mouse.midButton)
    BigTrialLoop.addData('ref_resp_mouse.rightButton', ref_resp_mouse.rightButton)
    BigTrialLoop.addData('ref_resp_mouse.time', ref_resp_mouse.time)
    BigTrialLoop.addData('ref_resp_mouse.clicked_name', ref_resp_mouse.clicked_name)
    # the Routine "SetReference" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    TrialsLoop1 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions.xlsx'),
        seed=None, name='TrialsLoop1')
    thisExp.addLoop(TrialsLoop1)  # add the loop to the experiment
    thisTrialsLoop1 = TrialsLoop1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsLoop1.rgb)
    if thisTrialsLoop1 != None:
        for paramName in thisTrialsLoop1:
            exec('{} = thisTrialsLoop1[paramName]'.format(paramName))
    
    for thisTrialsLoop1 in TrialsLoop1:
        currentLoop = TrialsLoop1
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsLoop1.rgb)
        if thisTrialsLoop1 != None:
            for paramName in thisTrialsLoop1:
                exec('{} = thisTrialsLoop1[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Trial1" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        EstResp.reset()
        EstResp.setText('')
        # setup some python lists for storing info about the resp_mouse
        resp_mouse.x = []
        resp_mouse.y = []
        resp_mouse.leftButton = []
        resp_mouse.midButton = []
        resp_mouse.rightButton = []
        resp_mouse.time = []
        resp_mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        Trial1Components = [intrText, RefStim, TargetStim, EstResp, textboxText, ME_submitButton, resp_mouse]
        for thisComponent in Trial1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Trial1" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *intrText* updates
            if intrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                intrText.frameNStart = frameN  # exact frame index
                intrText.tStart = t  # local t and not account for scr refresh
                intrText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(intrText, 'tStartRefresh')  # time at next scr refresh
                intrText.setAutoDraw(True)
            
            # *RefStim* updates
            if RefStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                RefStim.frameNStart = frameN  # exact frame index
                RefStim.tStart = t  # local t and not account for scr refresh
                RefStim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RefStim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RefStim.started')
                RefStim.setAutoDraw(True)
            
            # *TargetStim* updates
            if TargetStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TargetStim.frameNStart = frameN  # exact frame index
                TargetStim.tStart = t  # local t and not account for scr refresh
                TargetStim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TargetStim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TargetStim.started')
                TargetStim.setAutoDraw(True)
            if TargetStim.status == STARTED:  # only update if drawing
                TargetStim.setImage(visStim, log=False)
            
            # *EstResp* updates
            if EstResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                EstResp.frameNStart = frameN  # exact frame index
                EstResp.tStart = t  # local t and not account for scr refresh
                EstResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EstResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EstResp.started')
                EstResp.setAutoDraw(True)
            
            # *textboxText* updates
            if textboxText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textboxText.frameNStart = frameN  # exact frame index
                textboxText.tStart = t  # local t and not account for scr refresh
                textboxText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textboxText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textboxText.started')
                textboxText.setAutoDraw(True)
            
            # *ME_submitButton* updates
            if ME_submitButton.status == NOT_STARTED and TypeCastResp(EstResp.text) == True:
                # keep track of start time/frame for later
                ME_submitButton.frameNStart = frameN  # exact frame index
                ME_submitButton.tStart = t  # local t and not account for scr refresh
                ME_submitButton.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ME_submitButton, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ME_submitButton.started')
                ME_submitButton.setAutoDraw(True)
            # *resp_mouse* updates
            if resp_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp_mouse.frameNStart = frameN  # exact frame index
                resp_mouse.tStart = t  # local t and not account for scr refresh
                resp_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('resp_mouse.started', t)
                resp_mouse.status = STARTED
                resp_mouse.mouseClock.reset()
                prevButtonState = resp_mouse.getPressed()  # if button is down already this ISN'T a new click
            if resp_mouse.status == STARTED:  # only update if started and not finished!
                buttons = resp_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(ME_submitButton)
                            clickableList = ME_submitButton
                        except:
                            clickableList = [ME_submitButton]
                        for obj in clickableList:
                            if obj.contains(resp_mouse):
                                gotValidClick = True
                                resp_mouse.clicked_name.append(obj.name)
                        x, y = resp_mouse.getPos()
                        resp_mouse.x.append(x)
                        resp_mouse.y.append(y)
                        buttons = resp_mouse.getPressed()
                        resp_mouse.leftButton.append(buttons[0])
                        resp_mouse.midButton.append(buttons[1])
                        resp_mouse.rightButton.append(buttons[2])
                        resp_mouse.time.append(resp_mouse.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # abort routine on response
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Trial1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Trial1" ---
        for thisComponent in Trial1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        TrialsLoop1.addData('EstResp.text',EstResp.text)
        # store data for TrialsLoop1 (TrialHandler)
        TrialsLoop1.addData('resp_mouse.x', resp_mouse.x)
        TrialsLoop1.addData('resp_mouse.y', resp_mouse.y)
        TrialsLoop1.addData('resp_mouse.leftButton', resp_mouse.leftButton)
        TrialsLoop1.addData('resp_mouse.midButton', resp_mouse.midButton)
        TrialsLoop1.addData('resp_mouse.rightButton', resp_mouse.rightButton)
        TrialsLoop1.addData('resp_mouse.time', resp_mouse.time)
        TrialsLoop1.addData('resp_mouse.clicked_name', resp_mouse.clicked_name)
        # the Routine "Trial1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'TrialsLoop1'
    
    
    # --- Prepare to start Routine "RateConfidence" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    slider.reset()
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    RateConfidenceComponents = [questionTXT, slider, submitButton, mouse]
    for thisComponent in RateConfidenceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "RateConfidence" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *questionTXT* updates
        if questionTXT.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            questionTXT.frameNStart = frameN  # exact frame index
            questionTXT.tStart = t  # local t and not account for scr refresh
            questionTXT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(questionTXT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'questionTXT.started')
            questionTXT.setAutoDraw(True)
        
        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider.started')
            slider.setAutoDraw(True)
        
        # *submitButton* updates
        if submitButton.status == NOT_STARTED and slider.rating:
            # keep track of start time/frame for later
            submitButton.frameNStart = frameN  # exact frame index
            submitButton.tStart = t  # local t and not account for scr refresh
            submitButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(submitButton, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'submitButton.started')
            submitButton.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and slider.rating:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(submitButton)
                        clickableList = submitButton
                    except:
                        clickableList = [submitButton]
                    for obj in clickableList:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RateConfidenceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "RateConfidence" ---
    for thisComponent in RateConfidenceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    BigTrialLoop.addData('slider.response', slider.getRating())
    BigTrialLoop.addData('slider.rt', slider.getRT())
    # store data for BigTrialLoop (TrialHandler)
    BigTrialLoop.addData('mouse.x', mouse.x)
    BigTrialLoop.addData('mouse.y', mouse.y)
    BigTrialLoop.addData('mouse.leftButton', mouse.leftButton)
    BigTrialLoop.addData('mouse.midButton', mouse.midButton)
    BigTrialLoop.addData('mouse.rightButton', mouse.rightButton)
    BigTrialLoop.addData('mouse.time', mouse.time)
    BigTrialLoop.addData('mouse.clicked_name', mouse.clicked_name)
    # the Routine "RateConfidence" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'BigTrialLoop'


# --- Prepare to start Routine "StategyQ" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Qstrategy.reset()
# setup some python lists for storing info about the mouse_2
mouse_2.clicked_name = []
gotValidClick = False  # until a click is received
# Run 'Begin Routine' code from code_2
print("len(Qstrategy)")
print(len(Qstrategy.text))
# keep track of which components have finished
StategyQComponents = [Qstrategy, QstatTXT, submitQuestionButton, mouse_2]
for thisComponent in StategyQComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "StategyQ" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Qstrategy* updates
    if Qstrategy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Qstrategy.frameNStart = frameN  # exact frame index
        Qstrategy.tStart = t  # local t and not account for scr refresh
        Qstrategy.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Qstrategy, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Qstrategy.started')
        Qstrategy.setAutoDraw(True)
    
    # *QstatTXT* updates
    if QstatTXT.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        QstatTXT.frameNStart = frameN  # exact frame index
        QstatTXT.tStart = t  # local t and not account for scr refresh
        QstatTXT.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(QstatTXT, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'QstatTXT.started')
        QstatTXT.setAutoDraw(True)
    
    # *submitQuestionButton* updates
    if submitQuestionButton.status == NOT_STARTED and len(Qstrategy.text)!=0:
        # keep track of start time/frame for later
        submitQuestionButton.frameNStart = frameN  # exact frame index
        submitQuestionButton.tStart = t  # local t and not account for scr refresh
        submitQuestionButton.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(submitQuestionButton, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'submitQuestionButton.started')
        submitQuestionButton.setAutoDraw(True)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(submitQuestionButton)
                    clickableList = submitQuestionButton
                except:
                    clickableList = [submitQuestionButton]
                for obj in clickableList:
                    if obj.contains(mouse_2):
                        gotValidClick = True
                        mouse_2.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StategyQComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "StategyQ" ---
for thisComponent in StategyQComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Qstrategy.text',Qstrategy.text)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "StategyQ" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "EndScreen" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
EndScreenComponents = [endTXT]
for thisComponent in EndScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EndScreen" ---
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endTXT* updates
    if endTXT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endTXT.frameNStart = frameN  # exact frame index
        endTXT.tStart = t  # local t and not account for scr refresh
        endTXT.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endTXT, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'endTXT.started')
        endTXT.setAutoDraw(True)
    if endTXT.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > endTXT.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            endTXT.tStop = t  # not accounting for scr refresh
            endTXT.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endTXT.stopped')
            endTXT.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EndScreen" ---
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
