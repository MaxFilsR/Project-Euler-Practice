#include <iostream>


int main(){
    int one{0};
    int two{1};
    int sum;
    int evensums{0};

    for(int i = 0; i <4000000; i++){
        sum = one +two;
        one = two;
        two = sum;
        if(sum>4000000){
            break;
        }
        if(sum % 2 == 0){
            evensums+=sum;
        }
    }
    std::cout<<"\n"<<evensums;
}