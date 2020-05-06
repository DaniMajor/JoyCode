from rply import ParserGenerator
from syntaxtree import Number, Sum, Sub, Print, Mul, Div, ID, More, Less, If


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN', 'SEMI_COLON', 'SUM', 'SUB', 'MUL', 'DIV', 'ID', 'EQUALS', 'IF', 'MORE', 'LESS'], 
             precedence=[('left', ['SUM', 'SUB']), ('left', ['MUL', 'DIV'])]
        )

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return Print(p[2])

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        @self.pg.production('expression : expression MORE expression')
        @self.pg.production('expression : expression LESS expression')
        @self.pg.production('expression : ID EQUALS expression')
        @self.pg.production('expression : IF ID EQUALS expression SEMI_COLON expression SEMI_COLON expression')
        @self.pg.production('expression : IF ID MORE expression SEMI_COLON expression SEMI_COLON expression')
        @self.pg.production('expression : IF expression LESS expression SEMI_COLON expression SEMI_COLON expression')
        @self.pg.production('expression : IF expression EQUALS expression SEMI_COLON expression SEMI_COLON expression')
        @self.pg.production('expression : IF expression MORE expression SEMI_COLON expression SEMI_COLON expression')
        @self.pg.production('expression : IF expression LESS expression SEMI_COLON expression SEMI_COLON expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == 'MUL':
                return Mul(left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(left, right)
            elif operator.gettokentype() == 'MORE':
                return More(left,right)
            elif operator.gettokentype() == 'LESS':
                return Less(left,right)
            elif left.gettokentype() == 'ID':
                return ID(left, right)
            elif left.gettokentype() == 'IF':
                state = p[3]
                left = p[5]
                right = p[6]
                return If(state,left,right)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()