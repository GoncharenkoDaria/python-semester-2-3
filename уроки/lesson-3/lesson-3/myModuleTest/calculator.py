def plus(a: float, b: float) -> float:
  return a + b


def minus(a: float, b: float) -> float:
  return a - b


def mult(a: float, b: float) -> float:
  return a * b


def div(a: float, b: float) -> float:
  return a / b


# Использовать модуль как самостоятельную единицу
if __name__ == "__main__":
  print(f"3 + 20 = ${plus(3, 20)}")
