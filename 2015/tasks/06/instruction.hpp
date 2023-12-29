#ifndef INSTRUCTION
#define INSTRUCTION
#include "coordinate.hpp"
class Instruction {
private:
    Coordinate2D const start;
    Coordinate2D const end;
    int const action;
public:
    enum {
	ON,
	OFF,
	TOGGLE,
    };

    Instruction(Coordinate2D const& start_c, Coordinate2D const& end_c, int const action_c)
	: start { start_c }
	, end { end_c }
	, action { action_c } {
    };

    size_t x0() const {
	return start.x;
    };
    size_t x1() const {
	return end.x;
    };
    size_t y0() const {
	return start.y;
    };
    size_t y1() const {
	return end.y;
    };

    int get_action() const {
	return action;
    };
};

#endif
