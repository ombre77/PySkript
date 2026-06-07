# class for generating event code

import ast
import lines as lines
from lines import Lines,write

class Event:
    def __init__(self, node: ast.AST):
        self.node = node
        self.funcs = []

    def add(self, func, *args):
        self.funcs.append((func, args))

    def generate(self,header:str):
        write(header)

        old_indent = lines.Indent
        lines.Indent += 1

        for func, args in self.funcs:
            func(*args)

        lines.Indent = old_indent