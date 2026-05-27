from Bio import Entrez
Entrez.email = "email@gmail.com"
query = "zebrafish AND neuroscience AND 2015[pdat]"
handle = Entrez.esearch(
    db="pubmed",
    term=query,
    retmax=0
)
results = Entrez.read(handle)
print("Number of papers:", results["Count"])