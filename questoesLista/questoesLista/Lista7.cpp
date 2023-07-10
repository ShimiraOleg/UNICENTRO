#include <iostream>

using namespace std;

int main() {

    int A, B, C, D , AAB, AAC, AAD, ABC, ABD, ACD, MAB, MAC, MAD, MBC, MBD, MCD;

    cin >> A >> B >> C >> D;
    
    AAB = A + B;
    AAC = A + C;
    AAD = A + D;
    ABC = B + C;
    ABD = B + D;
    ACD = C + D;
    
    MAB = A * B;
    MAC = A * C;
    MAD = A * D;
    MBC = B * C;
    MBD = B * D;
    MCD = C * D;

    cout << "ADICOES: "<< endl << "A + B = " << AAB << endl << "A + C = " << AAC << endl << "A + D = " << AAD << endl <<  "B + C = " << ABC << endl <<  "B + D = " << ABD << endl <<  "C + D = " << ACD << endl;
    cout << "MULTIPLICACOES: "<< endl << "A * B = " << MAB << endl << "A * C = " << MAC << endl << "A * D = " << MAD << endl <<  "B * C = " << MBC << endl <<  "B * D = " << MBD << endl <<  "C * D = " << MCD << endl;
    
    return 0;
}