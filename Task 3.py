import numpy as np, pandas as pd, scipy.stats as st

# Обработка файла Excel и выделение из него столбцов
sanit_df = pd.read_excel('Вариант 5.xlsx')
sanit = sanit_df['Sanit'].tolist()

immun_df = pd.read_excel('Вариант 5.xlsx')
immun = sanit_df['Immun'].tolist()
print(sanit)
print(immun)

# Расчеты
mean_immun = np.mean(immun)
mean_sanit = np.mean(sanit)
disp_sanit = st.tstd(sanit)**2
disp_immun = st.tstd(immun)**2

teta = abs( (mean_sanit - mean_immun) / np.sqrt( disp_immun + disp_sanit) ) * np.sqrt(125)

print(teta)


# Расчеты: строим доверительный интервал для среднего значения разности наблюдений в двух выборках
#np_sanit = np.array(sanit)
#np_immun = np.array(immun)
#sanit_immun_difference = list(np_immun - np_sanit)

#mean_s_i_d = np.mean(sanit_immun_difference)

#ci = st.t.interval(0.9, len(sanit_immun_difference)-1, loc=mean_s_i_d, scale=st.sem(sanit_immun_difference))
#print(ci)
