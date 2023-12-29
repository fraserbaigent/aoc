#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <regex>
#include "instruction.hpp"

using LightGrid = std::vector<std::vector<bool>>;
using LightGrid2 = std::vector<std::vector<int>>;
const std::regex regex("^(.*) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)$");

std::vector<std::string> parse_input() {
    std::ifstream infile = std::ifstream("data.dat");
    std::vector<std::string> data;
    std::string line;
    while (getline(infile, line)) {
	data.push_back(line);
    };
    return data;
};

Instruction instruction_from_line(std::string const& line) {
    std::smatch match;
    int instruction_type { -1 };
    std::regex_match(line, match, regex);
    if (match[1] == "turn on") {
	instruction_type = Instruction::ON;
    } else if (match[1] == "turn off") {
	instruction_type = Instruction::OFF;
    } else if (match[1] == "toggle") {
	instruction_type = Instruction::TOGGLE;
    } else {
	std::cout<< "Something went wrong with " << line <<"\n";
	exit(1);
    };
    //    std::cout << line <<" " << match[2] << " " << match[3] << " " << match[4
    return Instruction(
		       Coordinate2D(std::stoi(match[2]), std::stoi(match[3])),
		       Coordinate2D(std::stoi(match[4]), std::stoi(match[5])),
		       instruction_type);
};

std::vector<Instruction> parse_instructions(std::vector<std::string> const& data) {
    std::vector<Instruction> instructions;
    instructions.reserve(data.size());

    for (auto const& line : data) {
	instructions.push_back(instruction_from_line(line));
    };
    
    return instructions;
};

LightGrid create_grid(size_t const width, size_t const height) {
    LightGrid grid(height, std::vector<bool>(width, false));
    return grid;
};

LightGrid2 create_grid2(size_t const width, size_t const height) {
    LightGrid2 grid(height, std::vector<int>(width, 0));
    return grid;
};

void apply_instruction(Instruction const& instruction, LightGrid & grid) {
    for (size_t i { instruction.x0() }; i <= instruction.x1(); ++i) {
	for (size_t j { instruction.y0() }; j <= instruction.y1(); ++j) {
	    switch(instruction.get_action()) {
	    case Instruction::ON:
		grid[j][i] = true;
		break;
	    case Instruction::TOGGLE:
		grid[j][i] = !grid[j][i];
		break;		
	    case Instruction::OFF:
		grid[j][i] = false;
		break;
	    default: {
		std::cout << "Something went wrong!\n"; 
		exit(1);
	    };
	    };
	};
    };
};

void apply_instruction2(Instruction const& instruction, LightGrid2 & grid) {
    for (size_t i { instruction.x0() }; i <= instruction.x1(); ++i) {
	for (size_t j { instruction.y0() }; j <= instruction.y1(); ++j) {
	    switch(instruction.get_action()) {
	    case Instruction::ON:
		grid[j][i] +=1;
		break;
	    case Instruction::TOGGLE:
		grid[j][i] +=2;
		break;		
	    case Instruction::OFF:
		grid[j][i] -= 1;
		if (grid[j][i] < 0) {
		    grid[j][i] = 0;
		};
		break;
	    default: {
		std::cout << "Something went wrong!\n"; 
		exit(1);
	    };
	    };
	};
    };
};

void mutate_grid(LightGrid & grid, std::vector<Instruction> const& instructions) {
    for (auto const& instruction : instructions) {
	apply_instruction(instruction, grid);
    };
};
void mutate_grid2(LightGrid2 & grid, std::vector<Instruction> const& instructions) {
    for (auto const& instruction : instructions) {
	apply_instruction2(instruction, grid);
    };
};

int count_on_lights(LightGrid const& grid) {
    int total { 0 };
    for (auto const& row : grid) {
	for (bool const light : row) {
	    if (light == true) {
		total +=1;
	    };
	};
    };
    return total;
};

int count_totals(LightGrid2 const& grid) {
    int total { 0 };
    for (auto const& row : grid) {
	for (int const brightness : row) {
	    total += brightness;
	};
    };
    return total;
};

void do_part_1(std::vector<std::string> const& data) {
    std::vector<Instruction> parsed_instructions = parse_instructions(data);
    LightGrid grid = create_grid(1000,1000);
    mutate_grid(grid, parsed_instructions);
    int const result = count_on_lights(grid);
    std::cout << "Part 1: " << result <<"\n";
};

void do_part_2(std::vector<std::string> const& data) {
    std::vector<Instruction> parsed_instructions = parse_instructions(data);
    LightGrid2 grid = create_grid2(1000,1000);
    mutate_grid2(grid, parsed_instructions);
    int const result = count_totals(grid);

    std::cout << "Part 2: " << result <<"\n";
};

int main(int, char *[])
{
    std::vector<std::string> data = parse_input();
    do_part_1(data);
    do_part_2(data);
    return 0;
}
