#include "darts.h"
#include <math.h>

/* Name: darts.c
 * Purpose: exercism, c track, darts
 * Written by Z Knight, 2021.11.06
 */

int score(coordinate_t location)
{
    float distance = sqrt(location.x*location.x+location.y*location.y);
    if (distance > 10){return 0;}
    if (distance >  5){return 1;}
    if (distance >  1){return 5;}
    return 10;
}
