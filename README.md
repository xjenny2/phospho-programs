# phospho-programs

This is a series of programs used to find the mutation frequency at phosphorylation sites in proteins.  

# Files
- [matchfrequency.py](matchfrequency.py): Given a protein name and a list of motifs, `find_freq()` finds the canonical amino acid sequence for that protein, searches it for matches to any of the motifs, and returns the allele frequencies at those locations.
- [gnomad.py](gnomad.py): Functions for retrieving information from the gnomAD database.  `get_canonical_id()` takes in the name of a protein and returns the canonical transcript ID; `get_variants()` returns all variants recorded in gnomAD under that ID.
- [ensembl.py](ensembl.py): Functions for retrieving information from ensembl.  `get_sequence()` returns the amino acid sequence corresponding to a particular canonical transcript ID.
- [testing.py](testing.py): My personal usage of the above functions for my specific project.  Iterates through two files (one containing a list of genes and the other a list of motifs), returning all the detected matches.
