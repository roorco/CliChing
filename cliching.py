#!/usr/bin/env/python2
# -*- coding: utf-8 -*-
# CliChing by roberto dell'orco 2014
# I-Ching on command line
#

import pydoc

import random 

from time import sleep

from iching64 import *


iching_A = 0

iching_B = 0

mutatis = False             # Variable that activates the mutation process


class Line(object):         # It starts the program, intro and choose the line of the hexagram

    def intro(self):

        print "\n"
        print bcolors.PURPLE + "CliChing by roberto dell'orco 2014" + bcolors.ENDC
        print "I-Ching on command line"
        print "Richard Wilhelm traslation 1950"
        print "CliChing is distribuited under"
        print "GNU Creative Commons License"
        print "\n"
        Line().question()

    def question(self):     # The question can be whatever, but not empty
        print bcolors.YELLOW + "Please, write your question: " + bcolors.ENDC
        quest = raw_input('> ')
        if quest == '':
            Line().question()
        else:
           Line().exa()

    def exa(self):          # I wonder if there is a better way of choosing ramndom lines, seems a bit rigid to me
        print "Here the exagram from I-Ching: "
        print "\n"
        print "Legend:"
        print "young yin line   -   -"
        print "young yang line  -----"
        print "old yin line     - x -"
        print "old yang line    --o--"
        sleep(1)            # it adds some waiting time, suspence.
        yin_yang = ['-   -', '-   -', '-   -', '-----', '-----', '-----', '- x -', '--o--'] # ratio 3/8+3/8+1/8+1/8
        line1 = random.choice(yin_yang)
        line2 = random.choice(yin_yang)
        line3 = random.choice(yin_yang)
        line4 = random.choice(yin_yang)
        line5 = random.choice(yin_yang)
        line6 = random.choice(yin_yang)
        print '\n'             
        print bcolors.BLUE + '6', '\t', line6 + bcolors.ENDC
        print bcolors.BLUE + '5', '\t', line5 + bcolors.ENDC
        print bcolors.BLUE + '4', '\t', line4 + bcolors.ENDC
        print bcolors.BLUE + '3', '\t', line3 + bcolors.ENDC
        print bcolors.BLUE + '2', '\t', line2 + bcolors.ENDC
        print bcolors.BLUE + '1', '\t', line1 + bcolors.ENDC
        sleep(1)               
        print '\n'             
                               
        T = Trans(line1, line2 , line3, line4, line5, line6)
        T.binary()             


class bcolors:              # add COLOR to printed lines in terminal
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'


class Trans(object):        # Translates the first hexagram in a binary number, I suppose is the same operation Leibniz did, when he first discovered binary numbers

    def __init__(self, line1, line2, line3, line4, line5, line6):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.line4 = line4
        self.line5 = line5
        self.line6 = line6

    def binary(self):       # Can be improved with curses giving the printing order from bottom to top
        bline1 = int(0) if self.line1 == '-   -' or self.line1 == '- x -' else int(1)
        bline2 = int(0) if self.line2 == '-   -' or self.line2 == '- x -' else int(1)
        bline3 = int(0) if self.line3 == '-   -' or self.line3 == '- x -' else int(1)
        bline4 = int(0) if self.line4 == '-   -' or self.line4 == '- x -' else int(1)
        bline5 = int(0) if self.line5 == '-   -' or self.line5 == '- x -' else int(1)
        bline6 = int(0) if self.line6 == '-   -' or self.line6 == '- x -' else int(1)

        binary = (bline6, bline5, bline4, bline3, bline2, bline1)
        num=int("".join(str(x) for x in binary),2)
        global mutatis
        if mutatis == True:
            global iching_B
            iching_B = iching64.exa[num]
            name = iching64.name[iching_B].decode('utf-8')
        else:
            global iching_A
            iching_A = iching64.exa[num]
            name = iching64.name[iching_A].decode('utf-8')
        print name
        print '----------------------------------'
        
        M = Mutation(self.line1, self.line2, self.line3, self.line4, self.line5, self.line6)
        return M.match()


class Mutation(object):     # It transform all mutating lines in their mutations

    def __init__(self, line1, line2, line3, line4, line5, line6):
        self.line1 = line1 
        self.line2 = line2
        self.line3 = line3
        self.line4 = line4
        self.line5 = line5
        self.line6 = line6

    def match(self):        # It matches the hexagram and its mutation 
        mline1 = '-   -' if self.line1 == '--o--' or self.line1 == '-   -' else '-----'
        mline2 = '-   -' if self.line2 == '--o--' or self.line2 == '-   -' else '-----'
        mline3 = '-   -' if self.line3 == '--o--' or self.line3 == '-   -' else '-----'
        mline4 = '-   -' if self.line4 == '--o--' or self.line4 == '-   -' else '-----'
        mline5 = '-   -' if self.line5 == '--o--' or self.line5 == '-   -' else '-----'
        mline6 = '-   -' if self.line6 == '--o--' or self.line6 == '-   -' else '-----'
        A = mline6 + mline5 + mline4 + mline3 + mline2 + mline1
        B = self.line6 + self.line5 + self.line4 + self.line3 + self.line2 + self.line1
        
        if A != B:
            global mutatis
            mutatis = True
            M = Mutation(mline1, mline2, mline3, mline4, mline5, mline6)
            M.exa()
        else:
            print "\n"
            raw_input('Press Enter to read the response')
            R = Response()
            R.wilhelm()

    def exa(self):          # Prints mutation with a different color from first one
        print "\n"
        raw_input('Press Enter to see the mutation')
        print "This is the mutation"
        #sleep(1)
        print '\n'
        print bcolors.YELLOW + '6', '\t', self.line6 + bcolors.ENDC
        print bcolors.YELLOW + '5', '\t', self.line5 + bcolors.ENDC
        print bcolors.YELLOW + '4', '\t', self.line4 + bcolors.ENDC
        print bcolors.YELLOW + '3', '\t', self.line3 + bcolors.ENDC
        print bcolors.YELLOW + '2', '\t', self.line2 + bcolors.ENDC
        print bcolors.YELLOW + '1', '\t', self.line1 + bcolors.ENDC
        print '\n'

        T = Trans(self.line1, self.line2, self.line3, self.line4, self.line5, self.line6)
        T.binary()


class Response(object):     # It gives the response of one or two response (It could be added a different color for mutating lines)

    def wilhelm(self):
        global mutatis
        global iching_A
        global iching_B

        if mutatis == True:
            ik_A = 'ik/ik-%r.txt' % (iching_A)
            ik_B = 'ik/ik-%r.txt' % (iching_B)
            ikopen_A = open(ik_A, 'r')
            ikopen_B = open(ik_B, 'r')
            responseA = ikopen_A.read()
            pydoc.pager(responseA)
            responseB = ikopen_B.read()
            pydoc.pager(responseB)
        else:
            ik_A = 'ik/ik-%r.txt' % (iching_A)
            ikopen_A = open(ik_A, 'r')
            responseA = ikopen_A.read()
            pydoc.pager(responseA)


Line().intro()
