#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>

using namespace std;
int getrandomdigit();

int main()
{
    srand(time(NULL));
    string input;
    int digit1_1;
    int digit1_2;
    int digit1_3;
    int digit1_4;

    int digit2_1;
    int digit2_2;
    int digit2_3;
    int digit2_4;
    int digit2_5;
    int digit2_6;
    int digit2_7;

    cout << "Enter four digits(area code): ";
    getline(cin, input);
    cout << "\n";
    cout << "\tAvailable numbers in your area.";
    cout << "\n\t******************************";

    cout << "\n\n";

    for(int i = 0; i < 10; ++i)
        cout << "\nPhone number: " << input  << getrandomdigit() << getrandomdigit()
        << getrandomdigit() << getrandomdigit()
        << getrandomdigit() << getrandomdigit() << getrandomdigit();

    cout<<"\n";
    return 0;

}

int getrandomdigit()
{
    return rand() % 10;
}
