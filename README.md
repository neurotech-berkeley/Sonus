# Full Waveform Inversion (FWI) for Brain Imaging

This repository contains an open-source implementation of Full Waveform Inversion (FWI) for neuroimaging and breast imaging applications. FWI is a powerful computational technique that uses acoustic wave data to reconstruct detailed internal structures. Our primary goal is to create an accessible, scalable FWI solution for research in neurotechnology and cancer detection.

## Project Overview

FWI is traditionally used in geophysical exploration, but its high-resolution capabilities also hold promise in medical imaging. We applied FWI to model soft tissue imaging first, starting with breast tissue as a foundation. This allows us to refine imaging accuracy and performance in a simpler anatomical model before advancing to brain imaging using the MIDA (Montreal Imaging Dataset of the Head) model, which provides a realistic head anatomy for neuroimaging research.

The project currently includes:
- **Data Simulation**: Generating synthetic datasets for FWI in soft tissue.
- **Model Setup**: Building and testing FWI models on breast tissue data.
- **FWI Implementation**: Running FWI algorithms to reconstruct detailed internal images.

In the next phase, we will adapt this framework for accelerated GPU usage for the MIDA head model.

