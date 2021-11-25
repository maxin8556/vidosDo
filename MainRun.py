import json

from Settings.settings import RESULT_PATH, VIDOS_PATH
from Utils.PublicMethod import PublicMethod


class Download(object):
    def __init__(self):
        self.public = PublicMethod()
        self.resultJson = RESULT_PATH
        self.path = VIDOS_PATH

    # 开始下载视频
    def download(self):
        with open(self.resultJson, 'r', encoding="UTF-8") as fl:
            json_data = json.load(fl)

        for data in json_data:
            title = data['title'].replace('\t', '')
            url = data['vidosUrl']
            self.public.download(url=url, path=self.path.format(title))

    def main(self):
        self.download()


if __name__ == '__main__':
    tmp = Download()
    tmp.main()
