class Token:
    """
        Token has a type and value. 
    """
    INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({}, {})'.format(self.type, repr(self.value))

    def __repr__(self):
        return str(self)


class InvalidExpression(Exception):
    pass

class InvalidToken(Exception):
    pass

class Interpreter:
    """
        Interpreter has:
            1. Lexical Analyzer(Lexer) that parses the expression and get the 
               tokens to evaluate
            2. Evaluator that evaluates the expression passed to the Interpreter.
            3. A consumer that consumes the tokens and returns the next token with
               talking to Lexer
    """
    def __init__(self, expr):
        self.expr = expr
        self._pos = 0
        self.currentToken = None

    def _eat(self, tokenType):
        if self.currentToken.type == tokenType:
            self.currentToken = self.getNextToken()
        else:
            raise InvalidToken

    def getNextToken(self):
        if self._pos > len(self.expr)-1:
            return Token(type=Token.EOF, value=None)
        
        t = self.expr[self._pos]

        if t.isdigit():
            self._pos += 1
            return Token(type=Token.INTEGER, value=int(t))
        elif t == '+':
            self._pos += 1
            return Token(type=Token.PLUS, value=t)
        elif t == '-':
            self._pos += 1
            return Token(type=Token.MINUS, value=t)

        raise InvalidToken

    def eval(self):
        self.currentToken = self.getNextToken()

        leftOperand = self.currentToken
        self._eat(Token.INTEGER)

        operator = self.currentToken
        if operator.type == Token.PLUS:
            self._eat(Token.PLUS)
        if operator.type == Token.MINUS:
            self._eat(Token.MINUS)

        rightOperand = self.currentToken
        self._eat(Token.INTEGER)

        print(operator)
        if operator.type == Token.PLUS:
            return leftOperand.value + rightOperand.value
        if operator.type == Token.MINUS:
            return leftOperand.value - rightOperand.value

        raise InvalidExpression
