import pandas as pd
import subprocess
import time

imbd_dataset = pd.read_csv('IMDb movies.csv', low_memory=False)

data = {'title': imbd_dataset['title'], 'description': imbd_dataset['description'],
        'genre': imbd_dataset['genre']}

test_data = pd.DataFrame(data=data, columns=['title', 'description', 'genre'])

#anws = []
for i in range(20):
    input_t = '--title ' + test_data.iloc[i, 0] + ' --description ' + test_data.iloc[i, 1]
    proc = subprocess.run(['./infer_movie.py', input_t], stdout=subprocess.PIPE)
    print(proc.stdout.decode("utf-8").rstrip())
    #anws.append(proc.stdout.decode("utf-8").rstrip())

'''score = 0
for j, anw in enumerate(anws):
    if anw == test_data.iloc[j,2]:
        score += 1

result = score/20
print(f'score: {result}')'''