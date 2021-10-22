# -*- mode: python ; coding: utf-8 -*-
# use with this command : pyinstaller main_cli.spec --onefile --clean

block_cipher = None

import gooey
gooey_root = os.path.dirname(gooey.__file__)
gooey_languages = Tree(os.path.join(gooey_root, 'languages'), prefix = 'gooey/languages')
gooey_images = Tree(os.path.join(gooey_root, 'images'), prefix = 'gooey/images')

a = Analysis(['med_to_csv/main_gui.py'],
             datas = [('med_to_csv/img', 'img')],
             pathex=['c:\\Python3\\Scripts'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             )
pyz = PYZ(a.pure)

options = [('u', None, 'OPTION'), ('u', None, 'OPTION'), ('u', None, 'OPTION')]

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          options,
          gooey_languages, # Add them in to collected files
          gooey_images, # Same here.
          name='portable_med_to_csv_gui',
          debug=False,
          strip=None,
          upx=False,
          console=False,
          windowed=True,
          icon=os.path.join(gooey_root, 'images', 'program_icon.ico'))

app = BUNDLE(exe,
         name='portable_med_to_csv_gui.app',
         bundle_identifier=None)