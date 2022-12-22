import csv


def write_csv(amino_acid, codon):
    f = open("../src/genetic_code.csv", "a", newline="")
    line = (f"{amino_acid}", f" {codon}")
    write = csv.writer(f)
    if write.writerow(line):
        print("Successfully added your values.")
