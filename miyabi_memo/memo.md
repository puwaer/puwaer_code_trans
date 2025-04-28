conda clean --all


qsub -I -l select=1 -W group_list=gj26 -q interact-g -l walltime=01:00:00
module purge 

module load python/3.10.16
module load singularity/4.2.1
