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
	
	# imports #
	
	import math
	
	# params and constants #
	
	all_wheels = params['all_wheels_on_track'] # boolean
    from_center = params['distance_from_center'] # float, 0:~track_width/2
    is_left = params['is_left_of_center'] # boolean
    track_width = params['track_width'] # float
    steering_float = params['steering_angle'] # float, -30:30
	steering_abs = abs(params['steering_angle']) # float, 0:30
    speed = params['speed'] # float, 0:5
    waypoints = params['waypoints'] # [[float_x, float_y], ...] # does not exists on track
    closest_waypoints = params['closest_waypoints'] # [float_x, float_y] # does not exists on track
    heading = params['heading'] # float, yaw, -180:+180
    progress = params['progress'] # float, 0:100
	
	# constants and initialize reward #
	
	MAX_REWARD = 1e2
	MIN_REWARD = 1e-3
	
	STRAIGHT = 1
	SHARP = 10
	STEERING_THRESHOLD = 20.0
	
	reward = math.exp (-13 * from_center) # non-zero positive small
		
	# functions #
	
	def always_track (sub_reward, all_wheels): # rewards for always within tracks
		if not all_wheels:
			sub_reward = MIN_REWARD   
		else:
			sub_reward = MAX_REWARD
		return sub_reward
		
	def straight_run (sub_reward, steering_abs, speed): # rewards for speed on straights
		if steering_abs < STRAIGHT and speed > 2:
			sub_reward *= 1.2
		return sub_reward
	
	def turn_slow (sub_reward, steering_abs, speed): # negative rewards for fast turns
		if steering_abs > SHARP and speed > 2:
			sub_reward -= 5
		return sub_reward
		
	def no_zigzag (sub_reward, steering_abs): # reward reduction for zigzag
		if steering_abs > STEERING_THRESHOLD:
			sub_reward *= 0.8
		return sub_reward
		
	def finishing (sub_reward, progress): # rewards for finishing, cumulative
		sub_reward += math.floor (progress)
		return sub_reward
		
	# rewards aggregation
	
	reward = always_track (reward, all_wheels)
	reward = straight_run (reward, steering_abs, speed)
	reward = turn_slow (reward, steering_abs, speed)
	reward = no_zigzag (reward, steering_abs)
	reward = finishing (reward, progress)

	'''
	Annotations :
		https://docs.aws.amazon.com/deepracer/latest/developerguide/awsracerdg.pdf#deepracer-get-started
		https://github.com/VilemR/AWS_DeepRacer
		https://github.com/hamham1004/DeepRacer/blob/master/reward_function.py
		https://github.com/sasasavic82/deepracer-reward/blob/master/model/reward_v1.py
		https://github.com/tgjohnst/DeepestRacer
		https://github.com/anhdle14/aws-deepracer
	'''

	return float (reward)