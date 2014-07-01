python-indent-parser
====================

python-indent-parser



#Usage:

content=......
parser = IndentParser(content)
lines = parser.find_line(['text_in_my_line'])


parser = IndentParser(content,exactmatch=True,ignore_characters=['!'])
lines = parser.find_line(['exact_line_text','exact_sub_line_text'])


childrens = parser.find_children(['exact_line_text','exact_sub_line_text']





