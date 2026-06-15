Welcome to ReguSync's documentation!
===================================

**ReguSync** is a GRN-guided single-cell multimodal language model for cross-modal translation in single-cell and spatial multi-omics data.

Single-cell multi-omics profiling has greatly advanced the characterization of cellular heterogeneity, but it remains costly, technically noisy, and often incomplete across modalities. ReguSync addresses these challenges by integrating the modeling capacity of single-cell language models with gene regulatory network (GRN)-derived biological knowledge.

ReguSync uses regulatory logic to guide intra-modal feature modeling and leverages GRN-derived biological context for cross-modal semantic synchronization. By combining self-attention, cross-attention, and regulatory prior knowledge, ReguSync enables accurate translation between omics modalities while preserving biologically meaningful signals.

ReguSync can be used for single-cell and spatial multi-omics translation tasks, as well as downstream analyses such as cell-type annotation, pseudotime inference, and perturbation response prediction.

.. note::

This project is under active development. The documentation will be continuously updated.

## Contents

.. toctree::
:maxdepth: 2
:caption: User Guide

installation
usage
tutorial
api
