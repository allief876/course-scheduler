#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstring>
using namespace std;

int main() {
    int i = 0;
    int j = 0;
    fstream file;
    string buf;
    string *buff;
    file.open("matkul.txt",ios::in);
    while (getline(file,buf)) {
        cout << buf << endl;
        //strcpy(buff[i],buf);
        //i++;
    }
    /*for (j = 0; j <= i; j++) {
        cout << buff[i] << endl;
    }*/
    file.close();
    return 0;
}