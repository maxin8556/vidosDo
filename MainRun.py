import json

from Settings.settings import RESULT_PATH, VIDOS_PATH
from Utils.PublicMethod import PublicMethod
from Converter.WeiBoMiaoPai import WeiBoMiaoPai


class Download(object):
    def __init__(self):
        self.weibo = WeiBoMiaoPai()
        self.public = PublicMethod()
        self.resultJson = RESULT_PATH
        self.path = VIDOS_PATH


    # 开始下载视频
    def download(self):
        with open(self.resultJson, 'r', encoding="UTF-8") as fl:
            json_data = json.load(fl)

        for data in json_data:
            if "未知错误" in str(data):
                pass
            title = data['title'].replace('\t', '')
            url = data['vidosUrl']
            self.public.download(url=url, path=self.path.format(title))

    def main(self):
        self.weibo.main()

        self.download()


if __name__ == '__main__':
    tmp = Download()
    tmp.main()
