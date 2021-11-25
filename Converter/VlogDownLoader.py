#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import logging
from Logger.logcfg import LOGGING_CONFIG
from Logger.logger import LoggerSingleton

LoggerSingleton().init_dict_config(LOGGING_CONFIG)


class VlogDownLoader(object):
    """
    解析地址2 https://pv.vlogdownloader.com/
    """
    def __init__(self):
        pass

    # 获取解析之后的视频地址
    def getVidosUrl(self):
        pass

    def main(self):
        pass


if __name__ == '__main__':
    tmp = VlogDownLoader()
    tmp.main()
