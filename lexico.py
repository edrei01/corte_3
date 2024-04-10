import ply.lex as lex
import tkinter as tk

def create_lexer(error_table):
    # Define reserved words
    reserved = {
    'pan':'PAN',
    'paraqoque':'PARAQOQUE',
    'agusticidad':'AGUSTICIDAD',
    'ububue':'UBUBUE',
    'vasir':'VASIR',
    'novasir':'NOVASIR',
    'vuelaoque':'VUELAOQUE',
    'siono':'SIONO',
    'contenido':'CONTENIDO'
    }

    tokens = [
        'DOUBLESTRING',
        'ID',
        'ENTERO',
        'LPAREN',
        'ID',
        'ASSIGN',
        'NUMBER',
        'SEMI',
        'GREATER',
        'INCREMENT',
        'RPAREN',
        'LBRACE',
        'RBRACE',
        'STRING',
        'MENOS',
        'MAS',
        'MULTI',
        'DIV',
        'IGUALMA',
        'IGUALMENO',
        'DOBLEIGUAL',
        'PUNTCOM',
        'MENOR',
        'DESIGUAL',
        'COMILLA'
    ] + list(reserved.values())

    t_DOUBLESTRING = r'"[^"]*"'
    t_LPAREN = r'\('
    t_ASSIGN = r'='
    t_GREATER = r'>'
    t_INCREMENT = r'\+\+'
    t_RPAREN = r'\)'
    t_LBRACE = r'{'
    t_RBRACE = r'}'
    t_MAS = r'\+'
    t_MENOS = r'-'
    t_MULTI = r'\*'
    t_DIV = r'\\'
    t_IGUALMA = r'>='
    t_IGUALMENO = r'<='
    t_DOBLEIGUAL = r'=='
    t_PUNTCOM = r';'
    t_MENOR = r'<'
    t_DESIGUAL = r'=!'
    t_COMILLA = r'"'    

    def t_ID(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reserved.get(t.value, 'ID')
        return t

    def t_NUMBER(t):
        r'\d+'
        t.value = int(t.value)
        return t

    t_ignore = ' \t\n'

    def t_error(t):
        error_table.insert(tk.END, f"Illegal character '{t.value[0]}'\n")
        t.lexer.skip(1)

    lexer = lex.lex()

    return lexer,tokens
