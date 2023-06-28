#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Июнь 28, 2023, at 11:32
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019)
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195.
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs

prefs.hardware['audioLib'] = 'ptb'
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
expName = 'probe2_edited'  # from the Builder filename that created this script
expInfo = {
    'session': '001',
    'participant': '001',
    'F/M': '',
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
                                 originPath='C:\\Users\\tempu\\OneDrive\\Рабочий стол\\Work and study\\HSE\\PsychoPy\\ensemble and VWM\\ensExp.py',
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename + '.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0,
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
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

# --- Initialize components for Routine "instr" ---
text = visual.TextStim(win=win, name='text',
                       text='Здравствуйте! \n\nВ данном эксперименте Вам на короткое время будет показан цветной квадрат в центре экрана и цветные треугольники с разным углом наклона. Ваша задача - запомнить цвет квадрата и определить принадлежность тестового треугольника к определенной подгруппе треугольников.\nВ начале каждой пробы Вам необходимо зафиксировать взгляд на белом перекрестии в центре экрана. Когда оно исчезнет, взгляд можно перемещать свободно.\n\nВ след за перекрестием появится цветной квадрат, далее группа треугольников, которые разделены на две подгруппы по цвету. После появится на краткое время тестовый треугольник. Здесь Вам нужно ответить на вопрос о принадлежности треугольника к определенной подгруппе. В конце пробы необходимо определить, совпадают ли цвета тестового квадрата и квадрата, показанного в начале.\n\nПожалуйста, следуйте инструкциям на экране.\n\nНажмите ПРОБЕЛ, если готовы начать.',
                       font='Open Sans',
                       pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0,
                       color='white', colorSpace='rgb', opacity=None,
                       languageStyle='LTR',
                       depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "instpreEXP" ---
text_3 = visual.TextStim(win=win, name='text_3',
                         text='\n\nДля лучшего понимания инструкции эксперимента, Вам будет представлено несколько тренировочных проб.\n\nДля ответа на задачу с треугольниками Вам нужно будет нажимать “← -  против часовой стрелки” или  “→ - по часовой стрелке", \nтогда как для задачи с цветом квадрата Вам нужно будет нажимать "Y - Да", если совпадает; "N - Нет", если не совпадает.\n\nНажмите клавишу "ПРОБЕЛ".\n',
                         font='Open Sans',
                         pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0,
                         color='white', colorSpace='rgb', opacity=None,
                         languageStyle='LTR',
                         depth=0.0);
key_resp_2 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_2
event.Mouse(visible=False, newPos=[0, 0], win=None)

# --- Initialize components for Routine "pre_vWM" ---
polygon_5 = visual.Rect(
    win=win, name='polygon_5',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor=[0.0000, 0.0000, 0.0000], fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
# Run 'Begin Experiment' code from code_10
import random

# start
vWM_start_test_trial = 1.5

# end
vWM_duration_test_trial = 0.5

# cross
cross_start = 0.0
cross_duration = 1

# color_vWMtask
darkblue = '-1.0000, -1.0000, 0.0902'
yellow = '1.0000, 1.0000, -1.0000'
red = '1.0000, -1.0000, -1.0000'
green = '-1.0000, 0.0039, -1.0000'
colorList = ['yellow', 'darkblue', 'red', 'green']
fix_cross = visual.TextStim(win=win, name='fix_cross',
                            text='+',
                            font='Open Sans',
                            pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                            color='white', colorSpace='rgb', opacity=None,
                            languageStyle='LTR',
                            depth=-2.0);

# --- Initialize components for Routine "ITI" ---
polygon_3 = visual.ShapeStim(
    win=win, name='polygon_3',
    size=(0.5, 0.5), vertices='triangle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "pre_trial_probe" ---
# Run 'Begin Experiment' code from code_13
import numpy as np
import random
from random import randint

# grid cell=g, jitter=j
g = 150
j = 15

# X and Y coordinates of the imaginary grid cell
x1 = (-2.5 * g)
x2 = (-1.5 * g)
x3 = (-0.5 * g)
x4 = ((0.5) * g)
x5 = ((1.5) * g)
x6 = ((2.5) * g)

y1 = (2.5 * g)
y2 = (1.5 * g)
y3 = (0.5 * g)
y4 = ((- 0.5) * g)
y5 = ((- 1.5) * g)
y6 = ((- 2.5) * g)

# color
darkblue = '-1.0000, -1.0000, 0.0902'
yellow = '1.0000, 1.0000, -1.0000'
red = '1.0000, -1.0000, -1.0000'
green = '-1.0000, 0.0039, -1.0000'
colorList = ['yellow', 'darkblue', 'red', 'green']

##set size of sequence
# 0 - the same color, 1 - diffrent color
set_size_0 = [16, 24, 36] * 1
set_size_1 = [16, 24, 36] * 1

# shuffle sequence
shuffle_set_0 = random.sample(set_size_0, len(set_size_0))
shuffle_set_1 = random.sample(set_size_1, len(set_size_1))

randomization_gr = list([shuffle_set_0, shuffle_set_1])

# Color for square and lines, 0 - the same color, 1 - diffrent color
color_square = random.choice(colorList)
ANS_color_square = random.choice(colorList)

condition_color_list = [0, 1] * 3
random.shuffle(condition_color_list)

# make a set size of ensemble
trial_elements = randomization_gr  # строго 12 проб с сет сайзом 18, 24, 36

set_size = trial_elements.pop()
s = None

# start
ens_start_test_trial = 0.5

# size of triangles
wx = 0.3
hx = 1.3

# end
ens_duration_test_trial = 0.5

l1_2 = visual.ShapeStim(
    win=win, name='l1_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=1.0, depth=-1.0, interpolate=True)
l2_2 = visual.ShapeStim(
    win=win, name='l2_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor=[0.0000, 0.0000, 0.0000], fillColor='white',
    opacity=1.0, depth=-2.0, interpolate=True)
l3_2 = visual.ShapeStim(
    win=win, name='l3_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-3.0, interpolate=True)
l4_2 = visual.ShapeStim(
    win=win, name='l4_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-4.0, interpolate=True)
l5_2 = visual.ShapeStim(
    win=win, name='l5_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-5.0, interpolate=True)
l6_2 = visual.ShapeStim(
    win=win, name='l6_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-6.0, interpolate=True)
l7_2 = visual.ShapeStim(
    win=win, name='l7_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-7.0, interpolate=True)
l8_2 = visual.ShapeStim(
    win=win, name='l8_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-8.0, interpolate=True)
l9_2 = visual.ShapeStim(
    win=win, name='l9_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-9.0, interpolate=True)
l10_2 = visual.ShapeStim(
    win=win, name='l10_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-10.0, interpolate=True)
l11_2 = visual.ShapeStim(
    win=win, name='l11_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-11.0, interpolate=True)
l12_2 = visual.ShapeStim(
    win=win, name='l12_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-12.0, interpolate=True)
l13_2 = visual.ShapeStim(
    win=win, name='l13_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-13.0, interpolate=True)
l14_2 = visual.ShapeStim(
    win=win, name='l14_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-14.0, interpolate=True)
l15_2 = visual.ShapeStim(
    win=win, name='l15_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-15.0, interpolate=True)
l16_2 = visual.ShapeStim(
    win=win, name='l16_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-16.0, interpolate=True)
l17_2 = visual.ShapeStim(
    win=win, name='l17_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-17.0, interpolate=True)
l18_2 = visual.ShapeStim(
    win=win, name='l18_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-18.0, interpolate=True)
l19_2 = visual.ShapeStim(
    win=win, name='l19_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-19.0, interpolate=True)
l20_2 = visual.ShapeStim(
    win=win, name='l20_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-20.0, interpolate=True)
l21_2 = visual.ShapeStim(
    win=win, name='l21_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-21.0, interpolate=True)
l22_2 = visual.ShapeStim(
    win=win, name='l22_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-22.0, interpolate=True)
l23_2 = visual.ShapeStim(
    win=win, name='l23_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-23.0, interpolate=True)
l24_2 = visual.ShapeStim(
    win=win, name='l24_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-24.0, interpolate=True)
l25_2 = visual.ShapeStim(
    win=win, name='l25_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-25.0, interpolate=True)
l26_2 = visual.ShapeStim(
    win=win, name='l26_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-26.0, interpolate=True)
l27_2 = visual.ShapeStim(
    win=win, name='l27_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-27.0, interpolate=True)
l28_2 = visual.ShapeStim(
    win=win, name='l28_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-28.0, interpolate=True)
l29_2 = visual.ShapeStim(
    win=win, name='l29_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-29.0, interpolate=True)
l30_2 = visual.ShapeStim(
    win=win, name='l30_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-30.0, interpolate=True)
l31_2 = visual.ShapeStim(
    win=win, name='l31_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-31.0, interpolate=True)
l32_2 = visual.ShapeStim(
    win=win, name='l32_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-32.0, interpolate=True)
l33_2 = visual.ShapeStim(
    win=win, name='l33_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-33.0, interpolate=True)
l34_2 = visual.ShapeStim(
    win=win, name='l34_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-34.0, interpolate=True)
l35_2 = visual.ShapeStim(
    win=win, name='l35_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-35.0, interpolate=True)
l36_2 = visual.ShapeStim(
    win=win, name='l36_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-36.0, interpolate=True)

# --- Initialize components for Routine "ITI2" ---
polygon_4 = visual.ShapeStim(
    win=win, name='polygon_4',
    size=(0.5, 0.5), vertices='triangle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "pre_ans_ENS" ---
l1_answer_2 = visual.ShapeStim(
    win=win, name='l1_answer_2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=None, pos=(0, 0), anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
key_resp_7 = keyboard.Keyboard()
text_8 = visual.TextStim(win=win, name='text_8',
                         text='\n\n\n\n\n\n\n\nПредставленный треугольникна экране ближе к группе треугольников против часовой стрелки “←” или к группе треугольников по часовой стрелке “→”?',
                         font='Open Sans',
                         pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                         color='white', colorSpace='rgb', opacity=None,
                         languageStyle='LTR',
                         depth=-2.0);

# --- Initialize components for Routine "pre_ans_vWM" ---
polygon_6 = visual.Rect(
    win=win, name='polygon_6',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor=[0.0000, 0.0000, 0.0000], fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
key_resp_6 = keyboard.Keyboard()
text_7 = visual.TextStim(win=win, name='text_7',
                         text='\n\n\n\n\n\n\n\n\n\n\n\n\n\nПохож ли по цвету представленный квадрат с тем, что был показан в начале пробы? Да - Y, Нет - N.',
                         font='Open Sans',
                         pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                         color='white', colorSpace='rgb', opacity=None,
                         languageStyle='LTR',
                         depth=-2.0);
# Run 'Begin Experiment' code from code_11
# color_vWMtask
# color
darkblue = '-1.0000, -1.0000, 0.0902'
yellow = '1.0000, 1.0000, -1.0000'
red = '1.0000, -1.0000, -1.0000'
green = '-1.0000, 0.0039, -1.0000'
colorList = ['yellow', 'darkblue', 'red', 'green']

# ANS_color_square = random.choice(colorList)

# --- Initialize components for Routine "instrEXP" ---
text_6 = visual.TextStim(win=win, name='text_6',
                         text='Сейчас Вам будет представлена основная часть эксперимента. Обратная связь предъявляться не будет.\nНажмите ПРОБЕЛ, чтобы начать экспериментальную серию.\n',
                         font='Open Sans',
                         pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                         color='white', colorSpace='rgb', opacity=None,
                         languageStyle='LTR',
                         depth=0.0);
key_resp_5 = keyboard.Keyboard()

# --- Initialize components for Routine "vWM_probe" ---
polygon_2 = visual.Rect(
    win=win, name='polygon_2',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor=[0.0000, 0.0000, 0.0000], fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
# Run 'Begin Experiment' code from code_4
import random

# start
vWM_start = 1.5

# end
vWM_duration = 0.5

# cross
cross_start = 0.0
cross_duration = 1

# color_vWMtask
darkblue = '-1.0000, -1.0000, 0.0902'
yellow = '1.0000, 1.0000, -1.0000'
red = '1.0000, -1.0000, -1.0000'
green = '-1.0000, 0.0039, -1.0000'
colorList = ['yellow', 'darkblue', 'red', 'green']

fix_cross_2 = visual.TextStim(win=win, name='fix_cross_2',
                              text='+',
                              font='Open Sans',
                              pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                              color='white', colorSpace='rgb', opacity=None,
                              languageStyle='LTR',
                              depth=-2.0);

# --- Initialize components for Routine "ITI" ---
polygon_3 = visual.ShapeStim(
    win=win, name='polygon_3',
    size=(0.5, 0.5), vertices='triangle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "trial_probe" ---
# Run 'Begin Experiment' code from code_3
import numpy as np
import random
from random import randint

# grid cell=g, jitter=j
g = 150
j = 15

# X and Y coordinates of the imaginary grid cell
x1 = (-2.5 * g)
x2 = (-1.5 * g)
x3 = (-0.5 * g)
x4 = ((0.5) * g)
x5 = ((1.5) * g)
x6 = ((2.5) * g)

y1 = (2.5 * g)
y2 = (1.5 * g)
y3 = (0.5 * g)
y4 = ((- 0.5) * g)
y5 = ((- 1.5) * g)
y6 = ((- 2.5) * g)

# color
darkblue = '-1.0000, -1.0000, 0.0902'
yellow = '1.0000, 1.0000, -1.0000'
red = '1.0000, -1.0000, -1.0000'
green = '-1.0000, 0.0039, -1.0000'
colorList = ['yellow', 'darkblue', 'red', 'green']

##set size of sequence
# 0 - the same color, 1 - diffrent color
set_size_0 = [16, 24, 36] * 90
set_size_1 = [16, 24, 36] * 90

# shuffle sequence
shuffle_set_0 = random.sample(set_size_0, len(set_size_0))
shuffle_set_1 = random.sample(set_size_1, len(set_size_1))

randomization_gr = list([shuffle_set_0, shuffle_set_1])

# Color for square and lines, 0 - the same color, 1 - diffrent color
color_square = random.choice(colorList)
ANS_color_square = random.choice(colorList)

condition_color_list = [0, 1] * 270
random.shuffle(condition_color_list)

# make a set size of ensemble
trial_elements = randomization_gr  # строго 12 проб с сет сайзом 18, 24, 36

set_size = trial_elements.pop()
s = None

# start
ens_start = 0.5

# size of triangles
wx = 0.3
hx = 1.3

# end
ens_duration = 0.5
l1 = visual.ShapeStim(
    win=win, name='l1', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor=[0.0000, 0.0000, 0.0000], fillColor='white',
    opacity=1.0, depth=-1.0, interpolate=True)
l2 = visual.ShapeStim(
    win=win, name='l2', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor=[0.0000, 0.0000, 0.0000], fillColor='white',
    opacity=1.0, depth=-2.0, interpolate=True)
l3 = visual.ShapeStim(
    win=win, name='l3', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-3.0, interpolate=True)
l4 = visual.ShapeStim(
    win=win, name='l4', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-4.0, interpolate=True)
l5 = visual.ShapeStim(
    win=win, name='l5', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-5.0, interpolate=True)
l6 = visual.ShapeStim(
    win=win, name='l6', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-6.0, interpolate=True)
l7 = visual.ShapeStim(
    win=win, name='l7', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-7.0, interpolate=True)
l8 = visual.ShapeStim(
    win=win, name='l8', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-8.0, interpolate=True)
l9 = visual.ShapeStim(
    win=win, name='l9',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-9.0, interpolate=True)
l10 = visual.ShapeStim(
    win=win, name='l10',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-10.0, interpolate=True)
l11 = visual.ShapeStim(
    win=win, name='l11', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-11.0, interpolate=True)
l12 = visual.ShapeStim(
    win=win, name='l12', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-12.0, interpolate=True)
l13 = visual.ShapeStim(
    win=win, name='l13', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-13.0, interpolate=True)
l14 = visual.ShapeStim(
    win=win, name='l14', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-14.0, interpolate=True)
l15 = visual.ShapeStim(
    win=win, name='l15', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-15.0, interpolate=True)
l16 = visual.ShapeStim(
    win=win, name='l16', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-16.0, interpolate=True)
l17 = visual.ShapeStim(
    win=win, name='l17', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-17.0, interpolate=True)
l18 = visual.ShapeStim(
    win=win, name='l18', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-18.0, interpolate=True)
l19 = visual.ShapeStim(
    win=win, name='l19', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-19.0, interpolate=True)
l20 = visual.ShapeStim(
    win=win, name='l20', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-20.0, interpolate=True)
l21 = visual.ShapeStim(
    win=win, name='l21', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-21.0, interpolate=True)
l22 = visual.ShapeStim(
    win=win, name='l22', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-22.0, interpolate=True)
l23 = visual.ShapeStim(
    win=win, name='l23', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-23.0, interpolate=True)
l24 = visual.ShapeStim(
    win=win, name='l24', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-24.0, interpolate=True)
l25 = visual.ShapeStim(
    win=win, name='l25', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-25.0, interpolate=True)
l26 = visual.ShapeStim(
    win=win, name='l26', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-26.0, interpolate=True)
l27 = visual.ShapeStim(
    win=win, name='l27', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-27.0, interpolate=True)
l28 = visual.ShapeStim(
    win=win, name='l28', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-28.0, interpolate=True)
l29 = visual.ShapeStim(
    win=win, name='l29', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-29.0, interpolate=True)
l30 = visual.ShapeStim(
    win=win, name='l30', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-30.0, interpolate=True)
l31 = visual.ShapeStim(
    win=win, name='l31', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-31.0, interpolate=True)
l32 = visual.ShapeStim(
    win=win, name='l32', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-32.0, interpolate=True)
l33 = visual.ShapeStim(
    win=win, name='l33', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-33.0, interpolate=True)
l34 = visual.ShapeStim(
    win=win, name='l34', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-34.0, interpolate=True)
l35 = visual.ShapeStim(
    win=win, name='l35', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-35.0, interpolate=True)
l36 = visual.ShapeStim(
    win=win, name='l36', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=None, anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=1.0, depth=-36.0, interpolate=True)

# --- Initialize components for Routine "ITI2" ---
polygon_4 = visual.ShapeStim(
    win=win, name='polygon_4',
    size=(0.5, 0.5), vertices='triangle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "answer_ENS_probe" ---
l1_answer = visual.ShapeStim(
    win=win, name='l1_answer', units='pix',
    size=[1.0, 1.0], vertices='triangle',
    ori=None, pos=(0, 0), anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
key_resp_3 = keyboard.Keyboard()
text_4 = visual.TextStim(win=win, name='text_4',
                         text='\n\n\n\n\n\n\n\nПредставленный треугольник на экране ближе к группе треугольников против часовой стрелки “←” или к группе треугольников по часовой стрелке “→”?',
                         font='Open Sans',
                         pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                         color='white', colorSpace='rgb', opacity=None,
                         languageStyle='LTR',
                         depth=-2.0);

# --- Initialize components for Routine "answer_vWM_probe" ---
polygon = visual.Rect(
    win=win, name='polygon',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor=[0.0000, 0.0000, 0.0000], fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
key_resp_4 = keyboard.Keyboard()
text_5 = visual.TextStim(win=win, name='text_5',
                         text='\n\n\n\n\n\n\n\n\n\n\n\n\nПохож ли по цвету представленный квадрат с тем, что был показан в начале пробы? Да - Y, Нет - N.',
                         font='Open Sans',
                         pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                         color='white', colorSpace='rgb', opacity=None,
                         languageStyle='LTR',
                         depth=-2.0);
# Run 'Begin Experiment' code from code_7
# color_vWMtask
# color
darkblue = '-1.0000, -1.0000, 0.0902'
yellow = '1.0000, 1.0000, -1.0000'
red = '1.0000, -1.0000, -1.0000'
green = '-1.0000, 0.0039, -1.0000'
colorList = ['yellow', 'darkblue', 'red', 'green']
ANS_color_square = random.choice(colorList)

# --- Initialize components for Routine "thx" ---
text_2 = visual.TextStim(win=win, name='text_2',
                         text='Благодарим Вас за участие в эксперименте!',
                         font='Open Sans',
                         pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                         color='white', colorSpace='rgb', opacity=None,
                         languageStyle='LTR',
                         depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine

# --- Prepare to start Routine "instr" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# Run 'Begin Routine' code from code
event.Mouse(visible=False, newPos=[0, 0], win=None)
# keep track of which components have finished
instrComponents = [text, key_resp]
for thisComponent in instrComponents:
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

# --- Run Routine "instr" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)

    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
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
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instr" ---
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instpreEXP" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# Run 'Begin Routine' code from code_2


# keep track of which components have finished
instpreEXPComponents = [text_3, key_resp_2]
for thisComponent in instpreEXPComponents:
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

# --- Run Routine "instpreEXP" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_3.started')
        text_3.setAutoDraw(True)

    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_2.started')
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
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
    for thisComponent in instpreEXPComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instpreEXP" ---
for thisComponent in instpreEXPComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instpreEXP" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pretrials = data.TrialHandler(nReps=6.0, method='random',
                              extraInfo=expInfo, originPath=-1,
                              trialList=[None],
                              seed=None, name='pretrials')
thisExp.addLoop(pretrials)  # add the loop to the experiment
thisPretrial = pretrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPretrial.rgb)
if thisPretrial != None:
    for paramName in thisPretrial:
        exec('{} = thisPretrial[paramName]'.format(paramName))

for thisPretrial in pretrials:
    currentLoop = pretrials
    # abbreviate parameter names if possible (e.g. rgb = thisPretrial.rgb)
    if thisPretrial != None:
        for paramName in thisPretrial:
            exec('{} = thisPretrial[paramName]'.format(paramName))

    # --- Prepare to start Routine "pre_vWM" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    polygon_5.setFillColor(color_square)
    # Run 'Begin Routine' code from code_10
    color_square = random.choice(colorList)

    # keep track of which components have finished
    pre_vWMComponents = [polygon_5, fix_cross]
    for thisComponent in pre_vWMComponents:
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

    # --- Run Routine "pre_vWM" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *polygon_5* updates
        if polygon_5.status == NOT_STARTED and tThisFlip >= vWM_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            polygon_5.frameNStart = frameN  # exact frame index
            polygon_5.tStart = t  # local t and not account for scr refresh
            polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_5.started')
            polygon_5.setAutoDraw(True)
        if polygon_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_5.tStartRefresh + vWM_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                polygon_5.tStop = t  # not accounting for scr refresh
                polygon_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_5.stopped')
                polygon_5.setAutoDraw(False)

        # *fix_cross* updates
        if fix_cross.status == NOT_STARTED and tThisFlip >= cross_start - frameTolerance:
            # keep track of start time/frame for later
            fix_cross.frameNStart = frameN  # exact frame index
            fix_cross.tStart = t  # local t and not account for scr refresh
            fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fix_cross.started')
            fix_cross.setAutoDraw(True)
        if fix_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross.tStartRefresh + cross_duration - frameTolerance:
                # keep track of stop time/frame for later
                fix_cross.tStop = t  # not accounting for scr refresh
                fix_cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_cross.stopped')
                fix_cross.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pre_vWMComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "pre_vWM" ---
    for thisComponent in pre_vWMComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_10
    # pre_trial_probe.addData('color_square',color_square)
    # the Routine "pre_vWM" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_5
    # Hide the mouse
    event.Mouse(visible=False, newPos=[0, 0], win=None)

    duration_ITI = random.choice([0.3, 0.5])
    # keep track of which components have finished
    ITIComponents = [polygon_3]
    for thisComponent in ITIComponents:
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

    # --- Run Routine "ITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *polygon_3* updates
        if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.tStart = t  # local t and not account for scr refresh
            polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_3.started')
            polygon_3.setAutoDraw(True)
        if polygon_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_3.tStartRefresh + duration_ITI - frameTolerance:
                # keep track of stop time/frame for later
                polygon_3.tStop = t  # not accounting for scr refresh
                polygon_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_3.stopped')
                polygon_3.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # --- Prepare to start Routine "pre_trial_probe" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_13
    from psychopy.tools.monitorunittools import posToPix
    from statistics import mean

    # make mouse invisible
    event.Mouse(visible=False, newPos=[0, 0], win=None)

    ##position grid
    # first pair
    l1_2.pos = [x1 + randint(-j, j), y1 + randint(-j, j)]
    l2_2.pos = [x2 + randint(-j, j), y1 + randint(-j, j)]
    l3_2.pos = [x3 + randint(-j, j), y1 + randint(-j, j)]
    l4_2.pos = [x4 + randint(-j, j), y1 + randint(-j, j)]
    l5_2.pos = [x5 + randint(-j, j), y1 + randint(-j, j)]
    l6_2.pos = [x6 + randint(-j, j), y1 + randint(-j, j)]
    # second pair
    l7_2.pos = [x1 + randint(-j, j), y2 + randint(-j, j)]
    l8_2.pos = [x2 + randint(-j, j), y2 + randint(-j, j)]
    l9_2.pos = [x3 + randint(-j, j), y2 + randint(-j, j)]
    l10_2.pos = [x4 + randint(-j, j), y2 + randint(-j, j)]
    l11_2.pos = [x5 + randint(-j, j), y2 + randint(-j, j)]
    l12_2.pos = [x6 + randint(-j, j), y2 + randint(-j, j)]
    # third pair
    l13_2.pos = [x1 + randint(-j, j), y3 + randint(-j, j)]
    l14_2.pos = [x2 + randint(-j, j), y3 + randint(-j, j)]
    l15_2.pos = [x3 + randint(-j, j), y3 + randint(-j, j)]
    l16_2.pos = [x4 + randint(-j, j), y3 + randint(-j, j)]
    l17_2.pos = [x5 + randint(-j, j), y3 + randint(-j, j)]
    l18_2.pos = [x6 + randint(-j, j), y3 + randint(-j, j)]
    # fourth pair
    l19_2.pos = [x1 + randint(-j, j), y4 + randint(-j, j)]
    l20_2.pos = [x2 + randint(-j, j), y4 + randint(-j, j)]
    l21_2.pos = [x3 + randint(-j, j), y4 + randint(-j, j)]
    l22_2.pos = [x4 + randint(-j, j), y4 + randint(-j, j)]
    l23_2.pos = [x5 + randint(-j, j), y4 + randint(-j, j)]
    l24_2.pos = [x6 + randint(-j, j), y4 + randint(-j, j)]
    # fifth pair
    l25_2.pos = [x1 + randint(-j, j), y5 + randint(-j, j)]
    l26_2.pos = [x2 + randint(-j, j), y5 + randint(-j, j)]
    l27_2.pos = [x3 + randint(-j, j), y5 + randint(-j, j)]
    l28_2.pos = [x4 + randint(-j, j), y5 + randint(-j, j)]
    l29_2.pos = [x5 + randint(-j, j), y5 + randint(-j, j)]
    l30_2.pos = [x6 + randint(-j, j), y5 + randint(-j, j)]
    # sixth pair
    l31_2.pos = [x1 + randint(-j, j), y6 + randint(-j, j)]
    l32_2.pos = [x2 + randint(-j, j), y6 + randint(-j, j)]
    l33_2.pos = [x3 + randint(-j, j), y6 + randint(-j, j)]
    l34_2.pos = [x4 + randint(-j, j), y6 + randint(-j, j)]
    l35_2.pos = [x5 + randint(-j, j), y6 + randint(-j, j)]
    l36_2.pos = [x6 + randint(-j, j), y6 + randint(-j, j)]

    Mo = randint(15, 180)  # set random orientation as the mean of an ensemble

    # save Mo for routine
    st_d = (30)  # sd for set

    list_random = None

    ## make a set size of ensemble
    if len(set_size) >= 0:
        if len(trial_elements) > 0:
            s = set_size.pop()

    # make a vector for the set
    if s == 16:
        list_random = np.random.normal(Mo, st_d, 16)
    elif s == 24:
        list_random = np.random.normal(Mo, st_d, 24)
    else:
        list_random = np.random.normal(Mo, st_d, 36)

    x = len(list_random) / 2

    # Line size (I should draw them wider)
    size_line = (25, 50)
    line_Width = 1.3

    l1_2.lineWidth = line_Width
    l2_2.lineWidth = line_Width
    l3_2.lineWidth = line_Width
    l4_2.lineWidth = line_Width
    l5_2.lineWidth = line_Width
    l6_2.lineWidth = line_Width
    l7_2.lineWidth = line_Width
    l8_2.lineWidth = line_Width
    l9_2.lineWidth = line_Width
    l10_2.lineWidth = line_Width
    l11_2.lineWidth = line_Width
    l12_2.lineWidth = line_Width
    l13_2.lineWidth = line_Width
    l14_2.lineWidth = line_Width
    l15_2.lineWidth = line_Width
    l16_2.lineWidth = line_Width
    l17_2.lineWidth = line_Width
    l18_2.lineWidth = line_Width
    l19_2.lineWidth = line_Width
    l20_2.lineWidth = line_Width
    l21_2.lineWidth = line_Width
    l22_2.lineWidth = line_Width
    l23_2.lineWidth = line_Width
    l24_2.lineWidth = line_Width
    l25_2.lineWidth = line_Width
    l26_2.lineWidth = line_Width
    l27_2.lineWidth = line_Width
    l28_2.lineWidth = line_Width
    l29_2.lineWidth = line_Width
    l30_2.lineWidth = line_Width
    l31_2.lineWidth = line_Width
    l32_2.lineWidth = line_Width
    l33_2.lineWidth = line_Width
    l34_2.lineWidth = line_Width
    l35_2.lineWidth = line_Width
    l36_2.lineWidth = line_Width

    # get opacity for set
    ##op_gr1(16) = 8, 9, 10, 11, 14, 15 ,16 ,17, 20, 21, 22, 23, 26, 27, 28, 29
    ##op_gr2(24) = 7, 12, 13, 18, 19, 24, 25, 30
    ##op_gr3(36) = 1, 2, 3, 4, 5, 6, 31, 32, 33 ,34 ,35, 36

    if s == 16:
        op_gr1 = 1
        op_gr2 = 0
        op_gr3 = 0
    elif s == 24:  # + 8
        op_gr1 = 1
        op_gr2 = 1
        op_gr3 = 0
    else:  # 24 + 12
        op_gr1 = 1
        op_gr2 = 1
        op_gr3 = 1

    # sort from smaller to higher
    sort_vers = sorted(list_random)

    # split group
    gr1 = sort_vers[:int(x)]
    gr2 = sort_vers[int(x):]

    # gr1 = list_random[:int(18)]
    # gr2 = list_random[int(18):]

    # тут условная функция  должна выдавать n (16; 24; 36) случайных значений
    # orientation1 = np.random.randint(0, 15, int(x))
    # orientation2 = np.random.randint(-15, 0, int(x))

    orientation1 = -15
    orientation2 = 15
    # gr1 += orientation1
    # gr2 += orientation2

    # gr 1 - CCW, gr 2 - CW
    gr1 = list(np.asarray(gr1) + (orientation1))
    gr2 = list(np.asarray(gr2) + (orientation2))

    # randomize target and distractor
    randomization = list([gr1, gr2])
    random.shuffle(randomization)
    target = randomization[0]
    dist = randomization[1]

    mean_dist_test = mean(target)
    mean_target_test = mean(dist)

    mean_one_unnecessary_1 = [1] * 20
    mean_one_unnecessary_2 = [1] * 12

    # get opacity for set
    ##op_gr1(16) = 8, 9, 10, 11, 14, 15 ,16 ,17, 20, 21, 22, 23, 26, 27, 28, 29
    ##op_gr2(24) = 7, 12, 13, 18, 19, 24, 25, 30
    ##op_gr3(36) = 1, 2, 3, 4, 5, 6, 31, 32, 33 ,34 ,35, 36

    if s == 16:
        l8_2.ori, l9_2.ori, l14_2.ori, l15_2.ori, l20_2.ori, l21_2.ori, l26_2.ori, l27_2.ori = target
        l10_2.ori, l11_2.ori, l16_2.ori, l17_2.ori, l22_2.ori, l23_2.ori, l28_2.ori, l29_2.ori = dist
        l1_2.ori, l2_2.ori, l3_2.ori, l4_2.ori, l5_2.ori, l6_2.ori, l7_2.ori, l12_2.ori, l13_2.ori, l18_2.ori, l19_2.ori, l24_2.ori, l25_2.ori, l30_2.ori, l31_2.ori, l32_2.ori, l33_2.ori, l34_2.ori, l35_2.ori, l36_2.ori = mean_one_unnecessary_1
    elif s == 24:
        l7_2.ori, l8_2.ori, l9_2.ori, l13_2.ori, l14_2.ori, l15_2.ori, l19_2.ori, l20_2.ori, l21_2.ori, l25_2.ori, l26_2.ori, l27_2.ori = target
        l10_2.ori, l11_2.ori, l12_2.ori, l16_2.ori, l17_2.ori, l18_2.ori, l22_2.ori, l23_2.ori, l24_2.ori, l28_2.ori, l29_2.ori, l30_2.ori = dist
        l1_2.ori, l2_2.ori, l3_2.ori, l4_2.ori, l5_2.ori, l6_2.ori, l31_2.ori, l32_2.ori, l33_2.ori, l34_2.ori, l35_2.ori, l36_2.ori = mean_one_unnecessary_2
    else:
        l1_2.ori, l2_2.ori, l3_2.ori, l7_2.ori, l8_2.ori, l9_2.ori, l13_2.ori, l14_2.ori, l15_2.ori, l19_2.ori, l20_2.ori, l21_2.ori, l25_2.ori, l26_2.ori, l27_2.ori, l31_2.ori, l32_2.ori, l33_2.ori = target
        l4_2.ori, l5_2.ori, l6_2.ori, l10_2.ori, l11_2.ori, l12_2.ori, l16_2.ori, l17_2.ori, l18_2.ori, l22_2.ori, l23_2.ori, l24_2.ori, l28_2.ori, l29_2.ori, l30_2.ori, l34_2.ori, l35_2.ori, l36_2.ori = dist

    # randomization of color
    if len(condition_color_list) > 0:
        current_color = condition_color_list.pop(0)
    elif len(condition_color_list) < 0:
        break

    # draw 1 and 2 group from color_square (vWM) and colorList with exception
    if s == 16:
        color_for_1gr = [[color_square]] * int(x)
        line_color_gr2 = random.choice([ele for ele in colorList if ele != color_square])
        color_for_2gr = [[line_color_gr2]] * int(x)
        zero_color = [[line_color_gr2]] * (36 - int(s))
    if s == 24:
        color_for_1gr = [[color_square]] * int(x)
        line_color_gr2 = random.choice([ele for ele in colorList if ele != color_square])
        color_for_2gr = [[line_color_gr2]] * int(x)
        zero_color = [[line_color_gr2]] * (36 - int(s))
    else:
        color_for_1gr = [[color_square]] * int(x)
        line_color_gr2 = random.choice([ele for ele in colorList if ele != color_square])
        color_for_2gr = [[line_color_gr2]] * int(x)

    # draw color's lines for group 2 from colorList with exception
    # line_color_gr2 = random.choice ([ele for ele in colorList if ele != color_square])
    # color_for_2gr = [[line_color_gr2]] * 18

    if current_color == 0:
        current_set_size = s
        ANS_color_square = color_square
        color_for_1gr == color_square
        color_gr1 = color_square
    elif current_color == 1:
        current_set_size = s
        ANS_color_square = random.choice([ele for ele in colorList if ele != color_square])
        line_color_gr1 = random.choice([ele for ele in colorList if ele != color_square])
        color_for_gr1 = [[line_color_gr1]] * int(x)
        color_gr1 = line_color_gr1

    if s == 16:
        l8_2.color, l9_2.color, l14_2.color, l15_2.color, l20_2.color, l21_2.color, l26_2.color, l27_2.color = color_for_1gr
        l10_2.color, l11_2.color, l16_2.color, l17_2.color, l22_2.color, l23_2.color, l28_2.color, l29_2.color = color_for_2gr
        l1_2.color, l2_2.color, l3_2.color, l4_2.color, l5_2.color, l6_2.color, l7_2.color, l12_2.color, l13_2.color, l18_2.color, l19_2.color, l24_2.color, l25_2.color, l30_2.color, l31_2.color, l32_2.color, l33_2.color, l34_2.color, l35_2.color, l36_2.color = zero_color
    elif s == 24:
        l7_2.color, l8_2.color, l9_2.color, l13_2.color, l14_2.color, l15_2.color, l19_2.color, l20_2.color, l21_2.color, l25_2.color, l26_2.color, l27_2.color = color_for_1gr
        l10_2.color, l11_2.color, l12_2.color, l16_2.color, l17_2.color, l18_2.color, l22_2.color, l23_2.color, l24_2.color, l28_2.color, l29_2.color, l30_2.color = color_for_2gr
        l1_2.color, l2_2.color, l3_2.color, l4_2.color, l5_2.color, l6_2.color, l31_2.color, l32_2.color, l33_2.color, l34_2.color, l35_2.color, l36_2.color = zero_color
    else:
        l1_2.color, l2_2.color, l3_2.color, l7_2.color, l8_2.color, l9_2.color, l13_2.color, l14_2.color, l15_2.color, l19_2.color, l20_2.color, l21_2.color, l25_2.color, l26_2.color, l27_2.color, l31_2.color, l32_2.color, l33_2.color = color_for_1gr
        l4_2.color, l5_2.color, l6_2.color, l10_2.color, l11_2.color, l12_2.color, l16_2.color, l17_2.color, l18_2.color, l22_2.color, l23_2.color, l24_2.color, l28_2.color, l29_2.color, l30_2.color, l34_2.color, l35_2.color, l36_2.color = color_for_2gr

    n = 36  # set size
    rand_jitter_x = []
    rand_jitter_y = []
    for i in range(n):
        rand_jitter_x.append(
            random.randint(-j, j))  # это лист со случайными занчениями для небольшого сдвига положений в пространстве
        rand_jitter_y.append(random.randint(-j, j))

    # lists of X and Y coordinates + random jitter
    x_list = np.repeat([x1, x2, x3, x4, x5, x6], 6) + rand_jitter_x  # output like x1,x1,x1,x1,x1,x2,x2,x2....x6,x6
    y_list = np.array([y1, y2, y3, y4, y5, y6] * 6) + rand_jitter_y  # output like y1,y2,y3,y4,y5,y6,y1,y2....y5,y6
    coord_index = list(range(n))  # create list of indexes for x_list and y_list to randomize the coordinates
    random.shuffle(coord_index)  # shuffle coordinates indexes

    # assign line spatial location
    l1_2.pos = [x_list[coord_index[0]], y_list[coord_index[0]]]
    l2_2.pos = [x_list[coord_index[1]], y_list[coord_index[1]]]
    l3_2.pos = [x_list[coord_index[2]], y_list[coord_index[2]]]
    l4_2.pos = [x_list[coord_index[3]], y_list[coord_index[3]]]
    l5_2.pos = [x_list[coord_index[4]], y_list[coord_index[4]]]
    l6_2.pos = [x_list[coord_index[5]], y_list[coord_index[5]]]
    l7_2.pos = [x_list[coord_index[6]], y_list[coord_index[6]]]
    l8_2.pos = [x_list[coord_index[7]], y_list[coord_index[7]]]
    l9_2.pos = [x_list[coord_index[8]], y_list[coord_index[8]]]
    l10_2.pos = [x_list[coord_index[9]], y_list[coord_index[9]]]
    l11_2.pos = [x_list[coord_index[10]], y_list[coord_index[10]]]
    l12_2.pos = [x_list[coord_index[11]], y_list[coord_index[11]]]
    l13_2.pos = [x_list[coord_index[12]], y_list[coord_index[12]]]
    l14_2.pos = [x_list[coord_index[13]], y_list[coord_index[13]]]
    l15_2.pos = [x_list[coord_index[14]], y_list[coord_index[14]]]
    l16_2.pos = [x_list[coord_index[15]], y_list[coord_index[15]]]
    l17_2.pos = [x_list[coord_index[16]], y_list[coord_index[16]]]
    l18_2.pos = [x_list[coord_index[17]], y_list[coord_index[17]]]
    l19_2.pos = [x_list[coord_index[18]], y_list[coord_index[18]]]
    l20_2.pos = [x_list[coord_index[19]], y_list[coord_index[19]]]
    l21_2.pos = [x_list[coord_index[20]], y_list[coord_index[20]]]
    l22_2.pos = [x_list[coord_index[21]], y_list[coord_index[21]]]
    l23_2.pos = [x_list[coord_index[22]], y_list[coord_index[22]]]
    l24_2.pos = [x_list[coord_index[23]], y_list[coord_index[23]]]
    l25_2.pos = [x_list[coord_index[24]], y_list[coord_index[24]]]
    l26_2.pos = [x_list[coord_index[25]], y_list[coord_index[25]]]
    l27_2.pos = [x_list[coord_index[26]], y_list[coord_index[26]]]
    l28_2.pos = [x_list[coord_index[27]], y_list[coord_index[27]]]
    l29_2.pos = [x_list[coord_index[28]], y_list[coord_index[28]]]
    l30_2.pos = [x_list[coord_index[29]], y_list[coord_index[29]]]
    l31_2.pos = [x_list[coord_index[30]], y_list[coord_index[30]]]
    l32_2.pos = [x_list[coord_index[31]], y_list[coord_index[31]]]
    l33_2.pos = [x_list[coord_index[32]], y_list[coord_index[32]]]
    l34_2.pos = [x_list[coord_index[33]], y_list[coord_index[33]]]
    l35_2.pos = [x_list[coord_index[34]], y_list[coord_index[34]]]
    l36_2.pos = [x_list[coord_index[35]], y_list[coord_index[35]]]
    l1_2.setOpacity(op_gr3)
    l1_2.setSize(size_line)
    l2_2.setOpacity(op_gr3)
    l2_2.setSize(size_line)
    l3_2.setOpacity(op_gr3)
    l3_2.setSize(size_line)
    l4_2.setOpacity(op_gr3)
    l4_2.setSize(size_line)
    l5_2.setOpacity(op_gr3)
    l5_2.setSize(size_line)
    l6_2.setOpacity(op_gr3)
    l6_2.setSize(size_line)
    l7_2.setOpacity(op_gr2)
    l7_2.setSize(size_line)
    l8_2.setOpacity(op_gr1)
    l8_2.setSize(size_line)
    l9_2.setOpacity(op_gr1)
    l9_2.setSize(size_line)
    l10_2.setOpacity(op_gr1)
    l10_2.setSize(size_line)
    l11_2.setOpacity(op_gr1)
    l11_2.setSize(size_line)
    l12_2.setOpacity(op_gr2)
    l12_2.setSize(size_line)
    l13_2.setOpacity(op_gr2)
    l13_2.setSize(size_line)
    l14_2.setOpacity(op_gr1)
    l14_2.setSize(size_line)
    l15_2.setOpacity(op_gr1)
    l15_2.setSize(size_line)
    l16_2.setOpacity(op_gr1)
    l16_2.setSize(size_line)
    l17_2.setOpacity(op_gr1)
    l17_2.setSize(size_line)
    l18_2.setOpacity(op_gr2)
    l18_2.setSize(size_line)
    l19_2.setOpacity(op_gr2)
    l19_2.setSize(size_line)
    l20_2.setOpacity(op_gr1)
    l20_2.setSize(size_line)
    l21_2.setOpacity(op_gr1)
    l21_2.setSize(size_line)
    l22_2.setOpacity(op_gr1)
    l22_2.setSize(size_line)
    l23_2.setOpacity(op_gr1)
    l23_2.setSize(size_line)
    l24_2.setOpacity(op_gr2)
    l24_2.setSize(size_line)
    l25_2.setOpacity(op_gr2)
    l25_2.setSize(size_line)
    l26_2.setOpacity(op_gr1)
    l26_2.setSize(size_line)
    l27_2.setSize(size_line)
    l28_2.setOpacity(op_gr1)
    l28_2.setSize(size_line)
    l29_2.setOpacity(op_gr1)
    l29_2.setSize(size_line)
    l30_2.setOpacity(op_gr2)
    l30_2.setSize(size_line)
    l31_2.setOpacity(op_gr3)
    l31_2.setSize(size_line)
    l32_2.setOpacity(op_gr3)
    l32_2.setSize(size_line)
    l33_2.setOpacity(op_gr3)
    l33_2.setSize(size_line)
    l34_2.setOpacity(op_gr3)
    l34_2.setSize(size_line)
    l35_2.setOpacity(op_gr3)
    l35_2.setSize(size_line)
    l36_2.setOpacity(op_gr3)
    l36_2.setSize(size_line)
    # keep track of which components have finished
    pre_trial_probeComponents = [l1_2, l2_2, l3_2, l4_2, l5_2, l6_2, l7_2, l8_2, l9_2, l10_2, l11_2, l12_2, l13_2,
                                 l14_2, l15_2, l16_2, l17_2, l18_2, l19_2, l20_2, l21_2, l22_2, l23_2, l24_2, l25_2,
                                 l26_2, l27_2, l28_2, l29_2, l30_2, l31_2, l32_2, l33_2, l34_2, l35_2, l36_2]
    for thisComponent in pre_trial_probeComponents:
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

    # --- Run Routine "pre_trial_probe" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *l1_2* updates
        if l1_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l1_2.frameNStart = frameN  # exact frame index
            l1_2.tStart = t  # local t and not account for scr refresh
            l1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l1_2.started')
            l1_2.setAutoDraw(True)
        if l1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l1_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l1_2.tStop = t  # not accounting for scr refresh
                l1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l1_2.stopped')
                l1_2.setAutoDraw(False)

        # *l2_2* updates
        if l2_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l2_2.frameNStart = frameN  # exact frame index
            l2_2.tStart = t  # local t and not account for scr refresh
            l2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l2_2.started')
            l2_2.setAutoDraw(True)
        if l2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l2_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l2_2.tStop = t  # not accounting for scr refresh
                l2_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l2_2.stopped')
                l2_2.setAutoDraw(False)

        # *l3_2* updates
        if l3_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l3_2.frameNStart = frameN  # exact frame index
            l3_2.tStart = t  # local t and not account for scr refresh
            l3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l3_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l3_2.started')
            l3_2.setAutoDraw(True)
        if l3_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l3_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l3_2.tStop = t  # not accounting for scr refresh
                l3_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l3_2.stopped')
                l3_2.setAutoDraw(False)

        # *l4_2* updates
        if l4_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l4_2.frameNStart = frameN  # exact frame index
            l4_2.tStart = t  # local t and not account for scr refresh
            l4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l4_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l4_2.started')
            l4_2.setAutoDraw(True)
        if l4_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l4_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l4_2.tStop = t  # not accounting for scr refresh
                l4_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l4_2.stopped')
                l4_2.setAutoDraw(False)

        # *l5_2* updates
        if l5_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l5_2.frameNStart = frameN  # exact frame index
            l5_2.tStart = t  # local t and not account for scr refresh
            l5_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l5_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l5_2.started')
            l5_2.setAutoDraw(True)
        if l5_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l5_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l5_2.tStop = t  # not accounting for scr refresh
                l5_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l5_2.stopped')
                l5_2.setAutoDraw(False)

        # *l6_2* updates
        if l6_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l6_2.frameNStart = frameN  # exact frame index
            l6_2.tStart = t  # local t and not account for scr refresh
            l6_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l6_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l6_2.started')
            l6_2.setAutoDraw(True)
        if l6_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l6_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l6_2.tStop = t  # not accounting for scr refresh
                l6_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l6_2.stopped')
                l6_2.setAutoDraw(False)

        # *l7_2* updates
        if l7_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l7_2.frameNStart = frameN  # exact frame index
            l7_2.tStart = t  # local t and not account for scr refresh
            l7_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l7_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l7_2.started')
            l7_2.setAutoDraw(True)
        if l7_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l7_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l7_2.tStop = t  # not accounting for scr refresh
                l7_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l7_2.stopped')
                l7_2.setAutoDraw(False)

        # *l8_2* updates
        if l8_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l8_2.frameNStart = frameN  # exact frame index
            l8_2.tStart = t  # local t and not account for scr refresh
            l8_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l8_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l8_2.started')
            l8_2.setAutoDraw(True)
        if l8_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l8_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l8_2.tStop = t  # not accounting for scr refresh
                l8_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l8_2.stopped')
                l8_2.setAutoDraw(False)

        # *l9_2* updates
        if l9_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l9_2.frameNStart = frameN  # exact frame index
            l9_2.tStart = t  # local t and not account for scr refresh
            l9_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l9_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l9_2.started')
            l9_2.setAutoDraw(True)
        if l9_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l9_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l9_2.tStop = t  # not accounting for scr refresh
                l9_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l9_2.stopped')
                l9_2.setAutoDraw(False)

        # *l10_2* updates
        if l10_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l10_2.frameNStart = frameN  # exact frame index
            l10_2.tStart = t  # local t and not account for scr refresh
            l10_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l10_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l10_2.started')
            l10_2.setAutoDraw(True)
        if l10_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l10_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l10_2.tStop = t  # not accounting for scr refresh
                l10_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l10_2.stopped')
                l10_2.setAutoDraw(False)

        # *l11_2* updates
        if l11_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l11_2.frameNStart = frameN  # exact frame index
            l11_2.tStart = t  # local t and not account for scr refresh
            l11_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l11_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l11_2.started')
            l11_2.setAutoDraw(True)
        if l11_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l11_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l11_2.tStop = t  # not accounting for scr refresh
                l11_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l11_2.stopped')
                l11_2.setAutoDraw(False)

        # *l12_2* updates
        if l12_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l12_2.frameNStart = frameN  # exact frame index
            l12_2.tStart = t  # local t and not account for scr refresh
            l12_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l12_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l12_2.started')
            l12_2.setAutoDraw(True)
        if l12_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l12_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l12_2.tStop = t  # not accounting for scr refresh
                l12_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l12_2.stopped')
                l12_2.setAutoDraw(False)

        # *l13_2* updates
        if l13_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l13_2.frameNStart = frameN  # exact frame index
            l13_2.tStart = t  # local t and not account for scr refresh
            l13_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l13_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l13_2.started')
            l13_2.setAutoDraw(True)
        if l13_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l13_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l13_2.tStop = t  # not accounting for scr refresh
                l13_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l13_2.stopped')
                l13_2.setAutoDraw(False)

        # *l14_2* updates
        if l14_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l14_2.frameNStart = frameN  # exact frame index
            l14_2.tStart = t  # local t and not account for scr refresh
            l14_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l14_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l14_2.started')
            l14_2.setAutoDraw(True)
        if l14_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l14_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l14_2.tStop = t  # not accounting for scr refresh
                l14_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l14_2.stopped')
                l14_2.setAutoDraw(False)

        # *l15_2* updates
        if l15_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l15_2.frameNStart = frameN  # exact frame index
            l15_2.tStart = t  # local t and not account for scr refresh
            l15_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l15_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l15_2.started')
            l15_2.setAutoDraw(True)
        if l15_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l15_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l15_2.tStop = t  # not accounting for scr refresh
                l15_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l15_2.stopped')
                l15_2.setAutoDraw(False)

        # *l16_2* updates
        if l16_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l16_2.frameNStart = frameN  # exact frame index
            l16_2.tStart = t  # local t and not account for scr refresh
            l16_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l16_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l16_2.started')
            l16_2.setAutoDraw(True)
        if l16_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l16_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l16_2.tStop = t  # not accounting for scr refresh
                l16_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l16_2.stopped')
                l16_2.setAutoDraw(False)

        # *l17_2* updates
        if l17_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l17_2.frameNStart = frameN  # exact frame index
            l17_2.tStart = t  # local t and not account for scr refresh
            l17_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l17_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l17_2.started')
            l17_2.setAutoDraw(True)
        if l17_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l17_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l17_2.tStop = t  # not accounting for scr refresh
                l17_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l17_2.stopped')
                l17_2.setAutoDraw(False)

        # *l18_2* updates
        if l18_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l18_2.frameNStart = frameN  # exact frame index
            l18_2.tStart = t  # local t and not account for scr refresh
            l18_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l18_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l18_2.started')
            l18_2.setAutoDraw(True)
        if l18_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l18_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l18_2.tStop = t  # not accounting for scr refresh
                l18_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l18_2.stopped')
                l18_2.setAutoDraw(False)

        # *l19_2* updates
        if l19_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l19_2.frameNStart = frameN  # exact frame index
            l19_2.tStart = t  # local t and not account for scr refresh
            l19_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l19_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l19_2.started')
            l19_2.setAutoDraw(True)
        if l19_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l19_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l19_2.tStop = t  # not accounting for scr refresh
                l19_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l19_2.stopped')
                l19_2.setAutoDraw(False)

        # *l20_2* updates
        if l20_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l20_2.frameNStart = frameN  # exact frame index
            l20_2.tStart = t  # local t and not account for scr refresh
            l20_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l20_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l20_2.started')
            l20_2.setAutoDraw(True)
        if l20_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l20_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l20_2.tStop = t  # not accounting for scr refresh
                l20_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l20_2.stopped')
                l20_2.setAutoDraw(False)

        # *l21_2* updates
        if l21_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l21_2.frameNStart = frameN  # exact frame index
            l21_2.tStart = t  # local t and not account for scr refresh
            l21_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l21_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l21_2.started')
            l21_2.setAutoDraw(True)
        if l21_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l21_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l21_2.tStop = t  # not accounting for scr refresh
                l21_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l21_2.stopped')
                l21_2.setAutoDraw(False)

        # *l22_2* updates
        if l22_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l22_2.frameNStart = frameN  # exact frame index
            l22_2.tStart = t  # local t and not account for scr refresh
            l22_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l22_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l22_2.started')
            l22_2.setAutoDraw(True)
        if l22_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l22_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l22_2.tStop = t  # not accounting for scr refresh
                l22_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l22_2.stopped')
                l22_2.setAutoDraw(False)

        # *l23_2* updates
        if l23_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l23_2.frameNStart = frameN  # exact frame index
            l23_2.tStart = t  # local t and not account for scr refresh
            l23_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l23_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l23_2.started')
            l23_2.setAutoDraw(True)
        if l23_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l23_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l23_2.tStop = t  # not accounting for scr refresh
                l23_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l23_2.stopped')
                l23_2.setAutoDraw(False)

        # *l24_2* updates
        if l24_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l24_2.frameNStart = frameN  # exact frame index
            l24_2.tStart = t  # local t and not account for scr refresh
            l24_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l24_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l24_2.started')
            l24_2.setAutoDraw(True)
        if l24_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l24_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l24_2.tStop = t  # not accounting for scr refresh
                l24_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l24_2.stopped')
                l24_2.setAutoDraw(False)

        # *l25_2* updates
        if l25_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l25_2.frameNStart = frameN  # exact frame index
            l25_2.tStart = t  # local t and not account for scr refresh
            l25_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l25_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l25_2.started')
            l25_2.setAutoDraw(True)
        if l25_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l25_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l25_2.tStop = t  # not accounting for scr refresh
                l25_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l25_2.stopped')
                l25_2.setAutoDraw(False)

        # *l26_2* updates
        if l26_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l26_2.frameNStart = frameN  # exact frame index
            l26_2.tStart = t  # local t and not account for scr refresh
            l26_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l26_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l26_2.started')
            l26_2.setAutoDraw(True)
        if l26_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l26_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l26_2.tStop = t  # not accounting for scr refresh
                l26_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l26_2.stopped')
                l26_2.setAutoDraw(False)

        # *l27_2* updates
        if l27_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l27_2.frameNStart = frameN  # exact frame index
            l27_2.tStart = t  # local t and not account for scr refresh
            l27_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l27_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l27_2.started')
            l27_2.setAutoDraw(True)
        if l27_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l27_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l27_2.tStop = t  # not accounting for scr refresh
                l27_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l27_2.stopped')
                l27_2.setAutoDraw(False)
        if l27_2.status == STARTED:  # only update if drawing
            l27_2.setOpacity(op_gr1, log=False)

        # *l28_2* updates
        if l28_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l28_2.frameNStart = frameN  # exact frame index
            l28_2.tStart = t  # local t and not account for scr refresh
            l28_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l28_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l28_2.started')
            l28_2.setAutoDraw(True)
        if l28_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l28_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l28_2.tStop = t  # not accounting for scr refresh
                l28_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l28_2.stopped')
                l28_2.setAutoDraw(False)

        # *l29_2* updates
        if l29_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l29_2.frameNStart = frameN  # exact frame index
            l29_2.tStart = t  # local t and not account for scr refresh
            l29_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l29_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l29_2.started')
            l29_2.setAutoDraw(True)
        if l29_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l29_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l29_2.tStop = t  # not accounting for scr refresh
                l29_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l29_2.stopped')
                l29_2.setAutoDraw(False)

        # *l30_2* updates
        if l30_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l30_2.frameNStart = frameN  # exact frame index
            l30_2.tStart = t  # local t and not account for scr refresh
            l30_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l30_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l30_2.started')
            l30_2.setAutoDraw(True)
        if l30_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l30_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l30_2.tStop = t  # not accounting for scr refresh
                l30_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l30_2.stopped')
                l30_2.setAutoDraw(False)

        # *l31_2* updates
        if l31_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l31_2.frameNStart = frameN  # exact frame index
            l31_2.tStart = t  # local t and not account for scr refresh
            l31_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l31_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l31_2.started')
            l31_2.setAutoDraw(True)
        if l31_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l31_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l31_2.tStop = t  # not accounting for scr refresh
                l31_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l31_2.stopped')
                l31_2.setAutoDraw(False)

        # *l32_2* updates
        if l32_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l32_2.frameNStart = frameN  # exact frame index
            l32_2.tStart = t  # local t and not account for scr refresh
            l32_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l32_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l32_2.started')
            l32_2.setAutoDraw(True)
        if l32_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l32_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l32_2.tStop = t  # not accounting for scr refresh
                l32_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l32_2.stopped')
                l32_2.setAutoDraw(False)

        # *l33_2* updates
        if l33_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l33_2.frameNStart = frameN  # exact frame index
            l33_2.tStart = t  # local t and not account for scr refresh
            l33_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l33_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l33_2.started')
            l33_2.setAutoDraw(True)
        if l33_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l33_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l33_2.tStop = t  # not accounting for scr refresh
                l33_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l33_2.stopped')
                l33_2.setAutoDraw(False)

        # *l34_2* updates
        if l34_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l34_2.frameNStart = frameN  # exact frame index
            l34_2.tStart = t  # local t and not account for scr refresh
            l34_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l34_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l34_2.started')
            l34_2.setAutoDraw(True)
        if l34_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l34_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l34_2.tStop = t  # not accounting for scr refresh
                l34_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l34_2.stopped')
                l34_2.setAutoDraw(False)

        # *l35_2* updates
        if l35_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l35_2.frameNStart = frameN  # exact frame index
            l35_2.tStart = t  # local t and not account for scr refresh
            l35_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l35_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l35_2.started')
            l35_2.setAutoDraw(True)
        if l35_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l35_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l35_2.tStop = t  # not accounting for scr refresh
                l35_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l35_2.stopped')
                l35_2.setAutoDraw(False)

        # *l36_2* updates
        if l36_2.status == NOT_STARTED and tThisFlip >= ens_start_test_trial - frameTolerance:
            # keep track of start time/frame for later
            l36_2.frameNStart = frameN  # exact frame index
            l36_2.tStart = t  # local t and not account for scr refresh
            l36_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l36_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l36_2.started')
            l36_2.setAutoDraw(True)
        if l36_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l36_2.tStartRefresh + ens_duration_test_trial - frameTolerance:
                # keep track of stop time/frame for later
                l36_2.tStop = t  # not accounting for scr refresh
                l36_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l36_2.stopped')
                l36_2.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pre_trial_probeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "pre_trial_probe" ---
    for thisComponent in pre_trial_probeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_13
    thisExp.addData('TrueOri', Mo)
    thisExp.addData('color_square', color_square)
    thisExp.addData('Dist_group', mean_dist_test)
    thisExp.addData('Targ_group', mean_target_test)
    thisExp.addData('Set_size', current_set_size)
    thisExp.addData('Color_cond', current_color)
    thisExp.addData('Color_gr1', color_gr1)
    thisExp.addData('Color_gr2', line_color_gr2)
    # the Routine "pre_trial_probe" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # --- Prepare to start Routine "ITI2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_6
    # Hide the mouse
    event.Mouse(visible=False, newPos=[0, 0], win=None)

    duration_ITI1 = random.choice([0.3, 0.5])
    # keep track of which components have finished
    ITI2Components = [polygon_4]
    for thisComponent in ITI2Components:
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

    # --- Run Routine "ITI2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_4.started')
            polygon_4.setAutoDraw(True)
        if polygon_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_4.tStartRefresh + duration_ITI1 - frameTolerance:
                # keep track of stop time/frame for later
                polygon_4.tStop = t  # not accounting for scr refresh
                polygon_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_4.stopped')
                polygon_4.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "ITI2" ---
    for thisComponent in ITI2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ITI2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # --- Prepare to start Routine "pre_ans_ENS" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    l1_answer_2.setSize(size_line)
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # Run 'Begin Routine' code from code_12
    size_line = (40, 500)

    line_Width = 1
    l1_answer_2.lineWidth = line_Width

    l1_answer_2.ori = Mo
    # gr3 = np.concatenate(([gr1 + gr2]), axis = None)
    # line_A = random.choice(gr3)
    # keep track of which components have finished
    pre_ans_ENSComponents = [l1_answer_2, key_resp_7, text_8]
    for thisComponent in pre_ans_ENSComponents:
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

    # --- Run Routine "pre_ans_ENS" ---
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *l1_answer_2* updates
        if l1_answer_2.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            l1_answer_2.frameNStart = frameN  # exact frame index
            l1_answer_2.tStart = t  # local t and not account for scr refresh
            l1_answer_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l1_answer_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l1_answer_2.started')
            l1_answer_2.setAutoDraw(True)
        if l1_answer_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l1_answer_2.tStartRefresh + 6.0 - frameTolerance:
                # keep track of stop time/frame for later
                l1_answer_2.tStop = t  # not accounting for scr refresh
                l1_answer_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l1_answer_2.stopped')
                l1_answer_2.setAutoDraw(False)

        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_7.started')
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_7.tStartRefresh + 6.0 - frameTolerance:
                # keep track of stop time/frame for later
                key_resp_7.tStop = t  # not accounting for scr refresh
                key_resp_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_7.stopped')
                key_resp_7.status = FINISHED
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_8.started')
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 6.0 - frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_8.stopped')
                text_8.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pre_ans_ENSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "pre_ans_ENS" ---
    for thisComponent in pre_ans_ENSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    pretrials.addData('key_resp_7.keys', key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        pretrials.addData('key_resp_7.rt', key_resp_7.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)

    # --- Prepare to start Routine "pre_ans_vWM" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    polygon_6.setFillColor(ANS_color_square)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    pre_ans_vWMComponents = [polygon_6, key_resp_6, text_7]
    for thisComponent in pre_ans_vWMComponents:
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

    # --- Run Routine "pre_ans_vWM" ---
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *polygon_6* updates
        if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            polygon_6.frameNStart = frameN  # exact frame index
            polygon_6.tStart = t  # local t and not account for scr refresh
            polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_6.started')
            polygon_6.setAutoDraw(True)
        if polygon_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_6.tStartRefresh + 6.0 - frameTolerance:
                # keep track of stop time/frame for later
                polygon_6.tStop = t  # not accounting for scr refresh
                polygon_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_6.stopped')
                polygon_6.setAutoDraw(False)

        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_6.tStartRefresh + 6.0 - frameTolerance:
                # keep track of stop time/frame for later
                key_resp_6.tStop = t  # not accounting for scr refresh
                key_resp_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_6.stopped')
                key_resp_6.status = FINISHED
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['y', 'n'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_7.started')
            text_7.setAutoDraw(True)
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + 6.0 - frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_7.stopped')
                text_7.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pre_ans_vWMComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "pre_ans_vWM" ---
    for thisComponent in pre_ans_vWMComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    pretrials.addData('key_resp_6.keys', key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        pretrials.addData('key_resp_6.rt', key_resp_6.rt)
    # Run 'End Routine' code from code_11
    thisExp.addData('ans_color_vWM', ANS_color_square)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    thisExp.nextEntry()

# completed 6.0 repeats of 'pretrials'


# --- Prepare to start Routine "instrEXP" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# Run 'Begin Routine' code from code_9
event.Mouse(visible=False, newPos=[0, 0], win=None)

# keep track of which components have finished
instrEXPComponents = [text_6, key_resp_5]
for thisComponent in instrEXPComponents:
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

# --- Run Routine "instrEXP" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_6.started')
        text_6.setAutoDraw(True)

    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_5.started')
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
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
    for thisComponent in instrEXPComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instrEXP" ---
for thisComponent in instrEXPComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instrEXP" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=540.0, method='random',
                           extraInfo=expInfo, originPath=-1,
                           trialList=[None],
                           seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))

    # --- Prepare to start Routine "vWM_probe" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    polygon_2.setFillColor(color_square)
    # Run 'Begin Routine' code from code_4
    color_square = random.choice(colorList)

    # keep track of which components have finished
    vWM_probeComponents = [polygon_2, fix_cross_2]
    for thisComponent in vWM_probeComponents:
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

    # --- Run Routine "vWM_probe" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= vWM_start - frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_2.started')
            polygon_2.setAutoDraw(True)
        if polygon_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_2.tStartRefresh + vWM_duration - frameTolerance:
                # keep track of stop time/frame for later
                polygon_2.tStop = t  # not accounting for scr refresh
                polygon_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_2.stopped')
                polygon_2.setAutoDraw(False)

        # *fix_cross_2* updates
        if fix_cross_2.status == NOT_STARTED and tThisFlip >= cross_start - frameTolerance:
            # keep track of start time/frame for later
            fix_cross_2.frameNStart = frameN  # exact frame index
            fix_cross_2.tStart = t  # local t and not account for scr refresh
            fix_cross_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fix_cross_2.started')
            fix_cross_2.setAutoDraw(True)
        if fix_cross_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross_2.tStartRefresh + cross_duration - frameTolerance:
                # keep track of stop time/frame for later
                fix_cross_2.tStop = t  # not accounting for scr refresh
                fix_cross_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_cross_2.stopped')
                fix_cross_2.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in vWM_probeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "vWM_probe" ---
    for thisComponent in vWM_probeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_4
    # color_square
    # the Routine "vWM_probe" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_5
    # Hide the mouse
    event.Mouse(visible=False, newPos=[0, 0], win=None)

    duration_ITI = random.choice([0.3, 0.5])
    # keep track of which components have finished
    ITIComponents = [polygon_3]
    for thisComponent in ITIComponents:
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

    # --- Run Routine "ITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *polygon_3* updates
        if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.tStart = t  # local t and not account for scr refresh
            polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_3.started')
            polygon_3.setAutoDraw(True)
        if polygon_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_3.tStartRefresh + duration_ITI - frameTolerance:
                # keep track of stop time/frame for later
                polygon_3.tStop = t  # not accounting for scr refresh
                polygon_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_3.stopped')
                polygon_3.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # --- Prepare to start Routine "trial_probe" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_3
    from psychopy.tools.monitorunittools import posToPix
    from statistics import mean

    # make mouse invisible
    event.Mouse(visible=False, newPos=[0, 0], win=None)

    ##position grid
    # first pairs
    l1.pos = [x1 + randint(-j, j), y1 + randint(-j, j)]
    l2.pos = [x2 + randint(-j, j), y1 + randint(-j, j)]
    l3.pos = [x3 + randint(-j, j), y1 + randint(-j, j)]
    l4.pos = [x4 + randint(-j, j), y1 + randint(-j, j)]
    l5.pos = [x5 + randint(-j, j), y1 + randint(-j, j)]
    l6.pos = [x6 + randint(-j, j), y1 + randint(-j, j)]
    # second pairs
    l7.pos = [x1 + randint(-j, j), y2 + randint(-j, j)]
    l8.pos = [x2 + randint(-j, j), y2 + randint(-j, j)]
    l9.pos = [x3 + randint(-j, j), y2 + randint(-j, j)]
    l10.pos = [x4 + randint(-j, j), y2 + randint(-j, j)]
    l11.pos = [x5 + randint(-j, j), y2 + randint(-j, j)]
    l12.pos = [x6 + randint(-j, j), y2 + randint(-j, j)]
    # third pairs
    l13.pos = [x1 + randint(-j, j), y3 + randint(-j, j)]
    l14.pos = [x2 + randint(-j, j), y3 + randint(-j, j)]
    l15.pos = [x3 + randint(-j, j), y3 + randint(-j, j)]
    l16.pos = [x4 + randint(-j, j), y3 + randint(-j, j)]
    l17.pos = [x5 + randint(-j, j), y3 + randint(-j, j)]
    l18.pos = [x6 + randint(-j, j), y3 + randint(-j, j)]
    # fourth pairs
    l19.pos = [x1 + randint(-j, j), y4 + randint(-j, j)]
    l20.pos = [x2 + randint(-j, j), y4 + randint(-j, j)]
    l21.pos = [x3 + randint(-j, j), y4 + randint(-j, j)]
    l22.pos = [x4 + randint(-j, j), y4 + randint(-j, j)]
    l23.pos = [x5 + randint(-j, j), y4 + randint(-j, j)]
    l24.pos = [x6 + randint(-j, j), y4 + randint(-j, j)]
    # fifth pairs
    l25.pos = [x1 + randint(-j, j), y5 + randint(-j, j)]
    l26.pos = [x2 + randint(-j, j), y5 + randint(-j, j)]
    l27.pos = [x3 + randint(-j, j), y5 + randint(-j, j)]
    l28.pos = [x4 + randint(-j, j), y5 + randint(-j, j)]
    l29.pos = [x5 + randint(-j, j), y5 + randint(-j, j)]
    l30.pos = [x6 + randint(-j, j), y5 + randint(-j, j)]
    # sixth pair
    l31.pos = [x1 + randint(-j, j), y6 + randint(-j, j)]
    l32.pos = [x2 + randint(-j, j), y6 + randint(-j, j)]
    l33.pos = [x3 + randint(-j, j), y6 + randint(-j, j)]
    l34.pos = [x4 + randint(-j, j), y6 + randint(-j, j)]
    l35.pos = [x5 + randint(-j, j), y6 + randint(-j, j)]
    l36.pos = [x6 + randint(-j, j), y6 + randint(-j, j)]

    Mo = randint(15, 180)  # set random orientation as the mean of an ensemble

    # save Mo for routine
    st_d = (30)  # sd for set

    list_random = None

    ## make a set size of ensemble
    if len(set_size) > 0:
        if len(trial_elements) > 0:
            s = set_size.pop()

    # make a vector for the set
    if s == 16:
        list_random = np.random.normal(Mo, st_d, 16)
    elif s == 24:
        list_random = np.random.normal(Mo, st_d, 24)
    else:
        list_random = np.random.normal(Mo, st_d, 36)

    x = len(list_random) / 2

    # Line size (I should draw them wider)
    size_line = (25, 50)
    line_Width = 1.3

    l1.lineWidth = line_Width
    l2.lineWidth = line_Width
    l3.lineWidth = line_Width
    l4.lineWidth = line_Width
    l5.lineWidth = line_Width
    l6.lineWidth = line_Width
    l7.lineWidth = line_Width
    l8.lineWidth = line_Width
    l9.lineWidth = line_Width
    l10.lineWidth = line_Width
    l11.lineWidth = line_Width
    l12.lineWidth = line_Width
    l13.lineWidth = line_Width
    l14.lineWidth = line_Width
    l15.lineWidth = line_Width
    l16.lineWidth = line_Width
    l17.lineWidth = line_Width
    l18.lineWidth = line_Width
    l19.lineWidth = line_Width
    l20.lineWidth = line_Width
    l21.lineWidth = line_Width
    l22.lineWidth = line_Width
    l23.lineWidth = line_Width
    l24.lineWidth = line_Width
    l25.lineWidth = line_Width
    l26.lineWidth = line_Width
    l27.lineWidth = line_Width
    l28.lineWidth = line_Width
    l29.lineWidth = line_Width
    l30.lineWidth = line_Width
    l31.lineWidth = line_Width
    l32.lineWidth = line_Width
    l33.lineWidth = line_Width
    l34.lineWidth = line_Width
    l35.lineWidth = line_Width
    l36.lineWidth = line_Width

    # get opacity for set
    ##op_gr1(16) = 8, 9, 10, 11, 14, 15 ,16 ,17, 20, 21, 22, 23, 26, 27, 28, 29
    ##op_gr2(24) = 7, 12, 13, 18, 19, 24, 25, 30
    ##op_gr3(36) = 1, 2, 3, 4, 5, 6, 31, 32, 33 ,34 ,35, 36

    if s == 16:
        op_gr1 = 1
        op_gr2 = 0
        op_gr3 = 0
    elif s == 24:  # + 8
        op_gr1 = 1
        op_gr2 = 1
        op_gr3 = 0
    else:  # 24 + 12
        op_gr1 = 1
        op_gr2 = 1
        op_gr3 = 1

    # sort from smaller to higher
    sort_vers = sorted(list_random)

    # split group
    gr1 = sort_vers[:int(x)]
    gr2 = sort_vers[int(x):]

    # тут условная функция  должна выдавать n (16; 24; 36) случайных значений
    orientation1 = np.random.randint(-15, 0, int(x))
    orientation2 = np.random.randint(0, 15, int(x))

    gr1 += orientation1
    gr2 += orientation2

    # randomize target and distractor
    randomization = list([gr1, gr2])
    random.shuffle(randomization)
    target = randomization[0]
    dist = randomization[1]

    mean_dist_test = mean(target)
    mean_target_test = mean(dist)
    mean_one_unnecessary_1 = [1] * 20
    mean_one_unnecessary_2 = [1] * 12

    # get opacity for set
    ##op_gr1(16) = 8, 9, 10, 11, 14, 15 ,16 ,17, 20, 21, 22, 23, 26, 27, 28, 29
    ##op_gr2(24) = 7, 12, 13, 18, 19, 24, 25, 30
    ##op_gr3(36) = 1, 2, 3, 4, 5, 6, 31, 32, 33 ,34 ,35, 36

    if s == 16:
        l8.ori, l9.ori, l14.ori, l15.ori, l20.ori, l21.ori, l26.ori, l27.ori = target
        l10.ori, l11.ori, l16.ori, l17.ori, l22.ori, l23.ori, l28.ori, l29.ori = dist
        l1.ori, l2.ori, l3.ori, l4.ori, l5.ori, l6.ori, l7.ori, l12.ori, l13.ori, l18.ori, l19.ori, l24.ori, l25.ori, l30.ori, l31.ori, l32.ori, l33.ori, l34.ori, l35.ori, l36.ori = mean_one_unnecessary_1
    elif s == 24:
        l7.ori, l8.ori, l9.ori, l3.ori, l14.ori, l15.ori, l19.ori, l20.ori, l21.ori, l25.ori, l26.ori, l27.ori = target
        l10.ori, l11.ori, l12.ori, l16.ori, l17.ori, l18.ori, l22.ori, l23.ori, l24.ori, l28.ori, l29.ori, l30.ori = dist
        l1.ori, l2.ori, l3.ori, l4.ori, l5.ori, l6.ori, l31.ori, l32.ori, l33.ori, l34.ori, l35.ori, l36.ori = mean_one_unnecessary_2
    else:
        l1.ori, l2.ori, l3.ori, l7.ori, l8.ori, l9.ori, l13.ori, l14.ori, l15.ori, l19.ori, l20.ori, l21.ori, l25.ori, l26.ori, l27.ori, l31.ori, l32.ori, l33.ori = target
        l4.ori, l5.ori, l6.ori, l10.ori, l11.ori, l12.ori, l16.ori, l17.ori, l18.ori, l22.ori, l23.ori, l24.ori, l28.ori, l29.ori, l30.ori, l34.ori, l35.ori, l36.ori = dist

    # l1.ori, l2.ori, l3.ori, l4.ori, l5.ori, l6.ori, l7.ori, l8.ori, l9.ori, l19.ori, l20.ori, l21.ori, l25.ori, l26.ori, l27.ori, l28.ori, l29.ori, l30.ori = target
    # l10.ori, l11.ori, l12.ori, l13.ori, l14.ori, l15.ori, l16.ori, l17.ori, l18.ori, l22.ori, l23.ori, l24.ori,l31.ori, l32.ori, l33.ori, l34.ori, l35.ori, l36.ori = dist

    # recode those scripts?
    # current_color = condition_color_list.pop(0)
    # randomization of color
    if len(condition_color_list) > 0:
        current_color = condition_color_list.pop(0)
    elif len(condition_color_list) < 0:
        break
    # draw 1 and 2 group from color_square (vWM) and colorList with exception
    if s == 16:
        color_for_1gr = [[color_square]] * int(x)
        line_color_gr2 = random.choice([ele for ele in colorList if ele != color_square])
        color_for_2gr = [[line_color_gr2]] * int(x)
        zero_color = [[line_color_gr2]] * (36 - int(s))
    if s == 24:
        color_for_1gr = [[color_square]] * int(x)
        line_color_gr2 = random.choice([ele for ele in colorList if ele != color_square])
        color_for_2gr = [[line_color_gr2]] * int(x)
        zero_color = [[line_color_gr2]] * (36 - int(s))
    else:
        color_for_1gr = [[color_square]] * int(x)
        line_color_gr2 = random.choice([ele for ele in colorList if ele != color_square])
        color_for_2gr = [[line_color_gr2]] * int(x)

    # draw color's lines for group 2 from colorList with exception
    # line_color_gr2 = random.choice ([ele for ele in colorList if ele != color_square])
    # color_for_2gr = [[line_color_gr2]] * 18

    if current_color == 0:
        current_set_size = set_size_0.pop(0)
        ANS_color_square = color_square
        color_for_1gr == color_square
    elif current_color == 1:
        current_set_size = set_size_1.pop(0)
        ANS_color_square = random.choice([ele for ele in colorList if ele != color_square])
        line_color_gr1 = random.choice([ele for ele in colorList if ele != color_square])
        color_for_gr1 = [[line_color_gr1]] * 18

    if s == 16:
        l8.color, l9.color, l14.color, l15.color, l20.color, l21.color, l26.color, l27.color = color_for_1gr
        l10.color, l11.color, l16.color, l17.color, l22.color, l23.color, l28.color, l29.color = color_for_2gr
        l1.color, l2.color, l3.color, l4.color, l5.color, l6.color, l7.color, l12.color, l13.color, l18.color, l19.color, l24.color, l25.color, l30.color, l31.color, l32.color, l33.color, l34.color, l35.color, l36.color = zero_color
    elif s == 24:
        l7.color, l8.color, l9.color, l13.color, l14.color, l15.color, l19.color, l20.color, l21.color, l25.color, l26.color, l27.color = color_for_1gr
        l10.color, l11.color, l12.color, l16.color, l17.color, l18.color, l22.color, l23.color, l24.color, l28.color, l29.color, l30.color = color_for_2gr
        l1.color, l2.color, l3.color, l4.color, l5.color, l6.color, l31.color, l32.color, l33.color, l34.color, l35.color, l36.color = zero_color
    else:
        l1.color, l2.color, l3.color, l7.color, l8.color, l9.color, l13.color, l14.color, l15.color, l19.color, l20.color, l21.color, l25.color, l26.color, l27.color, l31.color, l32.color, l33.color = color_for_1gr
        l4.color, l5.color, l6.color, l10.color, l11.color, l12.color, l16.color, l17.color, l18.color, l22.color, l23.color, l24.color, l28.color, l29.color, l30.color, l34.color, l35.color, l36.color = color_for_2gr

    n = 36  # set size
    rand_jitter_x = []
    rand_jitter_y = []
    for i in range(n):
        rand_jitter_x.append(
            random.randint(-j, j))  # это лист со случайными занчениями для небольшого сдвига положений в пространстве
        rand_jitter_y.append(random.randint(-j, j))

    # lists of X and Y coordinates + random jitter
    x_list = np.repeat([x1, x2, x3, x4, x5, x6], 6) + rand_jitter_x  # output like x1,x1,x1,x1,x1,x2,x2,x2....x6,x6
    y_list = np.array([y1, y2, y3, y4, y5, y6] * 6) + rand_jitter_y  # output like y1,y2,y3,y4,y5,y6,y1,y2....y5,y6
    coord_index = list(range(n))  # create list of indexes for x_list and y_list to randomize the coordinates
    random.shuffle(coord_index)  # shuffle coordinates indexes

    # assign line spatial location
    l1.pos = [x_list[coord_index[0]], y_list[coord_index[0]]]
    l2.pos = [x_list[coord_index[1]], y_list[coord_index[1]]]
    l3.pos = [x_list[coord_index[2]], y_list[coord_index[2]]]
    l4.pos = [x_list[coord_index[3]], y_list[coord_index[3]]]
    l5.pos = [x_list[coord_index[4]], y_list[coord_index[4]]]
    l6.pos = [x_list[coord_index[5]], y_list[coord_index[5]]]
    l7.pos = [x_list[coord_index[6]], y_list[coord_index[6]]]
    l8.pos = [x_list[coord_index[7]], y_list[coord_index[7]]]
    l9.pos = [x_list[coord_index[8]], y_list[coord_index[8]]]
    l10.pos = [x_list[coord_index[9]], y_list[coord_index[9]]]
    l11.pos = [x_list[coord_index[10]], y_list[coord_index[10]]]
    l12.pos = [x_list[coord_index[11]], y_list[coord_index[11]]]
    l13.pos = [x_list[coord_index[12]], y_list[coord_index[12]]]
    l14.pos = [x_list[coord_index[13]], y_list[coord_index[13]]]
    l15.pos = [x_list[coord_index[14]], y_list[coord_index[14]]]
    l16.pos = [x_list[coord_index[15]], y_list[coord_index[15]]]
    l17.pos = [x_list[coord_index[16]], y_list[coord_index[16]]]
    l18.pos = [x_list[coord_index[17]], y_list[coord_index[17]]]
    l19.pos = [x_list[coord_index[18]], y_list[coord_index[18]]]
    l20.pos = [x_list[coord_index[19]], y_list[coord_index[19]]]
    l21.pos = [x_list[coord_index[20]], y_list[coord_index[20]]]
    l22.pos = [x_list[coord_index[21]], y_list[coord_index[21]]]
    l23.pos = [x_list[coord_index[22]], y_list[coord_index[22]]]
    l24.pos = [x_list[coord_index[23]], y_list[coord_index[23]]]
    l25.pos = [x_list[coord_index[24]], y_list[coord_index[24]]]
    l26.pos = [x_list[coord_index[25]], y_list[coord_index[25]]]
    l27.pos = [x_list[coord_index[26]], y_list[coord_index[26]]]
    l28.pos = [x_list[coord_index[27]], y_list[coord_index[27]]]
    l29.pos = [x_list[coord_index[28]], y_list[coord_index[28]]]
    l30.pos = [x_list[coord_index[29]], y_list[coord_index[29]]]
    l31.pos = [x_list[coord_index[30]], y_list[coord_index[30]]]
    l32.pos = [x_list[coord_index[31]], y_list[coord_index[31]]]
    l33.pos = [x_list[coord_index[32]], y_list[coord_index[32]]]
    l34.pos = [x_list[coord_index[33]], y_list[coord_index[33]]]
    l35.pos = [x_list[coord_index[34]], y_list[coord_index[34]]]
    l36.pos = [x_list[coord_index[35]], y_list[coord_index[35]]]
    l1.setOpacity(op_gr3)
    l1.setSize(size_line)
    l2.setFillColor(color_square)
    l2.setOpacity(op_gr3)
    l2.setSize(size_line)
    l3.setOpacity(op_gr3)
    l3.setSize(size_line)
    l4.setOpacity(op_gr3)
    l4.setSize(size_line)
    l5.setOpacity(op_gr3)
    l5.setSize(size_line)
    l6.setOpacity(op_gr3)
    l6.setSize(size_line)
    l7.setOpacity(op_gr2)
    l7.setSize(size_line)
    l8.setOpacity(op_gr1)
    l8.setSize(size_line)
    l9.setOpacity(op_gr1)
    l9.setSize(size_line)
    l10.setOpacity(op_gr1)
    l10.setSize(size_line)
    l11.setOpacity(op_gr1)
    l11.setSize(size_line)
    l12.setOpacity(op_gr2)
    l12.setSize(size_line)
    l13.setOpacity(op_gr2)
    l13.setSize(size_line)
    l14.setOpacity(op_gr1)
    l14.setSize(size_line)
    l15.setOpacity(op_gr1)
    l15.setSize(size_line)
    l16.setOpacity(op_gr1)
    l16.setSize(size_line)
    l17.setOpacity(op_gr1)
    l17.setSize(size_line)
    l18.setOpacity(op_gr2)
    l18.setSize(size_line)
    l19.setOpacity(op_gr2)
    l19.setSize(size_line)
    l20.setOpacity(op_gr1)
    l20.setSize(size_line)
    l21.setOpacity(op_gr1)
    l21.setSize(size_line)
    l22.setOpacity(op_gr1)
    l22.setSize(size_line)
    l23.setOpacity(op_gr1)
    l23.setSize(size_line)
    l24.setOpacity(op_gr2)
    l24.setSize(size_line)
    l25.setOpacity(op_gr2)
    l25.setSize(size_line)
    l26.setOpacity(op_gr1)
    l26.setSize(size_line)
    l27.setSize(size_line)
    l28.setOpacity(op_gr1)
    l28.setSize(size_line)
    l29.setOpacity(op_gr1)
    l29.setSize(size_line)
    l30.setOpacity(op_gr2)
    l30.setSize(size_line)
    l31.setOpacity(op_gr3)
    l31.setSize(size_line)
    l32.setOpacity(op_gr3)
    l32.setSize(size_line)
    l33.setOpacity(op_gr3)
    l33.setSize(size_line)
    l34.setOpacity(op_gr3)
    l34.setSize(size_line)
    l35.setOpacity(op_gr3)
    l35.setSize(size_line)
    l36.setOpacity(op_gr3)
    l36.setSize(size_line)
    # keep track of which components have finished
    trial_probeComponents = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20,
                             l21, l22, l23, l24, l25, l26, l27, l28, l29, l30, l31, l32, l33, l34, l35, l36]
    for thisComponent in trial_probeComponents:
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

    # --- Run Routine "trial_probe" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *l1* updates
        if l1.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l1.frameNStart = frameN  # exact frame index
            l1.tStart = t  # local t and not account for scr refresh
            l1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l1.started')
            l1.setAutoDraw(True)
        if l1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l1.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l1.tStop = t  # not accounting for scr refresh
                l1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l1.stopped')
                l1.setAutoDraw(False)

        # *l2* updates
        if l2.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l2.frameNStart = frameN  # exact frame index
            l2.tStart = t  # local t and not account for scr refresh
            l2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l2.started')
            l2.setAutoDraw(True)
        if l2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l2.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l2.tStop = t  # not accounting for scr refresh
                l2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l2.stopped')
                l2.setAutoDraw(False)

        # *l3* updates
        if l3.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l3.frameNStart = frameN  # exact frame index
            l3.tStart = t  # local t and not account for scr refresh
            l3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l3.started')
            l3.setAutoDraw(True)
        if l3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l3.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l3.tStop = t  # not accounting for scr refresh
                l3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l3.stopped')
                l3.setAutoDraw(False)

        # *l4* updates
        if l4.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l4.frameNStart = frameN  # exact frame index
            l4.tStart = t  # local t and not account for scr refresh
            l4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l4.started')
            l4.setAutoDraw(True)
        if l4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l4.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l4.tStop = t  # not accounting for scr refresh
                l4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l4.stopped')
                l4.setAutoDraw(False)

        # *l5* updates
        if l5.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l5.frameNStart = frameN  # exact frame index
            l5.tStart = t  # local t and not account for scr refresh
            l5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l5.started')
            l5.setAutoDraw(True)
        if l5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l5.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l5.tStop = t  # not accounting for scr refresh
                l5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l5.stopped')
                l5.setAutoDraw(False)

        # *l6* updates
        if l6.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l6.frameNStart = frameN  # exact frame index
            l6.tStart = t  # local t and not account for scr refresh
            l6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l6.started')
            l6.setAutoDraw(True)
        if l6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l6.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l6.tStop = t  # not accounting for scr refresh
                l6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l6.stopped')
                l6.setAutoDraw(False)

        # *l7* updates
        if l7.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l7.frameNStart = frameN  # exact frame index
            l7.tStart = t  # local t and not account for scr refresh
            l7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l7.started')
            l7.setAutoDraw(True)
        if l7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l7.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l7.tStop = t  # not accounting for scr refresh
                l7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l7.stopped')
                l7.setAutoDraw(False)

        # *l8* updates
        if l8.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l8.frameNStart = frameN  # exact frame index
            l8.tStart = t  # local t and not account for scr refresh
            l8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l8.started')
            l8.setAutoDraw(True)
        if l8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l8.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l8.tStop = t  # not accounting for scr refresh
                l8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l8.stopped')
                l8.setAutoDraw(False)

        # *l9* updates
        if l9.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l9.frameNStart = frameN  # exact frame index
            l9.tStart = t  # local t and not account for scr refresh
            l9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l9.started')
            l9.setAutoDraw(True)
        if l9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l9.tStartRefresh + ens_start - frameTolerance:
                # keep track of stop time/frame for later
                l9.tStop = t  # not accounting for scr refresh
                l9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l9.stopped')
                l9.setAutoDraw(False)

        # *l10* updates
        if l10.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l10.frameNStart = frameN  # exact frame index
            l10.tStart = t  # local t and not account for scr refresh
            l10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l10.started')
            l10.setAutoDraw(True)
        if l10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l10.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l10.tStop = t  # not accounting for scr refresh
                l10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l10.stopped')
                l10.setAutoDraw(False)

        # *l11* updates
        if l11.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l11.frameNStart = frameN  # exact frame index
            l11.tStart = t  # local t and not account for scr refresh
            l11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l11.started')
            l11.setAutoDraw(True)
        if l11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l11.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l11.tStop = t  # not accounting for scr refresh
                l11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l11.stopped')
                l11.setAutoDraw(False)

        # *l12* updates
        if l12.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l12.frameNStart = frameN  # exact frame index
            l12.tStart = t  # local t and not account for scr refresh
            l12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l12.started')
            l12.setAutoDraw(True)
        if l12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l12.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l12.tStop = t  # not accounting for scr refresh
                l12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l12.stopped')
                l12.setAutoDraw(False)

        # *l13* updates
        if l13.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l13.frameNStart = frameN  # exact frame index
            l13.tStart = t  # local t and not account for scr refresh
            l13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l13.started')
            l13.setAutoDraw(True)
        if l13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l13.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l13.tStop = t  # not accounting for scr refresh
                l13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l13.stopped')
                l13.setAutoDraw(False)

        # *l14* updates
        if l14.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l14.frameNStart = frameN  # exact frame index
            l14.tStart = t  # local t and not account for scr refresh
            l14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l14.started')
            l14.setAutoDraw(True)
        if l14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l14.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l14.tStop = t  # not accounting for scr refresh
                l14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l14.stopped')
                l14.setAutoDraw(False)

        # *l15* updates
        if l15.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l15.frameNStart = frameN  # exact frame index
            l15.tStart = t  # local t and not account for scr refresh
            l15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l15.started')
            l15.setAutoDraw(True)
        if l15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l15.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l15.tStop = t  # not accounting for scr refresh
                l15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l15.stopped')
                l15.setAutoDraw(False)

        # *l16* updates
        if l16.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l16.frameNStart = frameN  # exact frame index
            l16.tStart = t  # local t and not account for scr refresh
            l16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l16.started')
            l16.setAutoDraw(True)
        if l16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l16.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l16.tStop = t  # not accounting for scr refresh
                l16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l16.stopped')
                l16.setAutoDraw(False)

        # *l17* updates
        if l17.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l17.frameNStart = frameN  # exact frame index
            l17.tStart = t  # local t and not account for scr refresh
            l17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l17.started')
            l17.setAutoDraw(True)
        if l17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l17.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l17.tStop = t  # not accounting for scr refresh
                l17.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l17.stopped')
                l17.setAutoDraw(False)

        # *l18* updates
        if l18.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l18.frameNStart = frameN  # exact frame index
            l18.tStart = t  # local t and not account for scr refresh
            l18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l18, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l18.started')
            l18.setAutoDraw(True)
        if l18.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l18.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l18.tStop = t  # not accounting for scr refresh
                l18.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l18.stopped')
                l18.setAutoDraw(False)

        # *l19* updates
        if l19.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l19.frameNStart = frameN  # exact frame index
            l19.tStart = t  # local t and not account for scr refresh
            l19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l19, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l19.started')
            l19.setAutoDraw(True)
        if l19.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l19.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l19.tStop = t  # not accounting for scr refresh
                l19.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l19.stopped')
                l19.setAutoDraw(False)

        # *l20* updates
        if l20.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l20.frameNStart = frameN  # exact frame index
            l20.tStart = t  # local t and not account for scr refresh
            l20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l20, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l20.started')
            l20.setAutoDraw(True)
        if l20.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l20.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l20.tStop = t  # not accounting for scr refresh
                l20.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l20.stopped')
                l20.setAutoDraw(False)

        # *l21* updates
        if l21.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l21.frameNStart = frameN  # exact frame index
            l21.tStart = t  # local t and not account for scr refresh
            l21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l21, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l21.started')
            l21.setAutoDraw(True)
        if l21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l21.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l21.tStop = t  # not accounting for scr refresh
                l21.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l21.stopped')
                l21.setAutoDraw(False)

        # *l22* updates
        if l22.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l22.frameNStart = frameN  # exact frame index
            l22.tStart = t  # local t and not account for scr refresh
            l22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l22, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l22.started')
            l22.setAutoDraw(True)
        if l22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l22.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l22.tStop = t  # not accounting for scr refresh
                l22.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l22.stopped')
                l22.setAutoDraw(False)

        # *l23* updates
        if l23.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l23.frameNStart = frameN  # exact frame index
            l23.tStart = t  # local t and not account for scr refresh
            l23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l23.started')
            l23.setAutoDraw(True)
        if l23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l23.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l23.tStop = t  # not accounting for scr refresh
                l23.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l23.stopped')
                l23.setAutoDraw(False)

        # *l24* updates
        if l24.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l24.frameNStart = frameN  # exact frame index
            l24.tStart = t  # local t and not account for scr refresh
            l24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l24, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l24.started')
            l24.setAutoDraw(True)
        if l24.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l24.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l24.tStop = t  # not accounting for scr refresh
                l24.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l24.stopped')
                l24.setAutoDraw(False)

        # *l25* updates
        if l25.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l25.frameNStart = frameN  # exact frame index
            l25.tStart = t  # local t and not account for scr refresh
            l25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l25, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l25.started')
            l25.setAutoDraw(True)
        if l25.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l25.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l25.tStop = t  # not accounting for scr refresh
                l25.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l25.stopped')
                l25.setAutoDraw(False)

        # *l26* updates
        if l26.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l26.frameNStart = frameN  # exact frame index
            l26.tStart = t  # local t and not account for scr refresh
            l26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l26, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l26.started')
            l26.setAutoDraw(True)
        if l26.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l26.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l26.tStop = t  # not accounting for scr refresh
                l26.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l26.stopped')
                l26.setAutoDraw(False)

        # *l27* updates
        if l27.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l27.frameNStart = frameN  # exact frame index
            l27.tStart = t  # local t and not account for scr refresh
            l27.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l27, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l27.started')
            l27.setAutoDraw(True)
        if l27.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l27.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l27.tStop = t  # not accounting for scr refresh
                l27.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l27.stopped')
                l27.setAutoDraw(False)
        if l27.status == STARTED:  # only update if drawing
            l27.setOpacity(op_gr1, log=False)

        # *l28* updates
        if l28.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l28.frameNStart = frameN  # exact frame index
            l28.tStart = t  # local t and not account for scr refresh
            l28.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l28, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l28.started')
            l28.setAutoDraw(True)
        if l28.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l28.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l28.tStop = t  # not accounting for scr refresh
                l28.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l28.stopped')
                l28.setAutoDraw(False)

        # *l29* updates
        if l29.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l29.frameNStart = frameN  # exact frame index
            l29.tStart = t  # local t and not account for scr refresh
            l29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l29, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l29.started')
            l29.setAutoDraw(True)
        if l29.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l29.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l29.tStop = t  # not accounting for scr refresh
                l29.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l29.stopped')
                l29.setAutoDraw(False)

        # *l30* updates
        if l30.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l30.frameNStart = frameN  # exact frame index
            l30.tStart = t  # local t and not account for scr refresh
            l30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l30, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l30.started')
            l30.setAutoDraw(True)
        if l30.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l30.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l30.tStop = t  # not accounting for scr refresh
                l30.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l30.stopped')
                l30.setAutoDraw(False)

        # *l31* updates
        if l31.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l31.frameNStart = frameN  # exact frame index
            l31.tStart = t  # local t and not account for scr refresh
            l31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l31, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l31.started')
            l31.setAutoDraw(True)
        if l31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l31.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l31.tStop = t  # not accounting for scr refresh
                l31.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l31.stopped')
                l31.setAutoDraw(False)

        # *l32* updates
        if l32.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l32.frameNStart = frameN  # exact frame index
            l32.tStart = t  # local t and not account for scr refresh
            l32.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l32, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l32.started')
            l32.setAutoDraw(True)
        if l32.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l32.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l32.tStop = t  # not accounting for scr refresh
                l32.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l32.stopped')
                l32.setAutoDraw(False)

        # *l33* updates
        if l33.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l33.frameNStart = frameN  # exact frame index
            l33.tStart = t  # local t and not account for scr refresh
            l33.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l33, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l33.started')
            l33.setAutoDraw(True)
        if l33.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l33.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l33.tStop = t  # not accounting for scr refresh
                l33.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l33.stopped')
                l33.setAutoDraw(False)

        # *l34* updates
        if l34.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l34.frameNStart = frameN  # exact frame index
            l34.tStart = t  # local t and not account for scr refresh
            l34.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l34, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l34.started')
            l34.setAutoDraw(True)
        if l34.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l34.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l34.tStop = t  # not accounting for scr refresh
                l34.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l34.stopped')
                l34.setAutoDraw(False)

        # *l35* updates
        if l35.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l35.frameNStart = frameN  # exact frame index
            l35.tStart = t  # local t and not account for scr refresh
            l35.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l35, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l35.started')
            l35.setAutoDraw(True)
        if l35.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l35.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l35.tStop = t  # not accounting for scr refresh
                l35.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l35.stopped')
                l35.setAutoDraw(False)

        # *l36* updates
        if l36.status == NOT_STARTED and tThisFlip >= ens_start - frameTolerance:
            # keep track of start time/frame for later
            l36.frameNStart = frameN  # exact frame index
            l36.tStart = t  # local t and not account for scr refresh
            l36.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l36, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l36.started')
            l36.setAutoDraw(True)
        if l36.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l36.tStartRefresh + ens_duration - frameTolerance:
                # keep track of stop time/frame for later
                l36.tStop = t  # not accounting for scr refresh
                l36.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l36.stopped')
                l36.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_probeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "trial_probe" ---
    for thisComponent in trial_probeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "trial_probe" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # --- Prepare to start Routine "ITI2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_6
    # Hide the mouse
    event.Mouse(visible=False, newPos=[0, 0], win=None)

    duration_ITI1 = random.choice([0.3, 0.5])
    # keep track of which components have finished
    ITI2Components = [polygon_4]
    for thisComponent in ITI2Components:
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

    # --- Run Routine "ITI2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_4.started')
            polygon_4.setAutoDraw(True)
        if polygon_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_4.tStartRefresh + duration_ITI1 - frameTolerance:
                # keep track of stop time/frame for later
                polygon_4.tStop = t  # not accounting for scr refresh
                polygon_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_4.stopped')
                polygon_4.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "ITI2" ---
    for thisComponent in ITI2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ITI2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # --- Prepare to start Routine "answer_ENS_probe" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    l1_answer.setSize(size_line)
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # Run 'Begin Routine' code from code_8
    size_line = (40, 500)

    line_Width = 1
    l1_answer.lineWidth = line_Width

    l1_answer.ori = Mo
    # gr3 = np.concatenate(([gr1 + gr2]), axis = None)
    # line_A = random.choice(gr3)
    # keep track of which components have finished
    answer_ENS_probeComponents = [l1_answer, key_resp_3, text_4]
    for thisComponent in answer_ENS_probeComponents:
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

    # --- Run Routine "answer_ENS_probe" ---
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *l1_answer* updates
        if l1_answer.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            l1_answer.frameNStart = frameN  # exact frame index
            l1_answer.tStart = t  # local t and not account for scr refresh
            l1_answer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l1_answer, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'l1_answer.started')
            l1_answer.setAutoDraw(True)
        if l1_answer.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l1_answer.tStartRefresh + 6.0 - frameTolerance:
                # keep track of stop time/frame for later
                l1_answer.tStop = t  # not accounting for scr refresh
                l1_answer.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'l1_answer.stopped')
                l1_answer.setAutoDraw(False)

        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_3.tStartRefresh + 6.0 - frameTolerance:
                # keep track of stop time/frame for later
                key_resp_3.tStop = t  # not accounting for scr refresh
                key_resp_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.stopped')
                key_resp_3.status = FINISHED
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 6.0 - frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_4.stopped')
                text_4.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in answer_ENS_probeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "answer_ENS_probe" ---
    for thisComponent in answer_ENS_probeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials.addData('key_resp_3.keys', key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials.addData('key_resp_3.rt', key_resp_3.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)

    # --- Prepare to start Routine "answer_vWM_probe" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    polygon.setFillColor(ANS_color_square)
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    answer_vWM_probeComponents = [polygon, key_resp_4, text_5]
    for thisComponent in answer_vWM_probeComponents:
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

    # --- Run Routine "answer_vWM_probe" ---
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon.started')
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 6.0 - frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon.stopped')
                polygon.setAutoDraw(False)

        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_4.started')
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_4.tStartRefresh + 6.0 - frameTolerance:
                # keep track of stop time/frame for later
                key_resp_4.tStop = t  # not accounting for scr refresh
                key_resp_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_4.stopped')
                key_resp_4.status = FINISHED
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['y', 'n'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.started')
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 6.0 - frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.stopped')
                text_5.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in answer_vWM_probeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "answer_vWM_probe" ---
    for thisComponent in answer_vWM_probeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    trials.addData('key_resp_4.keys', key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials.addData('key_resp_4.rt', key_resp_4.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    thisExp.nextEntry()

# completed 540.0 repeats of 'trials'


# --- Prepare to start Routine "thx" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
thxComponents = [text_2]
for thisComponent in thxComponents:
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

# --- Run Routine "thx" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_2.started')
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 5.0 - frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.stopped')
            text_2.setAutoDraw(False)

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "thx" ---
for thisComponent in thxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename + '.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
