#include <iostream>
#include <fstream>
#include <string>
#include <vector>

std::vector<std::string> parse_input() {
    std::ifstream infile = std::ifstream("data.dat");
    std::vector<std::string> data;
    std::string line;
    while (getline(infile, line)) {
	data.push_back(line);
    };
    return data;
};

void do_part_1(std::vector<std::string> const& data) {
    int result { 0 };
    std::cout << "Part 1: " << result <<"\n";
};

void do_part_2(std::vector<std::string> const& data) {
    int result { 0 };
    std::cout << "Part 2: " << result <<"\n";
};

int main(int, char *[])
{
    std::vector<std::string> data = parse_input();
    do_part_1(data);
    do_part_2(data);
    return 0;
}
