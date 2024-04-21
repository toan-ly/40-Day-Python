def calculate_can_chi_calendar(year):
  can = ('Canh', 'Tan', 'Nham', 'Quy', 'Giap', 'At', 'Binh', 'Dinh', 'Mau', 'Ky')
  chi = ('Than', 'Dau', 'Tuat', 'Hoi', 'Ty', 'Suu', 'Dan', 'Meo', 'Thin', 'Ty', 'Ngo', 'Mui')

  return f'{year}: {can[year%10]} {chi[year%12]}'

print(calculate_can_chi_calendar(2024))
print(calculate_can_chi_calendar(2023))
print(calculate_can_chi_calendar(1997))
print(calculate_can_chi_calendar(2000))