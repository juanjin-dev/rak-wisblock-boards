from __future__ import annotations

from pathlib import Path
import re
import shutil

DOC = Path(__file__).resolve().parent.parent
ROOT = DOC.parent
SRC_BOARDS = ROOT / 'boards' / 'rakwireless'
SRC_SHIELDS = ROOT / 'boards' / 'shields'
SAMPLES = DOC / 'samples'
GENERATED = DOC / '_generated'
GENERATED_BOARDS = GENERATED / 'boards' / 'rakwireless'
GENERATED_SHIELDS = GENERATED / 'shields'


def rst_title(text: str, ch: str = '=') -> str:
    return f"{text}\n{ch * len(text)}\n\n"


def board_names() -> list[str]:
    return sorted(p.name for p in SRC_BOARDS.iterdir() if (p / 'doc' / 'index.rst').exists())


def shield_names() -> list[str]:
    return sorted(p.name for p in SRC_SHIELDS.iterdir() if (p / 'doc' / 'index.rst').exists())


def referenced_code_samples() -> list[str]:
    pattern = re.compile(r":zephyr:code-sample:`([^`]+)`")
    names: set[str] = set()
    for path in list(SRC_BOARDS.glob('*/doc/index.rst')) + list(SRC_SHIELDS.glob('*/doc/index.rst')):
        names.update(pattern.findall(path.read_text(encoding='utf-8')))
    return sorted(names)


def write_code_sample_stubs(samples: list[str]) -> list[str]:
    SAMPLES.mkdir(parents=True, exist_ok=True)
    docnames: list[str] = []
    for sample in samples:
        stub = SAMPLES / f'{sample}.rst'
        stub.write_text(
            f".. zephyr:code-sample:: {sample}\n\n"
            f"   Auto-generated placeholder so out-of-tree board/shield docs can resolve "
            f"``:zephyr:code-sample:`{sample}``` during this build.\n",
            encoding='utf-8',
        )
        docnames.append(f'samples/{sample}')
    return docnames


def copy_doc_tree(src_doc_dir: Path, dst_dir: Path) -> None:
    shutil.copytree(src_doc_dir, dst_dir, dirs_exist_ok=True)


def write_generated_docs() -> tuple[list[str], list[str]]:
    if GENERATED.exists():
        shutil.rmtree(GENERATED)

    board_docs: list[str] = []
    shield_docs: list[str] = []

    for name in board_names():
        src_doc_dir = SRC_BOARDS / name / 'doc'
        dst_dir = GENERATED_BOARDS / name
        copy_doc_tree(src_doc_dir, dst_dir)
        board_docs.append(f'_generated/boards/rakwireless/{name}/index')

    for name in shield_names():
        src_doc_dir = SRC_SHIELDS / name / 'doc'
        dst_dir = GENERATED_SHIELDS / name
        copy_doc_tree(src_doc_dir, dst_dir)
        shield_docs.append(f'_generated/shields/{name}/index')

    return board_docs, shield_docs


def write_root_index(extra_docs: list[str]) -> None:
    lines = [rst_title('RAK WisBlock Boards and Shields')]
    lines.append('.. toctree::\n')
    lines.append('   :maxdepth: 2\n')
    lines.append('   :caption: Boards and Shields\n\n')
    lines.append('   boards/index\n')
    lines.append('   shields/index\n\n')
    if extra_docs:
        lines.append('.. toctree::\n')
        lines.append('   :hidden:\n\n')
        for docname in extra_docs:
            lines.append(f'   {docname}\n')
    (DOC / 'index.rst').write_text(''.join(lines), encoding='utf-8')


def write_boards(docnames: list[str]) -> None:
    out = DOC / 'boards'
    out.mkdir(parents=True, exist_ok=True)
    lines = [rst_title('Boards')]
    lines.append('.. toctree::\n')
    lines.append('   :maxdepth: 1\n\n')
    for docname in docnames:
        lines.append(f'   ../{docname}\n')
    (out / 'index.rst').write_text(''.join(lines), encoding='utf-8')


def write_shields(docnames: list[str]) -> None:
    out = DOC / 'shields'
    out.mkdir(parents=True, exist_ok=True)
    lines = [rst_title('Shields')]
    lines.append('.. toctree::\n')
    lines.append('   :maxdepth: 1\n\n')
    for docname in docnames:
        lines.append(f'   ../{docname}\n')
    (out / 'index.rst').write_text(''.join(lines), encoding='utf-8')


def main() -> None:
    extra_docs = write_code_sample_stubs(referenced_code_samples())
    board_docnames, shield_docnames = write_generated_docs()
    write_root_index(extra_docs)
    write_boards(board_docnames)
    write_shields(shield_docnames)


if __name__ == '__main__':
    main()
