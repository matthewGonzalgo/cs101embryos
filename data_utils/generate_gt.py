import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
from multiprocessing import Pool
from tqdm import tqdm

def generate_single(fluo_path):
    fluo = cv2.imread(fluo_path, cv2.IMREAD_GRAYSCALE)
    fluo_blur = cv2.GaussianBlur(fluo, (5,5), sigmaX=1, sigmaY=1)
    _, fluo_blur = cv2.threshold(fluo_blur, 5, 255, 0)
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(fluo_blur, connectivity=8)
    for j in range(1, num_labels):
        mask = labels == j
        if stats[j, -1] < 1000:
            fluo_blur[mask] = 0
    kernel = np.ones((5, 5), np.int8)
    fluo_blur = cv2.dilate(fluo_blur, kernel, 1000000)
    contours, hierarchy = cv2.findContours(fluo_blur, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    edge = np.zeros_like(fluo)
    cv2.drawContours(edge, contours, 0, 255, 3)
    img = Image.fromarray(edge)
    output_path = os.path.join('/'.join(fluo_path.split('/')[:7]), 'gt', '/'.join(fluo_path.split('/')[8:]))
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)

def generate(fluo_list):
    with open(fluo_list, 'r') as f:
        fluos = f.read().splitlines()
    p = Pool(10)
    for a in tqdm(p.imap(generate_single, fluos), total=len(fluos)):
        continue
    p.close()
    p.join()

if __name__ == '__main__':
    fluo_list = './clean.list'
    generate(fluo_list)
