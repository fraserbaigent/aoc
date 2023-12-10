#include <iostream>
#include "../../lib/file_reader.hpp"
#include "line_parser.hpp"
#include "grid.hpp"

int main()
{

    auto reader = FileReader("data.dat");
    LineParser parser;
    std::vector<Line> lines;
    while (reader.good()) {
	auto lines_to_add = parser.parseInputLine(reader.nextLine());
	lines.insert(lines.end(), lines_to_add.begin(), lines_to_add.end());
    }

    auto corners = parser.getGridCorners();
    int x_offset = corners.first.first;
    int width = corners.second.first - x_offset + 1;
    int height = corners.second.second + 1;
    Grid grid(width, height, x_offset);
    for (auto & line : lines) {
	grid.addLine(line);
    }
    grid.printGrid();
    exit(1);
    std::cout << width << " " << height << "\n";

    std::cout << "Gridding\n";
    auto answer { 0 };
    while (grid.addGrain()) {
	answer++;
    };
    std::cout << "Answer is: " << answer << "\n";  
    return 0;
}
