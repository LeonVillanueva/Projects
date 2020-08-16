import math

def reward_function(params):

# parameter input #

    all_wheels = params['all_wheels_on_track'] # boolean
    from_center = params['distance_from_center'] # 0:~track_width/2
    steering = params['steering_angle'] # float, -30:30, right_facing:left_facing
    steering_abs = abs(params['steering_angle']) # float, 0:30
    width = params['track_width'] # float, 0:~track_width/2
    speed = params['speed'] # float, 0:3
    progress = params['progress'] # float, 0:100
    waypoints = params['waypoints'] # float,  [(0:Max-1),(1:Max-1)]
    closest_waypoints = params['closest_waypoints'] # float,  [(0:Max-1),(1:Max-1)]
    heading = params['heading'] # float,  [(0:Max-1),(1:Max-1)]
    is_left = params['is_left_of_center'] # boolean

    SHARP = 15

    MIN_SPEED = 1.0
    MID_SPEED = 2.0
    MAX_SPEED = 3.0

    reward = (progress + 1e2)/10

    waypoint1 = waypoints[closest_waypoints[1]]
    waypoint0 = waypoints[closest_waypoints[0]]

    way_degree = math.degrees (math.atan2(waypoint1[1] - waypoint0[1], waypoint1[0] - waypoint0[0]))
    diff_degree = abs (way_degree - heading)

    if diff_degree > 30:
        reward *= 0.5
    if diff_degree < 10:
        reward *= 1.5

    if speed < MAX_SPEED:
        reward = 0.5

    if progress == 100:
        reward += 1000

    if (not all_wheels): # high penalty for being off track
        reward = 1e4

    return float (reward)
