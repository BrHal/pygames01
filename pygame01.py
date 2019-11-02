#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
From Youtube tutorial "PyGame Tutorial" by Tech with Tim.

A simple pygame.

"""
import os

import pygame

pygame.init()

screen_width = 500
screen_height = 480

win = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption("pygame01")
resource_path = os.path.join(os.path.dirname(__file__), 'resources')
bg = pygame.image.load(os.path.join(resource_path, 'bg.jpg'))


class Player(object):
    """
    Player class.

    It handles player moves and drawing

    """

    walkRight = [
        pygame.image.load(os.path.join(resource_path, 'R1.png')),
        pygame.image.load(os.path.join(resource_path, 'R2.png')),
        pygame.image.load(os.path.join(resource_path, 'R3.png')),
        pygame.image.load(os.path.join(resource_path, 'R4.png')),
        pygame.image.load(os.path.join(resource_path, 'R5.png')),
        pygame.image.load(os.path.join(resource_path, 'R6.png')),
        pygame.image.load(os.path.join(resource_path, 'R7.png')),
        pygame.image.load(os.path.join(resource_path, 'R8.png')),
        pygame.image.load(os.path.join(resource_path, 'R9.png'))
    ]
    walkLeft = [
        pygame.image.load(os.path.join(resource_path, 'L1.png')),
        pygame.image.load(os.path.join(resource_path, 'L2.png')),
        pygame.image.load(os.path.join(resource_path, 'L3.png')),
        pygame.image.load(os.path.join(resource_path, 'L4.png')),
        pygame.image.load(os.path.join(resource_path, 'L5.png')),
        pygame.image.load(os.path.join(resource_path, 'L6.png')),
        pygame.image.load(os.path.join(resource_path, 'L7.png')),
        pygame.image.load(os.path.join(resource_path, 'L8.png')),
        pygame.image.load(os.path.join(resource_path, 'L9.png'))
    ]
    idle = pygame.image.load(os.path.join(resource_path, 'standing.png'))

    def __init__(self, x, y, width, height):
        """Player init sets attributes."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True

    def draw(self, win):
        """Display player on win."""
        if not self.standing:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
            if self.left:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.left:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            elif self.right:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            else:
                win.blit(self.idle, (self.x, self.y))
        self.hitbox = (self.x + 18, self.y + 12, 30, 50)
        # pygame.draw.rect(win, (255, 255, 0, 10), self.hitbox, 2)


class Enemy(object):
    """
    Enemy class.

    It handles foo moves and drawing

    """

    walkRight = [
        pygame.image.load(os.path.join(resource_path, 'R1E.png')),
        pygame.image.load(os.path.join(resource_path, 'R2E.png')),
        pygame.image.load(os.path.join(resource_path, 'R3E.png')),
        pygame.image.load(os.path.join(resource_path, 'R4E.png')),
        pygame.image.load(os.path.join(resource_path, 'R5E.png')),
        pygame.image.load(os.path.join(resource_path, 'R6E.png')),
        pygame.image.load(os.path.join(resource_path, 'R7E.png')),
        pygame.image.load(os.path.join(resource_path, 'R8E.png')),
        pygame.image.load(os.path.join(resource_path, 'R9E.png')),
        pygame.image.load(os.path.join(resource_path, 'R10E.png')),
        pygame.image.load(os.path.join(resource_path, 'R11E.png'))
    ]
    walkLeft = [
        pygame.image.load(os.path.join(resource_path, 'L1E.png')),
        pygame.image.load(os.path.join(resource_path, 'L2E.png')),
        pygame.image.load(os.path.join(resource_path, 'L3E.png')),
        pygame.image.load(os.path.join(resource_path, 'L4E.png')),
        pygame.image.load(os.path.join(resource_path, 'L5E.png')),
        pygame.image.load(os.path.join(resource_path, 'L6E.png')),
        pygame.image.load(os.path.join(resource_path, 'L7E.png')),
        pygame.image.load(os.path.join(resource_path, 'L8E.png')),
        pygame.image.load(os.path.join(resource_path, 'L9E.png')),
        pygame.image.load(os.path.join(resource_path, 'L10E.png')),
        pygame.image.load(os.path.join(resource_path, 'L11E.png'))

    ]

    def __init__(self, x, y, width, height, end):
        """Enemy init sets attributes."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.vel = 3
        self.end = end
        self.walkCount = 0
        self.path = [self.x, self.end]
        self.hitbox = (self.x + 18, self.y, 30, 60)
        self.health = 10
        self.visible = True

    def draw(self, win):
        if self.visible:
            self.move()
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
            self.hitbox = (self.x + 18, self.y, 30, 60)
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 40, 4))
            pygame.draw.rect(win, (255, 255, 0),
                             (self.hitbox[0], self.hitbox[1] - 20, 40 - (4 * (10 - self.health)), 4))

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
        else:
            if self.x + self.vel > self.path[0]:

                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.visible = False


def collide(box1, box2):
    """
    Compute boxes intersection.

    If intersection is positive return True

    """
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[0] + box1[2], box2[0] + box2[2])
    y2 = min(box1[1] + box1[3], box2[1] + box2[3])
    return x1 < x2 and y1 < y2


class Bullet(object):
    """This is the Bullet class."""

    rightbullet = pygame.image.load(os.path.join(resource_path, 'RBul1.png'))
    leftbullet = pygame.image.load(os.path.join(resource_path, 'LBul1.png'))

    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 8 * facing
        if facing > 0:
            self.img = self.rightbullet
        else:
            self.img = self.leftbullet
            self.x -= 10
        self.hitbox = (self.x, self.y, 20, 16)

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        self.hitbox = (self.x, self.y, 20, 16)
        # pygame.draw.rect(win, (255, 0, 255), self.hitbox, 2)


def redraw_window():
    """Refresh UI."""
    win.blit(bg, (0, 0))
    text = font.render('Score : %d ' % score, 1, (0, 0, 0))
    win.blit(text, (360, 10))
    for bullet in bullets:
        bullet.draw(win)
    for goblin in goblins:
        goblin.draw(win)
    man.draw(win)
    pygame.display.update()


man = Player(50, 418, 64, 64)
bullets = []
goblins = []
run = True
enemybirth = 0
enemyfreq = 100
enemyheight = 0
shootLoop = 0
score = 0
font = pygame.font.SysFont('comicsans', 30, True)

while run:
    clock.tick(25)
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 5:
        shootLoop = 0
    enemybirth += 1
    if enemybirth >= enemyfreq:
        enemybirth = 0
        goblins.append(Enemy(0, 424 - enemyheight, 64, 64, screen_width - 64))
        enemyheight += 10
        if enemyheight > 300:
            enemyheight = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets[::-1]:
        for goblin in goblins[::-1]:
            if collide(bullet.hitbox, goblin.hitbox):
                bullets.pop(bullets.index(bullet))
                goblin.hit()
                score += 1
                break
        if bullet.x < screen_width and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    for goblin in goblins[::-1]:
        if not goblin.visible:
            goblins.pop(goblins.index(goblin))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and len(bullets) < 5000 and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
        bullets.append(
            Bullet(
                int(man.x + man.width // 2),
                int(man.y + man.height // 2),
                facing)
        )
        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > 0:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x + man.width < screen_width:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
    #        man.walkCount = 0

    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True
    #                man.walkCount = 0

    else:
        if man.jumpCount >= -10:
            if man.jumpCount > 0:
                neg = 1
            else:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 1.1 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redraw_window()
    if keys[pygame.K_ESCAPE]:
        run = False

pygame.quit()
