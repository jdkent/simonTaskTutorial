#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.3),
    on Wed 25 Oct 2017 02:04:50 PM CDT
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'simon_task'  # from the Builder filename that created this script
expInfo = {u'conterbalance': u'', u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1366, 768), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "simon_setup"
simon_setupClock = core.Clock()


# Initialize components for Routine "simon_trial"
simon_trialClock = core.Clock()
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text=u'+',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);
left_stim = visual.TextStim(win=win, name='left_stim',
    text='default text',
    font=u'Arial',
    pos=(-0.5, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0);
right_stim = visual.TextStim(win=win, name='right_stim',
    text='default text',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0);
ITI = visual.TextStim(win=win, name='ITI',
    text=u'+',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'simon_task_order.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "simon_setup"-------
    t = 0
    simon_setupClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if expInfo['counterbalance'] == '0':
        bindings = {'X': 'm', 'O': 'z'}
        if thisTrial['condition'] == 'incongruent':
            if thisTrial['stim'] == 'X':
                left_stim_text = thisTrial['stim']
                right_stim_text = ''
                ans = 'm'
            elif thisTrial['stim'] == 'O':
                left_stim_text = ''
                right_stim_text = thisTrial['stim']
                ans = 'z'
        elif thisTrial['condition'] == 'congruent':
            if thisTrial['stim'] == 'X':
                left_stim_text = ''
                right_stim_text = thisTrial['stim']
                ans = 'm'
            elif thisTrial['stim'] == 'O':
                left_stim_text = thisTrial['stim']
                right_stim_text = ''
                ans='z'
    elif expInfo['counterbalance'] == '1':
        bindings = {'O': 'm', 'X': 'z'}
        if thisTrial['condition'] == 'incongruent':
            if thisTrial['stim'] == 'X':
                left_stim_text = ''
                right_stim_text = thisTrial['stim']
                ans = 'z'
            elif thisTrial['stim'] == 'O':
                left_stim_text = thisTrial['stim']
                right_stim_text = ''
                ans = 'm'
        elif thisTrial['condition'] == 'congruent':
            if thisTrial['stim'] == 'X':
                left_stim_text = thisTrial['stim']
                right_stim_text = ''
                ans = 'z'
            elif thisTrial['stim'] == 'O':
                left_stim_text = ''
                right_stim_text = thisTrial['stim']
                ans = 'm'
    # keep track of which components have finished
    simon_setupComponents = []
    for thisComponent in simon_setupComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "simon_setup"-------
    while continueRoutine:
        # get current time
        t = simon_setupClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in simon_setupComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "simon_setup"-------
    for thisComponent in simon_setupComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "simon_setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "simon_trial"-------
    t = 0
    simon_trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    left_stim.setText(left_stim_text)
    right_stim.setText(right_stim_text)
    resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    simon_trialComponents = [fixation_cross, left_stim, right_stim, ITI, resp]
    for thisComponent in simon_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "simon_trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = simon_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross* updates
        if t >= 0.0 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)
        
        # *left_stim* updates
        if t >= 0.0 and left_stim.status == NOT_STARTED:
            # keep track of start time/frame for later
            left_stim.tStart = t
            left_stim.frameNStart = frameN  # exact frame index
            left_stim.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if left_stim.status == STARTED and t >= frameRemains:
            left_stim.setAutoDraw(False)
        
        # *right_stim* updates
        if t >= 0.0 and right_stim.status == NOT_STARTED:
            # keep track of start time/frame for later
            right_stim.tStart = t
            right_stim.frameNStart = frameN  # exact frame index
            right_stim.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if right_stim.status == STARTED and t >= frameRemains:
            right_stim.setAutoDraw(False)
        
        # *ITI* updates
        if t >= 1.0 and ITI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ITI.tStart = t
            ITI.frameNStart = frameN  # exact frame index
            ITI.setAutoDraw(True)
        frameRemains = 1.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ITI.status == STARTED and t >= frameRemains:
            ITI.setAutoDraw(False)
        
        # *resp* updates
        if t >= 0.2 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.2 + 1.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resp.status == STARTED and t >= frameRemains:
            resp.status = STOPPED
        if resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['z', 'm'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                resp.keys = theseKeys[-1]  # just the last key pressed
                resp.rt = resp.clock.getTime()
                # was this 'correct'?
                if (resp.keys == str(ans)) or (resp.keys == ans):
                    resp.corr = 1
                else:
                    resp.corr = 0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in simon_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "simon_trial"-------
    for thisComponent in simon_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys=None
        # was no response the correct answer?!
        if str(ans).lower() == 'none':
           resp.corr = 1  # correct non-response
        else:
           resp.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('resp.keys',resp.keys)
    trials.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        trials.addData('resp.rt', resp.rt)
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials'


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
