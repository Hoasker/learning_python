#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import random

import pygame

SCREEN_DIM = (800, 600)


class Vec2d():
    def __init__(self, x):
        self.x = x

    def length(self, x):
        """Ð²Ð¾Ð·Ð²Ñ€Ð°Ñ‰Ð°ÐµÑ‚ Ð´Ð»Ð¸Ð½Ñƒ Ð²ÐµÐºÑ‚Ð¾Ñ€Ð°"""
        return math.sqrt(self.x[0] * self.x[0] + self.x[1] * self.x[1])

    def __getitem__(self, i):
        return self.x[i]

    def int_pair(self):
        """Ð²Ð¾Ð·Ð²Ñ€Ð°Ñ‰Ð°ÐµÑ‚ Ð¿Ð°Ñ€Ñƒ ÐºÐ¾Ð¾Ñ€Ð´Ð¸Ð½Ð°Ñ‚, Ð¾Ð¿Ñ€ÐµÐ´ÐµÐ»ÑÑŽÑ‰Ð¸Ñ… Ð²ÐµÐºÑ‚Ð¾Ñ€ (ÐºÐ¾Ð¾Ñ€Ð´Ð¸Ð½Ð°Ñ‚Ñ‹ Ñ‚Ð¾Ñ‡ÐºÐ¸ ÐºÐ¾Ð½Ñ†Ð° Ð²ÐµÐºÑ‚Ð¾Ñ€Ð°),
        ÐºÐ¾Ð¾Ñ€Ð´Ð¸Ð½Ð°Ñ‚Ñ‹ Ð½Ð°Ñ‡Ð°Ð»ÑŒÐ½Ð¾Ð¹ Ñ‚Ð¾Ñ‡ÐºÐ¸ Ð²ÐµÐºÑ‚Ð¾Ñ€Ð° ÑÐ¾Ð²Ð¿Ð°Ð´Ð°ÑŽÑ‚ Ñ Ð½Ð°Ñ‡Ð°Ð»Ð¾Ð¼ ÑÐ¸ÑÑ‚ÐµÐ¼Ñ‹ ÐºÐ¾Ð¾Ñ€Ð´Ð¸Ð½Ð°Ñ‚ (0, 0)"""
        return int(self.x[0]), int(self.x[1])

    def __sub__(self, y):
        """"Ð²Ð¾Ð·Ð²Ñ€Ð°Ñ‰Ð°ÐµÑ‚ Ñ€Ð°Ð·Ð½Ð¾ÑÑ‚ÑŒ Ð´Ð²ÑƒÑ… Ð²ÐµÐºÑ‚Ð¾Ñ€Ð¾Ð²"""
        return self.x[0] - y[0], self.x[1] - y[1]

    @staticmethod
    def __add__(x, y):
        """Ð²Ð¾Ð·Ð²Ñ€Ð°Ñ‰Ð°ÐµÑ‚ ÑÑƒÐ¼Ð¼Ñƒ Ð´Ð²ÑƒÑ… Ð²ÐµÐºÑ‚Ð¾Ñ€Ð¾Ð²"""
        return Vec2d((x[0] + y[0], x[1] + y[1]))

    def __mul__(self, k):
        """Ð²Ð¾Ð·Ð²Ñ€Ð°Ñ‰Ð°ÐµÑ‚ Ð¿Ñ€Ð¾Ð¸Ð·Ð²ÐµÐ´ÐµÐ½Ð¸Ðµ Ð²ÐµÐºÑ‚Ð¾Ñ€Ð° Ð½Ð° Ñ‡Ð¸ÑÐ»Ð¾"""
        return Vec2d((self.x[0] * k, self.x[1] * k))

# =======================================================================================
# Ð¤ÑƒÐ½ÐºÑ†Ð¸Ð¸, Ð¾Ñ‚Ð²ÐµÑ‡Ð°ÑŽÑ‰Ð¸Ðµ Ð·Ð° Ñ€Ð°ÑÑ‡ÐµÑ‚ ÑÐ³Ð»Ð°Ð¶Ð¸Ð²Ð°Ð½Ð¸Ñ Ð»Ð¾Ð¼Ð°Ð½Ð¾Ð¹
# =======================================================================================

class Polyline():
    def __init__(self, points, count):
        self.points = points
        self.count = count
    
    def get_point(self, points, alpha, deg=None):
        """Ñ„ÑƒÐ½ÐºÑ†Ð¸Ñ Ð¿Ð¾Ð»ÑƒÑ‡Ð°ÐµÑ‚ Ð½Ð° Ð²Ñ…Ð¾Ð´ 3 Ð±Ð°Ð·Ð¾Ð²Ñ‹Ðµ Ñ‚Ð¾Ñ‡ÐºÐ¸ Ð¸ ÑˆÐ°Ð³ Ð½Ð°Ð¿Ñ€Ð¸Ð¼ÐµÑ€ 1/35
        Ñ€ÐµÐºÑƒÑ€ÑÐ¸Ð²Ð½Ð¾ ÑÑƒÐ¼Ð¼Ð¸Ñ€ÑƒÐµÐ¼ Ð²ÐµÐºÑ‚Ð¾Ñ€Ð° Ð½Ð°Ñ‡Ð¸Ð½Ð°Ñ Ñ ÑÐ°Ð¼Ð¾Ð³Ð¾ Ð¿ÐµÑ€Ð²Ð¾Ð³Ð¾
        v = add(mul(point[1], 1/35), mul(point[0], 34/35))
        Ð¿Ð¾Ñ‚Ð¾Ð¼ Ñ‚Ð¾ Ñ‡Ñ‚Ð¾ Ð¿Ð¾Ð»ÑƒÑ‡Ð¸Ð»Ð¾ÑÑŒ Ð½Ð° ÑÑ‚Ð¾Ð¼ ÑˆÐ°Ð³Ðµ Ð²Ð¾Ð·Ð²Ñ€Ð°Ñ‰Ð°ÐµÐ¼ Ð² Ð²Ñ‚Ð¾Ñ€Ð¾Ð¹ Ð°Ñ€Ð³ÑƒÐ¼ÐµÐ½Ñ‚
        add(mul(point[2], 1/35), mul(v, 34/35))
        Ñ‚Ð¾ÐµÑÑ‚ÑŒ Ð±ÐµÑ€ÐµÐ¼ Ð¿ÐµÑ€Ð²Ñ‹Ð¹ Ð²ÐµÐºÑ‚Ð¾Ñ€ Ñ Ð±Ð¾Ð»ÑŒÑˆÐ¸Ð¼ ÐºÐ¾ÑÑ„Ñ„Ð¸Ñ†Ð¸ÐµÐ½Ñ‚Ð¾Ð¼ Ð° Ð´Ñ€ÑƒÐ³Ð¸Ðµ Ð²ÑÐµ Ñ Ð¼Ð°Ð»ÐµÐ½ÑŒÐºÐ¸Ð¼
        Ð´Ð°Ð»ÐµÐµ ÐºÐ¾Ð³Ð´Ð° alpha Ð±ÑƒÐ´ÐµÑ‚ Ñ€Ð°ÑÑ‚Ð¸ Ð±ÑƒÐ´ÐµÑ‚ Ð¿ÐµÑ€Ð²Ñ‹Ð¹ Ð²ÐµÐºÑ‚Ð¾Ñ€ Ñ Ð¼Ð°Ð»ÐµÐ½ÑŒÐºÐ°Ð¼ ÐºÐ¾ÑÑ„Ñ„Ð¸Ñ†Ð¸ÐµÐ½Ñ‚Ð¾Ð¼
        """
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        v1 = points[deg].__mul__(alpha)
        v2 = self.get_point(points, alpha, deg - 1).__mul__(1 - alpha)

        return Vec2d.__add__(v1, v2)

    def get_points(self, base_points, count):
        """Ñ„ÑƒÐ½ÐºÑ†Ð¸Ñ Ð¿Ð¾Ð»ÑƒÑ‡Ð°ÐµÑ‚ Ð½Ð° Ð²Ñ…Ð¾Ð´ 3 Ð±Ð°Ð·Ð¾Ð²Ñ‹Ðµ Ñ‚Ð¾Ñ‡ÐºÐ¸
        Ð¸ ÐºÐ¾Ð»-Ð²Ð¾ ÑˆÐ°Ð³Ð¾Ð² ÐºÐ¾Ñ‚Ð¾Ñ€Ñ‹Ðµ Ð½ÑƒÐ¶Ð½Ð¾ Ð´Ð¾Ð±Ð°Ð²Ð¸Ñ‚ÑŒ
        ÐŸÐ¾Ð»ÑƒÑ‡Ð°ÐµÐ¼ n Ð¿Ñ€Ð¾Ð¼ÐµÐ¶ÑƒÑ‚Ð¾Ñ‡Ð½Ñ‹Ñ… Ñ‚Ð¾Ñ‡ÐµÐº
        """
        alpha = 1 / count
        res = []
        for i in range(count):
            p = self.get_point(base_points, i * alpha)
            res.append(p)

        return res

    def set_points(self, speeds):
        """Ñ„ÑƒÐ½ÐºÑ†Ð¸Ñ Ð¿ÐµÑ€ÐµÑ€Ð°ÑÑ‡ÐµÑ‚Ð° ÐºÐ¾Ð¾Ñ€Ð´Ð¸Ð½Ð°Ñ‚ Ð¾Ð¿Ð¾Ñ€Ð½Ñ‹Ñ… Ñ‚Ð¾Ñ‡ÐµÐº"""
        for p in range(len(self.points)):
            self.points[p] = Vec2d.__add__(self.points[p], speeds[p])
            if self.points[p][0] > SCREEN_DIM[0] or self.points[p][0] < 0:
                speeds[p] = [- speeds[p][0], speeds[p][1]]
            if self.points[p][1] > SCREEN_DIM[1] or self.points[p][1] < 0:
                speeds[p] = [speeds[p][0], -speeds[p][1]]


class Knot(Polyline):
    def __init__(self, points, count):
        super().__init__(points, count)

    def get_knot(self):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append(Vec2d.__add__(self.points[i], self.points[i + 1]).__mul__(0.5)) # Ð”Ð¾Ð±Ð°Ð²Ð»ÑÐµÐ¼ ÑÑ€ÐµÐ´Ð½ÑŽÑŽ Ñ‚Ð¾Ñ‡ÐºÑƒ Ð¼ÐµÐ¶Ð´Ñƒ i Ð¸ i+1
            ptn.append(points[i + 1])
            ptn.append(Vec2d.__add__(self.points[i + 1], self.points[i + 2]).__mul__(0.5)) # Ð”Ð¾Ð±Ð°Ð²Ð»ÑÐµÐ¼ ÑÑ€ÐµÐ´Ð½ÑŽÑŽ Ñ‚Ð¾Ñ‡ÐºÑƒ Ð¼ÐµÐ¶Ð´Ñƒ i + 1 Ð¸ i + 2
            res.extend(self.get_points(ptn, self.count)) # Ð”Ð¾Ð¿Ð¾Ð»Ð½ÑÐµÑ‚ ÑÐ¿Ð¸ÑÐ¾Ðº ÑÐ»ÐµÐ¼ÐµÐ½Ñ‚Ð°Ð¼Ð¸ Ð¸Ð· ÑƒÐºÐ°Ð·Ð°Ð½Ð½Ð¾Ð³Ð¾ Ð¾Ð±ÑŠÐµÐºÑ‚Ð°.
        return res


# =======================================================================================
# Ð¤ÑƒÐ½ÐºÑ†Ð¸Ð¸ Ð¾Ñ‚Ñ€Ð¸ÑÐ¾Ð²ÐºÐ¸
# =======================================================================================
def draw_points(points, style="points", width=3, color=(255, 255, 255)):
    """Ñ„ÑƒÐ½ÐºÑ†Ð¸Ñ Ð¾Ñ‚Ñ€Ð¸ÑÐ¾Ð²ÐºÐ¸ Ñ‚Ð¾Ñ‡ÐµÐº Ð½Ð° ÑÐºÑ€Ð°Ð½Ðµ"""
    if style == "line":
        for p_n in range(-1, len(points) - 1):
            intp1, intp2 = points[p_n].int_pair(), points[p_n + 1].int_pair()
            pygame.draw.line(gameDisplay, color,
                             (intp1[0], intp1[1]),
                             (intp2[0], intp2[1]), width)

    elif style == "points":
        for p in points:
            intp = p.int_pair()
            pygame.draw.circle(gameDisplay, color,
                               (intp[0], intp[1]), width)

def draw_help():
    """Ñ„ÑƒÐ½ÐºÑ†Ð¸Ñ Ð¾Ñ‚Ñ€Ð¸ÑÐ¾Ð²ÐºÐ¸ ÑÐºÑ€Ð°Ð½Ð° ÑÐ¿Ñ€Ð°Ð²ÐºÐ¸ Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ñ‹"""
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["Q", "Speed Up"])
    data.append(["W", "Speed Down"])
    data.append(["D", "Delete last point"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))

def change_speed(speeds, change):
    for speed in speeds:
        speed[0] = 0.1 if speed[0] + change <= 0 else speed[0] + change 
        speed[1] = 0.1 if speed[1] + change <= 0 else speed[1] + change 

# =======================================================================================
# ÐžÑÐ½Ð¾Ð²Ð½Ð°Ñ Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ð°
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    points = []
    speeds = []
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)
    knt = Knot(points, steps)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    points = []
                    speeds = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0
                if event.key == pygame.K_d:
                    points.pop()
                if event.key == pygame.K_q:
                    change_speed(speeds, 1)
                if event.key == pygame.K_w:
                    change_speed(speeds, -1)

            if event.type == pygame.MOUSEBUTTONDOWN:
                points.append(Vec2d(event.pos))
                speeds.append([random.random() * 2, random.random() * 2])

        gameDisplay.fill((0, 0, 0)) # background color
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100) # (hue, saturation, lightness) alpha
        draw_points(points)
        knt.points = points
        draw_points(knt.get_knot(), "line", 3, color)
        if not pause:
            knt.set_points(speeds)
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
