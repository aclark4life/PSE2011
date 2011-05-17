
from zope.publisher.browser import BrowserPage

class MyPackage(BrowserPage):

    def __call__(self):
        pass


    def my_package_view(self):
        return 'boo yah from view'
