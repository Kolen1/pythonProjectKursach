class MaterialPoint:

    def __init__(self, i, coord_x1, coord_x2, velocity_x1, velocity_x2, x1_0, x2_0, t):
        self.i = i
        self.coord_x1 = coord_x1
        self.coord_x2 = coord_x2
        self.velocity_x1 = velocity_x1
        self.velocity_x2 = velocity_x2
        self.x1_0 = x1_0
        self.x2_0 = x2_0
        self.t = t


class MaterialBody:
    def __init__(self, material_point):
        self.material_points = material_point


class PointTrajectory:
    def __init__(self, material_point, x1, x2):
        self.material_point = material_point
        self.x1 = x1
        self.x2 = x2


class BodyTrajectory:
    def __init__(self, point_trajectories, material_body):
        self.point_trajectories = point_trajectories
        self.material_body = material_body


class SpacePoint:
    def __init__(self, i, coord_x1, coord_x2, velocity_x1, velocity_x2, t):
        self.i = i
        self.coord_x1 = coord_x1
        self.coord_x2 = coord_x2
        self.velocity_x1 = velocity_x1
        self.velocity_x2 = velocity_x2
        self.t = t


class SpaceGrid:
    def __init__(self, space_point):
        self.space_points = space_point