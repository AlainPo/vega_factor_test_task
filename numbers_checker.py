import typing as tp

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

        pass


    def iterate(self, values_n: list, list_n: list):
        for a in values_n[-1]:
            vals_a_i = []
            for m in range (0, a//2+1):
                n = a - m
                next_value = NumbersPath.sq_sum1(m,n)
                path_a = next((item[1] for item in list_n if item[0] == a), [])  # Создаем копию пути
                new_path_a = path_a.copy()
                new_path_a.append(NumbersStep(m, n))  # Добавляем NumbersStep
                vals_a_i.append(next_value)
                list_n.append([next_value, new_path_a])  # Сохраняем значение и путь
            values_n.append(vals_a_i)

        return values_n, list_n

    def find_intersection(self, values_a: list, list_a: list, values_b: list, list_b: list):
        set_a = set(sum(values_a, []))
        set_b = set(sum(values_b, []))
        while not list(set_a.intersection(set_b)):
            values_a, list_a = self.iterate(values_a, list_a)
            values_b, list_b = self.iterate(values_b, list_b)

            set_a = set(sum(values_a, []))
            set_b = set(sum(values_b, []))
            
        common_values = list(set_a.intersection(set_b))
        min_value = min(common_values)
        min_path_a = next((item[1] for item in list_a if item[0] == min_value), None)
        min_path_b = next((item[1] for item in list_b if item[0] == min_value), None)
        
        return (min_path_a, min_path_b)

    def get_path(self, a: int, b: int) -> NumbersPath:
        list_a = []
        list_b = []

        list_a.append([a, []])
        list_b.append([b, []])

        values_a = [[a]]
        values_b = [[b]]

        (min_path_a, min_path_b) = self.find_intersection(values_a, list_a, values_b, list_b) 

        return NumbersPath(a, b, (min_path_a, min_path_b))
        

        
