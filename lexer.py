from rply import LexerGenerator


class Lexer():

    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Keywords
        self.lexer.add('PRINT', r'print')
        self.lexer.add('IF', r'if')
        self.lexer.add('ELSE', 'else')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Colon
        self.lexer.add('COLON', r'\:')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'/')
        self.lexer.add('MORE', r'\>')
        self.lexer.add('LESS', r'\<')
        self.lexer.add('EQUALS', r'\=')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # String
        self.lexer.add('ID', r'\w+')
        # Ignore spaces
        self.lexer.ignore(r'\s+') 

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()