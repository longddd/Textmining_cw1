import os
import random
'''
transform into lowercase txt

'''


def lowercase_txt(file_name, new_file):
    with open(file_name, 'r', encoding="utf8") as f:
        contents = f.read()  # read contents of file
    contents = contents.lower()  # convert to lower case
    with open(new_file, 'w', encoding="utf8") as f:  # open for output
        f.write(contents)


'''
randomly split the training set into 10 portions. 9 portions are for training, 
and the other is for development, which will be used for early
stopping or hyperparameter tuning.
'''


def split(file_name, ratio):
    random.seed(1)
    ratio = ratio  # Set ratio
    with open(file_name, 'r') as f1:
        lines = f1.readlines()
    random.shuffle(lines)  # random shuffle lines
    lines_split = int(len(lines) * ratio)
    open('.././data/train.txt', 'w').write(''.join(lines[:lines_split]))
    open('.././data/dev.txt', 'w').write(''.join(lines[lines_split:]))


if __name__ == '__main__':
    lowercase_txt('.././data/train_5500.txt', '.././data/train_5500lowercase.txt')
    split('.././data/train_5500lowercase.txt', 0.9)
