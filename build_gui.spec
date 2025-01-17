# -*- mode: python ; coding: utf-8 -*-

import os
import platform
import gooey

block_cipher = None

# Chemins Gooey
gooey_root = os.path.dirname(gooey.__file__)
gooey_languages = Tree(os.path.join(gooey_root, 'languages'), prefix='gooey/languages')
gooey_images = Tree(os.path.join(gooey_root, 'images'), prefix='gooey/images')

# Configuration de base
a = Analysis(
    ['med_to_csv/main_gui.py'],
    pathex=[],
    binaries=[],
    datas=[('med_to_csv/img', 'img')],
    hiddenimports=[],
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
    gooey_languages,
    gooey_images,
    [],
    name='portable_med_to_csv_gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=os.path.join(gooey_root, 'images', 'program_icon.ico')
)

# Bundle pour macOS uniquement
if platform.system() == 'Darwin':
    app = BUNDLE(
        exe,
        name='portable_med_to_csv_gui.app',
        icon=os.path.join(gooey_root, 'images', 'program_icon.ico'),
        bundle_identifier=None,
    )