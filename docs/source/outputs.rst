Outputs
=======

Each invocation creates a timestamped directory:

.. code-block:: text

   Results/dev_<dataset>/YYYY-MM-DD_HH-MM-SS/

For the default RNA-to-ATAC example, this becomes:

.. code-block:: text

   Results/dev_RNA_ATAC_translation/YYYY-MM-DD_HH-MM-SS/

Run log
-------

``run.log`` records the resolved configuration, training progress, evaluation
metrics, and final test loss. The console prints the same result directory at
startup so that concurrent experiments can be distinguished.

Saved arrays
------------

When ``save_embds=True`` and both evaluation modes are ``NMI``, final evaluation
writes the following artifacts. The ``0`` prefix is the current split index.

.. list-table::
   :header-rows: 1
   :widths: 36 64

   * - File
     - Contents
   * - ``0_true_matrix_a.h5``
     - Observed modality A matrix; HDF5 key ``true_matrix_a``.
   * - ``0_pred_matrix_a.h5``
     - Modality A reconstructed from modality B; key ``pred_matrix_a``.
   * - ``0_true_matrix_b.h5``
     - Observed modality B matrix; key ``true_matrix_b``.
   * - ``0_pred_matrix_b.h5``
     - Modality B reconstructed from modality A; key ``pred_matrix_b``.
   * - ``0_true_embeddings_a.h5``
     - Encoded modality A cell embeddings; key ``true_embeddings_a``.
   * - ``0_pred_embeddings_a.h5``
     - Translated modality A cell embeddings; key ``pred_embeddings_a``.
   * - ``0_true_embeddings_b.h5``
     - Encoded modality B cell embeddings; key ``true_embeddings_b``.
   * - ``0_pred_embeddings_b.h5``
     - Translated modality B cell embeddings; key ``pred_embeddings_b``.
   * - ``0_test_cell_names_a.csv``
     - Row labels for modality A output matrices.
   * - ``0_output_fnames_a.csv``
     - Column labels for modality A output matrices.
   * - ``0_test_cell_names_b.csv``
     - Row labels for modality B output matrices.
   * - ``0_output_fnames_b.csv``
     - Column labels for modality B output matrices.

Translation directions
----------------------

In the default example, modality A is RNA and modality B is ATAC. Therefore:

* ``pred_matrix_b`` is the RNA-to-ATAC prediction.
* ``pred_matrix_a`` is the ATAC-to-RNA prediction.

Load an HDF5 matrix
-------------------

.. code-block:: python

   import h5py

   with h5py.File("0_pred_matrix_b.h5", "r") as handle:
       predicted_atac = handle["pred_matrix_b"][:]

   print(predicted_atac.shape)

Use the matching cell-name and feature-name CSV files to label the rows and
columns. Do not assume that the output feature order matches the original input
order, because preprocessing filters and reorders features.
