from habanero import Crossref

cr = Crossref()

result = cr.works(query = 'An Evaluation of the Biological and Toxicological Properties of Aloe Barbadensis (Miller), Aloe Vera')

print(result['message']['items'][0]['DOI'])


result = cr.works(query = "A Modular Quantum Compilation Framework for Distributed Quantum Computing")

print(result['message']['items'][0]['DOI'])