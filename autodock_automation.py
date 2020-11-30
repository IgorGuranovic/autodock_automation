import pymol, re, os, subprocess
import numpy as np
import pandas as pd
from pymol import cmd

locations = ['D224', 'E266', 'R254', 'H34', 'H129', 'H128', 'W67', 'E66']
mutants = []
for element in locations:
    if element[0] != 'A':
        mutants.append(element+'A')
    if element[0] != 'R':
        mutants.append(element+'R')
    if element[0] != 'N':
        mutants.append(element+'N')
    if element[0] != 'D':
        mutants.append(element+'D')
    if element[0] != 'C':
        mutants.append(element+'C')
    if element[0] != 'Q':
        mutants.append(element+'Q')
    if element[0] != 'E':
        mutants.append(element+'E')
    if element[0] != 'G':
        mutants.append(element+'G')
    if element[0] != 'H':
        mutants.append(element+'H')
    if element[0] != 'I':
        mutants.append(element+'I')
    if element[0] != 'L':
        mutants.append(element+'L')
    if element[0] != 'K':
        mutants.append(element+'K')
    if element[0] != 'M':
        mutants.append(element+'M')
    if element[0] != 'F':
        mutants.append(element+'F')
    if element[0] != 'P':
        mutants.append(element+'P')
    if element[0] != 'S':
        mutants.append(element+'S')
    if element[0] != 'T':
        mutants.append(element+'T')
    if element[0] != 'W':
        mutants.append(element+'W')
    if element[0] != 'Y':
        mutants.append(element+'Y')
    if element[0] != 'V':
        mutants.append(element+'V')

pymol.finish_launching(['pymol', '-cq'])
for x in mutants:
    mutation = x
    mutation = mutation.replace(' ', '')
    mutation_list = list(mutation.split('+'))
    residue_list = ['']*len(mutation_list)
    position_list = ['']*len(mutation_list)
    for x in range(len(mutation_list)):
        position_list[x] = mutation_list[x][1:-1]
        if mutation_list[x][-1] == 'A':
            residue_list[x] = 'ALA'
        elif mutation_list[x][-1] == 'R':
            residue_list[x] = 'ARG'
        elif mutation_list[x][-1] == 'N':
            residue_list[x] = 'ASN'
        elif mutation_list[x][-1] == 'D':
            residue_list[x] = 'ASP'
        elif mutation_list[x][-1] == 'C':
            residue_list[x] = 'CYS'
        elif mutation_list[x][-1] == 'Q':
            residue_list[x] = 'GLN'
        elif mutation_list[x][-1] == 'E':
            residue_list[x] = 'GLU'
        elif mutation_list[x][-1] == 'G':
            residue_list[x] = 'GLY'
        elif mutation_list[x][-1] == 'H':
            residue_list[x] = 'HIS'
        elif mutation_list[x][-1] == 'I':
            residue_list[x] = 'ILE'
        elif mutation_list[x][-1] == 'L':
            residue_list[x] = 'LEU'
        elif mutation_list[x][-1] == 'K':
            residue_list[x] = 'LYS'
        elif mutation_list[x][-1] == 'M':
            residue_list[x] = 'MET'
        elif mutation_list[x][-1] == 'F':
            residue_list[x] = 'PHE'
        elif mutation_list[x][-1] == 'P':
            residue_list[x] = 'PRO'
        elif mutation_list[x][-1] == 'S':
            residue_list[x] = 'SER'
        elif mutation_list[x][-1] == 'T':
            residue_list[x] = 'THR'
        elif mutation_list[x][-1] == 'W':
            residue_list[x] = 'TRP'
        elif mutation_list[x][-1] == 'Y':
            residue_list[x] = 'TYR'
        elif mutation_list[x][-1] == 'V':
            residue_list[x] = 'VAL'
    cmd.load('D:/autodock_automation/tmafc.pdb') #Replace with your directory
    cmd.wizard('mutagenesis')
    for x in range(len(mutation_list)):
        cmd.get_wizard().do_select('/tmafc//A/%s' % (position_list[x]))
        cmd.get_wizard().set_mode("%s" % (residue_list[x]))
        cmd.get_wizard().apply()
    cmd.save('D:/autodock_automation/PDB_Files/mutant_%s.pdb' % (mutation))
    cmd.reinitialize('everything')
cmd.quit()

for pdbFile in os.listdir('D:/autodock_automation/PDB_FILES'):
    subprocess.run('cmd /c "python D:/autodock_automation/prepare_receptor4.py -r D:/autodock_automation/PDB_Files/' + pdbFile + ' -o D:/autodock_automation/PDBQT_Files/' + pdbFile + 'qt -U waters"')
    
for pdbqtFile in os.listdir('D:/autodock_automation/PDBQT_FILES'):
    writer = open("config.txt", "w")
    writer.write("receptor = " + pdbqtFile + "\nligand = pnp_xylose.pdbqt\n\ncenter_x = -17.6742\ncenter_y = 18.0661\ncenter_z = 58.4087\n\nsize_x = 44\nsize_y = 40\nsize_z = 52\n\nenergy_range = 4\n\nexhaustiveness = 8")
    writer.close()
    mutant_name = pdbqtFile[0:-6]
    writer1 = open("autodock.bat", "w")
    writer1.write('"C:/Program Files (x86)/The Scripps Research Institute/Vina/vina.exe" --receptor PDBQT_Files/' + mutant_name + '.pdbqt --ligand pnp_xylose.pdbqt --config D:/autodock_automation/config.txt --log Logs/log_' + mutant_name + '.txt --out Outputs/output_' + mutant_name + '.pdbqt')
    writer1.close()
    subprocess.call([r'D:/autodock_automation/autodock.bat'])

energies = []
mutants_ordered = []
for log in os.listdir('D:/autodock_automation/Logs'):
    reader = open("Logs/" + log, "r")
    text = reader.read()
    lower_bound = [m.start() for m in re.finditer('-\n', text)][0]
    upper_bound = [m.start() for m in re.finditer('0.000', text)][0]
    text1 = text[lower_bound:upper_bound]
    text2 = text1.replace(" 1 ", "")
    text3 = text2.replace("-\n", "")
    text_final = text3.replace(" ", "")
    mutant_ordered = log.replace("log_mutant_", "")
    mutant_ordered1 = mutant_ordered.replace(".txt", "")
    energies.append(text_final)
    mutants_ordered.append(mutant_ordered1)
    reader.close()
sorted_indices = np.argsort(energies)
sorted_indices = np.flip(sorted_indices)

matrix = []
for n in range(len(mutants_ordered)):
    matrix.append([mutants_ordered[n], energies[n]])
sorted_matrix = []
for n in sorted_indices:
    sorted_matrix.append(matrix[n])
for n in range(len(sorted_matrix)):
    sorted_matrix[n].insert(0,n+1)

df = pd.DataFrame(sorted_matrix)
df.to_csv(os.path.join('binding_affinity_rankings.csv'), sep=',', header=None, index=None)