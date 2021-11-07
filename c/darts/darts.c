#include "darts.h"

/* Name: darts.c
 * Purpose: exercism, c track, darts
 * Written by Z Knight, 2021.11.06
 * Removed src directory structure and used squared distance; ZK, 2021.11.07
 */

int score(coordinate_t location)
{
    float distance_squared = location.x*location.x+location.y*location.y;
    if (distance_squared > 100) return 0;
    if (distance_squared >  25) return 1;
    if (distance_squared >   1) return 5;
    return 10;
}
