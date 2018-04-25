#!/usr/bin/env python3
import sys
import os
import pathlib
import weasyprint

### this works
pdfbytes = weasyprint.HTML('foobar.html')
pdfbytes.write_pdf('foobar.pdf')

pdffile = pathlib.Path('./foobar2.pdf')
pdfbytes.write_pdf(pdffile)

### this does not
pdfbytes = weasyprint.HTML('./foobar.html')


### this does not
htmlfile = pathlib.Path('./foobar.html')
print(type(htmlfile))
print(htmlfile)
pdfbytes = weasyprint.HTML(htmlfile)


