Configuration Reference
=======================

ReguSync is configured by keyword arguments passed to ``run_ReguSync``. Unknown
arguments raise ``ValueError``. Six arguments are required for every call:
``dataset``, ``species``, ``modal_a_train``, ``modal_b_train``,
``modal_a_test``, and ``modal_b_test``.

Required arguments
------------------

.. list-table::
   :header-rows: 1
   :widths: 24 18 58

   * - Argument
     - Example
     - Description
   * - ``dataset``
     - ``RNA_ATAC_translation``
     - Experiment name. It also selects ``Cache/<dataset>/`` and names the result directory.
   * - ``species``
     - ``human``
     - Selects the human or mouse layered gene-order file.
   * - ``modal_a_train``
     - RNA train path
     - Training AnnData file for modality A.
   * - ``modal_b_train``
     - ATAC train path
     - Training AnnData file for modality B.
   * - ``modal_a_test``
     - RNA test path
     - Test AnnData file for modality A.
   * - ``modal_b_test``
     - ATAC test path
     - Test AnnData file for modality B.

Training and runtime
--------------------

.. list-table::
   :header-rows: 1
   :widths: 26 18 56

   * - Argument
     - Default
     - Description
   * - ``n_epochs``
     - ``10``
     - Number of training epochs. The example overrides this with 200.
   * - ``train_batch_size``
     - ``32``
     - Number of paired cells per training batch.
   * - ``test_batch_size``
     - ``64``
     - Number of paired cells per evaluation batch.
   * - ``device``
     - CUDA if available
     - Torch device string, such as ``cuda:0``.
   * - ``lr``
     - ``0.001``
     - Adam optimizer learning rate.
   * - ``seed``
     - ``2026``
     - Random seed used by the pipeline.
   * - ``enable_amp``
     - ``True``
     - Enables automatic mixed precision.
   * - ``ram_usage_optimization``
     - ``False``
     - Uses sparse, on-demand dataset access when enabled.
   * - ``log_interval``
     - ``5``
     - Number of batches between training log entries.
   * - ``save_embds``
     - ``True``
     - Saves prediction matrices and embeddings during final evaluation.

Model architecture
------------------

.. list-table::
   :header-rows: 1
   :widths: 24 16 60

   * - Argument
     - Default
     - Description
   * - ``d_model``
     - ``256``
     - Transformer embedding dimension. The example uses 128.
   * - ``n_heads``
     - ``8``
     - Number of attention heads.
   * - ``d_ff``
     - ``128``
     - Feed-forward hidden dimension.
   * - ``n_layers``
     - ``6``
     - Number of transformer layers.
   * - ``dropout``
     - ``0.2``
     - Dropout probability.
   * - ``max_seq_len``
     - ``2000``
     - Maximum tokenized sequence length before data-dependent truncation.
   * - ``n_bins``
     - ``50``
     - Number of expression or activity bins.

Biological preprocessing
------------------------

.. list-table::
   :header-rows: 1
   :widths: 26 18 56

   * - Argument
     - Default
     - Description
   * - ``modal_a``
     - ``RNA``
     - Modality A type.
   * - ``modal_b``
     - ``ATAC``
     - Modality B type; the code also contains an ADT preprocessing path.
   * - ``GRNs``
     - ``STRINGdb``
     - GRN directory and embedding source name.
   * - ``d_graph``
     - ``64``
     - Expected GRN embedding dimension.
   * - ``n_hvg``
     - ``2000``
     - Number of highly variable features selected per modality.
   * - ``hvg_flavor``
     - ``seurat_v3``
     - RNA highly variable gene selection method.
   * - ``hvg_flavor_2``
     - ``cell_ranger``
     - Modality B highly variable feature selection method.
   * - ``include_zero_gene``
     - ``True``
     - Retains zero-valued genes during tokenization.
   * - ``have_labels``
     - ``True``
     - Reads ``cell_type`` labels from modality A.
   * - ``spatial``
     - ``False``
     - Enables spatial coordinate processing from ``row`` and ``col``.

Losses and evaluation
---------------------

``modal_a_loss`` and ``modal_b_loss`` default to ``nb``. ``evaluation_a`` and
``evaluation_b`` default to ``NMI``. The public example and its output-writing
path have been validated for the joint ``NMI`` configuration.

Memory guidance
---------------

Reduce ``train_batch_size`` first when CUDA runs out of memory. If host memory
is the constraint, enable ``ram_usage_optimization`` and reduce
``test_batch_size``. Changes to ``d_model``, ``n_heads``, ``n_layers``, and
``max_seq_len`` alter model capacity and should be treated as experiment
changes, not only memory controls.
