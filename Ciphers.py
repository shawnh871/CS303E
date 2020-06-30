# File: Ciphers.py
# Description: HW 12: This program encodes and decodes messages with a simple substitution cipher.
# Student's Name: Shao-Po Huang
# Student's UT EID: sh45848
# Course Name: CS 303E
# Unique Number: 50075
#
# Date Created: 11/07/19
# Date Last Modified: 11/08/19

# encryption function with parameters: plaintext and key
def encode(plaintext,key):

    # initialize encoded string variable
    encodedString = ""

    # convert characters in plaintext to ciphertext using key
    for ch in plaintext:
        # uppercase letters
        if (65 <= ord(ch) <= 90):
            encodedString += key[ord(ch)-65].upper()
        # lowercase letters
        elif (97 <= ord(ch) <= 122):
            encodedString += key[ord(ch)-97]
        # non-alphabetical characters
        else:
            encodedString += ch

    # return encoded string
    return encodedString

# decryption function with parameters: ciphertext and key
def decode(ciphertext,key):

    # initialize decoded string variable
    decodedString = ""

    # convert characters in ciphertext to plaintext using key
    for ch in ciphertext:
        # non-alphabetical characters
        if (not ch.isalpha()):
            decodedString += ch
        else:
            for k in range(len(key)):
                if (ch.lower() == key[k]):
                    # uppercase letters
                    if (65 <= ord(ch) <= 90):
                        decodedString += chr(k+65)
                    # lowercase letters
                    else:
                        decodedString += chr(k+97)

    # return decoded string
    return decodedString

def main():

    # list of plaintext messages and keys
    plaintextMessages = [
        ["This is the plaintext message.",
         "bcdefghijklmnopqrstuvwxyza"],
        ["Let the Wookiee win!",
         "epqomxuagrdwkhnftjizlcbvys"],
        ["Baseball is 90% mental. The other half is physical.\n\t\t- Yogi Berra",
         "hnftjizlcbvysepqomxuagrdwk"],
        ["I used to think I was indecisive, but now I'm not too sure.",
         "mqncdaigyhkxflujzervptobws"],
        ["Einstein's equation 'e = mc squared' shows that mass and\n\t\tenergy are interchangeable.",
         "bludcmhojaifxrkzenpsgqtywv"] ]

    # list of encrypted messages and keys
    codedMessages = [
        ["Uijt jt uif dpefe nfttbhf.",
         "bcdefghijklmnopqrstuvwxyza"],
        ["Qnhxgomhqm gi 10% bnjd eho 90% omwlignh. - Zghe Xmy",
         "epqomxuagrdwkhnftjizlcbvys"],
        ["Ulj njxu htgcfj C'gj jgjm mjfjcgjt cx, 'Ep pej jyxj veprx rlhu\n\t\t uljw'mj tpcez jculjm'. - Mcfvw Zjmghcx",
         "hnftjizlcbvysepqomxuagrdwk"],
        ["M 2-wdme uxc yr kylc ua xykd m qxdlcde, qpv wup cul'v gmtd mlw\n\t\t vuj aue yv. - Hdeew Rdyladxc",
         "mqncdaigyhkxflujzervptobws"] ]

    print()

    # display plaintext messages and their encrypted versions
    for i in range(len(plaintextMessages)):
        print("plaintext:  ",plaintextMessages[i][0])
        print("encoded:    ",encode(plaintextMessages[i][0],plaintextMessages[i][1]))
        print("re-decoded: ",decode(encode(plaintextMessages[i][0],plaintextMessages[i][1]),plaintextMessages[i][1]))
        print()

    # display encrypted messages and their plaintext versions
    for j in range(len(codedMessages)):
        print("encoded: ",codedMessages[j][0])
        print("decoded: ",decode(codedMessages[j][0],codedMessages[j][1]))
        print()

main()
    


