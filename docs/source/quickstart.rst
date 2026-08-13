Quick Start
===========

This example trains ReguSync on paired RNA and ATAC data and evaluates
cross-modal reconstruction on a predefined test set.

Prepare the repository
----------------------

Confirm that the following files are available:

.. code-block:: text

   Dataset/Paired_RNA_train.h5ad
   Dataset/Paired_RNA_test.h5ad
   Dataset/Paired_ATAC_train.h5ad
   Dataset/Paired_ATAC_test.h5ad
   Cache/RNA_ATAC_translation/rp_score.pkl
   Cache/RNA_ATAC_translation/STRINGdb/pretrain_gene_embeddings.csv
   Gene_order/STRINGdb/gene_sequence_human_layered.csv

See :doc:`data_preparation` for the complete layout and input constraints.

Run the example
---------------

The supplied ``run.py`` calls ``run_ReguSync`` with the RNA-to-ATAC example
configuration:

.. code-block:: python

   from regusync_main import run_ReguSync

   run_ReguSync(
       n_epochs=200,
       train_batch_size=128,
       test_batch_size=256,
       dataset="RNA_ATAC_translation",
       modal_a_train="./Dataset/Paired_RNA_train.h5ad",
       modal_b_train="./Dataset/Paired_ATAC_train.h5ad",
       modal_a_test="./Dataset/Paired_RNA_test.h5ad",
       modal_b_test="./Dataset/Paired_ATAC_test.h5ad",
       species="human",
       d_model=128,
       n_hvg=1000,
       ram_usage_optimization=False,
       spatial=False,
   )

Start the run from the repository root:

.. code-block:: console

   conda activate regusync
   python run.py

For an initial environment check, set ``n_epochs=1`` in ``run.py``. Once the
pipeline completes successfully, restore the experiment value before a full
training run.

Inspect the result
------------------

At startup, ReguSync prints the newly created result directory:

.. code-block:: text

   save to Results/dev_RNA_ATAC_translation/YYYY-MM-DD_HH-MM-SS

The directory contains ``run.log`` and, when ``save_embds=True``, prediction
matrices, embeddings, cell names, and feature names. See :doc:`outputs` for the
file-level reference.
