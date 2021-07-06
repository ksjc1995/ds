#include<iostream>
using namespace std;

/*
* Stack is a linear DS which follows a particular order of operations.
* It may be LIFO (Last In First Out) or FIFO (First In First Out)
* 
* It usually has these basic operations:-
*   1) Push -> Add item in the stack
*   2) Pop -> Remove item from the stack
*   3) isEmpty -> Check whether stack is empty
*   4) peek or top -> To get top element of the stack
*
*  Examples:- Backtracking, Memory management, Expression evaluation, etc (http://jcsites.juniata.edu/faculty/rhodes/cs240/stackapps.htm) 


*//**
* Stack implementation using array
*/

#define MAX 1
#define UNDERFLOW "UNDERFLOW"
#define OVERFLOW "OVERFLOW"
#define EMPTY "EMPTY"

class Stack {
    public: 
        int stack[MAX];

        int top = -1;

    public: bool is_empty() {
        if(top == -1){
            return true;
        }
        return false;
    }

    public: int peek(){
        if(is_empty()){
            cout << UNDERFLOW << "\n";
            return -1;
        }
        return stack[top];
    }

    public: int push(int element){
        if(top >= MAX - 1){
            cout << OVERFLOW << "\n";
            return -1;
        }
        stack[++top] = element;
        return top;
    }

    public: int pop(){
        if(is_empty()){
            cout << UNDERFLOW << "\n";
            return -1;
        }
        return stack[top--];
    }

    public: int get_size(){
        return top;
    }

    public: void print(){
        cout << "Stack: \t";
        cout << "Size: " << sizeof(stack)/sizeof(stack[0]) << "\n";
        for(int i = top; i >=0; i--){
            cout << stack[i] << "\n";
        }
    }
};

int main() {
    Stack s;
    s.push(1);
    s.push(2); // overflow

    s.print();

    s.pop(); 
    s.pop(); // underflow


    cout << s.get_size();  // -1
    cout << s.is_empty();  // 1
}