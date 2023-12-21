# The 256-bit hash function
from Crypto.Hash import SHA256
import hashlib

# The HMAC function
from Crypto.Hash import HMAC
from scipy.spatial.distance import hamming
import numpy as np
import argparse

import hmac


# The Advanced Encryption System  CBC Mode(Symmetric Encryption)
from Crypto.Cipher import AES
from Crypto import Random

# The random number generation
import os

# The public key encrypton (RSA)
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# The bilinear pairing 
from bplib import bp

# The elliptic curve
from fastecdsa.curve import P256
from fastecdsa.point import Point


# The XOR_Arbiter_PUF operation
from pypuf.simulation import XORArbiterPUF
from pypuf.io import random_inputs

# FuzzyExtractor
from fuzzy_extractor import FuzzyExtractor


import time

import json

from mod import Mod

from fuzzy_extractor import FuzzyExtractor

parser = argparse.ArgumentParser()
parser.add_argument("iterations", type=int, help="number of iterations to run")
data = []
args = parser.parse_args()
n_iterations = args.iterations


# ======================================= The Hash function (SHA256) ===========================================
# 初始化最大和最小计算时间
hashMaxExecutionTime = 0
hashMinExecutionTime = float('inf')  #表示无穷大
hashTotalExecutionTime = 0


h = hashlib.sha256()
h.update(
b'rfvsjbnbkf nikvfabnbrnkbnbknv NBRNTENBBFKEDANKENG KNKFDANKGRNKBGKNBFKTFNBFR  KFBDNKBNFRK BFD BLKBNRFNRF KFNBKEG DNBNRKORMVFS BKRNKRNGRNNB;KNBRNRF KBFRNRJFEM  KFRNBFNKNG NVFRL;SBFBJGERINHKTNBNBITNERKNAKNKVFNKNRAFNKNGRKF;FEKPKEGR  GRGKFM FV;LRMGR;MV,MV;LGRMLGRNV ,;FKDGRMV;MSK NGFAKBRKB FKVNBDKFGTNFVM CXFKNRKADN CNKGRNFD ,VCSNFRKK DDSKTENFKZVFDNVD.NGTLKNMGFD  VFGRAMDCMRJNDNMVSC  MDCSJNF DCDCNSL.N.M NDDDDDDDNCDCJMD,C  ,M ,M ,M ,M ,M ,M ,M ,M ,MDSCJN MDSV CM J DCCMDANFKJN VDNDCKLNVDS DV SJCBJBDSJCBBDJJGRBJBGRJKBKJBGERWBJKJVDBRJVFBLCBVECBFRWVC U V  DCBSKDJEWNFRWBJFRBVFDFENCXBKSANDMXNLKJNEDSAFHFUEDWHGUGFBVBVBVBVBVBVLKENFDLKLKLKLK.NDSA MNSLKLKLKLKLKLKLKLKLKLKLKLKLKLKLKLKLKLKLKLKLKDC S,M,M,M,M,M,M,MJEWEWEWEWEWEWEWEWEWEWEW,Msaddddrehjjhq.JE.JE.JE.JE.JE.JE.JE.JE.JE.JEaf,nnnnnnn cxzzzzzzbewjkewrioooipoiiiiiiiiipcdklbdjcbsnccds<M,sDCAnDCSnmdb.vdjj dcms.fedn dcnjdcskbjkfbedjbfrjbdjvfbjdcbcbdckjbkjdcbjdcdcjdkjcbjdcbbcdckjbjbdjjbdcjkdsx m mxX<Mmnc.,mcdcmnmdcm,m<MNCXnC<,mnNN<,m<MNXZnxnNnmXnNXnnnxnxnnxmnnxxnbnXNBnxXkjdsbjkeds <MZ')

# loop #some computations
for i in range(n_iterations):
    # Getting the  hash start time
    hashStartTime = time.time()
    digest = h.hexdigest()
    hashEndTime = time.time()

    # 计算运行时间并更新最大和最小计算时间
    hashExecutionTime = (hashEndTime - hashStartTime)
    hashTotalExecutionTime += hashExecutionTime
    hashMaxExecutionTime = max(hashMaxExecutionTime, hashExecutionTime)
    if hashExecutionTime > 0:
        hashMinExecutionTime = min(hashMinExecutionTime, hashExecutionTime)

#计算平均时间
averageHashExecutionTime = hashTotalExecutionTime / n_iterations

dataSize = 1024

computation = {"computation": "SHA-256",
               "iterations": n_iterations,
               "Data size in bytes": dataSize,
               "Total Execution time": hashTotalExecutionTime* 1000,
               "Max Execution time": hashMaxExecutionTime* 1000,
               "Min Execution time": hashMinExecutionTime* 1000,
               "Average Execution time": averageHashExecutionTime * 1000}
# 写入数据
data.append(computation)
# === End ==================================================================================================


# ======================================= The AES encryption procedures ===========================================
# 初始化最大和最小计算时间
aesEncryptMaxExecutionTime = 0
aesEncryptMinExecutionTime = float('inf')  #表示无穷大
aesEncryptTotalExecutionTime = 0

aesDecryptMaxExecutionTime = 0
aesDecryptMinExecutionTime = float('inf')  #表示无穷大
aesDecryptTotalExecutionTime = 0

# The AES encryption procedures
key = b'Sixteen byte key'
# print (key)
iv = Random.new().read(AES.block_size)
# print (iv)

aes = AES.new(key, AES.MODE_CBC, iv)
message = b'rfvsjbnbkf nikvfabnbrnkbnbknv NBRNTENBBFKEDANKENG KNKFDANKGRNKBGKNBFKTFNBFR  KFBDNKBNFRK BFD BLKBNRFNRF KFNBKEG DNBNRKORMVFS BKRNKRNGRNNB;KNBRNRF KBFRNRJFEM  KFRNBFNKNG NVFRL;SBFBJGERINHKTNBNBITNERKNAKNKVFNKNRAFNKNGRKF;FEKPKEGR  GRGKFM FV;LRMGR;MV,MV;LGRMLGRNV ,;FKDGRMV;MSK NGFAKBRKB FKVNBDKFGTNFVM CXFKNRKADN CNKGRNFD ,VCSNFRKK DDSKTENFKZVFDNVD.NGTLKNMGFD  VFGRAMDCMRJNDNMVSC  MDCSJNF DCDCNSL.N.M NDDDDDDDNCDCJMD,C  ,M ,M ,M ,M ,M ,M ,M ,M ,MDSCJN MDSV CM J DCCMDANFKJN VDNDCKLNVDS DV SJCBJBDSJCBBDJJGRBJBGRJKBKJBGERWBJKJVDBRJVFBLCBVECBFRWVC U V  DCBSKDJEWNFRWBJFRBVFDFENCXBKSANDMXNLKJNEDSAFHFUEDWHGUGFBVBVBVBVBVBVLKENFDLKLKLKLK.NDSA MNSLKLKLKLKLKLKLKLKLKLKLKLKLKLKLKLKLKLKLKLKLKDC S,M,M,M,M,M,M,MJEWEWEWEWEWEWEWEWEWEWEW,Msaddddrehjjhq.JE.JE.JE.JE.JE.JE.JE.JE.JE.JEaf,nnnnnnn cxzzzzzzbewjkewrioooipoiiiiiiiiipcdklbdjcbsnccds<M,sDCAnDCSnmdb.vdjj dcms.fedn dcnjdcskbjkfbedjbfrjbdjvfbjdcbcbdckjbkjdcbjdcdcjdkjcbjdcbbcdckjbjbdjjbdcjkdsx m mxX<Mmnc.,mcdcmnmdcm,m<MNCXnC<,mnNN<,m<MNXZnxnNnmXnNXnnnxnxnnxmnnxxnbnXNBnxXkjdsbjkeds '  # <- 16 bytes
for i in range(n_iterations):
    #加密操作开始时间
    aesEncryptStartTime = time.time()
    encd = aes.encrypt(message)
    # print(encd)
    # #加密操作结束时间
    aesEncryptEndTime = time.time()

    # 计算运行时间并更新最大和最小计算时间
    aesEncryptExecutionTime = (aesEncryptEndTime - aesEncryptStartTime)
    aesEncryptTotalExecutionTime += aesEncryptExecutionTime
    aesEncryptMaxExecutionTime = max(aesEncryptMaxExecutionTime, aesEncryptExecutionTime)
    aesEncryptMinExecutionTime = min(aesEncryptMinExecutionTime, aesEncryptExecutionTime)

#计算平均时间
aesAverageEncryptionTime = aesEncryptTotalExecutionTime / n_iterations

computation = {"AES Encrypt computation": "AES-128-CBC",
               "Data size in bytes": dataSize,
               "Total Execution time": aesEncryptTotalExecutionTime * 1000,
               "Max Execution time": aesEncryptMaxExecutionTime * 1000,
               "Min Execution time": aesEncryptMinExecutionTime * 1000,
               "Average Execution time":aesAverageEncryptionTime * 1000}
# 写入数据
data.append(computation)


aes = AES.new(key, AES.MODE_CBC, iv)
for i in range(n_iterations):
    #加密操作开始时间
    aesDecryptStartTime = time.time()
    decrypted_data = aes.decrypt(encd)
    # print(decrypted_data) # 可正常解密
    # #加密操作结束时间
    aesDecryptEndTime = time.time()

    # 计算运行时间并更新最大和最小计算时间
    aesDecryptExecutionTime = (aesDecryptEndTime - aesDecryptStartTime)
    aesDecryptTotalExecutionTime += aesDecryptExecutionTime
    aesDecryptMaxExecutionTime = max(aesDecryptMaxExecutionTime, aesDecryptExecutionTime)
    aesDecryptMinExecutionTime = min(aesDecryptMinExecutionTime, aesDecryptExecutionTime)

#计算平均时间
aesAverageDecryptionTime = aesDecryptTotalExecutionTime / n_iterations

computation = {"AES Decrypt computation": "AES-128-CBC",
               "Data size in bytes": dataSize,
               "Total Execution time": aesDecryptTotalExecutionTime *1000,
               "Max Execution time": aesDecryptMaxExecutionTime *1000,
               "Min Execution time": aesDecryptMinExecutionTime *1000,
               "Average Execution time": aesAverageDecryptionTime *1000}
# 写入数据
data.append(computation)


# === End ==================================================================================================


# ======================================= # The elliptic curve operations  ===========================================
# The elliptic curve operations
xs = 0xde2444bebc8d36e682edd27e0f271508617519b3221a8fa0b77cab3989da97c9
ys = 0xc093ae7ff36e5380fc01a5aad1e66659702de80f53cec576b6350b243042a256
S = Point(xs, ys, curve=P256)

xt = 0x55a8b00f8da1d44e62f6b3b25316212e39540dc861c89575bb8cf92e35e0986b
yt = 0x5421c3209c2d6c704835d82ac4c3dd90f61a8a52598b9e7ab656e9d8c8b24316
T = Point(xt, yt, curve=P256)


# 初始化最大和最小计算时间
eccAdditionMaxExecutionTime = 0
eccAdditionMinExecutionTime = float('inf')  #表示无穷大
eccAdditionTotalExecutionTime = 0

# 初始化最大和最小计算时间
eccScalarMultiplicationMaxExecutionTime = 0
eccScalarMultiplicationMinExecutionTime = float('inf')  #表示无穷大
eccScalarMultiplicationTotalExecutionTime = 0


for i in range(n_iterations):
    # ECC 点加运算开始时间
    eccAdditionStartTime = time.time()
    S + T
    # ECC 点加运算技术时间时间
    eccAdditionEndTime = time.time()

    # 计算运行时间并更新最大和最小计算时间
    eccAdditionExecutionTime = (eccAdditionEndTime - eccAdditionStartTime)
    eccAdditionTotalExecutionTime += eccAdditionExecutionTime
    eccAdditionMaxExecutionTime = max(eccAdditionMaxExecutionTime, eccAdditionExecutionTime)
    eccAdditionMinExecutionTime = min(eccAdditionMinExecutionTime, eccAdditionExecutionTime)

#计算平均时间
eccAverageAdditionTime = eccAdditionTotalExecutionTime / n_iterations

computation = {"computation": "ECC Addition",
               "Data size in bytes": dataSize,
               "Total Execution time": eccAdditionTotalExecutionTime  *1000,
               "Max Execution time": eccAdditionMaxExecutionTime  *1000,
               "Min Execution time": eccAdditionMinExecutionTime  *1000,
               "Average Execution time": eccAverageAdditionTime  *1000}
# 写入数据
data.append(computation)


d = 0xc51f
for i in range(n_iterations):
    # ECC 点倍乘算开始时间
    eccScalarMultiplicationStartTime = time.time()
    R = d * S
    # ECC 点倍乘算结束时间
    ECCscalarMultiplicationEndTime = time.time()

    # 计算运行时间并更新最大和最小计算时间
    eccScalarMultiplicationExecutionTime = (ECCscalarMultiplicationEndTime - eccScalarMultiplicationStartTime)
    eccScalarMultiplicationTotalExecutionTime += eccScalarMultiplicationExecutionTime
    eccScalarMultiplicationMaxExecutionTime = max(eccScalarMultiplicationMaxExecutionTime, eccScalarMultiplicationExecutionTime)
    eccScalarMultiplicationMinExecutionTime = min(eccScalarMultiplicationMinExecutionTime, eccScalarMultiplicationExecutionTime)

#计算平均时间
eccScalarMultiplicationAverageTime = eccScalarMultiplicationTotalExecutionTime / n_iterations

computation = {"computation": "ECC Scalar Multiplication",
               "Data size in bytes": dataSize,
               "Total Execution time": eccScalarMultiplicationTotalExecutionTime *1000,
               "Max Execution time": eccScalarMultiplicationMaxExecutionTime *1000,
               "Min Execution time": eccScalarMultiplicationMinExecutionTime *1000,
               "Average Execution time": eccScalarMultiplicationAverageTime *1000}
# 写入数据
data.append(computation)

# === End ==================================================================================================




# ======================================= The bilinear pairing ===========================================
# 初始化最大和最小计算时间
bpMaxExecutionTime = 0
bpMinExecutionTime = float('inf')  #表示无穷大
bpTotalExecutionTime = 0


for i in range(n_iterations):
    # BP 运算开始时间
    bpTimeStartTime = time.time()
    G = bp.BpGroup()
    g1, g2 = G.gen1(), G.gen2()
    gt = G.pair(g1, g2)
    # BP 运算结束时间
    bpTimeEndTime = time.time()

    # 计算运行时间并更新最大和最小计算时间
    bpExecutionTime = (bpTimeEndTime - bpTimeStartTime)
    bpTotalExecutionTime += bpExecutionTime
    bpMaxExecutionTime = max(bpMaxExecutionTime, bpExecutionTime)
    bpMinExecutionTime = min(bpMinExecutionTime, bpExecutionTime)

#计算平均时间
bpAverageTime = bpTotalExecutionTime / n_iterations


computation = {"computation": "Bilinear Pairing",
               "iterations": n_iterations,
               "Total Execution time": bpTotalExecutionTime * 1000,
               "Max Execution time": bpMaxExecutionTime*1000,
               "Min Execution time": bpMinExecutionTime*1000,
               "Average Bilinear pairing time": bpAverageTime*1000}
data.append(computation)
# === End ==================================================================================================



# ======================================= The XOR_Arbiter_PUF operation ====================================

# 初始化最大和最小计算时间
xorpufMaxExecutionTime = 0
xorpufMinExecutionTime = float('inf')  #表示无穷大
xorpufTotalExecutionTime = 0

for i in range(n_iterations):
    puf = XORArbiterPUF(n=64, k=2, seed=1, noisiness=0.05)
    # XORArbiterPUF 运算开始时间     
    xorpufTimeStartTime = time.time()
    puf.eval(random_inputs(n=64, N=3, seed=2))
    # XORArbiterPUF 运算结束时间
    xorpufTimeEndTime = time.time()

    # 计算运行时间并更新最大和最小计算时间
    xorpufExecutionTime = (xorpufTimeEndTime - xorpufTimeStartTime)
    xorpufTotalExecutionTime += xorpufExecutionTime
    xorpufMaxExecutionTime = max(xorpufMaxExecutionTime, xorpufExecutionTime)
    xorpufMinExecutionTime = min(xorpufMinExecutionTime, xorpufExecutionTime)

#计算平均时间
xorpufAverageTime = xorpufTotalExecutionTime / n_iterations

computation = {"computation": "XOR_Arbiter_PUF",
               "iterations": n_iterations,
               "Total Execution time": xorpufTotalExecutionTime * 1000,
               "Max Execution time": xorpufMaxExecutionTime*1000,
               "Min Execution time": xorpufMinExecutionTime*1000,
               "Average XOR_Arbiter_PUF time": xorpufAverageTime*1000}
data.append(computation)

# === End ==================================================================================================


# ======================================= The FuzzyExtractor Generation operation ====================================
# 初始化最大和最小计算时间
feGenMaxExecutionTime = 0
feGenMinExecutionTime = float('inf')  #表示无穷大
feGenTotalExecutionTime = 0

# 创建的提取器接受 16 字节（128 位）输入值，保证相距 8 位以内的输入将产生相同密钥的概率超过 0.9999
extractor = FuzzyExtractor(16, 8)

for i in range(n_iterations):
    # FuzzyExtractor Gen 运算开始时间     
    feGenTimeStartTime = time.time()
    key, helper = extractor.generate('ABCDEFGHIJKLMNOP') # 生成 key 和 helper
    # FuzzyExtractor Gen 运算结束时间
    feGenTimeEndTime = time.time()

    # 计算运行时间并更新最大和最小计算时间
    feGenExecutionTime = (feGenTimeEndTime - feGenTimeStartTime)
    feGenTotalExecutionTime += feGenExecutionTime
    feGenMaxExecutionTime = max(feGenMaxExecutionTime, feGenExecutionTime)
    feGenMinExecutionTime = min(feGenMinExecutionTime, feGenExecutionTime)

#计算平均时间
feGenAverageTime = feGenTotalExecutionTime / n_iterations

computation = {"computation": "Fuzzy Extractor Generation",
               "iterations": n_iterations,
               "Total Execution time": feGenTotalExecutionTime * 1000,
               "Max Execution time": feGenMaxExecutionTime*1000,
               "Min Execution time": feGenMinExecutionTime*1000,
               "Average Fuzzy Extractor Generation time": feGenAverageTime*1000}
data.append(computation)
# === End ==================================================================================================


# ======================================= The FuzzyExtractor Reproduction operation ====================================
# 初始化最大和最小计算时间
feRepMaxExecutionTime = 0
feRepMinExecutionTime = float('inf')  #表示无穷大
feRepTotalExecutionTime = 0

extractor = FuzzyExtractor(16, 8)
key, helper = extractor.generate('ABCDEFGHIJKLMNOP')

for i in range(n_iterations):
    # FuzzyExtractor Gen 运算开始时间     
    feRepTimeStartTime = time.time()
    r_key = extractor.reproduce('ABCDEFGHIJKLMNOP', helper)  # r_key should equal key
    # FuzzyExtractor Gen 运算结束时间
    feRepTimeEndTime = time.time()

    # 计算运行时间并更新最大和最小计算时间
    feRepExecutionTime = (feRepTimeEndTime - feRepTimeStartTime)
    feRepTotalExecutionTime += feRepExecutionTime
    feRepMaxExecutionTime = max(feRepMaxExecutionTime, feRepExecutionTime)
    feRepMinExecutionTime = min(feRepMinExecutionTime, feRepExecutionTime)

#计算平均时间
feRepAverageTime = feRepTotalExecutionTime / n_iterations

computation = {"computation": "Fuzzy Extractor Reproduction",
               "iterations": n_iterations,
               "Total Execution time": feRepTotalExecutionTime * 1000,
               "Max Execution time": feRepMaxExecutionTime*1000,
               "Min Execution time": feRepMinExecutionTime*1000,
               "Average Fuzzy Extractor Reproduction time": feRepAverageTime*1000}
data.append(computation)
# === End ==================================================================================================




# Writing to JSON file
with open(f'PrimitiveComputationTime {n_iterations}.txt', 'w') as json_file:
    json.dump(data, json_file, indent=4)

