#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    float votoA, votoB, votoC, votoN, votoBr, totalVotos, porcentoVotosA, porcentoVotosB, porcentoVotosC, porcentoVotosN, porcentoVotosBr;

    cin >> votoA >> votoB >> votoC >> votoN >> votoBr;

    totalVotos = votoA + votoB + votoC + votoN + votoBr;
    
    porcentoVotosA = (votoA*100.0f)/totalVotos;
    porcentoVotosB = (votoB*100.0f)/totalVotos;
    porcentoVotosC = (votoC*100.0f)/totalVotos;
    porcentoVotosN = (votoN*100.0f)/totalVotos;
    porcentoVotosBr = (votoBr*100.0f)/totalVotos;

    cout << "Quantidade total de votos: " << totalVotos << endl;
    cout << fixed << setprecision(2) << "Porcentagem de votos para o canditado A: " << porcentoVotosA << "%" << endl;
    cout << fixed << setprecision(2) << "Porcentagem de votos para o canditado B: " << porcentoVotosB << "%" << endl;
    cout << fixed << setprecision(2) << "Porcentagem de votos para o canditado C: " << porcentoVotosC << "%" << endl;
    cout << fixed << setprecision(2) << "Porcentagem de votos nulos: " << porcentoVotosN << "%" << endl;
    cout << fixed << setprecision(2) << "Porcentagem de votos brancos: " << porcentoVotosBr << "%" << endl;

    return 0;

}