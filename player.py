import pygame
from constants import *
from circleshape import CircleShape
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, int(PLAYER_RADIUS * 0.5))
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        rad = self. radius * 2
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * rad / 1.5
        a = self.position + forward * rad
        b = self.position - forward * rad - right
        c = self.position - forward * rad + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity *= PLAYER_SHOT_SPEED
        shot.velocity = velocity
        self.timer = PLAYER_SHOOT_TIMER