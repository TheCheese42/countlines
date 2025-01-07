import sys
from pathlib import Path
import re


def count_files_and_lines(
    dir: Path,
    file_extensions: tuple[str, ...] = tuple(),
    excludes: tuple[str, ...] = tuple(),
    all_file_extensions: bool = False,
) -> tuple[int, int, dict[str, int]]:
    file_count = 0
    line_count = 0
    files_to_lines: dict[str, int] = {}

    for i in dir.iterdir():
        for exclude in excludes:
            if re.match(exclude, i.name):
                skip = True
                break
        else:
            skip = False
        if skip:
            continue

        if i.is_dir():
            files, lines, files_to_lines_ = count_files_and_lines(
                i, file_extensions, excludes, all_file_extensions
            )
            file_count += files
            line_count += lines
            files_to_lines.update(files_to_lines_)
        else:
            if all_file_extensions or (i.suffix in file_extensions):
                try:
                    lines_in_file = len(
                        i.open("r", encoding="utf-8").readlines()
                    )
                except UnicodeDecodeError:
                    continue
                file_count += 1
                line_count += lines_in_file
                files_to_lines[str(i.absolute())] = lines_in_file

    return file_count, line_count, files_to_lines


def main():
    try:
        path = Path(sys.argv[1])
    except IndexError:
        print(
            f"Usage: {sys.path[0]} <path> [--detailed] [--exts:.py,] "
            "[--excludes:.venv,venv, (supports regex)]"
        )
        sys.exit(1)

    for arg in sys.argv:
        if arg.startswith("--exts:"):
            exts: tuple[str, ...] = tuple()
            for ext in arg[7:].split(","):
                exts += (ext.strip(),)
            break
    else:
        exts = (".py",)

    for arg in sys.argv:
        if arg.startswith("--excludes:"):
            excludes: tuple[str, ...] = tuple()
            for exclude in arg[11:].split(","):
                excludes += (exclude.strip(),)
            break
    else:
        excludes = tuple()

    if "--all-exts" in sys.argv or "-a" in sys.argv:
        all_exts = True
    else:
        all_exts = False

    files, lines, files_to_lines = count_files_and_lines(
        path,
        exts,
        excludes,
        all_file_extensions=all_exts,
    )
    print(f"Files: {files}")
    print(f"Lines: {lines}")
    try:
        print(f"Lines per file: {round(lines / files, 2)}")
    except ZeroDivisionError:
        pass

    if "--detailed" in sys.argv:
        [print(f"{k}: {v}") for k, v in files_to_lines.items()]


if __name__ == "__main__":
    main()
