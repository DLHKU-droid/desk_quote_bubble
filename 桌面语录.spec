# -*- mode: python ; coding: utf-8 -*-
# PyInstaller 打包配置
# macOS: pyinstaller 桌面语录.spec --clean  → dist/桌面语录.app
# Windows: pyinstaller 桌面语录.spec --clean → dist/桌面语录.exe

import sys

block_cipher = None

a = Analysis(
    ['lc_cat.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'akshare',
        'pandas',
        'pandas._libs.tslibs.base',
        'lxml',
        'lxml.etree',
        'lxml._elementpath',
        'bs4',
        'html5lib',
        'requests',
        'tqdm',
        'openpyxl',
        'xlrd',
        'jsonpath',
        'tabulate',
        'curl_cffi',
        'decorator',
        'urllib3',
        'tkinter',
        'tkinter.ttk',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    # 排除用不到的大型库，减小体积
    excludes=[
        'matplotlib',
        'scipy',
        'PIL',
        'IPython',
        'notebook',
        'jupyter',
        'PyQt5',
        'wx',
        'gi',
        'cv2',
        'torch',
        'tensorflow',
    ],
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
    name='桌面语录',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,       # 不弹出黑色命令行窗口
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# macOS 专用：生成 .app bundle
if sys.platform == 'darwin':
    app = BUNDLE(
        exe,
        name='桌面语录.app',
        icon=None,
        bundle_identifier='com.dlhku.desk-quote-bubble',
        info_plist={
            'NSPrincipalClass': 'NSApplication',
            'NSHighResolutionCapable': True,
            'LSUIElement': True,    # 不在 Dock 栏显示图标
            'CFBundleName': '桌面语录',
            'CFBundleDisplayName': '桌面语录',
            'CFBundleShortVersionString': '1.0.0',
        },
    )
