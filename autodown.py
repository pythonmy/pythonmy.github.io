"""
Author: Shadowys
Date: 12/6/2014
Description:
Auto markdown pusher. Uses a text file for configuration and batch processing.
:template: is the filepath of the template html
:parsekey: is the point to be replaced by the markdown content
:pages:    is filepath the markdown pages to be converted
"""

import markdown
import codecs
import sys

def parser(filepath):
    """Parses the config file given"""
    try:
        with open(filepath, "r") as f:
            data=''.join([line for line in list(f) if (line and line[0]!=";")]).split(":")
            data=[line for line in data if line]
            data={data[i]:data[i+1] for i in range(0,len(data),2)}
            for k,v in data.items():
                data[k]=[ele for ele in v.split("\n") if ele]
        return data
    except IOError as e:
        print("Error : %s\n>File %s not found in same folder as script."%(e,filepath))
        return None
    except IndexError as e:
        print("Error : %s\n>Ensure file %s is formatted properly as :key:\nvalues."%(e,filepath))
        return None

def templateloader(filepath):
    """Gets the html contents of a template html"""
    template=""
    try:
        with open(filepath,'r') as f:
            template=f.read()
            print("template.html found. Templated site is used.")
    except IOError:
        print("Error : %s"%(e))
        print(">File %s not found in same folder as script."%(filepath))
        print(">Plain site rolled out")
    return template

def mdreader(filepath):
    """Read and write a markdown content file"""
    html=""
    try:
        with codecs.open(filepath, mode='r', encoding="utf-8") as f:
            text=f.read()
            html=markdown.markdown(text, extensions=["fenced_code"])
            print(">File %s converted to html"%(filepath))
    except IOError as e:
        print("Error : %s"%(e))
        print(">File %s not found in same folder as script."%(filepath))
    return html

def synthesis(filename,html,template, parsekey):
    """Merge markdown converted file with template"""
    filename=filename.split("/")[-1]
    htmlpath="".join(filename.split(".")[:-1]+[".html"])
    try:
        with codecs.open(htmlpath, 'w', encoding="utf-8") as f:
            fullfile=template.replace(parsekey, html)
            print(fullfile,file=f)
            return f
    except OSError as e:
        print("Error : %s"%(e))
        print(">File \"%s\" is not converted into html."%(filename))
        return None

def main(configfile):
    dex=parser(configfile)
    tem=templateloader(dex["template"][0])
    pages=[(page,mdreader(page)) for page in dex["pages"]]
    pages=[synthesis(dat[0],dat[1],tem,dex["parsekey"][0]) for dat in pages if dat[1]]

main("pages.txt")
input("Press Enter to exit")
