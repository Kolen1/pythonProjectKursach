import utils.utils as util

x1_corner = 8
x2_corner = -8
h_parts = 1
time = 1
h = 0.01
body = util.create_material_body(x1_corner, x2_corner, h_parts)
mov = util.move_material_body(time, h, body)

util.plot_trajectory(body, mov)

vf = util.move_through_space(1, 0.1)
util.plot_velocity_fields(vf)

