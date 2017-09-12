from xml.parsers.expat import ParserCreate

class DefaultSaxEandler(object):
    def start_element(self,name,attrs):
        print('sax:star:%s',name,str(attrs))

    def end_element(self,name):
        print('sax:end_element:',name)

    def char_data(self,text):
        print('sax:char_data',text)


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">python</a></li>
    <li><a href="/ruby">Ruby</a></li>
    </ol>'''

handler = DefaultSaxEandler()
parser = ParserCreate()
parser.StarElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)