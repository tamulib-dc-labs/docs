=========================================
Using the Super Computer when we Need GPU
=========================================

When running AI related tasks for images and video, the super computer is often needed. This doc helps understand workflows
and tasks for using GRACE or FASTER.

---------------------------
Finding and Loading Modules
---------------------------

Due to the restrictions of the connection node and its file system, you will normally want to find and load modules so
that it doesn't count against your quota.

To search for a module, you can do something like:

.. code-block:: console

    $ module -r spider '.*torch.*'

This will return your matches and the modules that must be installed prior to loading this module.

.. code-block:: console

    $ ml GCCcore/13.2.0 Python/3.11.5



--------------------------------------------
Building an Activating a Virtual Environment
--------------------------------------------



-----------------------
The Costs of Using GPUs
-----------------------

GRACE has 3 different GPUs each with there own costs and details:

Effective GPU SU charge per one hour
(wall_time)
A100 72
RTX 6000 48
T4 24

-----------------
Writing SLURM Job
-----------------

This is my template for writing a SLURM job:

.. code-block:: slurm

    #!/bin/bash

    ##NECESSARY JOB SPECIFICATIONS
    #SBATCH --job-name=marks template mob
    #SBATCH --time=00:15:00 # modify to needs
    #SBATCH --ntasks=1 # modify to needs
    #SBATCH --ntasks-per-node=2 # modify to needs
    #SBATCH --mem=4G # modify to needs
    #SBATCH --output=is_torch_details_log.%j
    #SBATCH --partition=gpu # Add this to Get GPUs
    #SBATCH --gres=gpu:a100:1 # Specify the GPUs you want to use (see above)
    #SBATCH --mail-type=ALL # add if you want an email
    #SBATCH --mail-user=mark.baggett@tamu.edu # add if you want an email

    # load required module(s)
    module purge # Purge everything just in case then add modules in order
    module load GCCcore/13.2.0
    module load Python/3.11.5
    source activate_venv mark_test_venv # Load Virtual Environment to Bring in Other Things You've added
    python execute.py # Run your job

    # Job Environment variables
    echo $SLURM_JOBID
    echo $SLURM_SUBMIT_DIR
    echo $TMPDIR
    echo $SCRATCH

--------------------------------
Calculating Costs of a SLURM JOB
--------------------------------

Before you run a job, there is piece of mind in understanding what that job might cost.  To do this, you can use
:code:`maxconfig` to get an estimate of what your job will cost and why:

.. code-block:: console

    $ max-config -f my-job.slurm
      Showing SU calculation for file is_torch_gpu.slurm

      (CPU-billing + (GPU-billing * GPU-count)) * hours * nodes =   SUs
      (          2 + (         72 *         1)) *  0.25 *     1 =  18.5

    #!/bin/bash
    #SBATCH --job-name=torch_details
    #SBATCH --time=00:15:00
    #SBATCH --ntasks=1
    #SBATCH --ntasks-per-node=2
    #SBATCH --nodes=1
    #SBATCH --mem=4G
    #SBATCH --output=is_torch_details_log.%j
    #SBATCH --gres=gpu:a100:1
    #SBATCH --partition=gpu
    #SBATCH --mail-type=ALL
    #SBATCH --mail-user=mark.baggett@tamu.edu

-------------
Running a Job
-------------

Calculate costs then exectute like:

.. code-block:: console

    $ sbatch demo.slurm
    Submitted batch job 12685166
    (from job_submit) your job is charged as below
              Project Account: 132667767747
              Account Balance: 19999.858889
              Requested SUs:   0.5
