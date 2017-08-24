
import urllib2
class HtmlDownloader(object):
	"""docstring for HtmlDownloader"""
	
	def download(self,url):
		if url is None:
			print("download url is None")
		rsp = urllib2.urlopen(url)

		if rsp.getcode() !=200:
			print("code is %d" % rsp.getcode())
			return None

		return rsp.read()
