# -*- coding:utf-8 -*-
__author__ = 'LH'
import sys
import jieba
reload(sys)

sys.setdefaultencoding('utf-8')

# 通过结巴分词工具将文本中的出现的每个词的权重计算出来
def createWordBook(File,goalFile):
    with open(File,"r") as RowFile:
        for line in RowFile.readlines():
            line.decode("utf-8")
            LineList = line.strip().split("\t")
            seg_list = jieba.cut(LineList[1])
            LineList[1] = ""
            index = 0
            value = ""
            for word in seg_list:
                value += " " + str(index) + ":" + word
                index += 1
            Line = LineList[0] + value + "\n"
            Line.encode("utf-8")
            with open(goalFile,"a") as resultFile:
                resultFile.write(Line)
                print Line

createWordBook("like_count.txt","1.txt")
createWordBook("forward_count.txt","forward_wordBook.txt")
createWordBook("comment_count.txt","comment_wordBook.txt")















