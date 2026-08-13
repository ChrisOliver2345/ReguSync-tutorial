Troubleshooting
===============

Run commands from the repository root
-------------------------------------

**Symptom:** A dataset, cache, gene-order, or resource file cannot be found even
though it exists.

**Cause:** Runtime paths are resolved relative to the current working directory.

**Fix:** Change to the ReguSync repository root before running ``python run.py``.

Missing RP score cache
----------------------

**Symptom:** ``FileNotFoundError`` reports a missing ``rp_score.pkl``.

**Fix:** Place the file at ``Cache/<dataset>/rp_score.pkl``. For the provided
example, the exact location is
``Cache/RNA_ATAC_translation/rp_score.pkl``. Ensure that the value passed as
``dataset`` matches the cache directory name.

No overlapping genes
--------------------

**Symptom:** ``No overlapping genes found between adata_a and STRINGdb GRN embeddings.``

**Fix:** Check that RNA ``var_names`` and the row index of
``pretrain_gene_embeddings.csv`` use compatible gene identifiers. Also verify
that the selected species and GRN files are correct.

Paired cells are not aligned
----------------------------

**Symptom:** The loader reports different cell counts or unmatched cell order.

**Fix:** Subset and reorder each paired RNA/ATAC split so that ``obs_names`` are
identical and in the same order. Do this independently for the training and test
splits.

Missing cell-type labels
------------------------

**Symptom:** Preprocessing raises a ``KeyError`` for ``cell_type``.

**Fix:** Add a ``cell_type`` column to modality A ``obs``, or pass
``have_labels=False`` when labels are unavailable. The default NMI evaluation
requires meaningful labels, so select evaluation settings appropriate for an
unlabelled dataset.

CUDA out of memory
------------------

Reduce ``train_batch_size`` and ``test_batch_size`` first. Close unrelated GPU
processes and retry. If necessary, reduce ``max_seq_len`` or model dimensions,
but record those changes because they alter the experiment configuration.

Host RAM pressure
-----------------

Set ``ram_usage_optimization=True`` and reduce the test batch size. The sparse
dataset path converts individual rows to dense tensors on demand instead of
placing all prepared matrices on the device at once.

FlashAttention installation fails
---------------------------------

FlashAttention depends on a compatible PyTorch, CUDA toolkit, compiler, and GPU
environment. Confirm the PyTorch CUDA build before installing it. Linux is the
recommended environment; native Windows installations are more likely to need
toolchain-specific workarounds.

Read the Docs build fails
-------------------------

Open the Read the Docs build log and locate the first warning or error. This
documentation treats Sphinx warnings as build failures. Reproduce the same
strict build locally:

.. code-block:: console

   python -m pip install -r docs/requirements.txt
   python -m sphinx -W --keep-going -b html docs/source docs/build/html

Fix all warnings before uploading the documentation source.
