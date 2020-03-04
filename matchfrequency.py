import re
import gnomad
import ensembl


def find_freq(protein_name):

    # PHOSPHORYLATION MOTIFS

    # Patterns with matches
    pattern_atm = re.compile(r'(SQ)')
    pattern_dnapk = re.compile(r'(?<=P)[ST](?=[A-Z])')

    # Patterns without matches
    pattern_mekk = re.compile(r'(?<=RRFG)S(?=[MLVIF]RR[MLVIF])')
    pattern_chk2 = re.compile(r'(?<=HFD)S(?=TYLI)')

    # Opens sequence file and finds amino acid location of any matches to the motif
    canonical_id = gnomad.get_canonical_id(protein_name)

    matches = []
    seq = ensembl.get_sequence(canonical_id)

    for match in pattern_dnapk.finditer(seq):
        matches.append([match.start() + 1, match.group()[0]])
    print("\nMatches found: ")
    print(matches)

    mutations = gnomad.get_variants(canonical_id)

    results = []  # final results
    for match in matches:
        match_pattern = re.compile(r'(?<=p.[A-Z][a-z]{2})' + str(match[0]) + '(?=[A-Z][a-z]+)')  # AA change/place
        has_match = False
        for mutation in mutations:
            consequence = mutation.get('consequence')
            af = mutation.get('af')
            m = match_pattern.search(consequence)
            if m:
                results.append([match[0], af])  # [location, frequency]
                has_match = True
        if not has_match:
            results.append([match[0], 0])  # appends 0 for frequency if there is no match
    print("\nResults:")
    print(results)


if __name__ == '__main__':
    name = input("Enter the name of the protein: ")
    find_freq(name)
