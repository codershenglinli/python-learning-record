#include <iostream>
#include <cstring>
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
class linkedstack : public stack<T>
{
    struct node
    {
        T data;
        node *next;
        node(const T &x, node *N = NULL)
        {
            data = x;
            next = N;
        };
        ~node(){delete node;}
        node() : next(NULL){};
    };
    node *top_p = NULL; 
public:
    linkedstack();
    ~linkedstack();
    bool isempty() const;
    void push(const T &x);
    T pop();
    T top() const;
    void daoxu();
    
};
template <class T>
linkedstack<T>::linkedstack() { top_p = NULL; } 
template <class T>
linkedstack<T>::~linkedstack()
{
    node *tmp;
    for (; top_p != NULL;)
    {
        tmp = top_p;
        top_p = top_p->next;
        delete tmp;
    }
}
template <class T>
bool linkedstack<T>::isempty() const { return top_p == NULL; }
template <class T>
void linkedstack<T>::push(const T &x) { top_p = new node(x, top_p); }
template <class T>
T linkedstack<T>::pop()
{
    node *tmp = top_p;
    T n = tmp->data;
    top_p = top_p->next;
    delete tmp;
    return n;
}
template <class T>
T linkedstack<T>::top() const { return top_p->data; }
template <class T>
void linkedstack<T>::daoxu()
{
    T *k = new T[20000];
    int m = 0;
    while (!isempty())
    {
        k[m] = this->pop();
        m++;
    }
    int i = 0;
    while (k[i++]!='\0')
    {
        this->push(k[i - 1]);
    }
}
int get(linkedstack<char> &op, int array[])
{
    int value;
    char a;
    int k = 1;
    while (true)
    {
        while (true)
        {
            a = op.pop();
            if (a == 0)
            {
                return value;
            }
            if (a == '&' || a == '!' || a == '|')
            {
                break;
            }
            value += a - '0';
        }
        switch (a)
        {
        case '&':
            value = (value == array[k++]) ? 1 : 0;
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
    }
}
