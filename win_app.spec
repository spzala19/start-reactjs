# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['app.py'],
             pathex=['F:/react-setup-automation-master1/react-setup-automation-master'],
             binaries=[],
             datas=[( 'F:/react-setup-automation-master1/react-setup-automation-master/images', 'images' ),('F:/react-setup-automation-master/react-setup-automation-master/commands.json','.')],
             hiddenimports=['Pillow'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='start-reactjs',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
	  icon = 'F:\\react-setup-automation-master1\\react-setup-automation-master\\images\\logo.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='start-reactjs')
