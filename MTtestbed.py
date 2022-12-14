#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on November 15, 2022, at 14:16
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
    originPath='H:\\git\\UncertainStimuliMT\\MTtestbed.py',
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
welcome_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Trial" ---
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
    text='How confident are you in estimating the uncertainty of the stimuli?',
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

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "WelcomeScreen" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
welcome_resp.keys = []
welcome_resp.rt = []
_welcome_resp_allKeys = []
# keep track of which components have finished
WelcomeScreenComponents = [welcome_txt, welcome_resp]
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
    
    # *welcome_resp* updates
    waitOnFlip = False
    if welcome_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_resp.frameNStart = frameN  # exact frame index
        welcome_resp.tStart = t  # local t and not account for scr refresh
        welcome_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_resp, 'tStartRefresh')  # time at next scr refresh
        welcome_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_resp.clock.reset)  # t=0 on next screen flip
    if welcome_resp.status == STARTED and not waitOnFlip:
        theseKeys = welcome_resp.getKeys(keyList=['space'], waitRelease=False)
        _welcome_resp_allKeys.extend(theseKeys)
        if len(_welcome_resp_allKeys):
            welcome_resp.keys = _welcome_resp_allKeys[-1].name  # just the last key pressed
            welcome_resp.rt = _welcome_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
TrialsLoop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
    seed=None, name='TrialsLoop')
thisExp.addLoop(TrialsLoop)  # add the loop to the experiment
thisTrialsLoop = TrialsLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsLoop.rgb)
if thisTrialsLoop != None:
    for paramName in thisTrialsLoop:
        exec('{} = thisTrialsLoop[paramName]'.format(paramName))

for thisTrialsLoop in TrialsLoop:
    currentLoop = TrialsLoop
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsLoop.rgb)
    if thisTrialsLoop != None:
        for paramName in thisTrialsLoop:
            exec('{} = thisTrialsLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Trial" ---
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
    TrialComponents = [intrText, RefStim, TargetStim, EstResp, textboxText, ME_submitButton, resp_mouse]
    for thisComponent in TrialComponents:
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
    
    # --- Run Routine "Trial" ---
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
        if ME_submitButton.status == NOT_STARTED and if(EstResp.):
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
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Trial" ---
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    TrialsLoop.addData('EstResp.text',EstResp.text)
    # store data for TrialsLoop (TrialHandler)
    TrialsLoop.addData('resp_mouse.x', resp_mouse.x)
    TrialsLoop.addData('resp_mouse.y', resp_mouse.y)
    TrialsLoop.addData('resp_mouse.leftButton', resp_mouse.leftButton)
    TrialsLoop.addData('resp_mouse.midButton', resp_mouse.midButton)
    TrialsLoop.addData('resp_mouse.rightButton', resp_mouse.rightButton)
    TrialsLoop.addData('resp_mouse.time', resp_mouse.time)
    TrialsLoop.addData('resp_mouse.clicked_name', resp_mouse.clicked_name)
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
    TrialsLoop.addData('slider.response', slider.getRating())
    TrialsLoop.addData('slider.rt', slider.getRT())
    # store data for TrialsLoop (TrialHandler)
    TrialsLoop.addData('mouse.x', mouse.x)
    TrialsLoop.addData('mouse.y', mouse.y)
    TrialsLoop.addData('mouse.leftButton', mouse.leftButton)
    TrialsLoop.addData('mouse.midButton', mouse.midButton)
    TrialsLoop.addData('mouse.rightButton', mouse.rightButton)
    TrialsLoop.addData('mouse.time', mouse.time)
    TrialsLoop.addData('mouse.clicked_name', mouse.clicked_name)
    # the Routine "RateConfidence" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'TrialsLoop'


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
