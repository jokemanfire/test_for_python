from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest

class Test(unittest.TestCase):
    bs = None
    def setUpClass(self):
        global bs
        url = "http://en.wikipedia.org/wiki/Monty_python"
        bs = BeautifulSoup(urlopen(url))

    def test_titleText(self):
        global bs
        pagetitle = bs.find("h1").get_text()
        self.assertEqual("Motnty Python",pagetitle)

    def test_contentExists(self):
        global  bs
        content = bs.find("div",{"id":"mw-content_text"})
        self.assertIsNotNone(content)

if __name__=="__main__":
    unittest.main()