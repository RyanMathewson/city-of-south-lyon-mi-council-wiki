"""MkDocs hook: publish each page's Markdown source in the built site so readers can download or copy it.
When site_url is set, links to other wiki pages in those copies are made absolute, so a file saved on its own still works."""
import posixpath
import re
import shutil
from pathlib import Path

LINK = re.compile(r"\]\(([^)#\s]+\.md)(#[^)\s]*)?\)")


def absolute(text, rel_dir, base):
    def fix(m):
        if m.group(1).startswith("http"):
            return m.group(0)
        target = posixpath.normpath(posixpath.join(rel_dir, m.group(1)))
        if target.startswith(".."):
            return m.group(0)
        page = target[:-3]
        if page == "index":
            url = base
        elif page.endswith("/index"):
            url = base + page[:-5]
        else:
            url = base + page + "/"
        return "](" + url + (m.group(2) or "") + ")"
    return LINK.sub(fix, text)


def on_post_build(config):
    docs, out = Path(config["docs_dir"]), Path(config["site_dir"])
    site_url = config.get("site_url") or ""
    base = site_url if site_url.endswith("/") or not site_url else site_url + "/"
    for src in docs.rglob("*.md"):
        dest = out / src.relative_to(docs)
        dest.parent.mkdir(parents=True, exist_ok=True)
        if base:
            rel_dir = src.parent.relative_to(docs).as_posix()
            dest.write_text(absolute(src.read_text(encoding="utf-8"), "" if rel_dir == "." else rel_dir, base), encoding="utf-8", newline="\n")
        else:
            shutil.copyfile(src, dest)
    exports = Path(config["config_file_path"]).parent / "exports"
    if exports.exists():
        shutil.copytree(exports, out / "exports", dirs_exist_ok=True)
