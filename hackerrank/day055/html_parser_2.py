from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self,data):
        if(data.__contains__("\n")):
            print (">>> Multi-line Comment")
            print(data)
        else:
            print (">>> Single-line Comment")
            print(data)
    def handle_data(self,data):
        if(len(data.split())>0):
            print(">>> Data")
            print(data)
  
  
  
  
  
  
  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()