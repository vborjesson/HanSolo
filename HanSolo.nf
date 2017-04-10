#!/usr/bin/env nextflow

// ~/nextflow HanSolo.nf --fasta --wind --step 


params.fasta = ""
fa = file(params.fasta)

GC_python = "~/HanSolo/HanSolo.py" 
GC_R = "~/HanSolo/HanSolo.R"

process GC_freq {

//	publishDir "${params.working_dir}" , mode: "copy", overwrite: true
//	errorStrategy: 'ignore'

	input:
	file fa

	output:
	set 'out1', 'out2' into csv 

	script:
	"""
	python3 ${GC_python} -n ${params.wind} -m ${params.step} -i ${fa} -o ${params.out1} -p ${params.out2} 
	"""

}

process plot_R {
	
	publishDir "${params.working_dir}" , mode: "copy", overwrite: true 

	input:
	set out1, out2 from csv

	output: 
	set file("output_R"), file("plot.pdf") into plots

	script:
	"""
	Rscript ${GC_R} ${out1} ${out2} plot > output_R 
	"""

}



