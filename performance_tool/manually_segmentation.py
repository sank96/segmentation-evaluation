#!/usr/bin/env python3
import json
import cv2
import numpy as np
import os
import sys
import tkinter as tk
from tkinter import messagebox

sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../..'))

shape = []
window_name = "Select the objects"
original_image = None
polygons = []
root = tk.Tk()
root.withdraw()


def plot_shape(saving=False):
    global shape, window_name

    image = get_image()

    if saving:
        color = (0, 0, 255)
    else:
        color = (0, 255, 0)

    if len(shape) == 1:
        point = shape[0]
        cv2.circle(image, point, 3, color, -1)
    elif len(shape) == 2:
        cv2.line(image, shape[0], shape[1], color, 2)
    elif len(shape) > 2:
        alpha = 0.3

        im2 = image.copy()

        pts = np.asarray(shape)
        pts = pts.reshape((-1, 1, 2))
        cv2.fillPoly(image, [pts], color)
        # apply the overlay
        cv2.addWeighted(image, alpha, im2, 1 - alpha, 0, image)
        cv2.polylines(image, [pts], True, color, 2)

    cv2.imshow(window_name, image)


def plot_all_polygons(pols: [dict], final=False):
    global window_name

    image = get_image(original=True)
    alpha = 0.5

    for i, pol in enumerate(pols):
        points = pol['points']

        x = [p[0] for p in points]
        y = [p[1] for p in points]
        cx, cy = (round(sum(x) / len(points)), round(sum(y) / len(points)))

        pts = np.asarray(points)
        pts = pts.reshape((-1, 1, 2))
        cv2.fillPoly(image, [pts], (1, 1, 1))
        len_label = len(pol['label'])
        offset = 5
        cx -= round(len_label * offset)
        if final:
            n = "{} - {}".format(i, pol['label'])
            cv2.putText(image, n, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 3)
        else:
            cv2.putText(image, pol['label'], (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 3)

    cv2.addWeighted(image, alpha, original_image.copy(), 1 - alpha, 0, image)
    if not final:
        cv2.imshow(window_name, image)

    return image


# function to control event
def shape_selection(event, x, y, flags, param):
    global shape
    if event == cv2.EVENT_LBUTTONDBLCLK:
        shape.append((x, y))

    plot_shape()


def get_image(original=False):
    global polygons

    if original:
        return original_image.copy()
    else:
        alpha = 0.8
        image = original_image.copy()
        for p in polygons:
            pts = p['points']
            pts = np.asarray(pts)
            pts = pts.reshape((-1, 1, 2))
            cv2.fillPoly(image, [pts], (1, 1, 1))
        cv2.addWeighted(image, alpha, original_image.copy(), 1 - alpha, 0, image)
        return image


def manually_segmentation():
    global original_image, shape

    image_path = ''
    image_path = '/Users/jarvis/Downloads/per_sank 2/cereali_little2.jpg'
    while image_path == '':
        image_path = input('Insert the path to the image to segment:\n')

    result_path = ''
    result_path = '/Users/jarvis/Downloads/per_sank 2'
    while result_path == '':
        result_path = input('Insert the path to the folder in which save the segmentation:\n')

    name, ext = os.path.splitext(os.path.basename(image_path))

    legend = "\nLEGEND:\n" \
             "{}: {}\n" \
             "{}: {}\n" \
             "{}: {}\n" \
             "{}: {}\n".format('u', 'Undo last insertion',
                               'c', 'Clear all insertions',
                               's', 'Save points and go to execution to insert label',
                               'q', 'Terminate the insertion')
    print(legend)

    list_of_labes = []

    # load the image, clone it, and setup the mouse callback function
    image = cv2.imread(image_path)
    original_image = image.copy()
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    # cv2.resizeWindow(window_name, 1600, 2560)
    # cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_AUTOSIZE)
    cv2.setMouseCallback(window_name, shape_selection)

    while True:
        plot_shape()
        key = cv2.waitKey(1)

        # if 'q' is pressed, exit the loop
        if key == ord('q'):
            break

        # if 'u' is pressed, undo last insertion
        if key == ord('u'):
            shape = shape[:-1]

        # if 'c' is pressed, clear all points
        if key == ord('c'):
            shape = []

        # if 's' is pressed, ask the label and save the polygon
        if key == ord('s'):
            if len(shape) >= 3:
                plot_shape(saving=True)
                cv2.waitKey(1)

                for l in list_of_labes:
                    print(l)

                messagebox.showinfo('Change window', 'Type the label of the object into the execution of the script')

                label = input('Insert the label to assign to the object: ')

                polygon = {'label': label, 'points': shape}
                polygons.append(polygon)
                shape = []

    print(polygons)
    # close all open windows
    cv2.destroyAllWindows()

    print("\nLEGEND:\n"
          "{}: {}\n".format('q', 'Close window'))
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    plot_all_polygons(polygons)

    while True:
        plot_all_polygons(polygons)
        key = cv2.waitKey(1)

        # if 'q' is pressed, exit the loop
        if key == ord('q'):
            break

    final_image = plot_all_polygons(polygons, final=True)
    img_path = os.path.join(result_path, '(performance_tool)-' + name + '.png')
    cv2.imwrite(img_path, final_image)

    result_path = os.path.join(result_path, '(performance_tool)-' + name + '.json')
    print(result_path)

    polygons_json = {}

    for i, p in enumerate(polygons):
        polygons_json[str(i)] = p

    with open(result_path, 'w') as file:
        file.write(json.dumps(polygons_json, indent=4))

    return True
