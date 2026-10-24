#!/usr/bin/env -S uv run --script
# -*- coding: utf-8 -*-
# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "markdown",
#     "weasyprint",
# ]
# ///

import os
from pathlib import Path

import markdown
from weasyprint import HTML, CSS


CV_CSS = """
@page {
    margin-top: 1.2cm;
    margin-right: 1.5cm;
    margin-bottom: 1.2cm;
    margin-left: 1.5cm;
    @bottom-center {
        content: counter(page) "/" counter(pages);
        font-family: "DejaVu Sans";
        font-size: 8pt;
        color: #000000;
    }
}
body {
    font-family: "DejaVu Sans";
    font-size: 9.5pt;
    text-align: justify;
}
h1, h2, h3, h4, h5, h6 {
    margin-top: 0.8em;
    margin-bottom: 0;
}
p {
    margin: 0;
}
a {
    text-decoration: none;
    color: #0645ad;
}
ul, ol {
    margin: 0;
    padding-left: 2em;
}
li {
    margin: 0;
}
"""


if __name__ == "__main__":
    root_path = Path(__file__).parent
    input_path = root_path / "README.md"
    output_path = root_path / "MarekBurzaCV.pdf"
    email = os.environ["EMAIL"]
    phone = os.environ["PHONE"]
    md = input_path.open().read()
    md = md.replace("<!-- EMAIL -->", f"· [{email}](mailto:{email})")
    md = md.replace("<!-- PHONE -->", f"· [{phone}](tel:{phone})")
    html = markdown.markdown(md)
    css = CSS(string=CV_CSS)
    HTML(string=html).write_pdf(output_path, stylesheets=[css])
