import csv, os, time
path = 'files_to_merge/'
list_of_CSVs = [item for item in os.listdir(path) if '.csv' in item]

def get_header(fileName):
    
    with open(path + fileName, 'r', encoding = '1250', newline = '') as rFile:
        header = rFile.readline().split(';')    
    for i, item in enumerate(header):
        header[i] = item.strip()
    return header

def get_final_header(all_CSVs):
    
    final_header = []
    for file in all_CSVs:
        for item in get_header(file):
            final_header.append(item) if item not in final_header else 0
            
    return final_header
#---------------------------------------------
print('Merging...')
if os.path.exists(path):
    
    with open('000_merge_{0}.csv'.format(time.strftime("%Y-%m-%d_%H%M%S")), 'w', encoding = '1250', newline = '') as newFile:
        
        csvWriter = csv.DictWriter(newFile, delimiter = ';', fieldnames = get_final_header(list_of_CSVs))
        csvWriter.writeheader()
        
        for file in list_of_CSVs:
            with open(path + file, 'r', encoding = '1250', newline = '') as rFile:
                
                csvReader = csv.DictReader(rFile, delimiter = ';')
                csvWriter.writerows(csvReader)

    print('Done.\n{0} files merged.'.format(len(list_of_CSVs)))
    
else:
    print('Failed! Folder missing: {}'.format(path))
