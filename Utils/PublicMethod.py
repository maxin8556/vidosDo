#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import requests
from contextlib import closing
import logging
from Logger.logcfg import LOGGING_CONFIG
from Logger.logger import LoggerSingleton
from Settings.settings import URLS_PATH
from urllib import parse
import re

LoggerSingleton().init_dict_config(LOGGING_CONFIG)


# 公共方法
class PublicMethod(object):
    def __init__(self):
        pass

    # 下载 模块
    def download(self, url, path):
        with closing(requests.get(url, stream=True)) as r:
            chunk_size = 1024
            content_size = int(r.headers['content-length'])
            logging.info('=================下载开始')
            print(path)
            with open(path, "wb") as f:
                n = 1
                for chunk in r.iter_content(chunk_size=chunk_size):
                    # loaded = n * 1024.0 / content_size
                    f.write(chunk)
                    # print('已下载{0:%}'.format(loaded))
                    # n += 1
            logging.info("################下载完成")

    # 获取全部的视频链接和标题
    def getUrl(self):
        path = URLS_PATH
        titleLink_list = []
        with open(path, "r", encoding="utf-8") as ff:
            urls = ff.readlines()
        crawledList = [_.strip() for _ in urls]
        for crawled in crawledList:
            result = re.findall('(.*)(https:.*)', crawled)
            if result:
                # title, link = result[0]
                titleLink_list.append(result[0])
            else:
                logging.error("正则匹配错误,及时修改规则")
                return "", ""
        return titleLink_list

    # url编码
    def urlDecode(self, url):
        parameter = url
        decode_url = parse.quote(parameter)  # quote()将字符串进行编码
        return decode_url

    def writeFile(self, resultPath, results):
        with open(resultPath, 'w', encoding='utf8')as fl:
            json.dump(results, fl, ensure_ascii=False, sort_keys=True, indent=4)
        logging.info("添加数据到result.json完成")


if __name__ == '__main__':
    tmp = PublicMethod()
    a = tmp.getUrl()
    print(len(a))
