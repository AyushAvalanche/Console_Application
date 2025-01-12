#include <iostream>
#include <cstring> 
using namespace std;

class hit {
    private:
        int empnum;
        char name[50];
        char department[30];
        float salary;
        int workex;

    public:
        void read() {
            
            cin.ignore();
            cout << "Enter the name of the employee: ";
            cin.getline(name, 50); 

            cout << "Enter the department of the employee: ";
            cin.getline(department, 30);

            cout << "Enter the work experience (years): ";
            cin >> workex;

            
            if (workex < 2) 
            {
                salary = 30000; 
            } else if (workex >= 2 && workex <= 5) 
            {
                salary = 60000; 
            } else if (workex > 5 && workex <= 10) 
            {
                salary = 150000; 
            } else 
            {
                salary = 500000; 
            }
        }

        void condition() {
           
            cout << "\nEMPLOYEE NAME: " << name;
            cout << "\nDEPARTMENT: " << department;
            cout << "\nWORK EXPERIENCE: " << workex << " years";
            cout << "\nSALARY: ₹" << salary << "\n";

            // Code for salary classification
            if (salary < 50000) {
                cout << salary;
            } else if (salary >= 50000 && salary < 100000) 
            {
                cout << salary;
            } else if (salary >= 100000 && salary < 300000) 
            {
                cout << salary;
            } else if (salary >= 300000 && salary < 700000) 
            {
                cout <<salary;
            } else if (salary >= 700000 && salary < 1500000) 
            {
                cout <<salary;
            } else if (salary >= 1500000 && salary < 3000000) 
            {
                cout <<salary;
            } else if (salary >= 3000000 && salary < 5000000) 
            {
                cout << salary;
            } else if (salary >= 5000000 && salary < 10000000) 
            {
                cout <<salary;
            } else if (salary >= 10000000) {
                cout <<salary;
            }

           // Code for status according to the work experience
            if (workex < 2) {
                cout << "Experience Level: ENTRY LEVEL\n";
            } else if (workex >= 2 && workex <= 5) 
            {
                cout << "Experience Level: MID LEVEL\n";
            } else if (workex > 5 && workex <= 10) 
            {
                cout << "Experience Level: SENIOR LEVEL\n";
            } else 
            {
                cout << "Experience Level: EXECUTIVE LEVEL\n";
            }
        }
};

int main() 
{
    int minentry;
    cout << "Enter the number of entries: ";
    cin >> minentry;

    hit* emp = new hit[minentry];

    // Code for reading the details of employee
    for (int i = 0; i < minentry; i++) {

        cout << "\nEntering details for employee " << i + 1 << ":\n";
        emp[i].read();

    }

    cout << "\n\nEmployee Records:\n";

    // Code for Displaying the details of employee
    for (int i = 0; i < minentry; i++) {
        
        cout << "\nDetails for employee " << i + 1 << ":\n";
        emp[i].condition();

    }

    
    return 0;
}
