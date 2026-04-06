from pathlib import Path
import shutil, yaml, re, textwrap

root = Path('/tmp/rakdoc_rework/rak/rak-wisblock-boards')
zephyr_doc = Path('/tmp/rakdoc_rework/zephyrzip/zephyr-main/doc')

doc = root / 'doc'
if doc.exists():
    shutil.rmtree(doc)
(doc / '_scripts').mkdir(parents=True)

# Copy exact Zephyr static/template assets for style parity
shutil.copytree(zephyr_doc / '_static', doc / '_static')
shutil.copytree(zephyr_doc / '_templates', doc / '_templates')

# helper

def title(text, ch):
    return text + '\n' + (ch * len(text)) + '\n\n'

def sanitize_features(features):
    result = []
    for feat in features or []:
        if not isinstance(feat, str):
            continue
        parts = [p.strip() for p in re.split(r'\s+-\s+|\s{2,}-\s*', feat) if p.strip()]
        if not parts:
            continue
        result.extend(parts)
    dedup = []
    for f in result:
        if f not in dedup:
            dedup.append(f)
    return dedup

board_dirs = sorted((root / 'boards' / 'rakwireless').iterdir())
shield_dirs = sorted((root / 'boards' / 'shields').iterdir())
boards = []
shields = []

for bdir in board_dirs:
    if not bdir.is_dir():
        continue
    byml = bdir / 'board.yml'
    if not byml.exists():
        continue
    board_meta = yaml.safe_load(byml.read_text())['board']
    targets = []
    supported = []
    yaml_files = sorted(bdir.glob('*.yaml'))
    for yf in yaml_files:
        data = yaml.safe_load(yf.read_text()) or {}
        ident = data.get('identifier')
        if ident:
            targets.append(ident)
        supported.extend(data.get('supported', []))
    targets = list(dict.fromkeys(targets))
    supported = sanitize_features(supported)
    boards.append({
        'dir': bdir,
        'name': bdir.name,
        'full_name': board_meta.get('full_name', bdir.name),
        'vendor': board_meta.get('vendor', 'rakwireless'),
        'socs': [s['name'] for s in board_meta.get('socs', [])],
        'targets': targets,
        'features': supported,
    })

for sdir in shield_dirs:
    if not sdir.is_dir():
        continue
    syml = sdir / 'shield.yml'
    if not syml.exists():
        continue
    smeta = yaml.safe_load(syml.read_text())['shield']
    features = sanitize_features(smeta.get('supported_features', []))
    shields.append({
        'dir': sdir,
        'name': sdir.name,
        'full_name': smeta.get('full_name', sdir.name),
        'vendor': smeta.get('vendor', 'rakwireless'),
        'features': features,
    })

board_overrides = {
    'rak11310': 'RAK11310 is a WisBlock Core module based on the RP2040. This temporary page is provided so the board can be indexed and rendered in a Zephyr-style documentation tree.',
    'rak11722': 'RAK11722 is a WisBlock LPWAN Core module. This temporary page is provided so the board can be indexed and rendered in a Zephyr-style documentation tree.',
    'rak19026': 'RAK19026 is a WisMesh Base Board that combines a WisBlock Core-compatible design with on-board peripherals such as GNSS, accelerometer, and OLED support. This temporary page is provided so the board can be indexed and rendered in a Zephyr-style documentation tree.',
    'rak3312': 'RAK3312 is a WisDuo LPWAN + BLE + Wi-Fi module family with multiple CPU targets. This temporary page is provided so the board can be indexed and rendered in a Zephyr-style documentation tree.',
    'rak3372': 'RAK3372 is a WisBlock LPWAN Core module based on STM32WLE5xx. This temporary page is provided so the board can be indexed and rendered in a Zephyr-style documentation tree.',
    'rak3401': 'RAK3401 is a WisBlock BLE Core module. This temporary page is provided so the board can be indexed and rendered in a Zephyr-style documentation tree.',
    'rak4631re': 'RAK4631re is a WisBlock LoRaWAN Core module. This temporary page is provided so the board can be indexed and rendered in a Zephyr-style documentation tree.',
}

shield_overrides = {
    'rakwireless_rak19001': 'RAK19001 is a WisBlock Dual IO Base Board.',
    'rakwireless_rak19003': 'RAK19003 is a WisBlock Mini Base Board.',
    'rakwireless_rak19007': 'RAK19007 is a 2nd generation WisBlock Base Board.',
    'rakwireless_rak19009': 'RAK19009 is a WisBlock Mini Base Board with a Power Slot.',
    'rakwireless_rak19010': 'RAK19010 is a WisBlock Base Board with a Power Slot.',
    'rakwireless_rak19011': 'RAK19011 is a WisBlock Base Board with a Power Slot and extended slots.',
    'rakwireless_rak19012': 'RAK19012 is a WisBlock LiPo Battery Power Slot module.',
    'rakwireless_rak19013': 'RAK19013 is a WisBlock solar battery Power Slot module.',
    'rakwireless_rak19014': 'RAK19014 is a WisBlock USB LiPo Power Slot module.',
    'rakwireless_rak19015': 'RAK19015 is a WisBlock button cell Power Slot module.',
    'rakwireless_rak19017': 'RAK19017 is a WisBlock PoE Power Slot module.',
}

# Create temporary board and shield docs in their own source directories
for b in boards:
    docdir = b['dir'] / 'doc'
    docdir.mkdir(exist_ok=True)
    rst = []
    rst.append(title(b['full_name'], '#'))
    rst.append(title('Overview', '*'))
    rst.append(board_overrides.get(b['name'], f"{b['full_name']} temporary documentation page."))
    rst.append('\n\n')
    rst.append(title('Hardware', '*'))
    rst.append(f"- Vendor: ``{b['vendor']}``\n")
    if b['socs']:
        rst.append(f"- SoC(s): ``{', '.join(b['socs'])}``\n")
    if b['targets']:
        rst.append(f"- Zephyr target(s): ``{', '.join(b['targets'])}``\n")
    rst.append(f"- Source directory: ``boards/rakwireless/{b['name']}``\n\n")
    rst.append(title('Supported Features', '='))
    if b['features']:
        for feat in b['features']:
            rst.append(f"- ``{feat}``\n")
    else:
        rst.append('This temporary page does not list supported features yet.\n')
    rst.append('\n')
    rst.append(title('Building', '*'))
    if b['targets']:
        rst.append('Example build commands::\n\n')
        for t in b['targets']:
            rst.append(f"   west build -b {t} samples/hello_world\n")
    else:
        rst.append('Build command example::\n\n')
        rst.append(f"   west build -b {b['name']} samples/hello_world\n")
    rst.append('\n')
    rst.append(title('Source Files', '*'))
    for f in sorted(p.name for p in b['dir'].iterdir() if p.is_file() and p.suffix in {'.dts', '.dtsi', '.yaml', '.yml', '.cmake', '.defconfig'} or p.name.startswith('Kconfig')):
        rst.append(f"- ``boards/rakwireless/{b['name']}/{f}``\n")
    rst.append('\n')
    rst.append(title('References', '*'))
    rst.append('This page is intentionally minimal and exists to validate Zephyr-style web documentation rendering for the board.\n')
    (docdir / 'index.rst').write_text(''.join(rst))

for s in shields:
    docdir = s['dir'] / 'doc'
    docdir.mkdir(exist_ok=True)
    rst = []
    rst.append(title(s['full_name'], '#'))
    rst.append(title('Overview', '*'))
    rst.append(shield_overrides.get(s['name'], f"{s['full_name']} temporary documentation page."))
    rst.append(' This temporary page exists so the shield can be rendered in the Zephyr-style documentation tree.\n\n')
    rst.append(title('Hardware', '*'))
    rst.append(f"- Vendor: ``{s['vendor']}``\n")
    rst.append(f"- Source directory: ``boards/shields/{s['name']}``\n\n")
    rst.append(title('Supported Features', '='))
    if s['features']:
        for feat in s['features']:
            rst.append(f"- ``{feat}``\n")
    else:
        rst.append('This temporary page does not list supported features yet.\n')
    rst.append('\n')
    rst.append(title('Build Usage', '*'))
    rst.append('Example build command::\n\n')
    rst.append(f"   west build -b rak4631re --shield {s['name']} samples/hello_world\n\n")
    rst.append(title('Source Files', '*'))
    for f in sorted(p.name for p in s['dir'].iterdir() if p.is_file()):
        rst.append(f"- ``boards/shields/{s['name']}/{f}``\n")
    rst.append('\n')
    rst.append(title('References', '*'))
    rst.append('This page is intentionally minimal and exists to validate Zephyr-style web documentation rendering for the shield.\n')
    (docdir / 'index.rst').write_text(''.join(rst))

# Makefile and conf.py
(doc / 'requirements.txt').write_text('sphinx\nsphinx_rtd_theme\n')
(doc / 'Makefile').write_text(textwrap.dedent('''\
# ------------------------------------------------------------------------------
# Minimal Zephyr-style documentation build
# SPDX-License-Identifier: Apache-2.0

SPHINXBUILD ?= sphinx-build
SOURCEDIR   = .
BUILDDIR    = _build
SPHINXOPTS ?= -j auto -W --keep-going

.PHONY: html clean

html:
	$(SPHINXBUILD) -M html $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS)

clean:
	rm -rf $(BUILDDIR)
'''))
(doc / 'conf.py').write_text(textwrap.dedent('''\
# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
import sys

DOC_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = DOC_DIR.parent

project = 'RAK WisBlock Boards Documentation'
author = 'RAKwireless'
version = 'latest'
release = version
root_doc = 'index'
master_doc = root_doc
extensions = [
    'sphinx.ext.todo',
]
templates_path = ['_templates']
exclude_patterns = ['_build']
source_suffix = '.rst'
pygments_style = 'sphinx'
highlight_language = 'none'
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
    'prev_next_buttons_location': None,
    'navigation_depth': 5,
}
html_title = 'Zephyr Project Documentation'
html_logo = str(DOC_DIR / '_static' / 'images' / 'logo.svg')
html_favicon = str(DOC_DIR / '_static' / 'images' / 'favicon.png')
html_static_path = ['_static']
html_last_updated_fmt = '%b %d, %Y'
html_domain_indices = False
html_split_index = True
html_show_sourcelink = False
html_show_sphinx = False
html_context = {
    'show_license': True,
    'docs_title': 'Docs / Latest',
    'is_release': False,
    'current_version': version,
    'versions': (
        ('latest', '/'),
    ),
    'reference_links': {},
}

def setup(app):
    app.add_css_file('css/custom.css')
    app.add_js_file('js/custom.js')
'''))

# top-level doc tree
(doc / 'boards' / 'rakwireless').mkdir(parents=True)
(doc / 'shields').mkdir(parents=True)
(doc / 'index.rst').write_text(
    title('RAK WisBlock Boards and Shields', '=') +
    'This documentation tree is intentionally minimal. It reuses the Zephyr documentation static assets and templates so that boards and shields from ``rak-wisblock-boards`` render with the same overall web style as Zephyr documentation.\n\n' +
    '.. toctree::\n   :maxdepth: 2\n   :caption: Boards and Shields\n\n   boards/index\n   shields/index\n'
)

boards_index = title('Boards', '=') + 'Supported RAKwireless boards included in this repository.\n\n.. toctree::\n   :maxdepth: 1\n\n'
for b in boards:
    boards_index += f'   rakwireless/{b["name"]}\n'
(doc / 'boards' / 'index.rst').write_text(boards_index)

for b in boards:
    rel = f'../../boards/rakwireless/{b["name"]}/doc/index.rst'
    (doc / 'boards' / 'rakwireless' / f'{b["name"]}.rst').write_text(f'.. include:: {rel}\n')

shields_index = title('Shields', '=') + 'Supported RAKwireless shields included in this repository.\n\n.. toctree::\n   :maxdepth: 1\n\n'
for s in shields:
    shields_index += f'   {s["name"]}\n'
(doc / 'shields' / 'index.rst').write_text(shields_index)

for s in shields:
    rel = f'../../boards/shields/{s["name"]}/doc/index.rst'
    (doc / 'shields' / f'{s["name"]}.rst').write_text(f'.. include:: {rel}\n')

# generation script for reproducibility
(doc / '_scripts' / 'generate_docs.py').write_text(Path(__file__).read_text())
print('generated', len(boards), 'boards and', len(shields), 'shields')
