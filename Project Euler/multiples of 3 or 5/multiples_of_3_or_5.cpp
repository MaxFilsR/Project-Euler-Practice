#include <iostream>

bool multipleOf3Or5(int num){
    if(num % 3 == 0 || num % 5 == 0){
        return true;
    }else{
        return false;
    }
}

int main(){
    int sum{0};

    for(int i = 999; i > 0; i--){
        if(multipleOf3Or5(i)){
            sum +=i;
        }
    }
    std::cout<<sum;
}