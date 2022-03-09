# Для запуска нужно  установить модули xlrd, openpyxl
import scipy.stats as st, pandas as pd, numpy as np

# Обработка файла Excel и выделение из него столбца Sanit
sanit_df = pd.read_excel('Вариант 5.xlsx')
sanit = sanit_df['Sanit'].tolist()
print(sanit)

# Среднее значение и стандартное отклонение доли людей с доступом к санитарному обслуживанию
mean_sanit = np.mean(sanit)
print("Среднее значение доли населения с доступом к санитарному обслуживанию = ", mean_sanit)

std_dev = st.tstd(sanit)
print("Стандартное отклонение = ", std_dev)

# Построение доверительного интервала
ci = st.t.interval(0.9, len(sanit)-1, loc=std_dev, scale=st.sem(sanit))
print("Доверительный интервал : ", ci)
