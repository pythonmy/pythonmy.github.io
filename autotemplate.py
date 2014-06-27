#Try to make a markdown file with complete control over the content
#Something like :title: denoting where the thing go

import markdown
import codecs
import sys
import re
import os

def parser(filepath, key="body"):
    """Parses the markdown file given"""
    try:
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                cur=""
                data={}
                for line in f :
                    if line.strip("- \n") and line[0]=="-":
                        line=line.strip("- \n").split(":") #former is the key, latter is unwanted tag
                        data[line[0]]=[[]]
                        cur=line[0]
                        if len(line)>1 : data[line[0]].append(line[1].strip())
                    elif line[0]!=":" and line[0]!=";":
                        # ; at the start of the line for lines to ignore
                        if not cur :
                            cur=key
                            data[cur]=[[],""]
                        data[cur][0].append(line)
            for k,v  in data.items() :
                data[k][0]=''.join(v[0])
            return data
        else:
            return None
    except IOError as e:
        print("Error : %s\n>File %s not found in same folder as script."%(e,filepath))
        return None
    except IndexError as e:
        print("Error : %s\n>Ensure file %s is formatted properly as :key:\nvalues."%(e,filepath))
        return None

def convertor(data):
    for k,v in data.items():
        data[k][0]=markdown.markdown(v[0], extensions=["fenced_code"])
        if len(v)>1:
            #remove tags that are unwanted
            start="^<%s>|\n"%v[1]
            data[k][0]=re.sub(start, "", data[k][0])
            end="\n|</%s>$"%v[1]
            data[k][0]=re.sub(end, "", data[k][0])
    return data

def merger(filename,template,data):
    html=template
    for k,v in data.items():
        parsekey="<!--#%s#-->"%k
        if parsekey in template:
            html=re.sub(parsekey,v[0], html)
    with codecs.open(filename, 'w', encoding="utf-8") as f:
        print(html,file=f)
        print("%s is written."%filename)
