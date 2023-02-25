import pygame
import random
import numpy as np
import math
import matplotlib.pyplot as plt
np.random.seed(42)

# 초기화
pygame.init()

#포인트
point = 0
graphd = []
grapht = []
# 창 설정
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")
#AI
Q = 0
qtlst= []
a = False
qlst = []
reward = 3
Qval = 0
new_x=0
distances = [0, 0, 0, 0]
new_y = 0
def get_distance(x, y):
    global rect_x
    global rect_y

    x1 = x
    y1 = y

    x2 = rect_x
    y2 = rect_y
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)



# 벽 생성
wall_thickness = 10
wall_color = (255, 255, 255)
wall_rects = [pygame.Rect(0, 0, width, wall_thickness),
              pygame.Rect(0, height - wall_thickness, width, wall_thickness),
              pygame.Rect(0, wall_thickness, wall_thickness, height - wall_thickness * 2),
              pygame.Rect(width - wall_thickness, wall_thickness, wall_thickness, height - wall_thickness * 2)]

# 랜덤한 위치에 사각형 생성
rect_size = 50
rect_color = (0, 255, 0)
rect_x = random.randint(wall_thickness + rect_size, width - wall_thickness - rect_size * 2)
rect_y = random.randint(wall_thickness + rect_size, height - wall_thickness - rect_size * 2)
rect = pygame.Rect(rect_x, rect_y, rect_size, rect_size)


#AI 정사각형 생성
ai_rect_size = 20
ai_rect_color = (255, 255, 0)
ai_rect_x = (wall_thickness + rect_size - ai_rect_size) // 2
ai_rect_y = (wall_thickness + rect_size - ai_rect_size) // 2
ai_rect = pygame.Rect(ai_rect_x, ai_rect_y, ai_rect_size, ai_rect_size)

#AI 움직임 함수 생성
def make_move_2_rect(x, y):
    global a
    global ai_rect
    global rect
    global move_speed
    global qlst
    qlst.append(50)
    a = True
    # Calculate the direction vector towards the target rectangle
    dx = rect.centerx - ai_rect.centerx
    dy = rect.centery - ai_rect.centery

    # Normalize the direction vector
    magnitude = math.sqrt(dx**2 + dy**2)
    if magnitude > 0:
        dx /= magnitude
        dy /= magnitude

    # Move the AI rectangle towards the target rectangle
    new_x = ai_rect.left + dx * move_speed
    new_y = ai_rect.top + dy * move_speed

    # Update the AI rectangle's position
    ai_rect.left = round(new_x)
    ai_rect.top = round(new_y)

#AI 움직임 함수 생성
def make_move(x, y):
    global new_x
    global new_y
    global ai_rect_color
    global distances
    global a
    global ai_rect
    global qlst
    global move_speed

    a  = False
    qlst.append(100)
    valid_moves = []

    if y > wall_thickness:
        valid_moves.append(0)  # 위로 이동 가능
    if y < height - wall_thickness - ai_rect_size:
        valid_moves.append(1)  # 아래로 이동 가능
    if x > wall_thickness:
        valid_moves.append(2)  # 왼쪽으로 이동 가능
    if x < width - wall_thickness - ai_rect_size:
        valid_moves.append(3)  # 오른쪽으로 이동 가능

    move_direction = np.random.choice(valid_moves)

    new_x, new_y = x, y
    if move_direction == 0:
        new_y -= move_speed
    elif move_direction == 1:
        new_y += move_speed
    elif move_direction == 2:
        new_x -= move_speed
    elif move_direction == 3:
        new_x += move_speed
    ai_rect.left = new_x
    ai_rect.top = new_y
############################################################################
############################################################################
# 초록 정사각형 생성
green_rect_size = 50
green_rect_color = (0, 255, 0)
green_rect_x = random.randint(wall_thickness + green_rect_size, width - wall_thickness - green_rect_size * 2)
green_rect_y = random.randint(wall_thickness + green_rect_size, height - wall_thickness - green_rect_size * 2)
green_rect = pygame.Rect(green_rect_x, green_rect_y, green_rect_size, green_rect_size)

# 이동 변수 설정
move_speed = 5
move_up = False
move_down = False
move_left = False
move_right = False


STOP = False
# 게임 루프 
while STOP != True:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            STOP = True

    Qchoice = random.randint(1, 100)
    if Qchoice > reward:
        make_move(round(ai_rect.left), round(ai_rect.top))
        distance = get_distance(round(ai_rect.left), round(ai_rect.top))
        graphd.append(round(distance))
    elif Qchoice <= reward:
        make_move_2_rect(round(ai_rect.left), round(ai_rect.top))
        distance = get_distance(round(ai_rect.left), round(ai_rect.top))
        graphd.append(round(distance))
    if a == True:
        print(distance, "\t", point, "\t" "Q")
    elif a == False:
        print(distance, "\t", point, "\t" "NOT")
    if point == 1000:
            break
    for i in range(len(graphd)):
        grapht.append(i)
    # 충돌 검사
    if ai_rect.colliderect(rect):
        rect_x = random.randint(wall_thickness + rect_size, width - wall_thickness - rect_size * 2)
        rect_y = random.randint(wall_thickness + rect_size, height - wall_thickness - rect_size * 2)
        rect = pygame.Rect(rect_x, rect_y, rect_size, rect_size)
        point +=1
        reward += random.randint(1, 3)
        
    if len(qlst) % 50 == 0:
        for i in qlst:
            if i == 100:
                Q += 1
        qtlst.append(round(Q / len(qlst) * 100))
    # 화면 그리기
    screen.fill((0, 0, 0))
    for wall in wall_rects:
        pygame.draw.rect(screen, wall_color, wall)
    pygame.draw.rect(screen, rect_color, rect)
    pygame.draw.rect(screen, ai_rect_color, ai_rect)
    pygame.display.flip()

print(qtlst)
# plot qlst
plt.plot(qtlst)
plt.title('Q values')
plt.xlabel('Iteration')
plt.ylabel('Q value')
plt.show()
