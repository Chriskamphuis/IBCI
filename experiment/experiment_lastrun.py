#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.03), Thu 11 Dec 2014 03:52:31 PM CET
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

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'experiment'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/home/koen/BCI/IBCI/experiment/experiment.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
welcome_text = visual.TextStim(win=win, ori=0, name='welcome_text',
    text='DOE DINGEN\n\nEN DOE ZE GOED GVD',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "select"
selectClock = core.Clock()


# Initialize components for Routine "left"
leftClock = core.Clock()
left_neutral = visual.ImageStim(win=win, name='left_neutral',
    image='../stimuli/neutral.jpg', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
side_left = visual.TextStim(win=win, ori=0, name='side_left',
    text='L',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)


# Initialize components for Routine "left_target"
left_targetClock = core.Clock()
target_left = visual.ImageStim(win=win, name='target_left',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "left_feedback"
left_feedbackClock = core.Clock()
feedback_left = visual.ImageStim(win=win, name='feedback_left',
    image='../stimuli/neutral_after.jpg', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "right"
rightClock = core.Clock()
right_base = visual.ImageStim(win=win, name='right_base',
    image='../stimuli/neutral.jpg', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
side_right = visual.TextStim(win=win, ori=0, name='side_right',
    text='R',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)


# Initialize components for Routine "right_target"
right_targetClock = core.Clock()
target_right = visual.ImageStim(win=win, name='target_right',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "right_feedback"
right_feedbackClock = core.Clock()
feedback_right = visual.ImageStim(win=win, name='feedback_right',
    image='../stimuli/neutral_after.jpg', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock 
frameN = -1
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
instructionsComponents = []
instructionsComponents.append(welcome_text)
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_text* updates
    if t >= 0.0 and welcome_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome_text.tStart = t  # underestimates by a little under one frame
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.setAutoDraw(True)
    if welcome_text.status == STARTED and t >= (0.0 + (5-win.monitorFramePeriod*0.75)): #most of one frame period left
        welcome_text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=40, method='sequential', 
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
    
    repsLeft = 0
    repsRight = 0
    preTargetDuration = random.uniform(0.5, 3)
    
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
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    leftBlock = data.TrialHandler(nReps=repsLeft, method='sequential', 
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
        # update component parameters for each repeat
        targets = ['color', 'size', 'shift', 'shift2']
        index = random.randint(0, 3)
        
        imageTargetPath = '../stimuli/left' + targets[index] + '.jpg'
        # keep track of which components have finished
        leftComponents = []
        leftComponents.append(left_neutral)
        leftComponents.append(side_left)
        for thisComponent in leftComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "left"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = leftClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *left_neutral* updates
            if t >= 0 and left_neutral.status == NOT_STARTED:
                # keep track of start time/frame for later
                left_neutral.tStart = t  # underestimates by a little under one frame
                left_neutral.frameNStart = frameN  # exact frame index
                left_neutral.setAutoDraw(True)
            if left_neutral.status == STARTED and t >= (2 + preTargetDuration-win.monitorFramePeriod*0.75): #most of one frame period left
                left_neutral.setAutoDraw(False)
            
            # *side_left* updates
            if t >= 1 and side_left.status == NOT_STARTED:
                # keep track of start time/frame for later
                side_left.tStart = t  # underestimates by a little under one frame
                side_left.frameNStart = frameN  # exact frame index
                side_left.setAutoDraw(True)
            if side_left.status == STARTED and t >= (1 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                side_left.setAutoDraw(False)
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in leftComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "left"-------
        for thisComponent in leftComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        #------Prepare to start Routine "left_target"-------
        t = 0
        left_targetClock.reset()  # clock 
        frameN = -1
        routineTimer.add(0.050000)
        # update component parameters for each repeat
        target_left.setImage(imageTargetPath)
        # keep track of which components have finished
        left_targetComponents = []
        left_targetComponents.append(target_left)
        for thisComponent in left_targetComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "left_target"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = left_targetClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *target_left* updates
            if t >= 0.0 and target_left.status == NOT_STARTED:
                # keep track of start time/frame for later
                target_left.tStart = t  # underestimates by a little under one frame
                target_left.frameNStart = frameN  # exact frame index
                target_left.setAutoDraw(True)
            if target_left.status == STARTED and t >= (0.0 + (0.05-win.monitorFramePeriod*0.75)): #most of one frame period left
                target_left.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in left_targetComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "left_target"-------
        for thisComponent in left_targetComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        #------Prepare to start Routine "left_feedback"-------
        t = 0
        left_feedbackClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        left_feedbackComponents = []
        left_feedbackComponents.append(feedback_left)
        for thisComponent in left_feedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "left_feedback"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = left_feedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_left* updates
            if t >= 0.0 and feedback_left.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedback_left.tStart = t  # underestimates by a little under one frame
                feedback_left.frameNStart = frameN  # exact frame index
                feedback_left.setAutoDraw(True)
            if feedback_left.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                feedback_left.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in left_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "left_feedback"-------
        for thisComponent in left_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed repsLeft repeats of 'leftBlock'
    
    
    # set up handler to look after randomisation of conditions etc
    rightBlock = data.TrialHandler(nReps=repsRight, method='sequential', 
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
        # update component parameters for each repeat
        targets = ['color', 'size', 'shift', 'shift2']
        index = random.randint(0, 3)
        
        imageTargetPath = '../stimuli/right' + targets[index] + '.jpg'
        # keep track of which components have finished
        rightComponents = []
        rightComponents.append(right_base)
        rightComponents.append(side_right)
        for thisComponent in rightComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "right"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = rightClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *right_base* updates
            if t >= 0.0 and right_base.status == NOT_STARTED:
                # keep track of start time/frame for later
                right_base.tStart = t  # underestimates by a little under one frame
                right_base.frameNStart = frameN  # exact frame index
                right_base.setAutoDraw(True)
            if right_base.status == STARTED and t >= (0.0 + (2 + preTargetDuration-win.monitorFramePeriod*0.75)): #most of one frame period left
                right_base.setAutoDraw(False)
            
            # *side_right* updates
            if t >= 1 and side_right.status == NOT_STARTED:
                # keep track of start time/frame for later
                side_right.tStart = t  # underestimates by a little under one frame
                side_right.frameNStart = frameN  # exact frame index
                side_right.setAutoDraw(True)
            if side_right.status == STARTED and t >= (1 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                side_right.setAutoDraw(False)
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rightComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "right"-------
        for thisComponent in rightComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        #------Prepare to start Routine "right_target"-------
        t = 0
        right_targetClock.reset()  # clock 
        frameN = -1
        routineTimer.add(0.050000)
        # update component parameters for each repeat
        target_right.setImage(imageTargetPath)
        # keep track of which components have finished
        right_targetComponents = []
        right_targetComponents.append(target_right)
        for thisComponent in right_targetComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "right_target"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = right_targetClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *target_right* updates
            if t >= 0.0 and target_right.status == NOT_STARTED:
                # keep track of start time/frame for later
                target_right.tStart = t  # underestimates by a little under one frame
                target_right.frameNStart = frameN  # exact frame index
                target_right.setAutoDraw(True)
            if target_right.status == STARTED and t >= (0.0 + (0.05-win.monitorFramePeriod*0.75)): #most of one frame period left
                target_right.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in right_targetComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "right_target"-------
        for thisComponent in right_targetComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        #------Prepare to start Routine "right_feedback"-------
        t = 0
        right_feedbackClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        right_feedbackComponents = []
        right_feedbackComponents.append(feedback_right)
        for thisComponent in right_feedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "right_feedback"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = right_feedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_right* updates
            if t >= 0.0 and feedback_right.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedback_right.tStart = t  # underestimates by a little under one frame
                feedback_right.frameNStart = frameN  # exact frame index
                feedback_right.setAutoDraw(True)
            if feedback_right.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                feedback_right.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in right_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "right_feedback"-------
        for thisComponent in right_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed repsRight repeats of 'rightBlock'
    
    thisExp.nextEntry()
    
# completed 40 repeats of 'trials'




win.close()
core.quit()
