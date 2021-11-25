#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import logging
from Logger.logcfg import LOGGING_CONFIG
from Logger.logger import LoggerSingleton
from Settings.settings import WEIBO_HASH, RESULT_PATH
from Utils.PublicMethod import PublicMethod


# LoggerSingleton().init_dict_config(LOGGING_CONFIG)


class WeiBoMiaoPai(object):
    """
    解析地址1 https://weibomiaopai.com/
    """

    def __init__(self):
        self.public = PublicMethod()
        # 这个参数是微博秒拍的动态参数(多久变化一次未统计),数据量不大,直接手动修改
        self.hash = WEIBO_HASH
        self.path = RESULT_PATH
        self.requestUrl = "https://video.justyy.workers.dev/api/video/?cached&lang=ch&hash={}&video={}"
        self.headers = {
            "Referer": "https://weibomiaopai.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
        }

    # 获取解析之后的视频地址
    def getVidosUrl(self):
        # 先获取需要解析的地址
        titleLink_list = self.public.getUrl()
        logging.info("需要解析视频个数<--->{}".format(len(titleLink_list)))
        download_info = []
        i = 0
        for titleLink in titleLink_list:
            i += 1
            title, link = titleLink
            logging.info("开始解析第 {} 视频<--->{}".format(i, title))
            # 编码URL
            resultLink = self.public.urlDecode(link)
            try:
                vidosUrl = self.requestUrl.format(self.hash, resultLink)
                response = requests.get(url=vidosUrl, headers=self.headers, timeout=60)
                content = response.json()
                download_title = title
                if "url" in str(content):
                    download_url = content['url']
                    items = {
                        "title": download_title,
                        "vidosUrl": download_url
                    }
                    download_info.append(items)
                else:
                    download_url = "解析失败"
                    items = {

                        "title": download_title,
                        "vidosUrl": download_url
                    }
                    download_info.append(items)
            except:
                logging.error("未知错误")
                items = {
                    "title": "未知错误",
                    "vidosUrl": "未知错误"
                }
                download_info.append(items)

        self.public.writeFile(self.path, download_info)
        return download_info

    def main(self):
        self.getVidosUrl()


if __name__ == '__main__':
    tmp = WeiBoMiaoPai()
    tmp.main()
