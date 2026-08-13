Installation
============

Requirements
------------

ReguSync requires Python 3.9.19 or later and an NVIDIA GPU for model training
and inference. The reference experiments used an NVIDIA RTX 4090. ReguSync is
compatible with both Windows and Linux, and the minimal environment uses the
PyTorch CUDA 12.1 runtime. The FlashAttention wheel referenced by
``environment.yml`` is available for Linux x86_64 only.

The principal software requirements are:

.. code-block:: text

   python >= 3.9.19
   pytorch >= 2.2.0
   numpy >= 1.24.3
   scipy >= 1.13.1
   pandas >= 2.3.3
   scikit-learn >= 1.4.0
   h5py >= 3.11.0
   flash-attn >= 2.5.2
   scanpy >= 1.9.8
   episcanpy >= 0.4.0
   scvi-tools >= 1.1.6.post2
   squidpy >= 1.6.1
   torchtext == 0.17.0

Create the environment
----------------------

Download or clone the ReguSync source code, enter the repository root, and
create the provided Conda environment:

.. code-block:: console

   git clone https://github.com/ChrisOliver2345/ReguSync.git
   cd ReguSync
   conda env create -f environment.yml
   conda activate regusync

``environment.yml`` contains the minimal runtime dependencies used by the
public pipeline.

Download runtime files
----------------------

The example requires data, reference files, a precomputed RP score matrix, GRN
gene ordering, and pretrained gene embeddings. Place these files in the
locations described in :doc:`data_preparation` before running the model.

.. important::

   Run all commands from the ReguSync repository root. The current release
   resolves ``Dataset/``, ``Resources/``, ``Gene_order/``, ``Cache/``, and
   ``Results/`` relative to the working directory.
