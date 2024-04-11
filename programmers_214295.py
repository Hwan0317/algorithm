# https://school.programmers.co.kr/learn/courses/30/lessons/214295?language=python3


def count_points_in_circle(n, m, a: int, b: int, r: int) -> int:

    # 탐색할 좌표 평면 범위를 정의
    min_x = (a - r) if (a - r) >= 0 else 0
    max_x = (a + r) if (a + r) <= n else n
    min_y = (b - r) if (b - r) >= 0 else 0
    max_y = (b + r) if (b + r) <= m else m

    # 원 안에 포함되는 좌표 개수를 카운팅
    count = 0
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            # 좌표가 원 안에 포함되는지 확인
            if (x - a)**2 + (y - b)**2 <= (r)**2:
                count += 1

    return count

# 예시
n, m = 9999, 9999
a, b, r = 5, 5, 2

# 결과 출력
num_points = count_points_in_circle(n, m, a, b, r)
print(f"원 안에 포함되는 좌표 개수: {num_points}")
