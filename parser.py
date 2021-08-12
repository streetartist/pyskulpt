from sly import Parser as SlyParser
from .lexer import Lexer

class Parser(SlyParser):
    debugfile = 'logs/parser.out'
    tokens = Lexer.tokens

    @_('empty')
    def program(self, p):
        return ()

    # Statement gatherer ruleset

    @_('statements')
    def program(self, p):
        return p.statements

    @_('statement')
    def statements(self, p):
        return (p.statement, )

    @_('statements statement')
    # Function args ruleset

    @_('expr')
    def arg(self, p):
        return p.expr

    @_('arg')
    def args(self, p):
        return [p.arg]

    @_('args "," arg')
    def args(self, p):
        return p.args + [p.arg]

    @_('empty')
    def args(self, p):
        return []

    # Hold identifier precedence higher 
    @_('ID')
    def expr(self, p):
        return ('id', p.ID)

    # Function declaration

    @_('FN "(" params ")" block')
    def function_definition(self, p):
        return ('fn', ('params', p.params), ('block', p.block))
    
    @_('"(" params ")" => block')
    def function_definition(self, p):
        return ('fn', ('params', p.params), ('block', p.block))

    # Function params ruleset

    @_('params "," param')
    def params(self, p):
        return p.params + [p.param]

    @_('param')
    def params(self, p):
        return [p.param]

    @_('empty')
    def params(self, p):
        return []

    @_('data_type ID')
    def param(self, p):
        return (p.ID, p.data_type)


    @_('ANY')
    def expr(self, p):
        return None

    @_('')
    def empty(self, p):
        pass

    @_('"{" program "}"')
    def block(self, p):
        return p.program

    @_('statement')
    def block(self, p):
        return (p.statement,)
