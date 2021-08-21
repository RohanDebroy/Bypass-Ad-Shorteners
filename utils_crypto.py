from base64 import b64decode

def decrypt_rot_47(string: str) -> str:
    '''
    This function can be used to decrypt rot_47 encoded string
    '''
    decrypted_string = ""
    for char in string:
        char_code = ord(char)
        if 32 < char_code < 80:
            decrypted_string += chr(char_code + 47)
        if 79 < char_code < 127:
            decrypted_string += chr(char_code - 47)  
    return decrypted_string

def hextobin(string: str) -> str:
    '''
    This function can be used to convert hex string to ascii
    '''
    return bytearray.fromhex(string).decode("utf-8")

def fix_padding_base64(string: str) -> str:
    '''
    This function can be used to fixe the padding of our base64 encoded string
    '''
    while True:
        if(len(string) % 4 !=0):
            string+="="
        else:
            return string

def decode_base64(string: str) -> str:
    '''
        This function can be used to decode base64 string to utf-8
    '''
    return b64decode(str(string)).decode("utf-8")


def decode_string(string: str) -> str:
    '''
    This function applies the below mentioned functions on a string in an order of 
    hextobin -> fix_padding -> decode_base64 -> decrypt_rot_47

    :param string: Accepts hex encoded strings
    :type string: str.

    :return: : decoded string in utf-8 encoding

    Usage::
        >>>import utils_crypto
        >>>string = "4e574a684e444e664e6d466f5a325a6c4d6d4a6c4e32..."
        >>>utils_crypto.decode_string(string)
        d32cb0e29876a36f6559c986354c4f74ed6f88d85cc69666a62f0fb93...

    '''
    return decrypt_rot_47(decode_base64(fix_padding_base64(hextobin(string))))
