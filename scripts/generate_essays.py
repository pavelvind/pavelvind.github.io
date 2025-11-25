from pathlib import Path

repo_root = Path(__file__).resolve().parents[1]
essays_dir = repo_root / "content" / "essays"
source_path = essays_dir / input("Enter source file name (include extension): ").strip()

if not source_path.is_file():
    raise FileNotFoundError(f"Could not find {source_path.relative_to(repo_root)}")

with source_path.open(encoding="utf-8") as f:
    title = f.readline().strip()
    date = f.readline().strip()
    essay = f.read()

html = f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <link rel="stylesheet" href="/assets/css/essay.css" />
    <title>Essay</title>
  </head>

  <body>
    <div class="container">
      <a href= "../../index.html" class="back-link">home</a>" class="back-link">home</a>
      <h1 class="title">{title}</h1>
      <h3 class="date">{date}</h3>
      <p class="essay">
        {essay}
      </p>
    </div>
  </body>
</html>
"""

output_dir = essays_dir
output_dir.mkdir(parents=True, exist_ok=True)
output_path = output_dir / f"{title}.html"
output_path.write_text(html, encoding="utf-8")
