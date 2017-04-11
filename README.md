# HanSolo

HanSolo is a program that takes a single or multi fasta file as input and returns a heat map with the sequence GC-frequency and the total GC-content. 

---

In order to run the program packages needs to be installed and the environmant needs to be setup. 

Install nextflow acording to https://www.nextflow.io/
Install packages in R; ggplot2 and viridis.  

Then clone this repository  

```
# Clone the directory to your home directory
git clone ..
cd HanSolo
```

---
# Run

Run the program: 
```
~/nextflow HanSolo.nf --fasta --working_dir -c HanSolo.config 

```
The heat map is located in the specified working_dir 
