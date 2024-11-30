#ifndef GRID_HPP
#define GRID_HPP

#include <iomanip>
#include <vector>
#include <iostream>

#include "line_parser.hpp"

class Grid {
private:
    using GridVector = std::vector<std::vector<char>>;
    GridVector _grid;
    int const _x_offset;
public:
    Grid(int const width, int const height, int const x_offset)
	: _grid{GridVector(height, std::vector<char>(width, '.'))}
	, _x_offset {x_offset} {
    }

    void printGrid() const {
	std::cout << "   ";
	for (int i = 0; i < _grid[0].size();++i) {
	    std::cout << (i  == 500 ? '+' : ' ') << " ";
	}
	std::cout << std::endl;
	for (int i = 0; i < _grid.size(); ++i) {
	    auto & row = _grid[i];
	    std::cout << std::setw(3) << i << " ";
	    for (auto c : row) {
		std::cout << c << " ";
	    }
	    std::cout << "\n";
	}
    }

    void addLine(Line const& line) {
	int diff { line.first.first - line.second.first };
	int y { line.first.second };
	int sign = diff < 0 ? 1 : -1;
	std::cout << "Coords: (" << line.first.first << ", " << line.first.second << ") (" << line.second.first <<", " << line.second.second << ")\n";
	std::cout << "X diff is : " << diff << "\n";
	for (int i = 0; i <= std::abs(diff); ++i) {
	    int x = line.first.first  + (i * sign);
	    std::cout << x << " " << y << "\n";
	    _grid[y][x] = '#';
	}

	diff = line.first.second - line.second.second;
	sign = diff < 0 ? 1 : -1;
	int x = line.first.first - _x_offset;
	std::cout << "Y diff is : " << diff << "\n";
	for (int i = 0; i <= std::abs(diff); ++i) {
	    int y = line.first.second + sign * i;
	    
	    std::cout << x << " " << y << "\n";
	    if ( x >= _grid[0].size()) {
		std::cout << "x is busted\n";
	    }
	    if (y >= _grid.size()) {
		std::cout <<"y is busted\n";
	    }
	    _grid[y][x] = '#';
	}
	std::cout << std::endl;
	exit(1);
    }

    bool addGrain() {
	int x { 500 - _x_offset };
	int y { 0 };
	std::cout << "Set " << x << ", " << y << " to be a sand\n";
	do {
	    if (y + 1 >= _grid.size()) {
		return false;
	    } else if (_grid[y+1][x] == '.') {
		y++;
	    } else {
		std::cout << "couldn't set at x = " << x << " y = " << y <<"\n";
		if (x-1 < 0) {
		    return false;
		} else if (_grid[y+1][x-1] == '.') {
		    x--;
		    y++;
		} else if (x + 1 >= _grid[y+1].size()) {
		    return false;
		} else if (_grid[y+1][x+1] == '.') {
		    x++;
		    y++;
		} else {
		    _grid[y][x] = 'o';
		    std::cout << "Set " << x << ", " << y << " to be a sand\n";
		    return true;
		}
	    }
	} while (true);

	
	return false;
    }
};

#endif
