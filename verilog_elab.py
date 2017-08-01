import os.path
import sys

init_filename = sys.argv[1]
dir_lst = ['', ]
result = open("result.v", 'w')


def parse_verilog(filename):
    global result
    file_exists = False
    for dir in dir_lst:
        if os.path.isfile(dir + filename):
            filename_sum = dir + filename
            file_exists = True
            break
    if not file_exists:
        print ("[-] " + filename)
        return 0
    else:
        print("[+] " + filename_sum)
    with open(filename_sum, 'r') as f:
        for string in f:
            nocomment_str = string.split('//')[0]
            if '`include' not in nocomment_str:
                result.write(string)
            else:
                begin_quote_pos = nocomment_str.find('"') + 1
                end_quote_pos = nocomment_str.find('"', begin_quote_pos)
                file_name = nocomment_str[begin_quote_pos:end_quote_pos]
                parse_verilog(file_name)
    result.write("\n")  # cause there is no eofs in the end of the file
    return 1


parse_verilog(init_filename)

result.close()
print("Verilog parse done!")
