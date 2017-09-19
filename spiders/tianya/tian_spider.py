# -*-coding:utf-8 -*-
import re
import urllib2


class TianSpider(object):
    def __init__(self):
        self.url = 1

    def craw(self):
        new_url = basic_url + str(self.url) +'.shtml'

        while new_url:
            # global file
            print self.url
            new_data = self.download(new_url)
            #print new_data
            file = self.write1(new_data)
            # file = open('ttyy.txt', 'a')
            # for item in new_data:
            #     print '正在加载第' + str(self.url) + '页数据'
            #     line = '\n ' + '----------------------第' + str(self.url) + '页-------------------------\n'
            #     file.write(line)
            #     file.write(item)
            self.url += 1
            new_url = basic_url + str(self.url) + '.shtml'
            if self.url == 300:
                break
        return file

    def download(self, new_url):
        html_node = urllib2.urlopen(new_url)
        html_content = html_node.read()

        pattern1 = re.compile('uname="再次路过之">.*?<span>时间：(.*?)</.*?"bbs-content".*?</div>', re.S)
        pattern2 = re.compile('uname="再次路过之">.*?<span>时间：.*?</.*?"bbs-content"(.*?)</div>', re.S)
        items1 = re.findall(pattern1, html_content)
        items2 = re.findall(pattern2, html_content)
        data = []
        bb = re.compile('<.*?>')
        for item1 in items1:

            data.append(item1)

            for item2 in items2:
                item2 = re.sub(bb, '\n', item2)
                data.append(item2)
        return data

    def write1(self, new_data):
        file = open('feeling.txt', 'a')
        for item in new_data:
            print '正在加载第'+ str(self.url) +'页数据'
            line = '\n ' + '----------------------第' + str(self.url) + '页-------------------------\n'
            file.write(line)
            file.write(item)
        return file

if __name__ == "__main__":
    # http://bbs.tianya.cn/post-free-1053021-1.shtml
    # http://bbs.tianya.cn/post-free-1053021-3.shtml
    basic_url = 'http://bbs.tianya.cn/post-free-1053021-'
    spider = TianSpider()
    spider.craw()

# self.file = open(title + ".txt","w+")
