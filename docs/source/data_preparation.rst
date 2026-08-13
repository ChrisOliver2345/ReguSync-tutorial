Data Preparation
================

ReguSync expects pre-split, paired AnnData files and several GRN-derived runtime
resources. The RNA-to-ATAC example uses the following layout:

.. code-block:: text

   ReguSync/
   |-- Dataset/
   |   |-- Paired_RNA_train.h5ad
   |   |-- Paired_RNA_test.h5ad
   |   |-- Paired_ATAC_train.h5ad
   |   `-- Paired_ATAC_test.h5ad
   |-- Cache/
   |   `-- RNA_ATAC_translation/
   |       |-- rp_score.pkl
   |       `-- STRINGdb/
   |           `-- pretrain_gene_embeddings.csv
   |-- Gene_order/
   |   `-- STRINGdb/
   |       `-- gene_sequence_human_layered.csv
   |-- Resources/
   |   `-- GRCh38.refgenes.genescore.adjusted.csv
   `-- Results/

Paired AnnData files
--------------------

The four ``.h5ad`` files represent one training split and one test split for
each modality. The public example uses RNA as modality A and ATAC as modality B.

The inputs must satisfy these constraints:

* RNA and ATAC training files must contain the same number of cells.
* RNA and ATAC test files must contain the same number of cells.
* Paired cells must have identical ``obs_names`` in identical order within each
  split.
* Feature names must be stored in ``var_names``.
* When ``have_labels=True`` (the default), RNA ``obs`` must contain a
  ``cell_type`` column. These labels are propagated to both modalities during
  preprocessing.
* Count or accessibility values must be stored in ``X``.

The loader adds ``train_test_split`` and ``pair_labels`` internally; these
columns do not need to be included in the original files.

Inspect inputs before training
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use Scanpy to confirm cell alignment and required metadata:

.. code-block:: python

   import scanpy as sc

   rna_train = sc.read_h5ad("Dataset/Paired_RNA_train.h5ad")
   atac_train = sc.read_h5ad("Dataset/Paired_ATAC_train.h5ad")

   assert rna_train.n_obs == atac_train.n_obs
   assert (rna_train.obs_names == atac_train.obs_names).all()
   assert "cell_type" in rna_train.obs

   print(rna_train.shape, atac_train.shape)
   print(rna_train.obs["cell_type"].value_counts())

RP score cache
--------------

For RNA-to-ATAC translation, ReguSync loads
``Cache/<dataset>/rp_score.pkl``. The example therefore expects:

.. code-block:: text

   Cache/RNA_ATAC_translation/rp_score.pkl

This pickle stores three objects in order: a sparse RP score matrix, its cell
index, and its gene columns. The cached cell index must match the paired input
cells used by the example.

GRN files
---------

With ``GRNs="STRINGdb"`` and ``species="human"``, ReguSync loads:

.. code-block:: text

   Gene_order/STRINGdb/gene_sequence_human_layered.csv
   Cache/RNA_ATAC_translation/STRINGdb/pretrain_gene_embeddings.csv

The gene-order CSV must contain ``gene`` and ``level`` columns. The embedding
CSV uses gene names as its row index. Input RNA genes, RP-score genes, gene-order
genes, and embedding genes must overlap; ReguSync raises an error if there is no
overlap with the STRINGdb embeddings.

Species selection
-----------------

Use ``species="human"`` with ``gene_sequence_human_layered.csv`` and
``species="mouse"`` with ``gene_sequence_mouse_layered.csv``. Other species
values are not accepted by the current loader.

Spatial data
------------

When ``spatial=True``, modality A ``obs`` must also contain numeric ``row`` and
``col`` columns. ReguSync converts them to ``obsm["spatial"]`` internally. Keep
``spatial=False`` for the non-spatial scCAT-seq example.

Downloads
---------

Sample data and precomputed cache files are available from the project data
folder on `Google Drive <https://drive.google.com/drive/folders/1BOGt_-5vxkRv5HdzHLPlAnnEJBBMrlp1?usp=sharing>`_.
Reference gene-score resources are available from the project
`resource folder <https://drive.google.com/drive/folders/1kt8DroYUTSJZWuzoQ0YRnehYXj7qXkNZ?usp=sharing>`_.

Only redistribute datasets and reference files when their original licenses or
terms permit redistribution.
