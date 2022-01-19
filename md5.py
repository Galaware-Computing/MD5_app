#python md5
import math
import logging as lg
import os

class MD5:
    # Rotations constants
    rotate_left= [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
                    5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
                    4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
                    6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]
    
    # Define the 64 constant values of word 32bits
    k_constants = [int(abs(math.sin(i+1)) * 2**32) & 0xFFFFFFFF for i in range(64)]
    # Define the five MD buffers
    md5Buffers = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]
    # Define the four auxiliary functions that produce one 32-bit word.
    functions = 16*[lambda b, c, d: (b & c) | (~b & d)] + \
                16*[lambda b, c, d: (d & b) | (~d & c)] + \
                16*[lambda b, c, d: b ^ c ^ d] + \
                16*[lambda b, c, d: c ^ (b | ~d)]
    # Define the index to MD5 hash
    index_functions = 16*[lambda i: i] + \
                    16*[lambda i: (5*i + 1)%16] + \
                    16*[lambda i: (3*i + 5)%16] + \
                    16*[lambda i: (7*i)%16]
    # Output the hash value
    @classmethod               
    def output(self, message):
       self.msg = message
       Hash = self.md5_to_hex(self.hash_md5(self.msg))
       self.write_file(self.msg,Hash)
       return Hash
   
    #this function write data to file
    @classmethod    
    def write_file(self, mes, hash):
        with open(".\hash_log.txt", 'a') as x_file:
            x_file.write('{} => {} \n'.format(mes, hash))
            x_file.close()
                    
    # Define the rotations operations
    @classmethod
    def left_rotate(self, x, amount):
        lg.info("We are in the rotation method")
        x &= 0xFFFFFFFF
        return ((x<<amount) | (x>>(32-amount))) & 0xFFFFFFFF
    # Iterative operations
    @classmethod
    def hash_md5(self, message):
        lg.info("We are in the hash function method")
        message = bytearray(message,'utf-8') #copy our input into a mutable buffer
        orig_len_in_bits = (8 * len(message)) & 0xffffffffffffffff
        message.append(0x80)
        while len(message)%64 != 56:
            message.append(0)
        message += orig_len_in_bits.to_bytes(8, byteorder='little')
    
        hash_pieces = MD5.md5Buffers[:]
    
        for buf in range(0, len(message), 64):
            a, b, c, d = hash_pieces
            chunk = message[buf:buf+64]
            for i in range(64):
                f = MD5.functions[i](b, c, d)
                g = MD5.index_functions[i](i)
                to_rotate = a + f + MD5.k_constants[i] + int.from_bytes(chunk[4*g:4*g+4], byteorder='little')
                new_b = (b + self.left_rotate(to_rotate, MD5.rotate_left[i])) & 0xFFFFFFFF
                a, b, c, d = d, new_b, b, c
            for i, val in enumerate([a, b, c, d]):
                hash_pieces[i] += val
                hash_pieces[i] &= 0xFFFFFFFF
    
        return sum(x<<(32*i) for i, x in enumerate(hash_pieces))
    
    @classmethod
    def md5_to_hex(self, digest):
        lg.info("We are in the hash to hexadeximal method")
        raw = digest.to_bytes(16, byteorder='little')
        return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))
    
    
# il reste encore à modifier le chemin du dossier hash_log pour que celui-ci soit depuis le fichier ou il a été installé
print(os.getcwd())