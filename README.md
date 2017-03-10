# HASH_CRACKER

Hash_cracker is a script for cracking password's hash from a dictionnary file.

Actually only those hash are support:
* unix encrypt
* md5
* sha256
* sha512

The final output will be write in a file named: crackingResult.passwd

### Prerequisites
You only need a version >= 3 for python.

If you still live in the past, you can delete all the output function to make it work

## Usage
```
python3 hash_cracker --hash <hash_type> -s <fileToCrack> -d <dict_file>
* hash_type  : all / UNIX_crypt / md5 / SHA256 / SHA512
* login_file : should only contain format: "user:password"
```
The exemple below is directly reproductible after a clone of the repo

```
python3 hash_cracker --hash all -s exemple_logsToCrack.txt -d dictPasswd.txt
```

### Dictionniary source
You can find on [cracking-station](https://crackstation.net/buy-crackstation-wordlist-password-cracking-dictionary.htm) one of the biggest password dictionnary.



```
To be a warrior is not a simple matter of wishing to be one. It is rather
an endless struggle that will go on to the very last moment of our lives.
Nobody is born a warrior, in exactly the same way that nobody is born
an average man. We make ourselves into one or the other
--Kokoro by Natsume So-sek, 1914, Japan.
```
