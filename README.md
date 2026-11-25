<h1 align="center">Project Sonus</h1>

<p align="center">
  A Brain Imaging Technique Using Ultrasound.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.837"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.837-blue.svg" alt="Run on brainlife.io"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **A Brain Imaging Technique Using Ultrasound.**

| | |
|---|---|
| **Run it** | [doi.org/10.25663/brainlife.app.837](https://doi.org/10.25663/brainlife.app.837) |

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.837](https://doi.org/10.25663/brainlife.app.837), choose the input datasets from your project and press **Execute**.

### Locally

You need [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {}
   ```

3. Run `./main`.

## Project Overview

FWI is traditionally used in geophysical exploration, but its high-resolution capabilities also hold promise in medical imaging. We applied FWI to model soft tissue imaging first, starting with breast tissue as a foundation. This allows us to refine imaging accuracy and performance in a simpler anatomical model before advancing to brain imaging using the MIDA (Montreal Imaging Dataset of the Head) model, which provides a realistic head anatomy for neuroimaging research.

The project currently includes:
- **Data Simulation**: Generating synthetic datasets for FWI in soft tissue.
- **Model Setup**: Building and testing FWI models on breast tissue data.
- **FWI Implementation**: Running FWI algorithms to reconstruct detailed internal images.

In the next phase, we will adapt this framework for accelerated GPU usage for the MIDA head model.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Project Sonus. brainlife.io App. [doi:10.25663/brainlife.app.837](https://doi.org/10.25663/brainlife.app.837)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

Maintained by [@neurotech-berkeley](https://github.com/neurotech-berkeley).
