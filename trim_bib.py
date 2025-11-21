# Zotero - export as BibLatex
# pip install --pre bibtexparser
# python3 trim_bib.py
import bibtexparser
library = bibtexparser.parse_file("pirovc.bib")
keep =  {"title", "author", "publisher", "journaltitle", "date", "url", "doi"}
for e in library.entries:
    for k in e.fields_dict:
        if k not in keep:
            e.pop(k)
bibtexparser.write_file("pirovc.bib", library)