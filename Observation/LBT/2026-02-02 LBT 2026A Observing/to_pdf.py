import glob
import pathlib

import astropaul.html as html

for categorical_file in glob.glob("../../../../Observing Files/LBT Observing 2026-05-03/uva_multistar*.html"):
    input_file = pathlib.Path(categorical_file)
    output_file = input_file.name.replace(".html", ".pdf")
    html.html_to_pdf(input_file, output_file)
    print(output_file)
