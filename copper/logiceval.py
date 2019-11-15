# -*- coding: utf-8 -*-

"""
logicaleval.py: Module for the Logical evaluation functionality of COPPER using ShuntingYard to
Postfix notation and an evaluation tree to finally obtain a function that takes
a pattern and returns if it fulfills the logical condition given on the generating
options.

__author__ = "Agustin Guevara Cogorno"
__copyright__ = "Copyright 2015, Copper Package"
__license__ = "GPL"
__maintainer__ = "Yoshitomi Eduardo Maehara Aliaga"
__credits__ = ["Agustin Guevara Cogorno", "Yoshitomi Eduardo Maehara Aliaga"]
__email__ = "ye.maeharaa@up.edu.pe"
__institution_ = "Universidad del Pacifico|University of the Pacific"
__version__ = "1.1"
__status__ = "Proof of Concept (POC)"
"""

def evaluator(logicalExpresion):
    """
    Evaluate logical expression.

    Extended description of function.

    Parameters
    ----------
    logicalExpresion : string
        Logical expression to evaluate

    Returns
    -------
    Boolean
        Logical Expression Value

    """
    tokenizedExpression = filter(lambda x: x, logicalExpresion.replace(' ','')
                                                              .replace('&',"\0&\0")
                                                              .replace(')',"\0)\0")
                                                              .replace('(',"\0(\0")
                                                              .replace('|',"\0|\0")
                                                              .split("\0"))
    evalTree = posttotree(shuntingyard(tokenizedExpression))
    return lambda x: evalTree.evaluate(x)


def shuntingyard(tokenChain):
    """
    Convert Infix Notation to Postfix Notation.

    Extended description of function.

    Parameters
    ----------
    tokenChain : string
        token string to analyze

    Returns
    -------
    Char Queue
        Queue Char in Postfix Order

    """
    stack = []
    queue = []
    for token in tokenChain:
        if token == "&" or token == "|":
            while stack and (stack[-1] == "&" or stack[-1] == "|"):
                queue.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            popped = stack.pop()
            while popped != '(':
                queue.append(popped)
                #try:
                popped = stack.pop()
                #except:
                #    raise("Mismatched Parenthesis)
        else:
            queue.append(token)
    while stack:
        queue.append(stack.pop())
    return queue

def posttotree(postfixChain):
    """
    Populate Evaluation Tree with List in Postfix Notation

    Extended description of function.

    Parameters
    ----------
    postfixChain : string
        postfix String used to populate a tree

    Returns
    -------
    Tree List
        List of tree leaves

    """
    stack = []
    for token in postfixChain:
        if token == "&" or token == "|":
            e1 = stack.pop()
            e2 = stack.pop()
            t = Tree(token, e1, e2)
            stack.append(t)
        else:
            stack.append(Tree(token))
    return stack.pop()

def dictionaryeval(dictionary, token):
    return token in dictionary
'''    if ':' in token:
        var, val = token.split(':')
        return var in dictionary and val in dictionary[var]
    else:
        return token in dictionary'''

class Tree:
    """
    Abstract Syntax Tree
    """
    def __init__(self, root, lLeaf=None, rLeaf=None):
        self.root = root
        self.left = lLeaf
        self.right = rLeaf

    def evaluate(self, dictionary):
        """
        Evaluate tree in semantic way.

        Extended description of function.

        Parameters
        ----------
        tokenChain : string
            token string to analyze

        Returns
        -------
        Boolean
            Logical Expression Value

        """
        if self.left:
            l = self.left.evaluate()
        else:
            return dictionaryeval(dictionary, self.root)
        if self.right:
            r = self.right.evaluate()
        if l and r:
            #if token == '&':
            if self.root == '&':
                return l and r
            #if token == '|':
            if self.root == '|':
                return l or r

    def __nonzero__(self):
        """
        evaluate if tree is empty

        Extended description of function.

        Parameters
        ----------
        tokenChain : string
            token string to analyze

        Returns
        -------
        Boolean
            Logical Expression Value

        """
        return bool(self.root)

    def show(self):
        """
        show tree in a string
        
        Extended description of function.

        Parameters
        ----------
        

        Returns
        -------
        String
            Leaf String Value

        """
        if self.left:
            return '('+self.left.show()+str(self.root)+self.right.show()+')'
        else:
            return self.root
