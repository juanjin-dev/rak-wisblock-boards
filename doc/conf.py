# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
import importlib.util
import os
import sys

DOC_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = DOC_DIR.parent
ZEPHYR_BASE = Path(os.environ.get("ZEPHYR_BASE", PROJECT_ROOT)).resolve()

sys.path[:0] = [
    str(DOC_DIR / "_scripts"),
    str(ZEPHYR_BASE / "scripts"),
    str(ZEPHYR_BASE / "scripts" / "west_commands"),
    str(ZEPHYR_BASE / "scripts" / "dts" / "python-devicetree" / "src"),
    str(ZEPHYR_BASE / "doc" / "_scripts"),
    str(ZEPHYR_BASE / "doc" / "_extensions"),
]

# Ensure Zephyr's domain extension imports the module-local board catalog helper,
# which tolerates out-of-tree board/shield images.
_local_gbc = DOC_DIR / "_scripts" / "gen_boards_catalog.py"
_spec = importlib.util.spec_from_file_location("gen_boards_catalog", _local_gbc)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
sys.modules["gen_boards_catalog"] = _mod

project = "RAK WisBlock Boards Documentation"
author = "RAKwireless"
version = "latest"
release = version
root_doc = "index"
master_doc = root_doc

extensions = [
    "sphinx.ext.todo",
    "zephyr.application",
    "zephyr.domain",
    "zephyr.external_content",
    "zephyr.gh_utils",
    "zephyr.link-roles",
]

templates_path = [str(ZEPHYR_BASE / "doc" / "_templates"), "_templates"]
exclude_patterns = [
    "_build",
    "404.rst",
    "LICENSING.rst",
    "glossary.rst",
    "index-tex.rst",
    "kconfig.rst",
    "build/**",
    "connectivity/**",
    "contribute/**",
    "develop/**",
    "hardware/**",
    "introduction/**",
    "kernel/**",
    "project/**",
    "releases/**",
    "safety/**",
    "security/**",
    "services/**",
    "templates/**",
    "boards/rakwireless/**",
    "boards/shields/**",
    "shields/rakwireless_*.rst",
]
source_suffix = ".rst"
pygments_style = "sphinx"
highlight_language = "none"
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "logo_only": True,
    "prev_next_buttons_location": None,
    "navigation_depth": 5,
}
html_title = "Zephyr Project Documentation"
html_logo = str(ZEPHYR_BASE / "doc" / "_static" / "images" / "logo.svg")
html_favicon = str(ZEPHYR_BASE / "doc" / "_static" / "images" / "favicon.png")
html_static_path = [str(ZEPHYR_BASE / "doc" / "_static"), "_static"]
html_last_updated_fmt = "%b %d, %Y"
html_domain_indices = False
html_split_index = True
html_show_sourcelink = False
html_show_sphinx = False
html_context = {
    "show_license": True,
    "docs_title": "Docs / Latest",
    "is_release": False,
    "current_version": version,
    "versions": (("latest", "/"),),
    "reference_links": {},
    "display_gh_links": False,
}

extra_modules = [str(PROJECT_ROOT)]
existing_extra = os.environ.get("ZEPHYR_EXTRA_MODULES")
if existing_extra:
    extra_modules.extend(p for p in existing_extra.split(";") if p)
os.environ["ZEPHYR_EXTRA_MODULES"] = ";".join(dict.fromkeys(extra_modules))

external_content_contents = []
external_content_keep = ["**/*"]
zephyr_generate_hw_features = False


def _register_template_filters(app):
    env = app.builder.templates.environment
    env.filters.setdefault("git_info", lambda pagename: (None, None))
    env.filters.setdefault("gh_link_get_blob_url", lambda pagename: None)
    env.filters.setdefault("gh_link_get_open_issue_url", lambda *args, **kwargs: None)


def setup(app):
    app.connect("builder-inited", _register_template_filters)
    app.add_css_file("css/custom.css")
    app.add_js_file("js/custom.js")
