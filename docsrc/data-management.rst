Metadata harvester
==================


Project-level Metadata 
----------------------
The **Project-level Metadata** lvel is related to the main CAGS interface website from which metadata are harvested through the online submission form. It collects metadata (derived and expended from Dublin Core metadata) which incorporates a number of descriptive and resource discovery focused elements describing either a scientific communication, a notebook and a dataset independently or jointly. 

File-level Metadata 
-------------------

The **File-level Metadata** is a gui designed to help with the initial preparation of one geophysical dataset. Starting from one or multiple input directories, a cleanly structured output directory is generated (without deleting any input files).
Generate suitable metadata from user input and write this metadata into the directory structure, making it ready for further distribution.

`geophysical Metadata Management using a Juypter Notebook <https://github.com/m-weigand/geometadp.git>`_

Data management
===============

Workflow for preparing dataset
------------------------------

-	**Sort data** into subdirectories. 
-	Make sure you have the **publication rights** for the data, using dedicated repositories such as Zenodo or other licensing schemes (e.g., Creative Commons licenses; https://creativecommons.org/share-your-work/licensingtypes-examples/)
-	Identify the used data formats and **check if they are documented/importable** by available free software;
-	**Write an ASCII ‘Readme’.txt** file which states the basic characteristics of the datasets (settings, procedures, etc);
-	**Formulate a JSON formatted metadata file** following one of our metadata standards.
-	**Upload the dataset** to a data repository;
-	**Register with CAGS** (using the form or by opening a tasks tracker on the github repository e.g. via github-issue).


Data package linter
-------------------


