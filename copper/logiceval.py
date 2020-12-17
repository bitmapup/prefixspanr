# -*- coding: utf-8 -*-

"""
Module for the Logical evaluation functionality of COPPER
using ShuntingYard to Postfix notation and an evaluation tree to finally
obtain a function that takes a pattern and returns if it fulfills the logical
condition given on the generating options.
"""

from seqpattern import Pattern


def evaluator(logical_expression):
    """
    Evaluate logical expression.

    Parameters
    ----------
    logical_expression : string
        Logical expression to evaluate

    Returns
    -------
    bool
        Logical Expression Value

    """
    tokenized_expression = filter(lambda x: x, logical_expression.replace(' ', '')
                                  .replace('&', "\0&\0")
                                  .replace(')', "\0)\0")
                                  .replace('(', "\0(\0")
                                  .replace('|', "\0|\0")
                                  .split("\0"))
    eval_tree = postfixtotree(shuntingyard(tokenized_expression))

    return lambda x: eval_tree.evaluate(x)


def shuntingyard(token_chain):
    """
    Convert Infix Notation to Postfix Notation using Shunting Yard Algorithm.

    Parameters
    ----------
    token_chain : string
        token string to analyze

    Returns
    -------
    list
        Queue Char in Postfix Order

    """
    stack = []
    queue = []
    for token in token_chain:
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
                popped = stack.pop()
        else:
            queue.append(token)

    while stack:
        queue.append(stack.pop())

    return queue


def postfixtotree(postfix_chain):
    """
    Populate Evaluation Tree with List in Postfix Notation

    Parameters
    ----------
    postfix_chain : string
        postfix String used to populate a tree

    Returns
    -------
    Tree List
        List of tree leaves

    """
    stack = []
    for token in postfix_chain:
        if token == "&" or token == "|":
            e1 = stack.pop()
            e2 = stack.pop()
            t = Tree(token, e1, e2)
            stack.append(t)
        else:
            stack.append(Tree(token))

    return stack.pop()


def dictionaryeval(dictionary, token):
    """
    Evaluate if a token is in a dictionary

    Parameters
    ----------
    dictionary: dict

    token: string

    Returns
    -------
    bool
    """
    return token in dictionary


class Tree:
    """
    Abstract Syntax Tree
    """

    def __init__(self, root, left_leaf=None, read_leaf=None):
        """
        Constructor of class Tree

        Extended description of function.

        Parameters
        ----------
        root: Tree
            root node of tree
        left_leaf: Tree
            left node of tree
        read_leaf: Tree
            right node of tree

        Returns
        -------
        None
        """
        self.root = root
        self.left = left_leaf
        self.right = read_leaf

    def evaluate(self, dictionary):
        """
        Evaluate tree in semantic way.

        Parameters
        ----------
        dictionary: string
            token string to analyze

        Returns
        -------
        Boolean
            Logical Expression Value

        """
        if type(dictionary) == Pattern:
            if ',' in str(dictionary):
                dictionary = str(dictionary).replace('<', '').replace('>', '').split(', ')
            else:
                dictionary = str(dictionary).replace('><', ',').replace('<', '').replace('>', '').split(',')

        if self.left:
            left = self.left.evaluate(dictionary)
        else:
            return dictionaryeval(dictionary, self.root)

        if self.right:
            right = self.right.evaluate(dictionary)

        if left:
            if self.root == '¬':
                return not left

        if right:
            if self.root == '¬':
                return not right

        if left and right:
            if self.root == '&':
                return left and right
            if self.root == '|':
                return left or right

    def __nonzero__(self):
        """
        Evaluate if tree is empty.

        Parameters
        ----------

        Returns
        -------
        Boolean
            Logical Expression Value

        """
        return bool(self.root)

    def show(self):
        """
        Show tree in a string

        Parameters
        ----------


        Returns
        -------
        String
            Leaf String Value

        """
        if self.left:
            return '(' + self.left.show() + str(self.root) + self.right.show() + ')'
        else:
            return self.root
