#!/usr/bin/python
# coding:utf8
import os

def is_file_contain_word(file_list, query_word):
    for _file in file_list:
        if query_word in open(_file).read():
            print _file
    print("Finish searching.")

def get_all_file(floder_path):
    file_list = []
    if floder_path is None:
        raise Exception("floder_path is None")
    for dirpath, dirnames, filenames in os.walk(floder_path):
        for name in filenames:
            file_list.append(dirpath + '/' + name)
    return file_list

query_word = raw_input("Please input the key word that you want to search:")
basedir = raw_input("Please input the directory:")

is_file_contain_word(get_all_file(basedir), query_word)
raw_input("Press Enter to quit.")