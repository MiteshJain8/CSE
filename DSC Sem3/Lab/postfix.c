#include <stdio.h>
#include <stdlib.h>
#define MAX 100
char expr[MAX];
typedef enum
{
    lparen,
    rparen,
    plus,
    minus,
    times,
    divide,
    mod,
    eos,
    operand
} precedence;
precedence stack[MAX];
int top = -1;
void push(precedence token)
{
    if (top >= MAX - 1)
    {
        printf("Stack full");
        return;
    }
    stack[++top] = token;
}
precedence pop()
{
    if (top <= -1)
    {
        printf("Stack empty");
        exit(0);
    }
    return stack[top--];
}
precedence getToken(char *symbol, int *n)
{
    *symbol = expr[(*n)++];
    switch (*symbol)
    {
    case '(':
        return lparen;
    case ')':
        return rparen;
    case '*':
        return times;
    case '/':
        return divide;
    case '-':
        return minus;
    case '+':
        return plus;
    case '%':
        return mod;
    case '\0':
        return eos;
    default:
        return operand;
    }
}

int eval()
{
    precedence token;
    char symbol;
    int op1, op2;
    int n = 0;
    for(token=getToken(&symbol, &n); token!=eos; token=getToken(&symbol, &n))
    {
        if (token == operand)
            push(symbol - '0');
        else
        {
            op2 = pop();
            op1 = pop();
            switch (token)
            {
            case plus:
                push(op1 + op2);
                break;
            case minus:
                push(op1 - op2);
                break;
            case times:
                push(op1 * op2);
                break;
            case divide:
                push(op1 / op2);
                break;
            case mod:
                push(op1 % op2);
                break;
            default:
                printf("Invalid token\n");
            }
        }
    }
    return pop();
}
int main()
{
    printf("Enter the postfix expression: ");
    scanf("%s", expr);
    printf("Answer: %d\n", eval());
    return 0;
}