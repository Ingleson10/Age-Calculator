from datetime import date

def calculate_age(date_nasciment):
    today = date.today()
    year_nasciment = date_nasciment.year
    age = today.year - year_nasciment

    if today.month < date_nasciment.month or (today.month == date_nasciment.month and today.day < date_nasciment.day):
        age -= 1
    return age

date_nasciment = date(2000, 1, 25)
age = calculate_age(date_nasciment)

print(f'Sua idade é: {age} anos')