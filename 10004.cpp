#include <iostream>
using namespace std;
    class Avltree
    {
        struct binarynode
        {
            int data;
            binarynode *left,*right;
            int height;
            binarynode (const int &x, binarynode *lt=NULL,binarynode *rt= NULL,int h=1):data(x),left(lt),right(rt),height(h) {}

        };
        void makeempty(binarynode *t)
        {
            if (t == NULL)
                return;
            makeempty(t->left);
            makeempty(t->right);
            delete t;
        }
    public:
        binarynode *root;
        Avltree (){root = NULL;}
        ~Avltree(){ makeempty (root);}
        int height(binarynode *t) const { return (t == NULL) ? 0 : t->height; }
        int max(int a, int b) { return (a > b) ? a : b; }
        void LL(binarynode *&t)
        {
            binarynode *tmp = t->left;
            t->left = tmp->right;
            tmp->right = t; // 改变构造
            t->height = max(height(t->left), height(t->right)) + 1;
            tmp->height = max(height(tmp->left), height(t)) + 1;
            t = tmp;
        }
        void RR(binarynode *&t)
        {
            binarynode *tmp = t->right;
            t->right = tmp->left;
            tmp->left = t;
            t->height = max(height(t->left), height(t->right)) + 1;
            tmp->height = max(height(tmp->right), height(t)) + 1;
            t = tmp;
        }
        void LR(binarynode *&t)
        {
            RR(t->left);
            LL(t);
        }
        void RL(binarynode *&t)
        {
            LL(t->right);
            RR(t);
        }
        void find(const int &x, binarynode *t, int &total, int num = 1)
        {
            if(t->data ==x) 
            {total +=num;return;}
            if(x< t ->data &&t->left!=NULL)
             {
                find(x,t->left,total,num+1);
            }
            if(x > t->data && t->right != NULL){
                find(x,t->right,total,num+1);
            }
            return;
        }
        void insert(const int &x,binarynode *&t)
        {            if (t == NULL)
            {
                t = new binarynode(x, NULL, NULL);
            }
            else {if (x < t->data)
            {
                insert(x, t->left);
                if (height(t->left) - height(t->right) == 2)
                {                                  // 若高度不一，则说明失衡；需要调整
                    if (x < t->left->data) // 判断是在左树的左子还是右子
                        // 左子则LL；右子则LR
                        LL(t);
                    else
                        LR(t);}}
            else {if (x>t->data)    
                    {   insert(x,t->right);
                    if (height(t->right) - height(t->left) == 2)
                        {
                        if (x < t->right->data)
                            RL(t);
                        else
                            RR(t);
                        }
                    }
            }
                t->height = max(height(t->left),height(t->right)) + 1;
        }
        }
    };
     
int main(){
    int array[20000];
    int i=0;
    Avltree tree;
    while(cin>>array[i++]){
            tree.insert(array[i-1], tree.root);
            if (cin.get() == '\n')
                break;
    }
    int j=0;
    int total;
    while(j++<i){ tree.find(array[j-1],tree.root,total,1);}
    cout<<total/i;
    return 0;
}