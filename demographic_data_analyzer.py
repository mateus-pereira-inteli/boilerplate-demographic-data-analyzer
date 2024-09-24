import pandas as pd

def calculate_demographic_data(print_data=True):
    # Carregar os dados do arquivo CSV
    df = pd.read_csv('adult.data.csv')

    # Quantidade de cada raça presente
    race_count = df['race'].value_counts()

    # Percentual de pessoas com Bachelors
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Nível de educação superior (Bachelors, Masters ou Doctorate)
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # Porcentagem de pessoas com nível superior que ganham mais de 50K
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)

    # Porcentagem de pessoas com nível inferior que ganham mais de 50K
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    # Idade média dos homens (arredondado)
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Porcentagem de pessoas que ganham mais de 50K
    percentage_rich = round((df['salary'] == '>50K').mean() * 100, 1)

    # País com a maior porcentagem de pessoas que ganham mais de 50K
    country_salary = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100)
    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = round(country_salary.max(), 1)

    # Horas mínimas trabalhadas
    min_work_hours = df['hours-per-week'].min()

    # Número de pessoas que trabalham as horas mínimas e ganham mais de 50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]['salary'].count()
    rich_percentage = round(
        (df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].shape[0] /
         df[df['hours-per-week'] == min_work_hours].shape[0]) * 100, 1)

    # Ocupação mais comum entre aqueles que ganham mais de 50K na Índia
    top_IN_occupation = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].value_counts().idxmax()

    if print_data:
        print("Contagem de raça:\n", race_count)
        print("Idade média dos homens:", average_age_men)
        print(f"Porcentagem com Bacharelado: {percentage_bachelors}%")
        print(f"Porcentagem com Bacharelado, Mestrado ou Doutorado que ganham mais de 50K: {higher_education_rich}%")
        print(f"Porcentagem sem educação superior que ganham mais de 50K: {lower_education_rich}%")
        print("Porcentagem total de pessoas que ganham mais de 50K:", percentage_rich)
        print("País com a maior porcentagem de pessoas que ganham mais de 50K:", highest_earning_country)
        print(f"Maior porcentagem de pessoas que ganham mais de 50K em um país: {highest_earning_country_percentage}%")
        print(f"Mínimo de horas trabalhadas por semana: {min_work_hours} horas")
        print(f"Porcentagem de pessoas ricas entre aqueles que trabalham as horas mínimas: {rich_percentage}%")
        print("Ocupação mais comum entre aqueles que ganham mais de 50K na Índia:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'percentage_rich': percentage_rich,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'top_IN_occupation': top_IN_occupation
    }
