#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.79.01), Wed 03 Dec 2014 01:13:47 PM CET
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Store info about the experiment session
expName = u'experiment'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
filename = 'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/home/koen/BCI/IBCI/experiment/experiment.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "select"
selectClock = core.Clock()
repsLeft = 0
repsRight = 0

# Initialize components for Routine "left"
leftClock = core.Clock()
image = visual.ImageStim(win=win, name='image',
    image=u'../stimuli/leftbase.jpg', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=False, depth=0.0)

# Initialize components for Routine "right"
rightClock = core.Clock()
image_2 = visual.ImageStim(win=win, name='image_2',
    image=u'../stimuli/rightbase.jpg', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=False, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=40, method=u'sequential', 
    extraInfo=expInfo, originPath=u'/home/koen/BCI/IBCI/experiment/experiment.psyexp',
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "select"-------
    t = 0
    selectClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    import random
    
    if random.randint(0, 1) == 0:
        repsLeft = 1
        repsRight = 0
    else:
        repsLeft = 0
        repsRight = 1
    # keep track of which components have finished
    selectComponents = []
    for thisComponent in selectComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "select"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = selectClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in selectComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "select"-------
    for thisComponent in selectComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # set up handler to look after randomisation of conditions etc
    leftBlock = data.TrialHandler(nReps=repsLeft, method=u'sequential', 
        extraInfo=expInfo, originPath=u'/home/koen/BCI/IBCI/experiment/experiment.psyexp',
        trialList=[None],
        seed=None, name='leftBlock')
    thisExp.addLoop(leftBlock)  # add the loop to the experiment
    thisLeftBlock = leftBlock.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisLeftBlock.rgb)
    if thisLeftBlock != None:
        for paramName in thisLeftBlock.keys():
            exec(paramName + '= thisLeftBlock.' + paramName)
    
    for thisLeftBlock in leftBlock:
        currentLoop = leftBlock
        # abbreviate parameter names if possible (e.g. rgb = thisLeftBlock.rgb)
        if thisLeftBlock != None:
            for paramName in thisLeftBlock.keys():
                exec(paramName + '= thisLeftBlock.' + paramName)
        
        #------Prepare to start Routine "left"-------
        t = 0
        leftClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        leftComponents = []
        leftComponents.append(image)
        for thisComponent in leftComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "left"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = leftClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            if t >= 0.0 and image.status == NOT_STARTED:
                # keep track of start time/frame for later
                image.tStart = t  # underestimates by a little under one frame
                image.frameNStart = frameN  # exact frame index
                image.setAutoDraw(True)
            elif image.status == STARTED and t >= (0.0 + 1.0):
                image.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in leftComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the [Esc] key)
            if event.getKeys(["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "left"-------
        for thisComponent in leftComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed repsLeft repeats of 'leftBlock'
    
    
    # set up handler to look after randomisation of conditions etc
    rightBlock = data.TrialHandler(nReps=repsRight, method=u'random', 
        extraInfo=expInfo, originPath=u'/home/koen/BCI/IBCI/experiment/experiment.psyexp',
        trialList=[None],
        seed=None, name='rightBlock')
    thisExp.addLoop(rightBlock)  # add the loop to the experiment
    thisRightBlock = rightBlock.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisRightBlock.rgb)
    if thisRightBlock != None:
        for paramName in thisRightBlock.keys():
            exec(paramName + '= thisRightBlock.' + paramName)
    
    for thisRightBlock in rightBlock:
        currentLoop = rightBlock
        # abbreviate parameter names if possible (e.g. rgb = thisRightBlock.rgb)
        if thisRightBlock != None:
            for paramName in thisRightBlock.keys():
                exec(paramName + '= thisRightBlock.' + paramName)
        
        #------Prepare to start Routine "right"-------
        t = 0
        rightClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        rightComponents = []
        rightComponents.append(image_2)
        for thisComponent in rightComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "right"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rightClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_2* updates
            if t >= 0.0 and image_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_2.tStart = t  # underestimates by a little under one frame
                image_2.frameNStart = frameN  # exact frame index
                image_2.setAutoDraw(True)
            elif image_2.status == STARTED and t >= (0.0 + 1.0):
                image_2.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rightComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the [Esc] key)
            if event.getKeys(["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "right"-------
        for thisComponent in rightComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed repsRight repeats of 'rightBlock'
    
    thisExp.nextEntry()
    
# completed 40 repeats of 'trials'


win.close()
core.quit()
