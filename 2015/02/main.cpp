#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <regex>

std::vector<std::string> parse_input() {
    std::ifstream infile = std::ifstream("data.dat");
    std::vector<std::string> data;
    std::string line;
    while (getline(infile, line)) {
	data.push_back(line);
    };
    return data;
};


std::vector<std::vector<int>> parse_data(std::vector<std::string> const& data) {
    std::vector<std::vector<int>> parsed_data(data.size(), {0,0,0});
    
    const std::regex regex("^([0-9]+)x([0-9]+)x([0-9]+)$");
    std::smatch match;
    for (int j = 0; j < data.size(); ++j) {
	std::string const& d = data[j];
	std::regex_match(d, match, regex);
	for (int i = 1; i < 4; ++i) {
	    parsed_data[j][i-1] = std::stoi(match[i]);
	};
	std::sort(parsed_data[j].begin(), parsed_data[j].end());
    };
    return parsed_data;
};

int get_paper_for(std::vector<int> const& gift_dimensions) {
    return 2 * ( gift_dimensions[0] * gift_dimensions[1] + gift_dimensions[0] * gift_dimensions[2] + gift_dimensions[1]*gift_dimensions[2] )
	+ gift_dimensions[0] * gift_dimensions[1];
};

int get_ribbon_for(std::vector<int> const& gift_dimensions) {
    int perimeter = 2*(gift_dimensions[0] + gift_dimensions[1]);
    int bow = gift_dimensions[0] * gift_dimensions[1] * gift_dimensions[2];
    return perimeter + bow;

};

void do_part_1(std::vector<std::string> const& data) {
    int result { 0 };
    auto const parsed = parse_data(data);
    for (auto & p : parsed) {
	result += get_paper_for(p);
    };
    std::cout << "Part 1: " << result <<"\n";
};

void do_part_2(std::vector<std::string> const& data) {
    int result { 0 };
    auto const parsed = parse_data(data);
    for (auto & p : parsed) {
	result += get_ribbon_for(p);
    };
    std::cout << "Part 2: " << result <<"\n";
};

int main(int, char *[])
{
    std::vector<std::string> data = parse_input();
    do_part_1(data);
    do_part_2(data);
    return 0;
}
