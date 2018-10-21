import numpy as np 
import cv2
from natsort import natsorted
from collections import defaultdict
from scipy.ndimage import rotate
from typing import List


def clean_slice(img, erode_iter = 3, dilate_iter = 1):
    """
    too much noise remains -> increase erode_iter
    too little brain left -> increase dilate_iter
    returns 2D array
    
    """
    img = img.copy()
    kernel = np.ones((5,5),np.uint8)
    if len(img.shape)==3:
        img = img[:,:,0]
    img_morph = cv2.erode(img, kernel, iterations = erode_iter)
    thres = img_morph>0
    thres = np.array(thres, dtype=np.uint8)
    
    mask = np.zeros(thres.shape, np.uint8)
    imgg, contours, hier = cv2.findContours(thres,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    areas = []
    for cnt in contours:
        areas.append(cv2.contourArea(cnt))
        
    index = areas.index(max(areas))
    cnt = contours[index]
    mask = cv2.drawContours(mask,[cnt],0,255,-1)
    mask = cv2.dilate(mask, kernel,iterations = dilate_iter)
    mask = mask>1
    img[~mask] = 0
    
    return img


def sort_paths(paths: List[str]) -> List[str]:  
    """Augmented natural sorting to group together brain slices"""
    ct_paths_sorted = natsorted(paths)
    curr_patient_id = ct_paths_sorted[0].split('/')[-2]
    fst = []
    snd = defaultdict(list)
    ct_sorted = []
    for i in range(len(ct_paths_sorted)-1):
        patient_id = ct_paths_sorted[i].split('/')[-2]
        if patient_id!=curr_patient_id:
            ct_sorted += fst 
            for scan_id in sorted(snd.keys()):
                ct_sorted += snd[scan_id]
            fst = []
            snd = defaultdict(list)
            curr_patient_id = patient_id
            
        if '_' in ct_paths_sorted[i].split('/')[-1]:
            scan_id = ct_paths_sorted[i].split('/')[-1].split('_')[-1]
            snd[scan_id].append(ct_paths_sorted[i])
        else:
            fst.append(ct_paths_sorted[i])

    ct_sorted += fst
    for scan_id in sorted(snd.keys()):
        ct_sorted += snd[scan_id]

    return ct_sorted


def rotate_scan(scan, angle, axes, keep_dim=True):
    s_rot = rotate(scan, angle, axes=axes)
    if keep_dim:
        shape = np.array(scan.shape)
        diff = np.array(s_rot.shape)-shape
        diff = diff//2
        end = shape+diff
        s_rot = s_rot[diff[0]:end[0], diff[1]:end[1], diff[2]:end[2]]
    return s_rot


def rotate_side_lr(scan, angle, keep_dim=True):
    return rotate_scan(scan, angle, (1,2))

    
def rotate_horisontally(scan, angle, keep_dim=True):
    return rotate_scan(scan, angle, (0,1))
