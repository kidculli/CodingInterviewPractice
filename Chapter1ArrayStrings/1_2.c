#include <stdio.h>
#include <stdlib.h>
char* ReverseString(char* s){
  int index = 0;
  do {
index ++; 
  }
  while(s[index] != '\0');
  int reverseIt = 0; 
  char* reversed = (char*) malloc(sizeof(char)*index); 
  for(int i = index; i > -1; i--) {
    //printf("%c",s[i]); 
    reversed[reverseIt] = s[i];
    reverseIt ++ ; 
    }
  reversed[reverseIt] = '\0'; 
  return reversed; 
}

int main(int argc, char** argv)
{
  char a[] = "cullin";   
  char* reversed = ReverseString(a);
  printf("\n **************** \n %s \n",reversed); 
}
 