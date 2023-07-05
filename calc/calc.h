#include <iostream>
#include<cstdbool>
using namespace std;
template <class T>
class stack
{
public:
    virtual bool isempty() const = 0;
    virtual void push(const T &x) = 0;
    virtual T pop() = 0;
    virtual T top() const = 0;
    virtual ~stack() {}
};
template <class T>
class seqstack : public stack<T>
{        // 顺序栈和初始抽象类差不多；不同点主要在私有成员，以及私有成员的实现
private: // 私有包括栈顶指示，数据指针，最大空间和扩容函数
    T *t;
    int top_p = -1; // 栈顶的位置,初始时刻栈内无元素，故栈内元素首地址为-1
    int maxsize;    // 表示最大空间
    void doublespace();

public:
    seqstack(int initsize = 200000); // 开一个10单位的空间
    ~seqstack();
    bool isempty() const;
    T pop();
    T top() const;
    void push(const T &x);
    void diaoxu()
    {
        T *w = new T[20000];
        for (int i = 0; i <= top_p; i++)
        {
            w[i] = t[i];
        }
        for (int i = 0; i <= top_p; i++)
        {
            t[i] = w[top_p - i];
        } // 调换顺序
    }
};
template <class T>
void seqstack<T>::push(const T &x)
{
    if (top_p == maxsize)
        doublespace();
    t[++top_p] = x;
}
template <class T>
T seqstack<T>::top() const { return t[top_p]; }
template <class T>
bool seqstack<T>::isempty() const { return (top_p == -1) ? 1 : 0; }
template <class T>
T seqstack<T>::pop() { return t[top_p--]; }
template <class T>
seqstack<T>::seqstack(int initsize)
{
    t = new T[initsize]; // 构造函数的实现时，参数列表中不能有常数
    maxsize = initsize;
    top_p = -1;
}
template <class T>
seqstack<T>::~seqstack() { delete[] t; }
template <class T>
void seqstack<T>::doublespace()
{
    T *tmp = t;
    t = new T[2 * maxsize];
    for (int i = 0; i < maxsize; i++)
        t[i] = tmp[i];
    maxsize *= 2;
    delete[] tmp;
}
int get(seqstack<char> &op,seqstack<char> &tmpt, int array[])
{
    int value=0;
    char a;
    int k = 1;
    while (true)
    {   
        while (true)
        {
            int j = 0;
            a = op.pop();
            if (op.isempty()&&(a=='0'||a=='1'))
            {
                return a-'0';
            }
            if (a == '&' || a == '!' || a == '|')
            {   while(j++<array[k]){
                value+=(tmpt.pop()-'0');
            }
                break;
            }
            tmpt.push(a);
        }
        switch (a)
        {
        case '&':
            value = (value == array[k]) ? 1 : 0;
            break;
        case '|':
            value = (value == 0) ? 0 : 1;
            break;
        case '!':
            value = (value == 1) ? 0 : 1;
            break;
        }
        op.push(value + '0');
        value = 0;
        while(!tmpt.isempty())
        {op.push(tmpt.pop());}
        k++;
    }
}
