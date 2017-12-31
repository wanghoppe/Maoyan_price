import os
import json
import subprocess
import scipy
import base64
import numpy as np
from scipy import ndimage
from scipy import io
from dnn_app_utils_v2 import *

def load_para():
    with open("trainning/numRegPara2.json") as f:
        para_lst = json.load(f)

    para = dict()
    for key, val in para_lst.items():
        para[key] = np.array(val)
    #     print(len(np.array(val)))
    return para

def make_woff(woff_source):
    work_dir = "mapping_num"
    if os.path.exists(work_dir):
        pass
    else:
        os.makedirs(work_dir)

    font = work_dir + os.path.sep + "mapping.woff"
    with open(font, "wb") as f:
        f.write(base64.b64decode(woff_source))

    return font

def mapping_num(text, para ,woff_file):
    work_dir = "mapping_num"
    if os.path.exists(work_dir):
        pass
    else:
        os.makedirs(work_dir)

    outdir = work_dir + os.path.sep + 'cache' + os.path.sep

    if os.path.exists(outdir):
        pass
    else:
        os.makedirs(outdir)

    outfile = outdir + os.path.sep + text + '.jpg'
    subprocess.call(["convert", "-background", "black", "-fill", "white",
                             "-font", woff_file, "-pointsize", "30",
                             "label:"+text, outfile])

    t1 = ndimage.imread(outfile)
    t2 = scipy.misc.imresize(t1, (30,20))/255

    predic = L_model_forward(t2.reshape((600,1)), para)[0]
    return predic.argmax()
