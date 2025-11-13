#!/usr/bin/env python
import os
import random
import time
import sys

VERTICAL_MONITORS = ('DP-2',)

# Configurazione dei parametri

os.environ.setdefault('SWWW_WAIT_TIME', '150')
FPS = 75  # FPS della transizione
STEP = 45  # Step della transizione
PATH_TO_FOLDER = os.path.join(os.environ['HOME'], "Pictures/vapor")
TRANS_TIME = 3  # Durata transizione
TYPE = "random"  # Tipo di effetto

try:
    outputs = sys.argv[1:]
except IndexError:
    outputs = ''
swww = "swww img {} --transition-fps {} \
                    --transition-duration {} \
                    --transition-step {} \
                    --transition-type {} \
                    {}"
image_files = os.listdir(PATH_TO_FOLDER)
while True:
    if not outputs:
        # Seleziona una immagine casuale dalla cartella
        while True:
            random_image = os.path.join(PATH_TO_FOLDER, random.choice(image_files))
            if random_image.endswith('.png') or random_image.endswith('.jpg'):
                break
        os.system(swww.format('',FPS,TRANS_TIME, \
                              STEP, TYPE, random_image))
    else:
        for monitor in outputs:
            if monitor in VERTICAL_MONITORS:
                image_path = os.path.join(PATH_TO_FOLDER, 'vert')
                image_files = os.listdir(image_path)
            else:
                image_path = PATH_TO_FOLDER
                image_files = os.listdir(image_path)
            while True:
                random_image = os.path.join(image_path, random.choice(image_files))
                if random_image.endswith('.png') or random_image.endswith('.jpg'):
                    break
            output_flag = f'-o {monitor}'
            os.system(swww.format(output_flag, FPS, TRANS_TIME, \
                                  STEP, TYPE, random_image))

    time.sleep(int(os.environ['SWWW_WAIT_TIME']))
