from __future__ import division
from boids import *
from precode import *
from vector2d import Vec2d

def ball_distance(player, ball):
    return (ball.pos - player.pos).get_length()
  
def move_to_ball(player, ball):
    distance = ball_distance(player, ball)
    print("balldistance = {}".format(distance))
    senter = Vec2d(0, 0)
    
    senter += player.pos

    if senter.get_length() != 0:
        return (senter - ball.pos) / 10
    
    return Vec2d(0, 0)

def catch_ball(player, ball):
    distance = ball_distance(player, ball)

    impulse = intersect_circles(player.pos, player.radius, ball.pos, ball.radius)
    if impulse:
        print("yofag")
        (ball.pos -player.pos).normalized() 


def Close_boids(boid_list, boid):
    """
    Find the close boids
    """
    closeboid_list = []
    for b in boid_list:
        if b != boid:
            if (b.pos - boid.pos).magnitude() < VIEW_DISTANCE:
                closeboid_list.append(b)
    return closeboid_list

def Rule1(boid_list, boid):
    """
    Rule 1: Boids try to fly towards the centre of mass of neighbouring boids.
    """
    closeboids = Close_boids(boid_list, boid)
    senter = Vec2d(0, 0)
    for b in closeboids:
        senter += b.pos

    if len(closeboids) !=0:
        senter /= len(closeboids)

    if senter.magnitude() != 0:
        return (senter - boid.pos) / BOID_SENTER
    return Vec2d(0, 0)


def Rule2(boid_list, boid):
    """
    Rule 2: Boids try to keep a small distance away from other objects (including other boids).
    """
    closeboids = Close_boids(boid_list, boid)
    distance = Vec2d(0, 0)

    for b in closeboids:
        if (b.pos - boid.pos).magnitude() < BOID_DISTANCE:
            distance -= (b.pos - boid.pos)

    if distance.magnitude() != 0:
        return distance / 5
    return Vec2d(0, 0)


def Rule3(boid_list, boid):
    """
    Rule 3: Boids try to match velocity with near boids.
    """
    closeboids = Close_boids(boid_list, boid)
    avgspeed = Vec2d(0, 0)
    for b in closeboids:
        avgspeed += b.speed

    if len(closeboids) != 0:
        avgspeed /= len(closeboids)

    if avgspeed.magnitude() != 0:
        return (avgspeed - boid.speed) / BOID_AVGSPEED
    return Vec2d(0, 0)


def Rule4(hoik_list, boid):
    """
    Rule 4: Boids fly away from Hoiks
    """
    close = Close_hoiks(hoik_list, boid)
    distance = Vec2d(0, 0)

    for b in close:
        if (b.pos - boid.pos).magnitude() < HOIK_DISTANCE:
            distance -= (b.pos - boid.pos)

    if distance.magnitude() != 0:
        return distance
    return Vec2d(0, 0)


def Rule5(object_list, boid):
    """
    Rule 4: Birds try to fly away from obstacles
    """
    close = Close_hoiks(object_list, boid)
    distance = Vec2d(0, 0)

    for b in close:
        if (b.pos - boid.pos).magnitude() < OBSTACLE_DISTANCE:
            distance -= (b.pos - boid.pos)

    if distance.magnitude() != 0:
        return distance
    return Vec2d(0, 0)


def Close_hoiks(hoik_list, hoik):
    """
    Find the close hoiks
    """
    closehoiks_list = []
    for h in hoik_list:
        if h != hoik:
            if (h.pos - hoik.pos).magnitude() < HOIK_VIEW_DISTANCE:
                closehoiks_list.append(h)
    return closehoiks_list


def Hoik_Rule1(boid_list, hoik):
    """
    Rule 1: Hoiks try to fly towards the centre to the mass of neighbouring boids.
    """
    close = Close_hoiks(boid_list, hoik)
    senter = Vec2d(0, 0)
    for h in close:
        senter += h.pos

    if len(close) != 0:
        senter /= len(close)

    if senter.magnitude() != 0:
        return (senter - hoik.pos) / 2
    return Vec2d(0, 0)


def Hoik_Rule2(hoik_list, hoik):
    """
    Rule 2: Hoik try to keep a small distance away from other hoiks.
    """
    closehoik = Close_hoiks(hoik_list, hoik)
    distance = Vec2d(0, 0)

    for h in closehoik:
        if (h.pos - hoik.pos).magnitude() < HOIK_DISTANCE:
            distance -= (h.pos - hoik.pos)

    if distance.magnitude() != 0:
        return distance
    return Vec2d(0, 0)

