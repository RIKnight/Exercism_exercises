#include "hello_world.h"
// exercism, cpp track, exercise 1
// Z Knight, 2019.09.07

// Use everything from the 'std' namespace.
// This lets us write 'string' instead of 'std::string'.
using namespace std;

namespace hello_world {

// Define the function itself. This could have also been written as:
// std::string hello_world::hello()
string hello() {
    // Return the string we need.
    return "Hello, World!";
}

}  // namespace hello_world
