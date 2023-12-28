#include <cstddef>

struct Coordinate2D {
    int x { 0 };
    int y { 0 };

    Coordinate2D(int xx, int yy)
	: x { xx }
	, y { yy } {
    };
    
    Coordinate2D(Coordinate2D const& other)
	: x { other.x }
	,y { other.y } {
    };
    
    Coordinate2D operator=(Coordinate2D const& other) {
	x = other.x ;
	y = other.y ;
	return *this;
    };
    
    bool operator==(Coordinate2D const& other) const {
	return this->x == other.x && this->y == other.y;
    };
};

class Coordinate2DHash {
public:
    size_t operator()(Coordinate2D const& coordinate) const {
	return coordinate.x + (coordinate.y << 16);
    };
};
