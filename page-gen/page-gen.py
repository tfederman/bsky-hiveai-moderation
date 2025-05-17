import glob

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))
tmpl = env.get_template("images.tmpl")

images = sorted(glob.glob("../images/*.png"))
image_pages = [images[n:n+30] for n in range(0, len(images), 30)]

for n,ip in enumerate(image_pages):
    open(f"images-{n+1}.html", "w").write(tmpl.render(images=ip, page_count=len(image_pages), page=n+1, total=len(images)))
