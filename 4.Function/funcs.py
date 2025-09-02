def is_even(value):
    """숫자가 짝수인지 확인"""
    return value % 2 == 0

def calculate_avg(numbers):
    """리스트의 평균값 계산"""
    if not numbers:  # 빈 리스트 확인
        return 0
    return sum(numbers) / len(numbers)  # sum() 내장함수 활용

def find_max(numbers):
    """리스트의 최댓값 찾기"""
    if not numbers:  # 빈 리스트 확인
        raise ValueError("빈 리스트에서는 최댓값을 찾을 수 없습니다")
    
    max_value = numbers[0]
    for num in numbers:  # 직접 순회 (더 효율적)
        if num > max_value:
            max_value = num
    return max_value

def find_min(numbers):
    """리스트의 최솟값 찾기"""
    if not numbers:  # 빈 리스트 확인
        raise ValueError("빈 리스트에서는 최솟값을 찾을 수 없습니다")
    
    min_value = numbers[0]
    for num in numbers:  # 직접 순회
        if num < min_value:
            min_value = num
    return min_value