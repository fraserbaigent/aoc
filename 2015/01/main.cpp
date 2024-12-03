#include <iostream>
#include <fstream>
#include <string>

void do_part_1(std::string const& line) {
    int floor = 0;
    for (size_t i = 0; i < line.size(); ++i) {
	char c = line[i];
	if (c == '(') {
	    floor++;
	} else if (c==')') {
	    floor--;
	};
    };
    std::cout << "Part 1: " << floor <<"\n";
};

void do_part_2(std::string const& line) {
    int floor = 0;
    int result = -1;
    for (size_t i = 0; i < line.size(); ++i) {
	char c = line[i];
	if (c == '(') {
	    floor++;
	} else if (c==')') {
	    floor--;
	};
	if (floor == -1) {
	    result = i+1;
	    break;
	};
		
    };
    std::cout << "Part 2: " << result <<"\n";
};
    
int main(int, char *[])
{
    std::ifstream infile = std::ifstream("data.dat");
    std::string line;
    getline(infile, line, '\n');
    do_part_1(line);
    do_part_2(line);
    return 0;
}
