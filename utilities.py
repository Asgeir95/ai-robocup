#!/usr/bin/env python

import pygame
import math
from variables import *
from vector2d import Vec2d

def intersect_rectangle_circle(rec_pos, sx, sy, circle_pos, circle_radius, circle_speed):
    # Position of the walls relative to the ball
    top    = (rec_pos.y     ) - circle_pos.y
    bottom = (rec_pos.y + sy) - circle_pos.y
    left   = (rec_pos.x     ) - circle_pos.x
    right  = (rec_pos.x + sx) - circle_pos.x

    r = circle_radius
    intersecting = left <= r and top <= r and right >= -r and bottom >= -r

    if intersecting:
        # Now need to figure out the vector to return.
        # should be just a matter of flipping x and y of the ball?

        impulse = circle_speed.normalized()

        if abs(left) < r and impulse.x > 0:
            impulse.x = -impulse.x
        if abs(right) < r and impulse.x < 0:
            impulse.x = -impulse.x
        if abs(top) < r and impulse.y > 0:
            impulse.y = -impulse.y
        if abs(bottom) < r and impulse.y < 0:
            impulse.y = -impulse.y

        #print("Impact", circle_speed, impulse.normalized())

        return impulse.normalized()
    return False


def intersect_circles(a_pos, a_radius, b_pos, b_radius):
    # vector from A to B
    dp1p2 = b_pos - a_pos

    if a_radius + b_radius >= dp1p2.get_length():
        return dp1p2.normalized()
    else:
        return False