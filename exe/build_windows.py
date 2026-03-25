# Сборка v8unpack под Windows
# Запускать на Windows машине с установленным Python 3.8+

import PyInstaller.__main__
import os
import sys

print("=" * 60)
print("Сборка v8unpack для Windows")
print("=" * 60)

# Проверяем что запускаем на Windows
if os.name != 'nt':
    print("ВНИМАНИЕ: Этот скрипт предназначен для Windows!")
    print(f"Текущая ОС: {os.name}")

PyInstaller.__main__.run([
    'source.py',
    '--name=v8unpack',
    '--onefile',
    '--console',
    '--collect-all=v8unpack',
    '--hidden-import=tqdm',
    '--hidden-import=multiprocessing',
    '--hidden-import=multiprocessing.spawn',
    '--hidden-import=multiprocessing.popen_spawn_win32',
    '--copy-metadata=v8unpack',
    '--clean',
    '--noconfirm',
])

print("\n" + "=" * 60)
if os.path.exists('./dist/v8unpack.exe'):
    print("✓ Сборка успешна!")
    print(f"Файл: {os.path.abspath('./dist/v8unpack.exe')}")
    print(f"Размер: {os.path.getsize('./dist/v8unpack.exe') / 1024 / 1024:.1f} MB")
else:
    print("✗ Ошибка сборки!")
print("=" * 60)
