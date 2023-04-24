import cv2
import sys
import numpy as np
import EncryptLogic
from Crypto.Util.Padding import pad, unpad

def start(cap, out):



    while (cap.isOpened()):
        ret, frame = cap.read()

        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('gray', gray)
            _bytes = gray.tobytes()
            _bytespad = pad(_bytes, AES.block_size)

            sm4.ecrypt_ecb(_bytes)
        out.write
    return


if __name__ == '__main__':
    path = input()
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    cap = cv2.VideoCapture(path)
    out = cv2.VideoWriter('./encrypted_video.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS),
                          (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))), False)

    bitrate = 20
    key = b'3l5butlj26hvv313'
    iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    sm4 = EncryptLogic.enc(key)

    out.set(cv2.CAP_PROP_FOURCC, fourcc)
    out.set(cv2.CAP_PROP_BITRATE, bitrate)
    start(cap, out)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
