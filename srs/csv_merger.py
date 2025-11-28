import pandas as pd
import os
import glob


#  Путь
root_folder = " "
output_file = " "

# Находим все CSV файлы
csv_files = glob.glob(os.path.join(root_folder, "**", "*.csv"), recursive=True)
print(f"Найдено {len(csv_files)} файлов")

all_data = []

for file in csv_files:
    try:
        # Читаем файл
        df = pd.read_csv(file, sep=';', encoding='utf-16')
        
        # Удаляем пустые колонки
        df = df.dropna(axis=1, how='all')
        
       
        all_data.append(df)
        print(f" {os.path.basename(file)}: {len(df)} строк")
        
    except Exception as e:
        print(f" {os.path.basename(file)}: {e}")

# Объединяем и сохраняем
if all_data:
    result = pd.concat(all_data, ignore_index=True)
    result.to_csv(output_file, sep=';', index=False, encoding='utf-8')
    print(f"\n Объединено {len(result)} строк в {output_file}")
else:
    print(" Нет данных для объединения")