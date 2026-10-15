#часы и минуты
minutes = int(input("Введите количество минут: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print("Часы:", hours)
print("Минуты:", remaining_minutes)