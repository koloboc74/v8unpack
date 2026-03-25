import PyInstaller.__main__
import os

# Создаем спецификацию для сборки
spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['source.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('../src/v8unpack', 'v8unpack'),
    ],
    hiddenimports=[
        'tqdm',
        'v8unpack',
        'v8unpack.v8unpack',
        'v8unpack.decoder',
        'v8unpack.metadata_types',
        'v8unpack.helper',
        'v8unpack.index',
        'v8unpack.MetaObject',
        'v8unpack.MetaObject.Configuration',
        'v8unpack.MetaObject.ConfigurationExtension',
        'v8unpack.MetaObject.ExternalDataProcessor',
        'v8unpack.MetaObject.ExternalReport',
        'v8unpack.MetaObject.Catalog',
        'v8unpack.MetaObject.Document',
        'v8unpack.MetaObject.Report',
        'v8unpack.MetaObject.DataProcessor',
        'v8unpack.MetaObject.CommonModule',
        'v8unpack.MetaObject.Subsystem',
        'multiprocessing',
        'multiprocessing.spawn',
        'multiprocessing.popen_spawn_win32',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='v8unpack',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
'''

with open('v8unpack.spec', 'w', encoding='utf-8') as f:
    f.write(spec_content)

print("Spec файл создан: v8unpack.spec")

# Теперь собираем с использованием spec файла
PyInstaller.__main__.run([
    'v8unpack.spec',
    '--clean',
    '--distpath', './dist',
    '--workpath', './build',
])

print("\nСборка завершена! Файл в папке ./dist/")
