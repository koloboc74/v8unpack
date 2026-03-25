import PyInstaller.__main__
import os
import sys

# Получаем директорию скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

print("Сборка v8unpack...")
print(f"Рабочая директория: {os.getcwd()}")

PyInstaller.__main__.run([
    'source.py',
    '--name=v8unpack',
    '--onefile',
    '--collect-all=v8unpack',
    '--hidden-import=tqdm',
    '--hidden-import=multiprocessing',
    '--hidden-import=multiprocessing.spawn',
    '--copy-metadata=v8unpack',
    '--clean',
])

# Копируем результат в удобное место
if os.path.exists('./dist/v8unpack'):
    print("\n✓ Сборка успешна!")
    print(f"Файл: {os.path.abspath('./dist/v8unpack')}")
else:
    print("\n✗ Ошибка сборки!")
