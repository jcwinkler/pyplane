# -*- mode: python -*-

block_cipher = None


a = Analysis(['D:\\winkler\\Jan\\Projekte\\PyPlane\\pyplane\\main.py'],
             pathex=['c:\\Progs\\WinPython-32bit-3.5.2.2Qt5\\python-3.5.2\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'c:\\Progs\\WinPython-32bit-3.5.2.2Qt5\\python-3.5.2\\Lib\\site-packages\\zmq', 'D:\\winkler\\Jan\\Projekte\\PyPlane\\pyplane\\core', 'D:\\winkler\\Jan\\Projekte\\PyPlane\\pyplane'],
             binaries=[],
             datas=[],
             hiddenimports=['scipy.special._ufuncs_cxx', 'mpl_toolkits', 'scipy.linalg.cython_blas', 'scipy.linalg.cython_lapack', 'tkinter.filedialog'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='PyPlane',
          debug=False,
          strip=False,
          upx=True,
          console=True , icon='D:\\winkler\\Jan\\Projekte\\PyPlane\\pyplane\\resources\\pyplane_icon_32px.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='PyPlane')
