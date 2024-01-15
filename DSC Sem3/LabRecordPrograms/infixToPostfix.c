//Week 5 program 1
#include <stdio.h>
#define max_expr_size 100
char expr[max_expr_size];
typedef enum
{
    lparen,
    plus,
    minus,
    times,
    divide,
    mod,
    rparen,
    eos,
    operand
} precedence;
precedence stack[max_expr_size];
int top = -1;
//  isp (in-stack precedence) and icp (incoming precedence)
int isp[] = {0, 12, 12, 13, 13, 13, 19};
int icp[] = {20, 12, 12, 13, 13, 13, 19};
void push(precedence token)
{
    if (top >= max_expr_size - 1)
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
        return eos;
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
void printToken(precedence token)
{
    switch (token)
    {
    case plus:
        printf("+");
        break;
    case minus:
        printf("-");
        break;
    case times:
        printf("*");
        break;
    case divide:
        printf("/");
        break;
    case mod:
        printf("%%");
        break;
    default:
        printf("%c", operand);
    }
}
void postfix()
{
    char symbol;
    precedence token;
    int n = 0;
    stack[0] = eos;
    top = 0;
    for (token = getToken(&symbol, &n); token != eos; token = getToken(&symbol, &n))
    {
        if (token == operand)
            printf("%c", symbol);
        else if (token == rparen)
        {
            while (stack[top] != lparen)
                printToken(pop());
            pop();
        }
        else
        {
            while (isp[stack[top]] >= icp[token])
                printToken(pop());
            push(token);
        }
    }
    while ((token = pop()) != eos)
        printToken(token);
    printf("\n");
}
int main()
{
    printf("Enter the infix expression: ");
    scanf("%s", expr);
    printf("The postfix expression: ");
    postfix();
    return 0;
}