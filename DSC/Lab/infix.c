#include <stdio.h>
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

int isp[] = {0, 19, 12, 12, 13, 13, 13, 0};
int icp[] = {20, 19, 12, 12, 13, 13, 13, 0};
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
    while ((stack[top]) != eos)
        printToken(pop());
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