
amino_acids_dict = {

    'UUU': 'Phe',
    'UUC': 'Phe',

    'UUA': 'Leu',
    'UUG': 'Leu',
    'CUU': 'Leu',
    'CUC': 'Leu',
    'CUA': 'Leu',
    'CUG': 'Leu',

    'AUU': 'Ile',
    'AUC': 'Ile',
    'AUA': 'Ile',

    'AUG': 'Met',

    'GUU': 'Val',
    'GUC': 'Val',
    'GUA': 'Val',
    'GUG': 'Val',

    'UCU': 'Ser',
    'UCC': 'Ser',
    'UCA': 'Ser',
    'UCG': 'Ser',
    'AGU': 'Ser',
    'AGC': 'Ser',

    'CCU': 'Pro',
    'CCC': 'Pro',
    'CCA': 'Pro',
    'CCG': 'Pro',

    'ACU': 'Thr',
    'ACC': 'Thr',
    'ACA': 'Thr',
    'ACG': 'Thr',

    'GCU': 'Ala',
    'GCC': 'Ala',
    'GCA': 'Ala',
    'GCG': 'Ala',

    'UAU': 'Tyr',
    'UAC': 'Tyr',

    'UAA': 'STOP',
    'UAG': 'STOP',

    'CAU': 'His',
    'CAC': 'His',

    'CAA': 'Gln',
    'CAG': 'Gln',

    'AAU': 'Asn',
    'AAC': 'Asn',

    'AAA': 'Lys',
    'AAG': 'Lys',

    'GAU': 'Asp',
    'GAC': 'Asp',

    'GAA': 'Glu',
    'GAG': 'Glu',

    'UGU': 'Cys',
    'UGC': 'Cys',

    'UGA': 'STOP',

    'UGG': 'Trp',

    'CGU': 'Arg',
    'CGC': 'Arg',
    'CGA': 'Arg',
    'CGG': 'Arg',
    'AGA': 'Arg',
    'AGG': 'Arg',

    'GGU': 'Gly',
    'GGC': 'Gly',
    'GGA': 'Gly',
    'GGG': 'Gly',
}

def transcriptation(dna):
    translate = {
        "A": "U",
        "U": "A",
        "C": "G",
        "G": "C",
        "T": "A",
    }

    dna = list(dna)
    for i, item in enumerate(dna):
        for key, value in translate.items():
            if item == key:
                dna[i] = value  
    return ''.join(dna)

def chunk_sequence (string,chunk_size) : 
    chunks = []
    for i in range(0, len(string), chunk_size) :
        chunk= string[i:i+chunk_size]
        chunks.append(chunk)
    return chunks

def translation (rna) :
    tri_set=chunk_sequence(rna,3)
    protein= []
    for tri_set in tri_set:
        amino_acids = amino_acids_dict.get(tri_set,"")
        if amino_acids == "STOP" :
            protein.append('STOP')
            break 
        elif amino_acids :
            protein.append(amino_acids)
    return " ".join(protein)

dna = 'TACGCAGAAAAAAATCAGCGGGGTTGTTGGTCATTAGTCTGAATT'
rna = transcriptation(dna)
protein = translation (rna)
print(f'DNA Sequence \n {dna}')
print (f'mRNA Sequences \n {rna}')
print (f"Protein Sequence \n {protein}")