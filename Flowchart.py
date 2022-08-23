from pyflowchart import Flowchart
with open('Web Scraping.py') as f:
    code = f.read()
fc = Flowchart.from_code(code)
print(fc.flowchart())
