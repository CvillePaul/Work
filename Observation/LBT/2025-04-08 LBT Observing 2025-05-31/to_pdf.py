import glob

import astropaul.html as html

for categorical_file in glob.glob("../../Observing Files/LBT Observing 2025-04-03/Categorical Priorities *.html"):

    html.html_to_pdf(categorical_file, categorical_file.replace(".html", ".pdf"))
    print(categorical_file)