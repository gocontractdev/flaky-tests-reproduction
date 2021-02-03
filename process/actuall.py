import shutil
import glob
import os
from nltk import sent_tokenize, word_tokenize, PorterStemmer, download
from nltk.corpus import stopwords
import collections
from operator import itemgetter
from wordsegment import load, segment
import sys
import csv

# base paths
# Warning: Do not move any files the whole thing breaks apart
dir_path = os.path.dirname(os.path.realpath(__file__))
data_path = 'data'
input_path = data_path + '/input'
temp_path = data_path + '/temp'
original_repo_path = input_path + '/original_repo/msr4flakiness'


def main():
    # Step 0 - copy base input files
    print('Step 0 : Copying base files to the input directory -- Please wait..')

    shutil.copy(original_repo_path + '/deflaker/historical_projects.csv',
                input_path + '/historical_projects_copied.csv')
    shutil.copy(original_repo_path + '/deflaker/historical_rerun_flaky_tests.csv',
                input_path + '/historical_projects_copied.csv')

    print('input is now populated ✔✔✔')

    # Step 1 : clone target directories
    print('Step 1 : Preparation -- Please choose the mode you want to run (Easy (e or ez)| Heavy (v)) ')
    mode = str(input('Please choose the mode? [Easy Mode (e or ez) | Heavy Mode (h or hv)]'))
    if mode.startswith('h'):
        heavy_mode()
    else:
        ez_mode()

    # Step 2 : Run the tokenization
    fixed_find_potential_features()

    # Step 3 :  frequency calculation

    #


def ez_mode():
    print('😳 Ease (EZ) mode skips heavy processes and simplifies steps for quick validation ...')

    shutil.rmtree(temp_path)

    # copy the samples and re-runs
    # shutil.copytree(original_repo_path + '/deflaker/reruns', temp_path + '/reruns')
    # shutil.copytree(original_repo_path + '/deflaker/samples_nonflaky', temp_path + '/samples_nonflaky')
    shutil.copytree(original_repo_path + '/deflaker/samples_flaky', temp_path + '/samples_flaky')


def heavy_mode():
    print('⚠️ You have chosen heavy mode -- This might take a while...')


# this code is from original repository -> but the code was broken so I had to fix it
def fixed_find_potential_features():
    sys.path.append(original_repo_path + '/deflaker')
    f = __import__('find_potential_features')

    pathname = temp_path + '/samples_flaky/test_tokens'
    numfiles = len(os.listdir(pathname))
    print("processing {} files".format(numfiles))

    test_words = {}
    num_processed_files = 0
    for filename in glob.glob(pathname + "/*"):
        with open(filename, 'r') as file:
            data = file.read().replace('\n', ' ')  # error 1 : missing space here
            test_words[filename] = f.read_words(data)
            num_processed_files = num_processed_files + 1
            print(f'\r{100 * (num_processed_files / numfiles):.2f}' + "% processed", end='')

    word_frequency = f.compute_frequency(test_words)
    sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

    with open(data_path + '/output/frequencies_raw.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["word", "count"])
        for elem in sorted_word_frequency:
            writer.writerow([elem[0], elem[1]])


if __name__ == '__main__':
    main()
