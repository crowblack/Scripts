#! python3

# run_tracker.py  tracking my monthy stats

import shelve



def data_entry():
    run_data = []
    while True:
           
        runs = []
        month = input('Enter Month:')
        runs = runs + [month]
        year = input('Enter year:')
        runs = runs + [year]
        dist = input('Enter distance:')
        runs = runs + [dist]
        pace = input('Enter pace as minutes.seconds:')
        runs = runs + [pace]
        run_data = run_data + [runs]
        ans = input('Enter more data y/n?')
        if ans == 'n':
            break
    return run_data

shelfFile = shelve.open('rundata')
deets = data_entry()
shelfFile['deets'] = deets
shelfFile.close()
print(data_entry)


        
