# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class MyHTMLParser (HTMLParser):
    def __handle_attrs(self,attrs):
        for name,value in attrs:
            print('->',name,'>',value)
    
    def handle_starttag(self, tag, attrs) :
        print("Start",":",tag)
        self.__handle_attrs(attrs)
    def handle_endtag(self, tag,):
        print("End".ljust(5),tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty".ljust(5),":",tag)
        self.__handle_attrs(attrs)


MyParser = MyHTMLParser()
MyParser.feed(''.join([input().strip() for i in range(int(input()))]))