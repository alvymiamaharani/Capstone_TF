# Script to create CSV data file from Pascal VOC annotation files
# Based off code from GitHub user datitran: https://github.com/datitran/raccoon_dataset/blob/master/xml_to_csv.py

import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        filename = root.find('filename').text
        width = int(root.find('size/width').text)
        height = int(root.find('size/height').text)
        class_name = root.find('object/name').text
        xmin = int(root.find('object/bndbox/xmin').text)
        xmax = int(root.find('object/bndbox/xmax').text)
        ymin = int(root.find('object/bndbox/ymin').text)
        ymax = int(root.find('object/bndbox/ymax').text)

        xml_list.append((filename, width, height, class_name, xmin, ymin, xmax, ymax))

    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df

def main():
    for folder in ['train', 'valid']:
        image_path = os.path.join(os.getcwd(), ('datasets/' + folder))
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv(('datasets/' + folder + '_labels.csv'), index=None)
        print('Successfully converted xml to csv.')

main()