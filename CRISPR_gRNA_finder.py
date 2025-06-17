def find_grnas(sequence):
    sequence = sequence.upper()
    grnas = []
    for i in range(len(sequence) - 23):  # 20-nt guide + 3-nt PAM (NGG)
        guide = sequence[i:i+20]
        pam = sequence[i+20:i+23]
        if pam[0] in 'ACGT' and pam[1:] == 'GG':
            grnas.append((i, guide, pam))
    return grnas

if __name__ == "__main__":
    seq_input = input("Enter the DNA sequence: ").strip()
    results = find_grnas(seq_input)
    for idx, guide, pam in results:
        print(f"Position {idx}: gRNA = {guide}, PAM = {pam}")
