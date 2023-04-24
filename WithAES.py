import cv2
import sys
import numpy as np
from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# AES
# 选择加密模式（包括ECB和CBC）
mode = AES.MODE_CBC
# mode = AES.MODE_ECB
if mode != AES.MODE_CBC and mode != AES.MODE_ECB:
    print('Only CBC and ECB mode supported...')
    sys.exit()
# 设置密钥长度
keySize = 16
# ivSize = 16 初始向量长度不变
ivSize = AES.block_size if mode == AES.MODE_CBC else 0

cap = cv2.VideoCapture("./video.mp4")
# Create a new video writer with outputing *.mp4
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
bitrate = 20
out = cv2.VideoWriter('./encrypted_video.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS),
                      (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))), False)
out.set(cv2.CAP_PROP_FOURCC, fourcc)
out.set(cv2.CAP_PROP_BITRATE, bitrate)

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rowOrig, columnOrig, depthOrig = frame.shape
        cv2.imshow('gray', gray)
        _bytes = gray.tobytes()
        # print(len(_bytes))

        # 加密
        # 随机生成密钥key和初始向量IV
        key = get_random_bytes(keySize)
        iv = get_random_bytes(ivSize)

        # 初始化AES加密器
        cipher = AES.new(key, AES.MODE_CBC, iv) if mode == AES.MODE_CBC else AES.new(key, AES.MODE_ECB)
        # 将字节数据进行填充，得到填充后的数据
        # _bytespadded = pad(_bytes, AES.block_size)

        # 得到密文
        ciphertext = cipher.encrypt(_bytes)

        # 填充的位数, 输出128bits 输出128bits, 但需要考虑是否需要填充, 以及字节流大小与图像格式的匹配
        # paddedSize = len(_bytes) - len(_bytes)
        # print('paddedSize:' + str(paddedSize))

        # void = columnOrig * depthOrig - ivSize - paddedSize
        # ivCiphertextVoid = iv + ciphertext
        # + bytes(void)
        # print(len(iv))

        # frombuffer将data以流的形式读入转化成ndarray对象
        # 第一参数为stream,第二参数为返回值的数据类型，第三参数指定从stream的第几位开始读入
        imageEncrypted = np.frombuffer(ciphertext, dtype=frame.dtype).reshape(rowOrig, columnOrig)

        out.write(imageEncrypted)
        # 显示加密后的图像
        cv2.imshow("Encrypted image", imageEncrypted)

        # 保存加密后的图像
        # cv2.imwrite("topsecretEnc.bmp", imageEncrypted)
        # imageEncrypted = cv2.imread("topsecretEnc.bmp")
    else:
        break

    if cv2.waitKey(25) & 0xFF == 27:
        break
# cv2.imshow('frame', frame)

cap.release()
out.release()
cv2.destroyAllWindows()
