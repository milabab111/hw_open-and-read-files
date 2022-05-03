#task 3
file_list = ['1.txt', '2.txt', '3.txt']
new_dict = {}

for file_name in file_list:
    with open(file_name, 'r') as file:
        lines = file.readlines() 
        new_dict[file_name] = lines
        len_lines = len(lines)
      
for file_name, lines in new_dict.items():
    for line_index in range(len(lines)):
        lines[line_index] = lines[line_index][:-1] + ' ' + file_name + '\n'

#print(new_dict)    

dict_lines = []
for file_name, lines in new_dict.items():
    lines.insert(0, str(len(lines)) + '\n')
    lines.insert(0, file_name + '\n')
    dict_lines.append(lines)
    
dict_lines.sort(key=lambda x: x[1])
print(dict_lines)

for lines in dict_lines:
    for line in lines:
        with open('newfile_sorted.txt', 'a') as file:
            file.write(str(line))







  
