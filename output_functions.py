#!/usr/bin/env python3

class col:
    LOWRED      = '\033[94m'
    OKGREEN     = '\033[92m'
    YELLOW      = '\033[93m'
    FAIL        = '\033[91m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'


###################################
#                                 #
#      Output functions           #
#                                 #
###################################

def printError():
    printFront('-', col.FAIL)
    print (col.FAIL + "Error" + col.ENDC + ': ', end='')

def printFront(c, color):
    print (col.BOLD + "[" + color + c + col.ENDC + col.BOLD + "] " + col.ENDC, end='')

def printUsage():
    print (col.BOLD + "    Usage:"+ col.ENDC +  " py3 hash_crack <hash_type*> <fileToCrack> <dict_file>")
    print ("     *hash_type: All / UNIX_crypt / SHA256 / SHA512")
    print ("     fileToCrack: must contain format: \"user:passwd\"")

def argLenError():
    printError()
    print ("number of arguments is not valid.")
    printUsage()
    return False

def fileDoNotExist(filename):
    printError()
    print (filename + " does not exist")

def wrongPermOnFile(filename):
    printError()
    print ("you don't have the right to read " + filename)

def errorInHash(hashName):
    printError()
    print ("\"" + hashName + "\" is not a valid hash")
    printUsage()
    return False

def printBye():
    print("\n\n########### Bye ###########\n")

def printSuccess(user, passToCrack, passwd):
    printFront('V', col.OKGREEN)
    print (passToCrack + " from " + user + col.OKGREEN + " CRACKED" + col.ENDC)
    printFront('V', col.OKGREEN)
    print ("password: \"" + passwd.strip('\n') + "\"\n")

def printFailure(user, passToCrack, hashName):
    printFront('X', col.FAIL)
    print ("PASSWORD" + col.FAIL + " RESISTED " + col.ENDC + "with " + hashName + " hash cracking")
    printFront('X', col.FAIL)
    print (user + ':' + passToCrack + " still remain\n")
