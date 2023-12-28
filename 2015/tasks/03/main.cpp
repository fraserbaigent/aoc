#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>

#include "coordinate.hpp"

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
    Coordinate2D position { 0, 0 };
    std::unordered_map<char, Coordinate2D> const directions {
	{'^',{0,-1}},
	{'v',{0,1}},
	{'<',{-1,0}},
	{'>',{1,0}},
    };

    std::string const& line = data[0];
    std::unordered_map<Coordinate2D, int, Coordinate2DHash> visited;
    visited[position] = 1;
    for (char c : line) {
	auto const& dx = directions.find(c)->second;
	position.x += dx.x;
	position.y += dx.y;
	auto it = visited.find(position);
	if (it== visited.end()) {
	    visited[position] = 1;
	} else {
	    it->second += 1;
	};
    };
    result = visited.size();
    std::cout << "Part 1: " << result <<"\n";
};

void do_part_2(std::vector<std::string> const& data) {
    int result { 0 };
    Coordinate2D santa { 0, 0 };
    Coordinate2D robo_santa = santa;
    std::unordered_map<char, Coordinate2D> const directions {
	{'^',{0,-1}},
	{'v',{0,1}},
	{'<',{-1,0}},
	{'>',{1,0}},
    };

    std::string const& line = data[0];
    std::unordered_map<Coordinate2D, int, Coordinate2DHash> visited;
    visited[santa] = 2;
    size_t i { 0 };
    do {
	char const c = line[i];
	auto const& dx = directions.find(c)->second;
	auto & position = i % 2 == 0 ? santa : robo_santa;
	position.x += dx.x;
	position.y += dx.y;
	auto it = visited.find(position);
	if (it== visited.end()) {
	    visited[position] = 1;
	} else {
	    it->second += 1;
	};
	i++;
    } while( i < line.size());	
    result = visited.size();
    std::cout << "Part 2: " << result <<"\n";
};

int main(int, char *[])
{
    std::vector<std::string> data = parse_input();
    do_part_1(data);
    do_part_2(data);
    return 0;
}
