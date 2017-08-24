# coding:utf8

import url_manager,html_downloader,html_outputer,html_parser
import traceback

NUM = 100


class SpiderMain(object):
	"""docstring for SpiderMain"""
	def __init__(self):
		self.urlmanager = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()


	def craw(self,root_url):
		count = 1
		self.urlmanager.add_new_url(root_url)
		print("begin spider:"+root_url)
		while self.urlmanager.has_new_url():
			try:
				new_url = self.urlmanager.get_new_url()
				print("haha")
				print("craw %d : %s" % (count,new_url))
				html_cont = self.downloader.download(new_url)
				new_urls, new_data = self.parser.parse(new_url,html_cont)
				self.urlmanager.add_new_urls(new_urls)
				self.outputer.collect_data(new_data)
				if count >= NUM:
					break
				count = count+1;
			except Exception as e:
				traceback.print_exc()
		self.outputer.output_html()


		

if __name__=="__main__":
	root_url = "http://baike.baidu.com/item/Python/407313?fr=aladdin"
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)


