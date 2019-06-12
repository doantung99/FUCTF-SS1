from pwn import *
import json, re, os
cmd_ls, cmd_cat, cmd_exit = '1', '2', '3'

def send_cmd(path, cmd_type):
    r = remote('139.180.213.85', 10005)
    r.sendline(cmd_type)
    r.sendline(path)
    result = r.readall()
    return str(result[140:], 'utf-8').strip()

def get_list(input):
    input = input[1:-1].split(', ')
    input = [t[1:-1] for t in input]
    return input

def ls(path):
    result = send_cmd(path, cmd_ls)
    if 'This is a file' not in result:
        result = get_list(result)
    return result

def cat(path):
    result = send_cmd(path, cmd_cat)
    if 'fuctf' in result:
        print(result)
        exit(0)

def dfs(path):
    print(path)
    list_file = ls(path)
    for f in list_file:
        if f == '':
            continue
        next_f = os.path.join(path, f)
        result = ls(next_f)
        if result == "This is a file":
            cat(next_f)
        else:
            dfs(next_f)

if __name__ == "__main__":
    dfs('.')
