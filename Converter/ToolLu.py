#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import logging
from Logger.logcfg import LOGGING_CONFIG
from Logger.logger import LoggerSingleton

LoggerSingleton().init_dict_config(LOGGING_CONFIG)


class ToolLu(object):
    """
    解析地址3 https://tool.lu/videoparser/
    """
    def __init__(self):
        pass

    # 获取解析之后的视频地址
    def getVidosUrl(self):
        pass

    def main(self):
        pass


if __name__ == '__main__':
    tmp = ToolLu()
    tmp.main()
