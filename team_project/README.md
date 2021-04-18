# _Precision imaging and personalized medicine in glioblastoma using methods from AI and network science_



## Description
Imagine that you are a group of established successful scientists that will team up to tackle an important biomedical and medical challenge. There is an open call for research proposals under a new umbrella program entitled “Artificial intelligence and computational (bio)medicine”, where your multidisciplinary group are aiming for a project entitled “Precision imaging and personalized medicine in glioblastoma using methods from AI and network science”.

The focus of the assignment is fivefold: **(i)** description of relevant imaging technologies and modalities - possibly at different scales e.g. from IMC to MRI and combined with omics data, **(ii)** proposal of imaging-derived biomarkers for glioblastoma, **(iii)** machine learning techniques for segmentation, classification, treatment stratification and prediction, partly combined with methods from network science, **(iv)** the novelty and expected impact of your approach and corresponding evaluation criteria, and **(v)** a discussion of the ethics of your project together with a data management plan (and not so much the basic science of brain tumors per se).


## Organization of your report

### Research plan
(3-5 pages incl. figures and bibliography)
 - A brief background to the field
 - Objectives and expected impact
 - Material and methods
 - Evaluation criteria

### Data management plan and ethical considerations
(1 1/2-2 1/2 pages incl. graphics / links)
 - Description of generated data and code
 - Sharing of data and code
 - Ethical considerations

-----------------------------------
## *Prepare you and your computer for the team-based project*



#### *Orient yourself in the material for the team-based project and how to use [LaTeX](https://www.latex-project.org) for writing your report*
<!-- _Note: Details will be modified and added before the course start_ -->

- We will be using the [**Overleaf**](https://www.overleaf.com) online, **collaborative LaTeX editor** (for more information on LaTeX, see [here](https://en.wikipedia.org/wiki/LaTeX) and [here](https://www.tug.org/pracjourn/2007-4/senthil/senthil.pdf) and [here](https://mildopinions.wordpress.com/2008/07/07/why-i-use-latex-in-biology), and for LeTeX templates, see e.g. [here](https://www.overleaf.com/latex/templates/template-for-submissions-to-molecular-systems-biology/kyxgttpbzhht) and [here](https://www.overleaf.com/latex/templates/tagged/academic-journal))

- **LaTeX template for the report**  is found [[here](./latex-template/MMIV-DLN-AI-2021_project_team_k.tex)] with a dummy figure [[here](./latex-template/mmiv-dln-ai-2021_dummy_fig.png)], resulting in the following [[pdf](./latex-template/MMIV-DLN-AI-2021_project_team_k.pdf)].

- **Expected level of detail** is illustrated with a [project report](https://www.overleaf.com/read/xwjxwcnpzhqv) from the 2019 Summer School at Seili (for which *Prostate Cancer* was the topic) to be found on Overleaf [[here](https://www.overleaf.com/project/5ec71af71aca320001385354)] and on the present repo as [[main.tex](./latex-template/main.tex)],  [[fig1](./latex-template/Fig1_The_process_of_autoEncoder.png)], [[fig2](./latex-template/Fig2_Overview_of_the_process.png)], resulting in the [[pdf](./latex-template/Seili_2020_project_template.pdf)]. See also the team reports from the [ELMED219-2021](https://github.com/MMIV-ML/ELMED219-2021) course [here](./assets).



### Some sources of information  (brain tumors - neuroimaging - AI - network science - [open] software & data)<br>


#### Pre reading (browse the following sources)

  - For those of you that have limited knowledge about biology and pathology of brain or want to refresh their knowledge, we recommend the free Coursera course
  https://www.coursera.org/learn/neurobiology, especially the lecture on [brain tumors](https://www.coursera.org/lecture/neurobiology/brain-tumors-fUcn4).
  - Aldape K et al. Challenges to curing primary brain tumors. Nat Rev Clin Oncol 2019;16:509-520.  [[link](https://www.nature.com/articles/s41571-019-0177-5)]

  - Louis DN et al. The 2016 World Health Organization Classification of Tumors of the Central Nervous System: A Summary. Acta Neuropathol 2016;131(6):803-820. [[link](https://link.springer.com/article/10.1007/s00401-016-1545-1)]

  - Weller M et al. EANO guidelines on the diagnosis and treatment of diffuse gliomas of adulthood. Nat Rev Clin Oncol 2021;18(3):170-186. [[link](https://pubmed.ncbi.nlm.nih.gov/33293629)] [[pdf](https://www.nature.com/articles/s41571-020-00447-z.pdf)].
   
  - Jiang T et al. (a Chinese update). Clinical practice guidelines for the management of adult diffuse gliomas. Cancer Lett 2021;499:60-72. [[link](https://pubmed.ncbi.nlm.nih.gov/33166616)] [[pdf](./refs/Jiang_etal_Clinical_practice_guidelines_for_the_management_of_adult_diffuse_gliomas_Cancer_Letters_2021.pdf)]

  - The Brain Atlas https://www.proteinatlas.org/humanproteome/brain


**Brain tumors & Neuroimaging at different scales and modalities e.g. IMC to MRI** (some pointers)

- Manni F et al. Hyperspectral Imaging for Glioblastoma Surgery: Improving Tumor Identification Using a Deep Spectral-Spatial Approach. Sensors 2020 Dec 5;20(23):6955. [[link](https://pubmed.ncbi.nlm.nih.gov/33291409)] [[pdf](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7730670/pdf/sensors-20-06955.pdf)].
- Baharlou H et al. Mass Cytometry Imaging for the study of human diseases — applications and data analysis strategies. Front Immunol 2019;10:2657 [[link](https://www.frontiersin.org/articles/10.3389/fimmu.2019.02657/full)] [[pdf](https://www.frontiersin.org/articles/10.3389/fimmu.2019.02657/pdf)]
- FLUIDIGM [IMC](https://www.fluidigm.com/applications/imaging-mass-cytometry). Exploring the Tissue and Tumor Microenvironment - A review of recent Mass Cytometry and
Imaging Mass Cytometry publications [[link](https://www.fluidigm.com/binaries/content/documents/fluidigm/search/hippo%3Aresultset/exploring-the-tissue-and-tumor-microenvironment/fluidigm%3Afile)]
- CCBIO, UiB. Opening symposium for the Hyperion Imaging System, 6 Feb 2019 [[link](https://www.uib.no/en/ccbio/122900/opening-symposium-hyperion-imaging-system)]
- Fernández‐Zapata C et al. The use and limitations of single‐cell mass cytometry for studying human microglia function. Brain Pathology 2020;30(6):1178-1191 [[link](https://onlinelibrary.wiley.com/doi/10.1111/bpa.12909)] [[pdf](https://onlinelibrary.wiley.com/doi/epdf/10.1111/bpa.12909)]
- Hiratsuka T. Hierarchical Cluster and Region of Interest Analyses Based on Mass Spectrometry Imaging of Human Brain Tumours. Sci Rep 2020;10:5757. [[link](https://www.nature.com/articles/s41598-020-62176-8)] [[pdf](https://www.nature.com/articles/s41598-020-62176-8.pdf)]
- Otsuka Y et al. High-Spatial-Resolution Multimodal Imaging by Tapping-Mode Scanning Probe Electrospray Ionization with Feedback Control. Anal Chem 2021;93(4):2263–2272 [[link](https://pubs.acs.org/doi/10.1021/acs.analchem.0c04144)] [[pdf](https://pubs.acs.org/doi/pdf/10.1021/acs.analchem.0c04144)] (see also [here](https://www.eurekalert.org/pub_releases/2021-01/ou-wtd010721.php))
- Clement P et al. GliMR: Cross-Border Collaborations to Promote Advanced MRI Biomarkers for Glioma. J Med Biol Eng 2020 Dec;1-11. [[link](https://pubmed.ncbi.nlm.nih.gov/33293909)] [[pd](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7712600/pdf/40846_2020_Article_582.pdf)] (https://glimr.eu).
- Abd-Ellah MK et al. A review on brain tumor diagnosis from MRI images: Practical implications, key achievements, and lessons learned. Magnetic Resonance Imaging 2019;61:300-318. [[link](https://www.sciencedirect.com/science/article/pii/S0730725X18304302)]
- Hamid MAA, Khan NA. Investigation and Classification of MRI Brain Tumors Using Feature Extraction Technique. Journal of Medical and Biological Engineering 2020;40:307–317. [[link](https://link.springer.com/article/10.1007/s40846-020-00510-1)]
- Lohmann P et al. PET/MRI Radiomics in Patients With Brain Metastases. Front. Neurol., 07 February 2020. [[link](https://www.frontiersin.org/articles/10.3389/fneur.2020.00001/full)]
- Henderson F et al. Tractography and the connectome in neurosurgical treatment of gliomas: the premise, the progress, and the potential. Neurosurg Focus 2020;48(2):E6. [[link](https://pubmed.ncbi.nlm.nih.gov/32006950)] [[pdf](https://thejns.org/focus/downloadpdf/journals/neurosurg-focus/48/2/article-pE6.xml)].
- Tiwari A et al. Brain tumor segmentation and classification from magnetic resonance images: Review of selected methods from 2014 to 2019. Pattern Recognition Letters 2020;131:244-260. [[link](https://www.sciencedirect.com/science/article/pii/S016786551930340X)]
- Nadeem MW et al. Brain Tumor Analysis Empowered with Deep Learning: A Review, Taxonomy, and Future Challenges. Brain Sci 2020;10(2):118. [[link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7071415)]
- Brain Tumor Segmentation (BraTS) Challenge 2020: Scope  (MICCAI2020) - Center for Biomedical Image Computing & Analytics, Perelman School of Medicine, University of Pennsylvania [[link](https://www.med.upenn.edu/cbica/brats2020)] [[Data description](https://www.med.upenn.edu/cbica/brats2020/data.html)]


**Brain tumors & Artificial intelligence** (some pointers)

- NCI: Artificial Intelligence Expedites Brain Tumor Diagnosis during Surgery. 2020 Feb 12. [[link](https://www.cancer.gov/news-events/cancer-currents-blog/2020/artificial-intelligence-brain-tumor-diagnosis-surgery#:~:text=Now%2C%20a%20new%20study%20shows,tumor%20tissue%20from%20healthy%20tissue)]
- Hollon TC et al. Near Real-Time Intraoperative Brain Tumor Diagnosis Using Stimulated Raman Histology and Deep Neural Networks. Nature Medicine 2020;26(1):52-58. [[link](https://www.nature.com/articles/s41591-019-0715-9)]  [[GitHub repository](https://github.com/toddhollon/srh_cnn)] [[video](https://labblog.uofmhealth.org/health-tech/artificial-intelligence-improves-brain-tumor-diagnosis?utm_source=youtube&utm_medium=organic&utm_campaign=ai_neuro&utm_content=labblog)]
- Luo H et al. A novel image signature-based radiomics method to achieve precise diagnosis and prognostic stratification of gliomas. Laboratory Investigation 2021;101:450–462. [[link](https://pubmed.ncbi.nlm.nih.gov/32829381)] [[pdf](https://www.nature.com/articles/s41374-020-0472-x.pdf)].
- Yogananda CGB et al. A novel fully automated MRI-based deep-learning method for classification of IDH mutation status in brain gliomas. Neuro-Oncology 2020;22(3):402–411. [[link](https://watermark.silverchair.com/noz199.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAAsQwggLABgkqhkiG9w0BBwagggKxMIICrQIBADCCAqYGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM_l0qCe0X3j7sec-zAgEQgIICd-ksYewnKy45LqXTHXhHOAzzJHK3d4tFLFHnfz8trcRb48Op3XkTRQnJTc68VoXcq-91GkhszdO1gk8fttfzAwFwW5XMt_eLL4rqoKEbl2mNWd3wzyvmluUTIWhhmnLFvEWPTHh6PW1CpBxGu_T3RwFvulqSVi-DWv_K37kCY4DY-5nROmyiX6ZI0G77UhPodnbG0S8LjAz02cK0xfz2fpahloSHSm8TfTzWz_AlUKLJEKmdNMVQuy9x7uhAHVYQwf_sS6Q2gAz09ETmmfO3DzwPA34F_ss3vszaphRudvW1aMteB9K6eqWYmqOiMfI4r8LFM_fzoLzLk9JvtQJv8KjJXkOorVG7oVFh-jiIrOnQgV1IJ0xKYLv1maRksi6J4SmpO0gDY5XXVH8Vih99007mvG_nr-E7UtFz5dUUyzERxW6O_1dvClEjpokBpDP-JBxyOwibwNQobzV8c4sT7n99wIVWOgwwJNEKADqHYECBuEH2wO0NT0_pBlJx0JAJQL8i-dg949euJo_gKqq8DHOymDDkaEd4o-QXgsJ5bMZiZ3iiH-xUAlJsdh2UxLLGCEKezghbLN40_qf_yVhH-NLM_8JbTI-nVuxH2a-dIaHAu0Q_YmHpItMRzBYxNrud99epxTorOe1RgKGhr2Hp8Xb7EGYvJNDC-4ymCTWlB2pET8NudI1e7YZBRH9UDmc6GYJbZnryuYbpWUvR5_rm7FicF8-gysEn9cIVW6vycxsLPompsjQhXrkLJWYOCLBt1P1_blJVk8ASUpzOTPNjhngR4ZfGdgs8_aRF-15kzdsqDA2Id1QqMwZsXRL8PtydJWMP3HXkM3k)]
- Kickinereer P et al. Automated quantitative tumour response assessment of MRI in neuro-oncology with artificial neural networks: a multicentre, retrospective study. The Lancet Oncology 2019;20(5):728-740. [[link](https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045(19)30098-1/fulltext)]
- Zhang N et al. Multivariate machine learning-based language mapping in glioma patients based on lesion topography. Brain Imaging Behav 2021 Feb 22.  [[link](https://pubmed.ncbi.nlm.nih.gov/33619646)]
- Jin L et al. Artificial intelligence neuropathologist for glioma classification using deep learning on hematoxylin and eosin stained slide images and molecular markers. Neuro Oncol 2021;23(1):44-52. [[link](https://pubmed.ncbi.nlm.nih.gov/32663285)] Editorial [comment](https://pubmed.ncbi.nlm.nih.gov/33059363).
- Fang K et al. Convolutional neural network for accelerating the computation of the extended Tofts model in dynamic contrast‐enhanced magnetic resonance imaging. J Magn Reson Imaging 2020 Dec 31. [[link](https://pubmed.ncbi.nlm.nih.gov/33382513)].


**Brain tumors & Network science** (some pointers)

- Jin L et al. The Functional Reorganization of Language Network Modules in Glioma Patients: New Insights From Resting State fMRI Study. Front Oncol 2021 Feb 26;11:617179 [[link](https://pubmed.ncbi.nlm.nih.gov/33718172)]
- Duffau H. Brain connectomics applied to oncological neuroscience: from a traditional surgical strategy focusing on glioma topography to a meta-network approach. Acta Neurochir 2021;163(4):905-917. [[link](https://pubmed.ncbi.nlm.nih.gov/33564906)]
- D’Souza S ety al. Retrospective analysis of hemispheric structural network change as a function of location and size of glioma. Brain Commun 2021;3(1):fcaa216. [[link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7811759)] [[pdf](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7811759/pdf/fcaa216.pdf)].
- Fang S et al. Contralesional functional network reorganization of the insular cortex in diffuse low-grade glioma patients. Sci Rep 2021;11(1):623. [[link](https://pubmed.ncbi.nlm.nih.gov/33436741)] [[pdf](https://www.nature.com/articles/s41598-020-79845-3.pdf)].
- Miele V et al. Nine quick tips for analyzing network data. PLoS Comput Biol 2019;15(12):e1007434 [[link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007434)]
- Gates AJ et al. The effective graph reveals redundancy, canalization, and control pathways in biochemical regulation and signaling. Proc Natl Acad Sci 2021;118(12):e2022598118. [[link](https://pubmed.ncbi.nlm.nih.gov/33737396)] [[pdf](./refs/Gates_etal_The_effective_graph_reveals_redundancy_canalization_and_control_pathways_in_biochemical_regulation_and_signaling_PNAS_2021.pdf)].  Using the CANA Python package for quantifying control and canalization in Boolean Networks (by Correia et al. 2018) [[link](https://www.frontiersin.org/articles/10.3389/fphys.2018.01046/full)] (https://github.com/rionbr/CANA)

**Brain tumors & [Open] software and data** (some pointers for illustration and inspiration)

- Brain Tumor Segmentation | Papers With Code [https://paperswithcode.com/task/brain-tumor-segmentation/latest]
- Akshay Kumaar M. Brain Tumor Classification (using ResNet50 and Google Colab)  [https://github.com/aksh-ai/brain_tumor_classification]
- Joohyun Lee. BraTs (Brain Tumor Segmentation) [https://github.com/cv-lee/BraTs]
- National Cancer Institute. TCGA's Study of Glioblastoma Multiforme. [[link](https://www.cancer.gov/about-nci/organization/ccg/research/structural-genomics/tcga/studied-cancers/glioblastoma)]
- Bakas S et al. Advancing The Cancer Genome Atlas glioma MRI collections with expert segmentation labels and radiomic features. Scientific Data 2017;4, Article number: 170117 [https://www.nature.com/articles/sdata2017117] [[pdf](https://www.nature.com/articles/sdata2017117.pdf)]<br>
*Excerpt*: Considering the value of big data and the potential of publicly available datasets for increased reproducibility of scientific findings, the National Cancer Institute (NCI) of the National Institutes of Health (NIH) created TCGA ([cancergenome.nih.gov](https://www.cancer.gov/about-nci/organization/ccg/research/structural-genomics/tcga)) and [TCIA](https://link.springer.com/article/10.1007/s10278-013-9622-7) (www.cancerimagingarchive.net). TCGA is a multi-institutional comprehensive collection of various molecularly characterized tumor types, and its data are available in NCI’s Genomic Data Commons portal ([gdc-portal.nci.nih.gov](https://portal.gdc.cancer.gov)). Building upon NIH’s investment in TCGA, the NCI’s Cancer Imaging Program approached sites that contributed tissue samples, to obtain corresponding de-identified routine clinically-acquired radiological data and store them in TCIA. These repositories make available multi-institutional, high-dimensional, multi-parametric data of cancer patients, allowing for radiogenomic analysis.
- Beers A et al. DeepNeuro: an open-source deep learning toolbox for neuroimaging. Neuroinformatics 2020, June 23 [[link]( https://link.springer.com/article/10.1007/s12021-020-09477-5)] [[pdf](https://link.springer.com/content/pdf/10.1007/s12021-020-09477-5.pdf)]; GitHub: https://github.com/QTIM-Lab/DeepNeuro - A deep learning python package for neuroimaging data. Focused on validated command-line tools you can use today. Created by the Quantitative Tumor Imaging Lab at the Martinos Center (Harvard-MIT Program in Health, Sciences, and Technology / Massachusetts General Hospital).
- Chang K et al. Automatic assessment of glioma burden: A deep learning algorithm for fully automated volumetric and bi-dimensional measurement. Neuro-Oncology 2019;21(11):1412-1422 [[link](https://academic.oup.com/neuro-oncology/article/21/11/1412/5514498)] [[pdf](https://scholar.google.com/scholar_url?url=https://academic.oup.com/neuro-oncology/article-pdf/21/11/1412/30391573/noz106.pdf&hl=en&sa=T&oi=ucasa&ct=ufr&ei=de7jX5XYM4-Ny9YPjJ6xwAs&scisig=AAGBfm2TQE4zFdIsfPkZZOKNbcylAzCecA)]. Code: https://github.com/QTIM-Lab/DeepNeuro.
- Bao G et al. PathoFusion: An Open-Source AI Framework for Recognition of Pathomorphological Features and Mapping of Immunohistochemical Data. Cancers 2021 Feb; 13(4):617. [[link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7913958)] [[pdf](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7913958/pdf/cancers-13-00617.pdf)]   Code: https://github.com/guoqingbao/Pathofusion.
- Ellis DG, Aizenberg MR. Deep Learning Using Augmentation via Registration: 1st Place Solution to the AutoImplant 2020 Challenge. In: Li J., Egger J. (eds) Towards the Automatization of Cranial Implant Design in Cranioplasty. AutoImplant 2020. Lecture Notes in Computer Science, vol 12439. Springer, Cham. [[link](https://link.springer.com/chapter/10.1007%2F978-3-030-64327-0_6)]; Code: https://github.com/ellisdg/3DUnetCNN; Pretrained models: https://zenodo.org/record/4289225; Augmented Data Set: https://zenodo.org/record/4270278
- Ellis DG, Aizenberg MR. Structural brain imaging predicts individual-level task activation maps using deep learning. bioRxiv, 2020 [[link](https://www.biorxiv.org/content/10.1101/2020.10.05.306951v1)] [[pdf](https://www.biorxiv.org/content/10.1101/2020.10.05.306951v1.full.pdf)]; Code: https://github.com/ellisdg/3DUnetCNN;   "... _The reliable functional activation predictions from structural imaging may be of use to clinicians in cases where task activation mapping is critical for patient care, including neurosurgical operative planning. Task mapping predictions could give neurosurgeons the ability to visualize eloquent areas and avoid potential surgically induced deficits, even without collecting any fMRI data. Our future efforts will focus on using CNNs to provide enhanced mapping accuracy and validating the use of structural imaging to predict task activation maps in clinical populations, such as brain tumor patients._"
- Lundervold AS, Lundervold A. An overview of deep learning in medical imaging focusing on MRI. Zeitschrift fur Medizinische Physik. 2019;29(2):102-127. [[link](https://www.sciencedirect.com/science/article/pii/S0939388918301181)] [[pdf](https://reader.elsevier.com/reader/sd/pii/S0939388918301181?token=F0F5572A8CA576BB20A27E381932486EAD2ECEAA5FEE098EAE183438F8BA7A989E8046160DDE10526E3698BD6D27784A)]


David G. Ellis [BraTS 2020 Tutorial](https://github.com/ellisdg/3DUnetCNN/tree/master/examples/brats2020) using [3DUNetCNN](https://github.com/ellisdg/3DUnetCNN):<br>

![Brain Tumor Segmentation (BraTS) Tutorial](https://github.com/ellisdg/3DUnetCNN/raw/master/legacy/doc/tumor_segmentation_illusatration.gif)

### Ethics of artificial intelligence, machine learning, data sharing and reproducible research (some pointers)
- Wikipedia [https://en.wikipedia.org/wiki/Ethics_of_artificial_intelligence]
- Rigby MJ. Ethical Dimensions of Using Artificial Intelligence in Health Care. AMA Journal of Ethics, Feb 2019 [https://journalofethics.ama-assn.org/article/ethical-dimensions-using-artificial-intelligence-health-care/2019-02]
- Morley J, Machado C, Burr C et al. The Debate on the Ethics of AI in Health Care: A Reconstruction and Critical Review (November 13, 2019). [https://ssrn.com/abstract=3486518]
- Bostrom N, Yudkowsky E. The Ethics of Artificial Intelligence. In Frankish K, Ramsey W (ed) Cambridge Handbook of Artificial Intelligence, CUP 2014   [https://intelligence.org/files/EthicsofAI.pdf]
- Ethics of Artificial Intelligence and Robotics. First published Apr 30, 2020. Stanford Encyclopedia of Philosophy [https://plato.stanford.edu/entries/ethics-ai]
- Gibney W. The battle for ethical AI at the world’s biggest machine-learning conference. Nature news 20 Jan 2020 [https://www.nature.com/articles/d41586-020-00160-y]
- Ethics of AI in Radiology. European and North America Multisociety Statement 2019 [https://www.acr.org/-/media/ACR/Files/Informatics/Ethics-of-AI-in-Radiology-European-and-North-American-Multisociety-Statement--6-13-2019.pdf]
- Vollmer S, Mateen BA, Bohner G et al. Machine learning and artificial intelligence research for patient benefit: 20 critical questions on transparency, replicability, ethics, and effectiveness. BMJ 2020;368:l6927. [https://www.bmj.com/content/368/bmj.l6927]
- Bannier E et al. The Open Brain Consent: Informing research participants and obtaining consent to share brain imaging data. Human Brain Mapping 2021:1-7 [[link](https://onlinelibrary.wiley.com/doi/10.1002/hbm.25351)] (also at https://psyarxiv.com/f6mnp) GitHub: https://github.com/con/open-brain-consent
- Make open data sharing a no-brainer for ethics committees (https://open-brain-consent.readthedocs.io/en/stable)

**Data sharing**, [**FAIR**](https://www.go-fair.org/fair-principles) (**F**indability, **A**ccessibility, **I**nteroperability, and **R**euse of digital assets) and **Code sharing**
- Popkin G. Data sharing and how it can benefit your scientific career. Nature 13 May 2019 (https://www.nature.com/articles/d41586-019-01506-x)
- The Transparency and Openness Promotion (TOP) Guidelines created by journals, funders, and societies to align scientific ideals with practices by [Center for Open Science](https://www.cos.io) (https://www.cos.io/initiatives/top-guidelines)
- The Research Council of Norway (NFR): Policy on Open access to research data (https://www.forskningsradet.no/en/Adviser-research-policy/open-science/open-access-to-research-data). See also Uninett Sigma2 [Data Planning](https://www.sigma2.no/data-planning) and their [EasyDMP](https://documentation.sigma2.no/services/easydmp-user-documentation.html).
- [_FAIRsharing.org_](https://fairsharing.org) - A curated, informative and educational resource on data and metadata standards, inter-related to databases and data policies. 
- nature > [scientific data](https://www.nature.com/sdata) > policies > recommended data repositories: https://www.nature.com/sdata/policies/repositories (with _view FAIRsharing entry_)
- [_fighshare_](https://figshare.com) - a home for papers, FAIR data and non-traditional research outputs that is easy to use and ready now.
- [_FOSTER_](https://www.fosteropenscience.eu) - an e-learning platform that brings together the best training resources addressed to those who need to know more about Open Science. 
- Open Science by Design: Realizing a Vision for 21st Century Research. Concensus study report of the National Academies of Science Engineering Medicine, 2018 (https://www.nap.edu/read/25116)
- [Zenodo](https://zenodo.org) (name derived from [Zenodotus](https://en.wikipedia.org/wiki/Zenodotus), the first librarian of the Ancient Library of Alexandria and father of the first recorded use of metadata, a landmark in library history) is a CERN service, being an open dependable home for the long-tail of science, enabling researchers to share and preserve any research outputs in any size, any format and from any science  (the zenodo code itself is on https://github.com/zenodo/zenodo)
- Katz DS. Recognizing the value of software: a software citation guide [version 2; peer review: 2 approved] Previously titled: "The importance of software citation". [F1000Research](https://f1000research.com) 2021;9:1257 (https://f1000research.com/articles/9-1257/v2)
- Stoudt S et al. Principles for data analysis workflows. PLoS Comput Biol 2021;17(3):e1008770. [[link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008770)]  "... _A systematic and reproducible “workflow” - the process that moves a scientific investigation from raw data to coherent research question to insightful contribution - should be a fundamental part of academic data-intensive research practice._"
- Romano JD & Moore JH. Ten simple rules for writing a paper about scientific software. PLoS Comput Biol 2020;16(11):e1008390 [[link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008390)] See also [this](https://www.software.ac.uk/resources/guides/software-management-plans) link to Writing and using a software management plan.
- Lee BD. Ten simple rules for documenting scientific software. PLoS Comput Biol 2018;14(12):e1006561 [[link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006561)]
- Boudreau M et al. On the open-source landscape of PLOS Computational Biology. PLoS Comput Biol 2021;17(2):e1008725 [[link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008725)]
- Rule A et al. Ten simple rules for writing and sharing computational analyses in Jupyter Notebooks. PLoS Comput Biol 2019;15(7):e1007007 [[link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007007)] (GitHub: https://github.com/jupyter-guide/ten-rules-jupyter)
- PLoS Computational Biology (2021). Code Availability - Summary of Policy Requirements for Authors Publishing in PLOS Computational Biology in effect from 30 March 2021. [[link](https://journals.plos.org/ploscompbiol/s/code-availability)]
- PLoS Computational Biology (2021). Data Availability - Policy that applies to all PLOS journals, unless otherwise noted. [[link](https://journals.plos.org/ploscompbiol/s/data-availability)]
__________________________________________________________________________
