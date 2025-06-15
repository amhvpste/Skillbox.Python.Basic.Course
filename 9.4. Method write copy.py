speakers_file = open('speakers.txt','r')

for i_line in speakers_file:
    print(i_line, end='')
    sym_count.apppend(str(len(i_line)))
sym_count_str = ''.join(sym_count)

speakers_file.close

counts_file = open('sym_count.text', 'w')
counts_file.write(sym_count_str)
counts_file.close

