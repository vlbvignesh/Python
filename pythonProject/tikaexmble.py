# import parser object from tike
import tika
from tika import parser
tika.initVM()

# opening pdf file
parsed_pdf = parser.from_file("E:\\TNPSC\\25-trb-pg-2007-physics-qa.pdf")

# saving content of pdf
# you can also bring text only, by parsed_pdf['text']
# parsed_pdf['content'] returns string
data = parsed_pdf['content']

# Printing of content
#print(data)

print(parsed_pdf[data])
#print(parsed_pdf["content"])


# <class 'str'>
#print(type(data))