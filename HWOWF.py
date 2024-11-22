from six import print_

files = ['1.txt', '2.txt', '3.txt']
all_info = []
for file in files:
    with open(file, 'r' ) as f:
        line_count = sum(1 for line in f)
    with open(file, 'r') as f:
        text = f.readlines()
        info_file = [file, line_count, text]
        all_info.append(info_file)
all_info = sorted(all_info, key=lambda x: x[1])
print(all_info)

with open('result.txt', 'a') as fres:
    for i in all_info:
        fres.write(i[0])
        fres.write('\n')
        fres.write(str(i[1]))
        fres.write('\n')
        for el in i[2]:
            fres.write(el)
        fres.write('\n')

