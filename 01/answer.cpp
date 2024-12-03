#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int str_to_num(char *str){
  int result, puiss;
  result = 0;
  puiss = 1;

  while (('-' == (*str)) || ((*str) == '+')){
    if (*str == '-'){
      puiss = puiss * -1;
    }
    str++;
  }
  while ((*str >= '0') && (*str <= '9')){
    result = (result * 10) + ((*str) - '0');
    str++;
  }
  return (result * puiss);
}

char* str_to_char(string str){
  int n = str.length();
  char* arr = malloc(n * sizeof(char));

  // Null terminate char array
  arr[n] = '\0';

  for (int i = 0; i<n;i++){
    arr[i] = str[i];
  }

  return arr;
}

int main (int argc, char *argv[]) {
  string line, fiStr, seStr;
  ifstream myfile ("input");
  int fiNum, seNum;
  if (myfile.is_open()){
    while ( getline(myfile, line) ){
      fiStr = line.substr(0, 5);
      fiNum = str_to_num(str_to_char(fiStr));
      seStr = line.substr(8,5);
      seNum = str_to_num(str_to_char(seStr));
      cout << "First Num: "<< fiStr << ", Second Num: " << seStr << ", total = " << fiNum + seNum << "\n";
    }
  }
  else{
    cout << "Unable to open file";
  }

  return 0;
}
