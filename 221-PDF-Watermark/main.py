'''
Adds watermarks ro every page of a file called super.pdf
'''

import sys
import PyPDF2

inputs = sys.argv[1:]


source = PyPDF2.PdfReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()
page_count = len(source.pages)

# linter was giving me a suggestion to use enumerate instead of range
# but it does not work with the pages _VirtualList data type
print(type(source.pages))

for i in range(page_count):
    page = source.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

with open('watermarked.pdf', 'wb') as file:
    output.write(file)
