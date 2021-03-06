#!/usr/bin/python
#-*- encoding:utf-8 -*-
import jieba                                                    #导入结巴分词模块

def splitSentence(inputFile, outputFile):
    fin = open(inputFile, 'r')                                  #以读的方式打开文件
    fout = open(outputFile, 'w')                                #以写的方式打开文件

    for eachLine in fin:
        line = eachLine.strip().decode('utf-8', 'ignore')       #去除每行首尾可能出现的空格，并转为Unicode进行处理
        wordList = list(jieba.cut(line))                        #用结巴分词，对每行内容进行分词
        outStr = ''
        for word in wordList:
            outStr += word
            outStr += '/ '
        fout.write(outStr.strip().encode('utf-8') + '\n')       #将分词好的结果写入到输出文件
    fin.close()
    fout.close()

splitSentence('分词前.txt', '分词后.txt')