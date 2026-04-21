# pdb-chain-merger-renumber
A Python tool for automatic detection, merging, and renumbering of protein chains in PDB files. Converts multi-chain structures into a single chain with continuous residue numbering, optimized for molecular docking and structural preprocessing workflows.

**1. Features**
Automatically detects all chains in a PDB file
Merges all protein chains into a single chain (Chain A)
Renumbers residues sequentially (1 → N)
Resets atom serial numbers for clean structure formatting
Ignores non-protein components (ligands, water, heteroatoms)

**2. Requirements**
Python ≥ 3.8
Biopython

**3. Installation**
Option 1 — Using Conda (recommended)
conda create -n docking_env python=3.10 biopython
conda activate docking_env
Option 2 — Using pip
pip install biopython

**4. Usage**
Run the script by providing a PDB file as input:
python renumber.py input.pdb

Output
The script generates a new PDB file:
input_merged_chainA.pdb
Output characteristics:
Single chain: A
Continuous residue numbering (no gaps)
Clean atom serial numbering

**5. Example**
Input:
9D0X.pdb

Command:
python renumber.py 9D0X.pdb

Output:
9D0X_merged_chainA.pdb

Console output:
Chains detected: ['A', 'B', 'C', 'D']
Output saved as: 9D0X_merged_chainA.pdb

**6. Important Notes**
Only standard protein residues are processed
Ligands, ions, and water molecules are excluded
Merging multiple chains into one is not biologically meaningful
Intended for technical preprocessing, especially for:
molecular docking
structure cleanup
pipeline standardization

**7. Use Cases**
Preparing structures for docking tools (AutoDock, Vina, Glide)
Standardizing residue numbering across datasets
Simplifying multi-chain protein complexes
