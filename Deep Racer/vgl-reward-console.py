def reward_function(params):
    '''
    In @params object:
    {
        "all_wheels_on_track": Boolean,    # flag to indicate if the vehicle is on the track
        "x": float,                        # vehicle's x-coordinate in meters
        "y": float,                        # vehicle's y-coordinate in meters
        "distance_from_center": float,     # distance in meters from the track center
        "is_left_of_center": Boolean,      # Flag to indicate if the vehicle is on the left side to the track center or not.
        "heading": float,                  # vehicle's yaw in degrees
        "progress": float,                 # percentage of track completed
        "steps": int,                      # number steps completed
        "speed": float,                    # vehicle's speed in meters per second (m/s)
        "streering_angle": float,          # vehicle's steering angle in degrees
        "track_width": float,              # width of the track
        "waypoints": [[float, float], … ], # list of [x,y] as milestones along the track center
        "closest_waypoints": [int, int]    # indices of the two nearest waypoints.
    }
'''

    # read input parameters
    all_wheels = params['all_wheels_on_track'] # boolean
    from_center = params['distance_from_center'] # 0:~track_width/2
    steering_abs = abs(params['steering_angle']) # float, 0:30
    width = params['track_width'] # float, 0:~track_width/2
    speed = params['speed'] # float, 0:4
    progress = params['progress'] # float, 0:100

    # initialize constant and reward #
    MAX_REWARD = 10
    MIN_REWARD = 1e-4
    STRAIGHT = 1
    SHARP = 15
    STEERING = 15

    reward = 1e-2
    third1 = 0.1*width
    third2 = 0.2*width
    third3 = 0.5*width

    # sub functions reward #

    def always_track (sub_reward, all_wheels): # reward for keeping on track
        if not all_wheels:
            sub_reward = MAX_REWARD
        else:
            sub_reward = MIN_REWARD
        return float (sub_reward)

    def straight_run (sub_reward, steering_abs, speed, from_center): # reward for accelerate on straights
        if steering_abs < STRAIGHT and speed > 2 and (from_center <= third2):
            sub_reward *= 1.1
        return float (sub_reward)

    def turn_slow (sub_reward, steering_abs, speed, from_center): # reward for decelarate on turns
        if (steering_abs <= SHARP) and (speed < 2) and (from_center <= third2):
            sub_reward += 1
        elif (steering_abs <= SHARP) and (speed < 2) and (from_center <= third3):
            sub_reward += 0.5
        else:
            sub_reward += MIN_REWARD
        return float (sub_reward)

    def no_zigzag (sub_reward, steering_abs, from_center): # reward for keeping straights
        if (steering_abs <= STEERING) and (from_center <= third1):
            sub_reward += 2
        elif (steering_abs <= STEERING) and (from_center <= third2):
            sub_reward += 1
        else:
            sub_reward += MIN_REWARD
        return float (sub_reward)

    def finishing (sub_reward, progress): # reward for completing the race
        sub_reward += progress/10
        return float (sub_reward)

    def centering (sub_reward, from_center): # reward to keep center, basic from developer example
        if from_center <= third1:
            sub_reward += 1
        elif from_center <= third2:
            sub_reward += 0.5
        elif from_center <= third3:
            sub_reward += 0.25
        else:
            sub_reward = MIN_REWARD

        return float (sub_reward)

    reward = always_track (reward, all_wheels)
    reward = centering (reward, from_center)
    reward = finishing (reward, progress)
    reward = turn_slow (reward, steering_abs, speed, from_center)
    reward = no_zigzag (reward, steering_abs, from_center)
    reward = straight_run (reward, steering_abs, speed, from_center)

    '''
Annotations :
https://docs.aws.amazon.com/deepracer/latest/developerguide/awsracerdg.pdf#deepracer-get-started
https://github.com/VilemR/AWS_DeepRacer
https://github.com/hamham1004/DeepRacer/blob/master/reward_function.py
https://github.com/sasasavic82/deepracer-reward/blob/master/model/reward_v1.py
https://github.com/tgjohnst/DeepestRacer
https://github.com/anhdle14/aws-deepracer
https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-reward-function-examples.html#deepracer-reward-function-example-2
'''

    return float(reward)