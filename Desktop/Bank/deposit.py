# Модуль для расчета депозитов

def calculate_simple(amount, rate, years):
    """Расчет простых процентов"""
    return amount * (1 + rate/100 * years)

def calculate_compound(amount, rate, years):
    """Расчет сложных процентов"""
    return amount * (1 + rate/100) ** years

# Пример использования
if __name__ == "__main__":
    amount = 100000  # сумма вклада
    rate = 10        # годовая ставка
    years = 3        # срок
    
    simple = calculate_simple(amount, rate, years)
    compound = calculate_compound(amount, rate, years)
    
    print(f"Начальная сумма: {amount} руб.")
    print(f"Простые проценты: {simple:.2f} руб.")
    print(f"Сложные проценты: {compound:.2f} руб.")
