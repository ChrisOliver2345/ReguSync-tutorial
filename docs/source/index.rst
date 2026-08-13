ReguSync Documentation
======================

**ReguSync** is a gene regulatory network (GRN)-guided single-cell multimodal
language model for cross-modal translation in single-cell and spatial
multi-omics data.

ReguSync combines regulatory prior knowledge with self-attention and
cross-attention to model features within each modality and synchronize
biological semantics across modalities. This guide focuses on installing the
public release and running the paired RNA-to-ATAC example.

.. note::

   The tutorial will continue to expand with new examples and workflows.

Start here
----------

New users should follow :doc:`installation`, verify the expected files in
:doc:`data_preparation`, and then run :doc:`quickstart`.

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   installation
   quickstart
   data_preparation

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   tutorials/rna_atac_translation
   configuration
   outputs
   troubleshooting

.. toctree::
   :maxdepth: 1
   :caption: Project

   citation
