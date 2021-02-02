# Warning: Do not move any files the whole thing breaks apart!
import shutil
data_path = 'data'
input_path = data_path + '/input'
original_repo_path = input_path + '/original_repo/msr4flakiness'

# Step 0 - part 1 : copy base input files
print('Step 0 : Copying base files to the input directory -- Please wait..')

newPath = shutil.copy(original_repo_path + '/deflaker/historical_projects.csv', input_path + '/historical_projects_copied.csv')


print('input is now fully populated ✅')

# step 0 - part 2



# Step 1 : clone target directories
print('Step 1 : Clone target git directories')

# Step 2 : Run the tokenizers and NLP
f = __import__(original_repo_path + '.defalker.find_potential_features.py')

x = f.read_words('xxxxxxxxxx xx')
print(x)
# del
