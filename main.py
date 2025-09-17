import sys
import pygame

# 파이게임 라이브러리 초기화
pygame.init()

# 320x240 크기의 윈도우(게임 화면) 생성
surface = pygame.display.set_mode((320, 240))

# FPS(초당 프레임 수)를 관리하기 위한 Clock 객체 생성
fps = pygame.time.Clock()

# 게임 실행 상태를 저장하는 변수
running = True

# 게임 루프 시작
while running:
    # 매 프레임마다 이벤트를 확인
    for event in pygame.event.get():
        # 창의 닫기 버튼(X)을 눌렀을 때 실행 종료
        if event.type == pygame.QUIT:
            running = False

    # 화면 전체를 색상 선택 (RGB)
    surface.fill((0, 0, 0))

    # 화면 업데이트
    pygame.display.flip()

    # 초당 60프레임 속도 제한
    fps.tick(60)

# 게임 루프가 끝나면 pygame 종료
pygame.quit()

# 시스템 종료
sys.exit()
