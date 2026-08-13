RNA-to-ATAC Translation
=======================

This walkthrough explains the public paired RNA-to-ATAC example in ``run.py``.
It trains both translation directions jointly and evaluates reconstructed RNA
and ATAC matrices on the test cells.

1. Activate the environment
---------------------------

From the ReguSync repository root:

.. code-block:: console

   conda activate regusync

Verify CUDA before starting a long run:

.. code-block:: console

   python -c "import torch; print(torch.cuda.is_available())"

2. Validate the runtime files
-----------------------------

Confirm that all paths used by ``run.py`` exist:

.. code-block:: console

   python -c "from pathlib import Path; paths=['Dataset/Paired_RNA_train.h5ad','Dataset/Paired_RNA_test.h5ad','Dataset/Paired_ATAC_train.h5ad','Dataset/Paired_ATAC_test.h5ad','Cache/RNA_ATAC_translation/rp_score.pkl','Cache/RNA_ATAC_translation/STRINGdb/pretrain_gene_embeddings.csv','Gene_order/STRINGdb/gene_sequence_human_layered.csv']; missing=[p for p in paths if not Path(p).is_file()]; print('Missing:', missing)"

The result should be ``Missing: []``.

3. Review the configuration
---------------------------

The example specifies the required data and experiment identity explicitly:

.. code-block:: python

   run_ReguSync(
       dataset="RNA_ATAC_translation",
       species="human",
       modal_a_train="./Dataset/Paired_RNA_train.h5ad",
       modal_b_train="./Dataset/Paired_ATAC_train.h5ad",
       modal_a_test="./Dataset/Paired_RNA_test.h5ad",
       modal_b_test="./Dataset/Paired_ATAC_test.h5ad",
       n_epochs=200,
       train_batch_size=128,
       test_batch_size=256,
       d_model=128,
       n_hvg=1000,
       ram_usage_optimization=False,
       spatial=False,
   )

Parameters not listed here use the defaults defined by ``get_parser()``. In
particular, the example uses RNA for modality A, ATAC for modality B, STRINGdb
for the GRN, automatic mixed precision, and NMI evaluation.

4. Run a smoke test
-------------------

Before a full experiment, temporarily set ``n_epochs=1`` and use smaller batch
sizes if GPU memory is limited. Then run:

.. code-block:: console

   python run.py

A successful startup reports the result directory, loads the RP score cache,
prints the regulatory-level tensor shape, and begins epoch logging. Restore the
intended epoch and batch settings after the smoke test.

5. Run the experiment
---------------------

Start the final configuration from the same repository root:

.. code-block:: console

   python run.py

ReguSync performs the following operations:

#. Loads paired train and test AnnData objects.
#. Verifies cell counts, names, and ordering across modalities.
#. Preprocesses RNA and converts the ATAC input through the cached RP scores.
#. Selects highly variable features and aligns genes with the GRN resources.
#. Tokenizes and bins modality values.
#. Trains the GRN-guided multimodal transformer.
#. Reconstructs RNA from ATAC and ATAC from RNA on the test cells.
#. Computes evaluation metrics and writes output artifacts.

6. Read the predictions
-----------------------

For the default NMI evaluation, prediction matrices are stored as HDF5 files.
The RNA-to-ATAC prediction is ``0_pred_matrix_b.h5``:

.. code-block:: python

   import h5py
   import pandas as pd

   result_dir = "Results/dev_RNA_ATAC_translation/YYYY-MM-DD_HH-MM-SS"

   with h5py.File(f"{result_dir}/0_pred_matrix_b.h5", "r") as handle:
       predicted_atac = handle["pred_matrix_b"][:]

   cells = pd.read_csv(f"{result_dir}/0_test_cell_names_b.csv")
   features = pd.read_csv(f"{result_dir}/0_output_fnames_b.csv")

   assert predicted_atac.shape == (len(cells), len(features))
   print(predicted_atac.shape)

The reverse ATAC-to-RNA prediction is stored in ``0_pred_matrix_a.h5``. See
:doc:`../outputs` for all output files and dataset keys.

Next steps
----------

After reproducing the example, adjust one group of parameters at a time. Start
with batch sizes and ``n_epochs``; then evaluate changes to ``n_hvg``,
``d_model``, and the transformer depth. Keep ``dataset`` synchronized with the
corresponding directory under ``Cache/``.
