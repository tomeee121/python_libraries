from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Employee(ABC):
    name: str
    id: int

    @abstractmethod
    def compute_pay(self) -> float:
        pass


@dataclass
class HourlyEmployee(Employee):
    name: str
    id: int
    commission: float = 100
    contracts_landed: float = 0
    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def compute_pay(self) -> float:
        return(
            self.commission * self.contracts_landed
        )
    
@dataclass
class SalariedEmployee(HourlyEmployee):
    commission: float = 100
    contracts_landed: float = 0
    monthly_salary: float = 0
    percentage: float = 1

    def compute_pay(self) -> float:
        return(
            super().compute_pay()+self.monthly_salary * self.percentage
        )
    
def main() -> None:
    """main function"""
    henry = HourlyEmployee('Henry', 1, 100, 3, 4, 300, 1000)
    natan = SalariedEmployee(100, 5, 4000, 1)

    print(f"{henry.name} landed nr of contracts: {henry.contracts_landed} and earned {henry.compute_pay()}")
    print(f"{natan.name} earned on monthly salary of {natan.monthly_salary} and earned {natan.compute_pay()}")


if __name__ == '__main__':
    main() 
