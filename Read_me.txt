#############################################
#                 MD5 Hash _ read me        #
#############################################

A modifier

Informations
This code realized by the students :
    -NGAH ESSENGUE BRICE MICHEL
    -BENAM NOE YVAN
in the frame of advance cryptography work at academic year 2021/2022.
This work implements the md5 algorithm in the program that hashes the message value
and/or the file to determined the digest of them.
It is a personal choice of realize this program in english.
This program based on two script both realized in python because it is the langage
that we know best.
The first script named "md5.py" is the md5 algorithm based from the RFC 1321 (MD5 
Message-Digest Algorithm) avialable on that link : https://www.ietf.org/rfc/rfc1321.txt
The second script named "gui.py" content the interface and all the configurations
and operations who permit to use the first script in order to product the the hash.
The third script is "test.py" this scripthave been used to perform the test of first
script "md5.py".

Script brief content :
The script "md5.py" divided in two class : MD5Buffer and MD5.
MD5Buffer() is class in which created a four-word buffer (A,B,C,D). This buffer is used 
to compute the message digest. Here each of A, B, C, D is a 32-bit register.
MD5() is the second class in which we have created the five who represent the five 
steps are performed to compute the message digest of the message. It is :
    -Completion()
    -length()
    -initialisation()
    -mainOperation()
    -outPut()

The second script "gui.py" have one class : Application()
this class has fifteen functions of which eight use the python tkinter module to create 
the interface and seven others that link the widgets to the operations who performed by
the interactions between the user and the interface.

##### MD5
The MD5 message-digest algorithm is a cryptographically broken but still widely used hash function 
producing a 128-bit hash value. Although MD5 was initially designed to be used as a cryptographic 
hash function, it has been found to suffer from extensive vulnerabilities. It can still be used as 
a checksum to verify data integrity, but only against unintentional corruption. It remains suitable 
for other non-cryptographic purposes, for example for determining the partition for a particular key 
in a partitioned database, and may be preferred due to lower computational requirements than more 
recent Secure Hash Algorithms algorithms.

MD5 was designed by Ronald Rivest in 1991 to replace an earlier hash function MD4, and was specified in 1992 as RFC 1321.
One basic requirement of any cryptographic hash function is that it should be computationally infeasible
to find two distinct messages that hash to the same value. MD5 fails this requirement catastrophically; 
such collisions can be found in seconds on an ordinary home computer.