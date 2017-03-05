#!/usr/bin/env python3

import os
import crypt
import sys
import hashlib
import optparse

from output_functions import *

result		= {}

###################################
#                                 #
#      Preprocess                 #
#                                 #
###################################

def main():
    hashType, logsToCrack, dictFile = parserCmd()
    if (trueArg(hashType, logsToCrack, dictFile) == True and
        areArgsValids(hashType, logsToCrack, dictFile) == True):
        startCracking(hashType, logsToCrack, dictFile)
        writeResultInFile()
    printBye()

def trueArg(hashType, logsToCrack, dictFile):
    if (hashType == None) or (logsToCrack == None) or (dictFile == None):
        return False
    return True

def parserCmd():
    parser = optparse.OptionParser(col.BOLD + '    Usage:'+ col.ENDC +  \
    ' hash_crack --hash <hash_type> ' + '-s <fileToCrack> ' + '-d <dict_file>')
    parser.add_option('--hash', dest='hashType', type='string', \
                      help='type of hash to crack')
    parser.add_option('-s', dest='logsToCrack', type='string',  \
                      help='file with login/pass to crack')
    parser.add_option('-d', dest='dictFile', type='string',     \
                      help='dicionnary password')
    (options, args) = parser.parse_args()
    hashType = options.hashType
    logsToCrack = options.logsToCrack
    dictFile = options.dictFile
    if(trueArg(hashType, logsToCrack, dictFile) == False):
        print (parser.usage)
        return None, None, None
    return hashType, logsToCrack, dictFile


def areArgsValids(hashType, logsToCrack, dictFile):
    if isNotValidFile(logsToCrack) or isNotValidFile(dictFile):
        return False
    if isNotValidHash(hashType):
        return errorInHash(hashType)
    return True

def isNotValidFile(filename):
    if not os.path.isfile(filename):
        return fileDoNotExist(filename)
    elif not os.access(filename, os.R_OK):
        return wrongPermOnFile(filename)
    return False

def isNotValidHash(hashType):
    validHash = ('all', 'unix_crypt', 'md5', 'sha256', 'sha512')
    return not (hashType.lower() in validHash)

def writeResultInFile():
    with open('crackingResult.passwd', 'a+') as res:
        for user in result:
            res.write(user + ':' + result[user])
    printWhereFindOutput()


###################################
#                                 #
#     Initialisation Cracking     #
#                                 #
###################################

def startCracking(hashType, logsToCrack, dictFile):
    logFile = open(logsToCrack)
    for line in logFile.readlines():
        passToCrack = line.split(':')[1].strip('\n')
        user        = line.split(':')[0]
        hashName    = setHashName(hashType)
        for hsh in hashName:
            printFront('+', col.YELLOW)
            print ('Start cracking with ' + hsh + ' hash')
            res = redirectHsh(hsh, dictFile, passToCrack)
            if (res != False):
                addSolution(user, res)
                printSuccess(user, passToCrack, res)
                break ;
            else:
                printFailure(user, passToCrack, hsh)


def setHashName(hashType):
    hashName = hashType.lower()
    if (hashName == 'all'):
        return ['unix_crypt', 'md5', 'sha256', 'sha512']
    return [hashName]


def redirectHsh(hsh, filename, passToCrack):
    if (hsh == 'unix_crypt'):
        return crackUnixCrypt(filename, passToCrack)
    elif (hsh == 'md5'):
        return crackMD5(filename, passToCrack)
    elif (hsh == 'sha256'):
        return crackSHA256(filename, passToCrack)
    elif (hsh == 'sha512'):
        return crackSHA512(filename, passToCrack)
    return False

def addSolution(user, res):
    result[user] = res

###################################
#                                 #
#   Hash Cracking                 #
#                                 #
###################################

## CRACKING UNIX ENCRYPTION

def crackUnixCrypt(filename, password):
    dictFile = open(filename)
    salt = password[:2]
    if invalidSalt(salt):
        return False
    for word in dictFile.readlines():
        if (cmpGeneratePassHash(salt, word, password)):
            return (word)
    return False

def invalidSalt(salt):
    if False in map(lambda x: x is ascii, salt):
        return False
    return True

def cmpGeneratePassHash(salt, word, password):
    if (crypt.crypt(word.replace('\n', ''), salt) == password):
        return True
    return False


## MD5 ENCRYPTION

def crackMD5(filename, password):
    dictFile = open(filename)
    for word in dictFile.readlines():
        cpy = word
        word = str.encode(word.strip('\n'))
        if (password == hashlib.md5(word).hexdigest()):
            return (cpy)
    return False

## SHA256 ENCRYPTION

def crackSHA256(filename, password):
    dictFile = open(filename)
    for word in dictFile.readlines():
        cpy = word
        word = str.encode(word.strip('\n'))
        if (password == hashlib.sha256(word).hexdigest()):
            return (cpy)
    return False

## SHA512 ENCRYPTION

def crackSHA512(filename, password):
    dictFile = open(filename)
    for word in dictFile.readlines():
        cpy = word
        word = str.encode(word.strip('\n'))
        if (password == hashlib.sha512(word).hexdigest()):
            return (cpy)
    return False


if __name__ in '__main__':
    main()
