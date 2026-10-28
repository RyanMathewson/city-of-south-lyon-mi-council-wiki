"""MkDocs hook: publish each page's Markdown source in the built site so readers can download or copy it."""
import shutil
from pathlib import Path


def on_post_build(config):
    docs, out = Path(config["docs_dir"]), Path(config["site_dir"])
    for src in docs.rglob("*.md"):
        dest = out / src.relative_to(docs)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dest)
    exports = Path(config["config_file_path"]).parent / "exports"
    if exports.exists():
        shutil.copytree(exports, out / "exports", dirs_exist_ok=True)
