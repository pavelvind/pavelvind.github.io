from pathlib import Path

file = input("enter essay name")

with open(file, encoding="utf-8") as f:
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

output_dir = Path("content") / "essays"
output_dir.mkdir(parents=True, exist_ok=True)
output_path = output_dir / f"{title}.html"
output_path.write_text(html, encoding="utf-8")
