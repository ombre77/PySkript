# this file contain the lines list so it can be access everywhere in the code

Lines=[]

Indent=0

def write(line:str):
    Lines.append(("    "*Indent)+line)