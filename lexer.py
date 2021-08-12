from sly import Lexer as SlyLexer

class Lexer(SlyLexer):
    tokens = {ID,STRING, ANY}

    ignore = ' \t'
    ignore_comment_slash = r'//.*'

    literals = {'(', ')', ',', '{', '}',
                }

    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['function'] = FN
    
    ANY = r'([\s\S]*)'
    
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    def remove_quotes(self, text: str):
        if text.startswith('\"') or text.startswith('\''):
            return text[1:-1]
        return text

    @_(r'''("[^"\\]*(\\.[^"\\]*)*"|'[^'\\]*(\\.[^'\\]*)*')''')
    def STRING(self, t):
        t.value = self.remove_quotes(t.value)
        chars = ((r'\n', '\n'), (r'\t', '\t'), (r'\\', '\\'),
                 (r'\"', '\"'), (r'\'', '\''), (r'\a', '\a'),
                 (r'\b', '\b'), (r'\r', '\r'), (r'\v', '\v'))
        for pair in chars:
            t.value = t.value.replace(*pair)
        return t
