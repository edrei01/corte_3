import ply.yacc as yacc
import tkinter as tk

def create_parser(error_table, resust_table, tokens):
    global variableelse
    global operado1
    global numeroIF
    global valor
    global numberFun
    numberFun = None
    def p_init(p):
        '''init : program
                | opcion2
                | opcion3
                | opcion4
                | ububuefun'''

    def p_opcion2(p):
        '''opcion2 : AGUSTICIDAD UBUBUE ID ASSIGN ID
                    | AGUSTICIDAD PAN ID ASSIGN NUMBER'''
        global variableelse
        global valor
        global typevar
        typevar=p[2]
        variableelse = p[5]
        valor = p[3]
        iden=p[5]
        if isinstance(iden, int) and p[2]=="pan":
            resust_table.insert(tk.END, f"Variable declarada '{valor}' con valor '{iden}'\n")
        elif isinstance(iden, str) and p[2]=="ububue":
            resust_table.insert(tk.END, f"Variable declarada '{valor}' con valor '{iden}'\n")
        else:
            resust_table.insert(tk.END, f"sintasis de variable mal '{valor}' con valor '{iden}'\n")
    def p_var(p):
        '''var : AGUSTICIDAD PAN ID ASSIGN NUMBER'''
        global variablef
        global valor3
        
        variablef = p[5]
        valor3 = p[3]
        resust_table.insert(tk.END, f"Variable declarada '{valor3}' con valor '{variablef}'\n")
        
    def p_opcion3(p):
        '''opcion3 : opcion2 VASIR LPAREN ID operador ident RPAREN LBRACE cualquierIF RBRACE NOVASIR LBRACE cualquierELSE RBRACE'''  
        global operado1
        global valor01
        global var
        var=p[4]
        varnumero=p[6]
        print("soy operador", operado1)
        
        # Definir un diccionario que mapea operadores a funciones o condiciones
        operadores_diccionario = {
            '>': lambda x, y: x > y,
            '<': lambda x, y: x < y,
            '=': lambda x, y: x == y,
            # Agrega más operadores según sea necesario
        }
        if valor!=p[4]:
             error_table.insert(tk.END, f"variable utilzada no difinida'{var}'\n")
        else:
            print("misdo codision XD ", variableelse)
            print("misdo codision XD2222 ", numeroIF)
        #Convertir los valores a números
            try:
                num_variable = int(variableelse)
                num_numeroIF = int(numeroIF)
            
            except ValueError:
                print("Error: Los valores no son números enteros")
                return

     #    Obtener la función correspondiente al operador
            funcion_condicional = operadores_diccionario.get(operado1)
            print("misdo codision XD ", variableelse)
            print("misdo codision XD2222 ", numeroIF)

            if funcion_condicional is not None:
                if funcion_condicional(num_variable, num_numeroIF): 
                    resust_table.insert(tk.END, f"resultado vasir '{valor02}'\n")
                else:
                    print("else ", p[12])
                    resust_table.insert(tk.END, f"resultado novasir '{valor03}'\n")
            else:
                print("Operador no válido:", operado1)


    def p_opcion4(p):
        '''opcion4 : VUELAOQUE ID LPAREN PAN ID RPAREN LBRACE opcion2 var ID ASSIGN ID MAS ID RBRACE'''
        #  | VUELAOQUE ID LPAREN UBUBUE ID RPAREN LBRACE cualquierFun RBRACE
        
        print('hola desde fun',typevar)
        print(variablef,"valor3")
        print(variableelse, "numif")
        try:
                num_variable1 = int(variablef)
                num_numeroIF = int(variableelse)
        except ValueError:
                print("Error: Los valores no son números enteros")
                return
        print("numberFun des de",numberFun)
        if typevar== "pan" and p[12]==valor and p[14]==valor3 and valor!=valor3 and p[5]==p[10] :   
                   suma= num_variable1 + num_numeroIF
                   resust_table.insert(tk.END, f"resultado '{suma}'\n")
        else:
             error_table.insert(tk.END, f"Error, variables utilizadas no declaradas\n")
    def p_ububuefun(p):
        '''ububuefun : VUELAOQUE ID LPAREN UBUBUE ID RPAREN LBRACE ID ASSIGN ID RBRACE'''
        if p[5]==p[8]:
            resust_table.insert(tk.END, f"La variable dio como resultado '{p[10]}'\n") 
        else:
            error_table.insert(tk.END, f"Error,variable no defida\n")
              
    def p_program(p):
        '''program : PARAQOQUE LPAREN variable ID ASSIGN NUMBER PUNTCOM ID operador NUMBER PUNTCOM ID INCREMENT PUNTCOM RPAREN LBRACE cualquier RBRACE'''
        global user_value
        global user_value2
        global number2
        user_value = p[6]
        user_value2 = p[10]
        print("user value", user_value)
        print("user value2", user_value2)
        number2 = user_value2 - user_value
        print(varfor, "hola soy p3")
        if varfor== "pan" and p[4]==p[8]: 
            for _ in range(number2):
                resust_table.insert(tk.END, f"resultado '{valor01}'\n")
        else:
            error_table.insert(tk.END, f"Error detectado\n")
          
    def p_variable(p):
        '''variable : UBUBUE
                    | PAN'''
        global varfor
        varfor=p[1]

    def p_cualquier(p):
        '''cualquier : CONTENIDO
                     | ID'''
        global valor01
        valor01 = p[1]
    def p_cualquierIF(p):
        '''cualquierIF : CONTENIDO
                     | ID'''
        global valor02
        valor02 = p[1]
        
    def p_cualquierELSE(p):
        '''cualquierELSE : CONTENIDO
                     | ID'''
        global valor03
        valor03 = p[1]
   
    def p_operador(p):
        '''operador : GREATER
                    | IGUALMA
                    | IGUALMENO
                    | DOBLEIGUAL
                    | MENOR
                    | DESIGUAL
                    | ASSIGN'''
        global operado1
        operado1 = p[1]

    def p_ident(p):
        '''ident : ID  
                 | NUMBER'''  
        global numeroIF
        numeroIF = p[1]          

    def p_error(p):
        if p:
            error_table.insert(tk.END, f"Syntax error in token '{p.value}'\n")
        else:
            error_table.insert(tk.END, "Syntax error in EOF\n")

    parser = yacc.yacc()

    return parser
