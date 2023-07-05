#include <iostream>
#include <cstring>
#include"calc.h"
using namespace std;

int main()
{
    char *s = new char[20000];
    cin >> s;
    bool out = true;
    if(*s=='t') {cout<<out;return 1;}
    if(*s=='f') {cout<<!out;return 0;}    
    int length = strlen(s);
    int array[20000] = {0};
    linkedstack<char> calc;
    linkedstack<char> signal;
    int time = 0;
    int signalnum = 0;

    while (time++ < length)
    {
        switch (*s)
        {
        case 'f':
            calc.push('0');
            s++;
            break;
        case 't':
            calc.push('1');
            s++;
            break;
        case ',':
            signal.push(',');
            s++;
            break;
        case '&':
            signal.push('&');
            s++;
            break;
        case '|':
            signal.push('|');
            s++;
            break;
        case '!':
            signal.push('!');
            s++;
            break;
        case '(':
            signal.push('(');
            s++;
            break;
        case ')':
        {
            signalnum++;

            while (true)
            {
                array[signalnum]++;
                if (signal.pop() == '(')
                    break;
            }
            calc.push(signal.pop());
            s++;
            break;
        }
        }
    }
    calc.daoxu();
    int ans = get(calc, array);
    if (ans == 1)
        {cout<<out;return 1;}
    else
        {cout<<!out; return 0;}
}