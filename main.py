import os
from pprint import pprint
out_data = []

for i in range(3):
    file_name = str(i + 1) + '.txt'
    file_path = os.path.join(os.getcwd(),  'sorted', file_name)
    with open(file_path, encoding='UTF-8') as infile:
        string_list = infile.readlines()
        out_data.append([file_name, len(string_list), ''.join(string_list)])

out_data.sort(key=lambda n: n[1])

with open('out_file.txt', 'w', encoding='UTF-8') as outfile:
    outfile.write('\n'.join([str(b) for a in out_data for b in a]))
