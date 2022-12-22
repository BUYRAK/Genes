def start_program():
    print("Welcome to Genes App")
    my_codon = str(input("Please enter several codons: "))

    total_codon = len(my_codon) / 3

    codons = []
    x = 0
    y = 3
    for i in range(0, int(total_codon)):
        codons.append(my_codon[x:y])
        x += 3
        y += 3

    # print("".join(my_codon))

    with open("../src/genetic_code.csv") as g_obj:
        lines = g_obj.readlines()
        your_data = []
        # first_line = lines[2]
        for codon in codons:
            for line in lines:
                try:
                    if line.find(codon) == 5:
                        your_data.append(line[:3])
                    elif line.find(codon) == 10:
                        your_data.append(line[:3])
                    elif line.find(codon) == 10:
                        your_data.append(line[:3])
                    elif line.find(codon) == 15:
                        your_data.append(line[:3])
                    elif line.find(codon) == 20:
                        your_data.append(line[:3])
                    elif line.find(codon) == 25:
                        your_data.append(line[:3])
                    elif line.find(codon) == 30:
                        your_data.append(line[:3])
                except Exception as ex:
                    print("Error")

        """
        # My attempts -1
        print(lines[1][:3])
        if lines[1].find(codons[codon_count]) == 1:
            your_data.append([line[0:3] for line in lines][codon_count])
            codon_count += 1


        # My attempts -1
        for row in reader:

            for codon in codons:
                try:
                    if row[1].find(codons[codon_count]) == 1:
                        your_data.append(row[0])
                        codon_count += 1
                    elif row[2].find(codons[codon_count]) == 1:
                        your_data.append(row[0])
                        codon_count += 1
                    elif row[3].find(codons[codon_count]) == 1:
                        your_data.append(row[0])
                        codon_count += 1
                    elif row[4].find(codons[codon_count]) == 1:
                        your_data.append(row[0])
                        codon_count += 1
                    elif row[5].find(codons[codon_count]) == 1:
                        your_data.append(row[0])
                        codon_count += 1
                    elif row[6].find(codons[codon_count]) == 1:
                        your_data.append(row[0])
                        codon_count += 1
                    else:
                        data_error += 1
                except Exception as ex:
                    break
        """

    print("".join(your_data))
    if not your_data:
        print("Some data not found.")