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
    steering_float = params['steering_angle'] # float
	steering_abs = abs(params['steering_angle']) # float
    speed = params['speed'] # float, 0:5
    waypoints = params['waypoints'] # [[float_x, float_y], ...] # does not exists on track
    closest_waypoints = params['closest_waypoints'] # [float_x, float_y] # does not exists on track
    heading = params['heading'] # float, yaw
    progress = params['progress'] # float, 0:100
	
	# constants and initialize #
	
	MAX_REWARD = 1000
	MIN_REWARD = 1e-3
	
	MAX_STEER = 30
	DLT_STEER = 10
	
	reward = math.exp (-1 * d
	
	
	# functions #
	
	def always_track
		if not all_wheels:
			reward = -1   
		else if params["progress"] == 1 :
			reward = 10
		return reward
		
	# rewards aggregation
	
	
	reward = always_track(reward, on_track)


	return float (reward)