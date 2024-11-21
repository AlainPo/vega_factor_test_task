import typing as tp

from dataclasses import dataclass
from collections import deque, defaultdict


@dataclass
class NumbersStep:
    m: int
    n: int

    def next(self) -> int:
        return self.m ** 2 + self.n ** 2 + 1


@dataclass
class NumbersPath:
    a: int
    b: int
    steps: tp.Tuple[
        tp.List[NumbersStep], # steps for a
        tp.List[NumbersStep] # steps for b
    ]
    
    @staticmethod
    def sum(m: int, n: int) -> int:
        return m + n
    
    @staticmethod
    def sq_sum1(m: int, n: int) -> int:
        return m ** 2 + n ** 2 + 1


class Checker:
    def __init__(self, max_n: int) -> None:
        """
        Class to check hypothesis
        Args:
            max_n (int): N from the task description
        """
        self.N = max_n
        self.graph = defaultdict(set)

    def run_check(self) -> None:
        pass

    def generate_graph(self, N):
        """Генерирует граф с рёбрами по условиям задачи."""
        for m in range(N + 1):
            for n in range(m, N + 1 - m):

                a = m + n
                b = m**2 + n**2 + 1
                if a <= N:
                    self.graph[a].add((b, m, n))
                    self.graph[b].add((a, m, n))


    def check_path(self, path):
        """Перед тем, как вернуть путь, проверяем на соответствие условиям"""
        cur_a, cur_b = path.a, path.b
        for numbers_step in path.steps[0]: # check a
            if numbers_step.m + numbers_step.n != cur_a:
                return False                                  
            cur_a  = numbers_step.next()

        for numbers_step in path.steps[1]: # check b
            if numbers_step.m + numbers_step.n != cur_b:
                return False   
            cur_b = numbers_step.next()

        if cur_a != cur_b:
            return False
        return True

    
    def find_path(self, a, b):
        """Поиск пути между числами a и b с использованием BFS."""
        queue = deque([(a, [])])  # (текущее число, путь для a, путь для b)
        visited = set()

        while queue:
            current, path = queue.popleft()

            if current == b:
                # Найдено пересечение, возвращаем путь

                nums = []
                for step in path:
                    nums.append(step.m**2 + step.n**2+1)
                index = nums.index(max(nums))

                path_a = path[:index+1]
                path_b = path[index+1:][::-1]
                return NumbersPath(
                    a, b,
                    (path_a, path_b)
                )

            if current in visited:
                continue

            visited.add(current)

            # Обходим соседей
            for neighbor, m, n in self.graph[current]:
                if neighbor not in visited:
                    new_path = path.copy() + [NumbersStep(m, n)]
                    queue.append((neighbor, new_path))

        return None

    def get_path(self, a, b):
        """Возвращает путь между числами a и b."""
        N = self.N
        path = None
        while not path or not self.check_path(path):
            N*=2
            self.generate_graph(N)
            path = self.find_path(a, b) # возвращает NumberPath(a, b, steps=([NumbersStep], [NumbersStep]) )

        return path

    

        
