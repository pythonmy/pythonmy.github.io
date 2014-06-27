"""
Author: Shadowys
Date: 12/6/2014
Description:
Auto markdown pusher. Uses a text file for configuration and batch processing.
:template: is the filepath of the template html
:parsekey: is the point to be replaced by the markdown content
:pages:    is filepath the markdown pages to be converted
"""

import autotemplate as at
import re

def parser(filepath, key="body"):
    """Parses the config file given"""
    try:
        with open(filepath, "r") as f:
            cur=""
            data={}
            for line in f :
                if line.strip("- \n") and line[0]=="-":
                    line=line.strip("- \n")
                    data[line]=[]
                    cur=line
                elif line[0]!=":" and line[0]!=";":
                    # ; at the start of the line for lines to ignore
                    if not cur :
                        cur="-"+key
                        data[cur]=[]
                    data[cur].append(line)
        for k,v  in data.items() :
            data[k]=''.join(v).strip("\n").split("\n")
        return data
    except IOError as e:
        print("Error : %s\n>File %s not found in same folder as script."%(e,filepath))
        return None
    except IndexError as e:
        print("Error : %s\n>Ensure file %s is formatted properly as :key:\nvalues."%(e,filepath))
        return None

def loader(filepath):
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

def moveto(name,ext="html", folder=".", delimiter="-"):
    deli=delimiter
    name=name.split("/")[-1]
    #dots and spaces cannot be accepted by the browser
    #in filenames
    name=re.sub("[\.\ ]+",deli,name)
    name="%s/%s.%s"%(folder,deli.join(name.split(deli)[:-1]), ext)
    return name
    
def synthesiser(config):
    con=parser(config)
    tem=loader(con["template"][0])
    pages=con["pages"]
    for file in pages:
        data=at.parser(file)
        if data:
            data=at.convertor(data)
            name=moveto(file)
            at.merger(name, tem, data)
        else:
            print("Failed for %s"%file)

if __name__=="__main__":
    synthesiser("pages.txt")
    input("Completed. Enter->Exit")
