import glob
import subprocess
import csv
import os
import sys
import re
import shutil
import subprocess

# base paths
# Warning: Do not move any files the whole thing breaks apart
dir_path = os.path.dirname(os.path.realpath(__file__))
data_path = 'data'
input_path = data_path + '/input'
temp_path = data_path + '/temp'
original_repo_path = input_path + '/original_repo/msr4flakiness'
test_folder = temp_path + "/test_files"
test_cases_folder = temp_path + "/test_cases"


def main():
    # Step 0 - copy base input files
    print('Step 0 : Copying base files to the input directory -- Please wait..')

    shutil.copy(original_repo_path + '/deflaker/historical_projects.csv',
                input_path + '/historical_projects_copied.csv')
    shutil.copy(original_repo_path + '/deflaker/historical_rerun_flaky_tests.csv',
                input_path + '/historical_rerun_flaky_tests.csv')
    shutil.copy(original_repo_path + '/idflakies/list-flaky.csv',
                input_path + '/list-flaky.csv')

    print('input is now populated ✔✔✔')

    # Step 1 : clone target directories
    print('Step 1 : Preparation -- Please choose the mode you want to run (Easy (e or ez)| Heavy (v)) ')
    mode = str(input('Please choose the mode? [Easy Mode (e or ez) | Heavy Mode (h or hv)]'))
    if mode.startswith('h'):
        heavy_mode()
    else:
        ez_mode()

    # Step 2 :
    # Run the tokenization
    fixed_find_potential_features()
    # frequency calculation
    frequencies()


def ez_mode():
    print('😳 Ease (EZ) mode skips heavy processes and simplifies steps for quick validation ...')
    exit('222')
    shutil.rmtree(temp_path)
    # copy the samples and re-runs
    # shutil.copytree(original_repo_path + '/deflaker/reruns', temp_path + '/reruns')
    # shutil.copytree(original_repo_path + '/deflaker/samples_nonflaky', temp_path + '/samples_nonflaky')
    shutil.copytree(original_repo_path + '/deflaker/samples_flaky', temp_path + '/samples_flaky')


def heavy_mode():
    print('⚠️ You have chosen heavy mode -- This might take a while...')

    #shutil.rmtree(temp_path)
    #mine_all_repos()  # this makes test cases
    separate_all_tests()


# ❌ this code is from original repository -> but the code was broken so I had to fix it
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

    with open(data_path + '/output/features_raw.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["token", "count"])
        for elem in sorted_word_frequency:
            writer.writerow([elem[0], elem[1]])


# ❌ this is not my code -> it is modified version of original
def frequencies():
    sys.path.append(original_repo_path + '/deflaker')
    f = __import__('frequency_potential_features')
    coverage_matrix = {}
    pathname = temp_path + '/samples_flaky/test_tokens'
    for filename in glob.glob(pathname + "/*"):
        with open(filename, 'r') as file:
            presence = set()
            data = file.read().replace('\n', '')
            for feature in f.features:
                if f.re.search(feature, data, f.re.IGNORECASE):
                    presence.add(feature)
                    if f.word_frequency.get(feature) == None:
                        f.word_frequency[feature] = 1
                    else:
                        tmp = f.word_frequency[feature]
                        f.word_frequency[feature] = tmp + 1
            coverage_matrix[filename] = presence
            tmp = [1 if x in presence else 0 for x in f.features]
            print(tmp)
    sorted_word_frequency = sorted(f.word_frequency.items(), key=lambda x: x[1], reverse=True)
    # save the output

    with open(data_path + '/output/features_frequency.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["token", "count"])
        for elem in sorted_word_frequency:
            writer.writerow([elem[0], elem[1]])


# ❌ This code is not mine -- I have only fixed it
def mine_all_repos():
    print('⚠️ WARNING: Do not stop the process untill this step is finished')
    basedir = os.getcwd()
    urls = set()
    with open(input_path + '/list-flaky.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        usage_dir = None
        for row in csv_reader:
            if (row["Category"] == "OD"):
                continue
            url = row["URL"]
            if (not url in urls):

                if (not usage_dir is None):
                    os.chdir("..")
                    if (os.path.exists(usage_dir)):
                        shutil.rmtree(usage_dir, ignore_errors=True)
                parts = url.split("/")
                usage_dir = parts[len(parts) - 1]
                if usage_dir == None:
                    raise Exception("fatal error")
                if (os.path.exists(usage_dir)):
                    pass
                # clone the repository
                if (not os.path.exists(usage_dir)):
                    print("cloning project " + url)
                    myprocess = subprocess.Popen(['git', 'clone', url],
                                                 stdout=subprocess.PIPE,
                                                 stderr=subprocess.STDOUT)
                    stdout, stderr = myprocess.communicate()
                    sha = row["SHA"]
                    print("checking out revision {}".format(sha))
                    myprocess = subprocess.Popen(['git', 'checkout', sha],
                                                 stdout=subprocess.PIPE,
                                                 stderr=subprocess.STDOUT)
                    stdout, stderr = myprocess.communicate()
                os.chdir(usage_dir)
                urls.add(url)
            testcase = row["Test Name"]
            testcase = testcase.split()[0]
            parts = testcase.split(".")
            testfile = parts[len(parts) - 2]

            myprocess = subprocess.Popen(['find', '.', '-name', "{}.*".format(testfile)],
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT)
            stdout, stderr = myprocess.communicate()
            result = stdout.decode("utf-8")

            if (len(stdout) == 0):
                print("  empty file {}:{}:{}".format(usage_dir, sha, testfile))
                continue
            if (len(re.findall('un', result)) == 1):
                path_to_testfile = result.strip(" \n")
            else:
                path_to_testfile = result.split("\n")[0]

            from pathlib import Path
            Path("../" + test_folder).mkdir(parents=True, exist_ok=True)
            print(testfile)
            shutil.copy(path_to_testfile, "../" + test_folder + '/' + testcase)

        os.chdir(basedir)
        if (os.path.exists(usage_dir)):
            shutil.rmtree(usage_dir, ignore_errors=True)


def separate_all_tests():
    print('⛴ This part is handled virtually through docker -- if it is running already it will fail...')
    filenames = [f for f in glob.glob(test_folder + "/*", recursive=False)]
    os.system("cd process; docker stop my_little_alpine")
    os.system("cd process; docker container rm my_little_alpine")
    os.system("cd process; docker-compose build")
    os.system("cd process; docker-compose up -d")

    # build the main jar file
    runnable_command = "java -jar " + '/utilities/vis_method/build/libs/vis_method.jar ' + filename + " " + testname
    os.system("cd process; docker container exec -it my_little_alpine " + runnable_command + ";")

    for filename in filenames:
        parts = filename.split(".")
        testname = parts[len(parts) - 1]
        runnable_command = "java -jar " + '/utilities/vis_method/build/libs/vis_method.jar ' + filename + " "+ testname
        os.system("cd process; docker container exec -it my_little_alpine " + runnable_command + ";")

        exit('1111')
        # myprocess = subprocess.Popen(
        #    ['java', '-jar', original_repo_path + '/utils/vis_method/build/libs/vis_method.jar', filename, testname],
        #    stdout=subprocess.PIPE,
        #    stderr=subprocess.STDOUT)
        # mbody, stderr = myprocess.communicate()

        mbody = ''
        parseError = b'com.github.javaparser.ParseProblemException' in mbody
        # create a file with the test case
        print('ss')
        if not parseError and len(mbody) > 400:
            with open(test_cases_folder + os.path.basename(filename), "wt+") as testfile:
                print(mbody.decode("utf-8"))
                testfile.write(mbody.decode("utf-8"))
        else:
            print(os.path.basename(filename))


if __name__ == '__main__':
    main()
