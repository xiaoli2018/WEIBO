# -*- coding:utf8 -*-
__author__ = 'LH'
import time
import sys

reload(sys)

sys.setdefaultencoding('utf8')
#将weibo_train_data.txt中的转发数,评论数，赞数和微博的内容提取出来
def extractData(RowFile,*goalFile):
    with open(RowFile,"r") as file:
        for line in file.readlines():
            line.decode('utf8')
            Linelist = line.strip().split("\t")
            index = 4
            for i in goalFile:
                ExtractLine = Linelist[index] + "\t" + Linelist[6] + "\n"
                ExtractLine.encode("utf-8")

                with open(i,'a') as extractFile:
                    extractFile.write(ExtractLine)
                    print ExtractLine.encode("utf-8")
extractData("weibo_train_data.txt","comment_count.txt")








