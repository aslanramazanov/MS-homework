import numpy as np, pandas as pd

# Обработка файла Excel и выделение из него столбца Sanit
sanit_df = pd.read_excel('Вариант 5.xlsx')
sanit = sanit_df['Sanit'].tolist()
print(sanit)

# Обработка данных и расчет значения статистики Колмогорова
f_zero = [i / 100 for i in sanit]
second_term_in_abs = [(2*i -1)/(2*len(sanit)) for i in sanit]

np_one = np.array(f_zero)
np_two = np.array(second_term_in_abs)
first_term_in_d_statistics = list(abs(np_one - np_two))

d_statistics = max(first_term_in_d_statistics) + 1/(2*(len(sanit)))

print("Значение статистики Колмогорова = ", d_statistics)

lambda_ = np.sqrt(len(sanit)-1) * d_statistics
print("lambda = ", lambda_)
