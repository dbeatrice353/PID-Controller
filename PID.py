

class PIDController:
    def __init__(self):
        self.previous_error_x = 0
        self.previous_error_y = 0
        self.error_sum_x = 0
        self.error_sum_y = 0

    def get_u(self,set_point,current_value):
        # parameters: 
        Kp = 30
        Ki = 30
        Kd = 30
        # get the set point x & y components
        set_point_x = set_point[0]
        set_point_y = set_point[1]
        # get the current position x & y components
        current_value_x = current_value[0]
        current_value_y = current_value[1]
        # calculate the errors
        error_x = set_point_x - current_value_x
        error_y = set_point_y - current_value_y
        # accumulate the errors
        self.error_sum_x += error_x
        self.error_sum_y += error_y
        # calculate the rate of change on the errors
        delta_error_x = error_x - self.previous_error_x
        delta_error_y = error_y - self.previous_error_y
        # save the current error as the previous error for the next iteration
        self.previous_error_x = error_x
        self.previous_error_y = error_y
        # pid equation...
        output_x = Kp*error_x + Ki*self.error_sum_x + Kd*delta_error_x
        output_y = Kp*error_y + Ki*self.error_sum_y + Kd*delta_error_y

        return [output_x, output_y]
