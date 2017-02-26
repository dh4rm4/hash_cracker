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
python3 hash_cracker <hash_type> <login_file> <dictionnary file>
* hash_type  : all / UNIX_crypt / md5 / SHA256 / SHA512
* login_file : should only contain format: "user:password"
```
The exemple below is directly reproductible after a clone of the repo

```
python3 hash_cracker all exeple_logsToCrack.txt dictPasswd.txt
```