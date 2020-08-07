import math

    def reward_function(params):

        # parameter input #

        all_wheels = params['all_wheels_on_track'] # boolean
        from_center = params['distance_from_center'] # 0:~track_width/2
        steering_abs = abs(params['steering_angle']) # float, 0:30
        width = params['track_width'] # float, 0:~track_width/2
        speed = params['speed'] # float, 0:3
        progress = params['progress'] # float, 0:100
        waypoints = params['waypoints'] # float,  [(0:Max-1),(1:Max-1)]
        closest_waypoints = params['closest_waypoints'] # float,  [(0:Max-1),(1:Max-1)]
        heading = params['heading'] # float,  [(0:Max-1),(1:Max-1)]

        # initial rewards, zone definitions, constants #

        SHARP = 15

        reward = 1e3
        safe = (from_center < 0.5*width) # predefining zones
        optimal = (from_center < 0.3*width)
        perfect = (from_center < 0.1*width)

        if perfect:
            reward += 3
        elif optimal:
            reward += 2
        elif safe:
            reward += 1
        else:
            reward += 0

        # waypoints calculation aka 'guard rails' #

        waypoint1 = waypoints[closest_waypoints[1]]
        waypoint0 = waypoints[closest_waypoints[0]]

        way_degree = math.degrees (math.atan2(waypoint1[1] - waypoint0[1], waypoint1[0] - waypoint0[0]))
        diff_degree = abs (way_degree - heading)

        if diff_degree >= 40:
            reward *= 0.5
        if diff_degree <= 5:
            reward *= 1.2

        # specific situations modifiers #

        if (safe) and (steering_abs < SHARP) and (speed < 1): # slow down when turning
            reward *= 1.2

        if (not safe) and (speed > 1): # penalty for speeding in the not safe zone
            reward *= 0.8

        if (not perfect) and (safe) and (speed < 2): # speed limit outside of the perfect zone
            reward *= 1.2

        if (perfect) and (steering_abs == 0) and (speed == 2) and (diff_degree <= 10): # speed up only on specific straight runs
            reward *= 1.2

        if (steering_abs > SHARP): # generic zigzag penalty
            reward *= 0.8

        if (not all_wheels): # high penalty for being off track
            reward = 1e4

        # progress bump #

        reward *= (1+(progress/100)) # high reward for progress on the track

        return float (reward)