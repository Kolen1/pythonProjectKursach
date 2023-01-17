import numpy as np

import models.models as model
import math
import matplotlib.pyplot as plotlib


def f_x1(t, x1):  # скорость A
    return - t * x1


def f_x2(t, x2):  # Скорость B
    return math.pow(t, 3) * x2


def create_material_body(x1_c, x2_c, h):       # x1_c - начальные, h-шаг интегрирования
    t = 0
    m = 0
    material_points = []
    for i in range(int( 4/ h) + 1):
        for j in range(int(4 / h) + 1):
            x1 = x1_c - j * h
            x2 = x2_c - i * h
            material_points.append(model.MaterialPoint(m, x1, x2, f_x1(t, x1), f_x2(t, x2), x1, x2, t))
            m += 1
    material_body = model.MaterialBody(material_points)
    return material_body


def move_material_body(time, h, mb):
    point_trajectories = []
    for i in range(len(mb.material_points)):
        t = 0
        x1_0 = mb.material_points[i].x1_0
        x2_0 = mb.material_points[i].x2_0
        x1_t = [x1_0]
        x2_t = [x2_0]
        for n in range(int(time / h) + 1):
            x1_k = x1_t[n]
            x2_k = x2_t[n]
            x1_t.append(x1_k + h * (1 / 2) * (f_x1(t, x1_k) + f_x1(t + h, x1_k + h * f_x1(t, x1_k))))  # Метод рунге-кутта
            x2_t.append(x2_k + h * (1 / 2) * (f_x2(t, x2_k) + f_x2(t + h, x2_k + h * f_x2(t, x1_k))))
            t += h
        point_trajectories.append(model.PointTrajectory(mb.material_points[i], x1_t, x2_t))
    body_trajectories = model.BodyTrajectory(point_trajectories, mb)
    return body_trajectories


def plot_trajectory(mb, tr):
    for i in range(len(mb.material_points)):
        plotlib.plot(mb.material_points[i].coord_x1, mb.material_points[i].coord_x2, 'r.')
    for i in range(len(mb.material_points)):
        plotlib.plot(tr.point_trajectories[i].x1, tr.point_trajectories[i].x2, 'b', linewidth=0.5)
    for i in range(len(mb.material_points)):
        time = len(tr.point_trajectories[i].x1) - 1
        plotlib.plot(tr.point_trajectories[i].x1[time], tr.point_trajectories[i].x2[time], 'g.')
    plotlib.axis('equal')
    plotlib.grid()
    plotlib.savefig('assets/plot_trajectory.svg', format='svg', dpi=1200)


def move_through_space(time, h):
    t = h
    m = 0
    a = np.linspace(-5, 5, 11)
    x1_s, x2_s = np.meshgrid(a, a)
    velocity_fields = []
    for n in range(int(time / h)):
        space_points = []
        for i in range(11):
            for j in range(11):
                x = x1_s[i, j]
                y = x2_s[i, j]
                space_points.append(model.SpacePoint(m, x, y, f_x1(t, x), f_x2(t, y), t))
                m += 1
        velocity_fields.append(model.SpaceGrid(space_points))
        t += h
    return velocity_fields


def plot_velocity_fields(vf):
    h = vf[0].space_points[0].t
    t = h
    for n in range(len(vf)):
        plotlib.figure(n)
        plotlib.suptitle('t = ' + str(t))
        m = 0
        coord_x1 = []
        coord_x2 = []
        v_x1 = []
        v_x2 = []
        for i in range(11):
            for j in range(11):
                coord_x1.append(vf[n].space_points[m].coord_x1)
                coord_x2.append(vf[n].space_points[m].coord_x2)
                v_x1.append(vf[n].space_points[m].velocity_x1)
                v_x2.append(vf[n].space_points[m].velocity_x2)
                m += 1
        plotlib.subplot(1, 2, 1)
        plotlib.quiver(coord_x1, coord_x2, v_x1, v_x2)
        for p in range(1, 5):
            for q in range(1, 5):
                x = np.linspace(0.1, 5.0, 100)
                d = f_x2(t, 1) / f_x1(t, 1)
                c = q * (p ** d)
                y = c * (-x ** d)
                plotlib.subplot(1, 2, 2)
                plotlib.axis([-1, 5, -5, 1])
                plotlib.plot(x, y)
            plotlib.savefig('assets/velocity_fields' + str(n) + '.svg', format='svg', dpi=1200)
            t += h