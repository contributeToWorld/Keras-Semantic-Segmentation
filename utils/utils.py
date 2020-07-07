import os
import cv2
from keras.callbacks import (CSVLogger, EarlyStopping, ModelCheckpoint,
                             ReduceLROnPlateau)

def mk_if_not_exits(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def cv2_letterbox_image(image, dst_size):
    ih, iw = image.shape[0:2]
    ew, eh = dst_size
    scale = min(eh / ih, ew / iw)
    nh = int(ih * scale)
    nw = int(iw * scale)
    image = cv2.resize(image, (nw, nh), interpolation=cv2.INTER_CUBIC)
    top = (eh - nh) // 2
    bottom = eh - nh - top
    left = (ew - nw) // 2
    right = ew - nw - left
    new_img = cv2.copyMakeBorder(image, top, bottom, left, right,
                                 cv2.BORDER_CONSTANT)
    return new_img

# class ParallelModelCheckpoint(ModelCheckpoint):
#     def __init__(self,model,filepath, monitor='loss', verbose=0,
#                  save_best_only=False, save_weights_only=False,
#                  mode='auto', period=1):
#         self.single_model = model
#         super(ParallelModelCheckpoint,self).__init__(filepath, monitor, verbose,save_best_only, save_weights_only,mode, period)

#     def set_model(self, model):
#         super(ParallelModelCheckpoint,self).set_model(self.single_model)