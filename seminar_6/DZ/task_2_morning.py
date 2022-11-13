# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:* 
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример:*
# 1+2*3 => 7;
# (1+2)*3 => 9;

from operator import truediv, mul, add, sub  
from sympy import expand

operators = {'+': add, '-': sub, '*': mul, '/': truediv}

def calculate(expression):
    if '(' in expression:
            result = float(expand(expression))
            return result    
    else:        
        for i in expression:
            if expression.isdigit():
                return float(expression)
            for i in operators.keys():
                left, operator, right = expression.partition(i)
                if operator in operators:
                        result = operators[operator](calculate(left), calculate(right))
                        return result

try:
    expression = input("Введите арифметическое выражение в строку: ")
    string_expression = expression.replace(' ','')
    print(f'Ответ: {round(calculate(string_expression), 3)}')
except:
    print('Нужно вводить цифры и знаки арифметических операций!')
