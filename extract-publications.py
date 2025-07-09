#!/usr/bin/env python3

"""
Script to extract publications-old.html into separate data files for _publications with appropriate tags

CC July 2025
"""

STARTITEM = "<li>"
ENDITEM = "</li>"
STARTTITLE = "<h4>"
ENDTITLE = "</h4>"
STOPSCAN = "<hr>"

PUB = {}
QUOTES = ["\"", "'"]

def remove_spaces(text):
    t1 = text.replace(" ","")
    t2 = t1.replace("\t","")
    return t2

def quote(text):
    global QUOTES

    text = text.strip()
    for q in QUOTES:
        if q not in text:
            return "%s%s%s" % (q, text, q)
    ntext = text.replace("\"", "\\\"")
    return "\"%s\"" % (ntext)

def title_to_tag(title):
    tag = title
    if "Overview" in tag:
        tag = "overview"
    elif "theory" in tag:
        tag = "theory"
    elif "Extensions" in tag:
        tag = "extensions"
    elif "Advanced" in tag:
        tag = "advanced primitives"
    elif "using" in tag:
        tag = "applications"
    print("TITLE: %s" % title)
    print("TAG: %s" % tag)
    return tag

def find_paper_title(text):
    """
    Try to find the paper's title, or None. Assumes balanced non-nested double quotes
    We pick the first substring that doesn't follow an equals sign (typically html tag attributes)
    """
    dt = text.split('"')
    for i in range(1,len(dt),2):
        if not (dt[i-1].endswith("=")):
            return dt[i].strip()
    return None

def find_year(text):
    import re

    m = re.search(r'20\d{2}', text)
    if m:
        return int(m.group(0))
    else:
        return -1

def find_authors(alltext):
    author_prefix = "by "

    dt = alltext.split('"')
    for idx in range(0,len(dt),2):
        text = dt[idx]
        i = text.find(author_prefix)
        if i >= 0:
            authors = text[i + len(author_prefix):]
            for terminal in [", presented",".",", paper presented"]:
                j = authors.find(terminal)
                if j >= 0:
                    authors = authors[:j].strip()
            if len(authors) > 0:
                return authors
        
    return None

def expand_urls(text,fp):
    dt = text.split('"')
    for i in range(1,len(dt)):
        if remove_spaces(dt[i-1]).endswith("href="):
            fp.write("url: %s\n" % (quote(dt[i])))

def expand_theses(text,fp):
    for thesis_type in ["PhD","bachelor","master"]:
        thesis_text = "%s thesis" % (thesis_type)
        if thesis_text in text:
            fp.write("thesis: %s\n" % thesis_type)

def process_item(tag, summary):
    global PUB

    paper_title = find_paper_title(summary)
    year = find_year(summary)
    authors = find_authors(summary)

    # print("ITEM: %s" % summary)
    # print("\n")

    # Update section/tag counter
    if tag in PUB.keys():
        count = PUB[tag] + 1
    else:
        count = 0
    PUB[tag] = count

    fn = "_publications/pub_%s_%s.md" % (tag, f"{count:03}")
    fp = open(fn,'w')
    fp.write("---\n")
    fp.write("layout: publication\n")
    fp.write("tag: %s\n" % tag)
    if authors:
        fp.write("authors: \"%s\"\n" % authors)
    if paper_title:
        fp.write("title: \"%s\"\n" % paper_title)
    if year >= 0:
        fp.write("year: %i\n" % year)
    fp.write("summary: %s\n" % quote(summary))
    expand_urls(summary,fp)
    expand_theses(summary,fp)
    fp.write("---\n")
    fp.close()

def process(fn):
    print("Processing %s" % fn)
    fp = open(fn,'r')
    inside = False
    summary = ""
    tag = "unknown"
    year = -1
    paper_title = None
    for ll in fp.readlines():
        l = ll.strip() + " "
        
        if STOPSCAN in l:
            break

        if STARTTITLE in l and ENDTITLE in l:
            i = l.index(STARTTITLE) + len(STARTTITLE)
            j = l.index(ENDTITLE)
            title = l[i:j]
            tag = title_to_tag(title)

        if inside:

            if ENDITEM in l:
                i = l.index(ENDITEM)
                summary += l[:i]

                process_item(tag,summary)
                # Reset buffers
                summary = ""
                inside = False
                year = -1
                paper_title = None
            else:
                summary += l

        else:
            if STARTITEM in l:
                i = l.index(STARTITEM)
                summary = l[i+len(STARTITEM):]
                inside = True

    fp.close()

def main():
    process("publications-old.html")

if __name__ == '__main__':


    main()
