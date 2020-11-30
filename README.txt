REQUIREMENTS:
Python 3.7.4 64-bit
Make sure you have MGLTools 1.5.7 installed and set the PYTHONPATH to where your MGLTools is
Autodock Vina is mandatory
Feel free to modify the directories in the code to suit your computer


HOW TO USE:
Step 1: Download this repository and extract it.
Step 2: Edit the "locations" list with your desired locations on the Alpha-L-Fucosidase protein
Step 3: Make sure the "config" file coordinates are where you want to dock your protein, and make sure that the "prepare_receptor4.py" file is in the folder
Step 4: Place the PDB file of your desired wild-type protein and the PDBQT file of your desired ligand
Step 5: Open the "autodock_automation.py" file to start the program, and when it finishes, you will get an output CSV file, where the first column is the rank number, the second column is the mutant, and the third column is the binding energy in kcal/mol

This program is used to determine which mutant (single point mutation) has the best binding energy (in other words, to which mutant does the ligand bind the most easily)

I added a sample "tmafc.pdb" file for the wild-type protein, as well as a "pnp_xylose.pdbqt" file for the ligand. I set the "locations" list to eight of the residues in the active site.

I DO NOT OWN THE CODE FOR THE PREPARE_RECEPTOR4.PY FILE, IT ALREADY COMES WITH MGLTOOLS 1.5.7
