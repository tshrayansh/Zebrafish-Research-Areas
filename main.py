from Bio import Entrez
import pandas as pd
import time

Entrez.email = "email@gmail.com"

topics = {
    "Neuroscience":
        '(neural OR neuron OR brain OR behavior OR behaviour OR neurodevelopment)[Title/Abstract]',

    "Cancer":
        '(cancer OR tumor OR tumour OR oncology OR metastasis)[Title/Abstract]',

    "Toxicology":
        '(toxicology OR toxicity OR xenobiotic)[Title/Abstract]',

    "Genetics":
        '(genetics OR genomic OR mutation OR CRISPR OR transgenic)[Title/Abstract]',

    "Development":
        '(development OR embryogenesis OR organogenesis)[Title/Abstract]'
}

years = range(2000, 2026)

data = []

for topic_name, search_term in topics.items():

    print(f"\nProcessing: {topic_name}")

    for year in years:

        query = f'(zebrafish OR "Danio rerio") AND {search_term} AND {year}[pdat]'

        handle = Entrez.esearch(
            db="pubmed",
            term=query,
            retmax=0
        )

        results = Entrez.read(handle)

        count = int(results["Count"])

        print(year, count)

        data.append({
            "topic": topic_name,
            "year": year,
            "count": count
        })

        time.sleep(0.1)

df = pd.DataFrame(data)

df.to_csv("data/zebrafish_publications.csv", index=False)

print("\nDone!")