import typing as tp
import numpy as np

from dataclasses import dataclass

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


    def run_check(self) -> None:
        # for a in range(1, self.N + 1):
        #     for b in range(a + 1, self.N + 1):
        #         path = self.get_path(a, b)

        #         cur_a, cur_b = a, b
        #         for numbers_step in path.steps[0]: # check a
        #             assert numbers_step.m + numbers_step.n == cur_a
        #             cur_a  = numbers_step.next()

        #         for numbers_step in path.steps[1]: # check b
        #             assert numbers_step.m + numbers_step.n == cur_b
        #             cur_b = numbers_step.next()

        #         assert cur_a == cur_b

        pass


    def iterate(self, a: int, values_a: list, list_a: list, path: list, depth: int=0, max_depth: int=5):
        if a > self.N**4 or depth > max_depth:
            return
        for m in range(0, a // 2 + 1):
            n = a - m
            next_value = NumbersPath.sq_sum1(m,n)

            new_path = path.copy()  # Создаем копию пути
            new_path.append(NumbersStep(m, n))  # Добавляем NumbersStep

            values_a.append(next_value)
            list_a.append([next_value, new_path])  # Сохраняем значение и путь
            self.iterate(next_value, values_a, list_a, new_path, depth+1)


    def get_path(self, a: int, b: int) -> NumbersPath:
        list_a = []
        list_b = []

        list_a.append([a, []])
        list_b.append([b, []])

        values_a = [a]
        values_b = [b]

        self.iterate(a, values_a, list_a, [])
        self.iterate(b, values_b, list_b, [])

        # Находим общие значения a и b
        common_values = list(set(values_a).intersection(values_b))

        if common_values:
            min_value = min(common_values)
            min_path_a = next((item[1] for item in list_a if item[0] == min_value), None)
            min_path_b = next((item[1] for item in list_b if item[0] == min_value), None)

            return NumbersPath(a, b, (min_path_a, min_path_b))
        else:
            print("Нет общих значений.")
            return None
        

        
