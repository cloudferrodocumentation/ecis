import os
import sys
from pathlib import Path

# Paths
HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
MAIN_SOURCE = REPO_ROOT / "source"

# Allow importing the main conf.py
sys.path.insert(0, str(MAIN_SOURCE))

# Load the main site config into this namespace
main_conf_path = MAIN_SOURCE / "conf.py"
with open(main_conf_path, "r", encoding="utf-8") as f:
    code = compile(f.read(), str(main_conf_path), "exec")
    exec(code, globals())

# Hidden-project-specific overrides
project = "ECIS Hidden Resources"
root_doc = "index"

# Keep hidden docs self-contained
exclude_patterns = list(globals().get("exclude_patterns", []))

# Reuse the main site's templates and static files
templates_path = [str(MAIN_SOURCE / "_templates")]
html_static_path = [str(MAIN_SOURCE / "_static")]

# Copy any extra hidden standalone files if needed
html_extra_path = ["_extra"]

# Optional: remove anything you do not want in hidden docs
# for example, if the main conf has logic tied to the public index only,
# override it here as needed.