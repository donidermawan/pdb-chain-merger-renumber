import sys
import os
from Bio.PDB import PDBParser, PDBIO
from Bio.PDB import Structure, Model, Chain

# =========================
# 1. Get input file from command line
# =========================
if len(sys.argv) < 2:
    print("Usage: python renumber.py input.pdb")
    sys.exit(1)

input_file = sys.argv[1]
output_file = os.path.splitext(input_file)[0] + "_merged_chainA.pdb"

# =========================
# 2. Parse the structure
# =========================
parser = PDBParser(QUIET=True)
structure = parser.get_structure("input_structure", input_file)

# =========================
# 3. Detect all chains in the structure
# =========================
chains_found = set()
for model in structure:
    for chain in model:
        chains_found.add(chain.id)

print(f"Chains detected: {sorted(chains_found)}")

# =========================
# 4. Create a new structure with a single chain
# =========================
new_structure = Structure.Structure("merged_structure")
new_model = Model.Model(0)
new_chain = Chain.Chain("A")

new_res_id = 1

# =========================
# 5. Merge all chains and renumber residues
# =========================
for model in structure:
    for chain in model:
        for residue in chain:
            # Only process standard protein residues (exclude ligands, water, etc.)
            if residue.id[0] == " ":
                residue.id = (" ", new_res_id, " ")
                new_chain.add(residue)
                new_res_id += 1

new_model.add(new_chain)
new_structure.add(new_model)

# =========================
# 6. Reset atom serial numbers
# =========================
for i, atom in enumerate(new_structure.get_atoms(), start=1):
    atom.serial_number = i

# =========================
# 7. Save output file
# =========================
io = PDBIO()
io.set_structure(new_structure)
io.save(output_file)

print(f"Output saved as: {output_file}")