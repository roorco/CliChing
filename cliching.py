# -*- coding: utf-8 -*-
# CliChing by roberto dell'orco 2014
# An attempt to make I-Ching accessible from command line
#
#
#

import pydoc
import random 
from time import sleep

iching_A = 0
iching_B = 0
mutatis = False


class Line(object): 

    def intro(x):

        print "\n"
        print bcolors.OKBLUE + "CliChing by roberto dell'orco 2014" + bcolors.ENDC
        print "I-Ching on command line"
        print "Richard Wilhelm traslation 1950"
        print "CliChing is distribuited under"
        print "GNU Creative Commons License"
        print "\n"
        Line().question()

    def question(x):
        print bcolors.WARNING + "Please, write your question: " + bcolors.ENDC
        quest = raw_input('> ')
        if quest == '':
            Line().question()
        else:
           Line().exa()

    def exa(x):
        yin_yang = ['-   -', '-   -', '-   -', '-----', '-----', '-----', '- x -', '--o--'] # ratio should be 3/8+3/8+1/8+1/8
        line1 = random.choice(yin_yang)
        line2 = random.choice(yin_yang)
        line3 = random.choice(yin_yang)
        line4 = random.choice(yin_yang)
        line5 = random.choice(yin_yang)
        line6 = random.choice(yin_yang)
        print "Here the exagram from I-Ching: "
        print "\n"
        print "Legend:"
        print "young yin line   -   -"
        print "young yang line  -----"
        print "old yin line     - x -"
        print "old yang line    --o--"
        sleep(2) # it adds some waiting time
        print '\n'
        print bcolors.OKBLUE + '\t', line6 + bcolors.ENDC
        print bcolors.OKBLUE + '\t', line5 + bcolors.ENDC
        print bcolors.OKBLUE + '\t', line4 + bcolors.ENDC
        print bcolors.OKBLUE + '\t', line3 + bcolors.ENDC
        print bcolors.OKBLUE + '\t', line2 + bcolors.ENDC
        print bcolors.OKBLUE + '\t', line1 + bcolors.ENDC
        print '\n'

        T = Trans(line1, line2, line3, line4, line5, line6)
        T.binary()

class Trans(object): # Translates the first hexagram in a binary number, I suppose is the same operation Leibniz did, when he first discovered binary numbers
    def __init__(self, line1, line2, line3, line4, line5, line6):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.line4 = line4
        self.line5 = line5
        self.line6 = line6

    def binary(self):
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

class Response(object):
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

class Mutation(object): # It transform all mutating lines in their mutations
    def __init__(self, line1, line2, line3, line4, line5, line6):
        self.line1 = line1 
        self.line2 = line2
        self.line3 = line3
        self.line4 = line4
        self.line5 = line5
        self.line6 = line6

    def match(self):
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

    def exa(self):
        print "\n"
        print "This is the mutation"
        #sleep(1)
        print '\n'
        print bcolors.WARNING + '\t', self.line6 + bcolors.ENDC
        print bcolors.WARNING + '\t', self.line5 + bcolors.ENDC
        print bcolors.WARNING + '\t', self.line4 + bcolors.ENDC
        print bcolors.WARNING + '\t', self.line3 + bcolors.ENDC
        print bcolors.WARNING + '\t', self.line2 + bcolors.ENDC
        print bcolors.WARNING + '\t', self.line1 + bcolors.ENDC
        print '\n'

        T = Trans(self.line1, self.line2, self.line3, self.line4, self.line5, self.line6)
        T.binary()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class iching64(object): # Contains the dictionary of binary number and actual number of I-Ching.
    name = {
            1 : "1. Ch'ien / The Creative",
            2 : "2. K'un / The Receptive, Earth",
            3 : "3. Chun / Difficulty at the Beginning ",
            4 : "4. Mêng / Youthful Folly",
            5 : "5. Hsü / Waiting (Nourishment)",
            6 : "6. Sung / Conflict",
            7 : "7. Shih / The Army",
            8 : "8. Pi / Holding Together [union]",
            9 : "9. Hsiao Ch'u / The Taming Power of the Small",
            10 : "10. Lü / Treading [conduct]",
            11 : "11. T'ai / Peace",
            12 : "12. P'i / Standstill [Stagnation]",
            13 : "13. T'ung Jên / Fellowship with Men",
            14 : "14. Ta Yu / Possession in Great Measure",
            15 : "15. Ch'ien / Modesty",
            16 : "16. Yü / Enthusiasm",
            17 : "17. Sui / Following",
            18 : "18. Ku / Work on what has been spoiled [ Decay ]",
            19 : "19. Lin / Approach",
            20 : "20. Kuan / Contemplation (View)",
            21 : "21. Shih Ho / Biting Through",
            22 : "22. Pi / Grace",
            23 : "23. Po / Splitting Apart",
            24 : "24. Fu / Return (The Turning Point)",
            25 : "25. Wu Wang / Innocence (The Unexpected)",
            26 : "26. Ta Ch'u / The Taming Power of the Great",
            27 : "27. I / Corners of the Mouth (Providing Nourishment)",
            28 : "28. Ta Kuo / Preponderance of the Great",
            29 : "29. K'an / The Abysmal (Water)",
            30 : "30. Li / The Clinging, Fire",
            31 : "31. Hsien / Influence (Wooing)",
            32 : "32. Hêng / Duration",
            33 : "33. TUN / Retreat",
            34 : "34. Ta Chuang / The Power of the Great",
            35 : "35. Chin / Progress",
            36 : "36. Ming I / Darkening of the light",
            37 : "37. Chia Jên / The Family [The Clan]",
            38 : "38. K'uei / Opposition",
            39 : "39. Chien / Obstruction",
            40 : "40. Hsieh / Deliverance",
            41 : "41. Sun / Decrease",
            42 : "42. I / Increase",
            43 : "43. Kuai / Break-through (Resoluteness)",
            44 : "44. Kou / Coming to Meet",
            45 : "45. Ts'ui / Gathering Together [Massing]",
            46 : "46. Shêng / Pushing Upward",
            47 : "47. K'un / Oppression (Exhaustion)",
            48 : "48. Ching / The Well",
            49 : "49. Ko / Revolution (Molting)",
            50 : "50. Ting / The Caldron",
            51 : "51. Chên / The Arousing (Shock, Thunder)",
            52 : "52. Kên / Keeping Still, Mountain",
            53 : "53. Chien / Development (Gradual Progress)",
            54 : "54. Kuei Mei / The Marrying Maiden",
            55 : "55. Fêng / Abundance [Fullness]",
            56 : "56. Lü / The Wanderer",
            57 : "57. Sun / The Gentle (The Penetrating, Wind)",
            58 : "58. Tui / The Joyous, Lake",
            59 : "59. Huan / Dispersion [Dissolution]",
            60 : "60. Chieh / Limitation",
            61 : "61. Chung Fu / Inner Truth",
            62 : "62. Hsiao Kuo / Preponderance of the Small",
            63 : "63. Chi Chi / After Completion",
            64 : "64. Wei Chi / Before Completion"
    }

    exa= {
            0b111111 : 1,
            0b000000 : 2,
            0b010001 : 3,
            0b100010 : 4,
            0b010111 : 5,
            0b111010 : 6,
            0b000010 : 7,
            0b000010 : 8,
            0b111011 : 9,
            0b110111 : 10,
            0b000111 : 11,
            0b111000 : 12,
            0b111101 : 13,
            0b101111 : 14,
            0b000100 : 15,
            0b001000 : 16,
            0b011001 : 17,
            0b100110 : 18,
            0b000011 : 19,
            0b110000 : 20,
            0b101001 : 21,
            0b100101 : 22,
            0b100000 : 23,
            0b000001 : 24,
            0b111001 : 25,
            0b100111 : 26,
            0b100001 : 27,
            0b011110 : 28,
            0b010010 : 29,
            0b101101 : 30,
            0b011100 : 31,
            0b001110 : 32,
            0b111100 : 33,
            0b001111 : 34,
            0b101000 : 35,
            0b000101 : 36,
            0b110101 : 37,
            0b101011 : 38,
            0b010100 : 39,
            0b001010 : 40,
            0b100011 : 41,
            0b110001 : 42,
            0b011111 : 43,
            0b111110 : 44,
            0b011000 : 46,
            0b011010 : 47,
            0b010110 : 48,
            0b011101 : 49,
            0b101110 : 50,
            0b001001 : 52,
            0b110100 : 53,
            0b001011 : 55,
            0b101100 : 56,
            0b110110 : 57,
            0b011011 : 58,
            0b110010 : 59,
            0b010011 : 60,
            0b110011 : 61,
            0b001100 : 62,
            0b010101 : 63,
            0b101010 : 64
}

Line().intro()
