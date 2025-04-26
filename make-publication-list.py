#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import argparse
from collections import namedtuple
import sys


def _print(args, text, **kwargs):
    if not args.quiet:
        print(text, **kwargs)


class Author(namedtuple("Author", ["name", "url"])):
    @property
    def is_me(self):
        return self.name == "Korrawe Karunratanakul"


class Paper(namedtuple("Paper", [
        "title",
        "url",
        "image",
        "authors",
        "conference",
        "year",
        "special",
        "links"
    ])):
    pass


class Conference(namedtuple("Conference", ["name"])):
    pass


class Link(namedtuple("Link", ["name", "url", "html", "text"])):
    pass


def author_list(authors, *names):
    return [authors[n] for n in names]


authors = {
    "korrawe": Author("Korrawe Karunratanakul", ""),
    "konpat": Author("Konpat Preechakul", "https://konpat.me/"),
    "siyu": Author("Siyu Tang", "https://vlg.inf.ethz.ch/team/Prof-Dr-Siyu-Tang.html"),
    "mjb": Author("Michael Black", "https://scholar.google.com/citations?user=6NjbexEAAAAJ&hl=en"),
    "krikamol": Author("Krikamol Muandet", "https://www.krikamol.org/"),
    "jinlong": Author("Jinlong Yang", "https://scholar.google.fr/citations?user=HGt39SUAAAAJ&hl=en"),
    "yanz": Author("Yan Zhang", "https://yz-cnsdqz.github.io/"),
    "burin": Author("Burin Naowarat", ""),
    "thananchai": Author("Thananchai Kongthaworn", ""),
    "shenghui": Author("Sheng Hui Wu", ""),
    "ekapol": Author("Ekapol Chuangsuwanich", "https://ekapolc.github.io/"),
    "adrian": Author("Adrian Spurr", "https://scholar.google.com/citations?user=2gCGNbYAAAAJ&hl=en"),
    "otmar": Author("Otmar Hilliges", "https://ait.ethz.ch/people/hilliges"),
    "zfan": Author("Zicong Fan", "https://zc-alexfan.github.io/"),
    "sergey": Author("Sergey Prokudin", "https://scholar.google.de/citations?user=xSywCzAAAAAJ&hl=en"),
    "supasorn": Author("Supasorn Suwajanakorn", "https://www.supasorn.com/"),
    "emre": Author("Emre Aksan", "https://emreaksan.github.io/"),
    "thabo": Author("Thabo Beeler", "https://thabobeeler.com/"),

    "ekkasit": Author("Ekkasit Pinyoanuntapong", "https://www.ekkasit.com/"),
    "muhammad": Author(" Muhammad Usama Saleem", "https://m-usamasaleem.github.io/"),
    "puwang": Author("Pu Wang", "https://webpages.charlotte.edu/pwang13/"),
    "hongfei": Author("Hongfei Xue", "https://havocfixer.github.io/"),
    "chen": Author("Chen Chen", "https://www.crcv.ucf.edu/chenchen/"),
    "chuan": Author("Chuan Guo", "https://ericguo5513.github.io/"),
    "junli": Author("Junli Cao", "https://research.snap.com/team_members/junli-cao.html"),
    "jianren": Author("Jian Ren", "https://alanspike.github.io/"),
    "sergeytu": Author("Sergey Tulyakov", "https://stulyakov.com/"),

    "yanwu": Author("Yan Wu", "https://wuyan01.github.io/"),
    "zhengyi": Author("Zhengyi Luo", "https://www.zhengyiluo.com/"),



    # Bio
    "sira": Author("Sira Sriswasdi", "https://www.research.chula.ac.th/researcher-/sira-sriswasdi/"),
    "hsinyao": Author("Hsin-Yao Tang", ""),
    "davidw": Author("David W Speicher", ""),
}
conferences = {
    "arxiv": Conference("ArXiv"),
    "cvpr": Conference("Conference on Computer Vision and Pattern Recognition (CVPR)"),
    "iccv": Conference("International Conference on Computer Vision (ICCV)"),
    "3dv": Conference("International Conference on 3D Vision (3DV)"),
    "icassp": Conference("IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)"),
    "mcp": Conference("Molecular & Cellular Proteomics")
}
publications = [
    Paper(
        "UniPhys: Unified Planner and Controller with Diffusion for Flexible Physics-Based Character Control",
        "http://arxiv.org/abs/2504.12540",
        "teasers/uniphys.gif",
        author_list(authors, "yanwu", "korrawe", "zhengyi", "siyu"),
        conferences["arxiv"],
        2025,
        None,
        [
            Link("Project page", "https://wuyan01.github.io/uniphys-project/", None, None),
            Link("Paper", "http://arxiv.org/abs/2504.12540", None, None),
            # Link("Code", "https://github.com/wuyan01/uniphys", None, None),
        ]
    ),
    Paper(
        "ControlMM: Controllable Masked Motion Generation",
        "https://arxiv.org/abs/2410.10780",
        "teasers/ControlMM.gif",
        author_list(authors, "ekkasit", "muhammad", "korrawe", "puwang", "hongfei", "chen", "chuan", "junli", "jianren", "sergeytu"),
        conferences["arxiv"],
        2024,
        None,
        [
            Link("Project page", "https://www.ekkasit.com/ControlMM-page/", None, None),
            Link("Paper", "https://arxiv.org/abs/2410.10780", None, None),
            Link("Code", "https://github.com/exitudio/ControlMM/", None, None),
        ]
    ),
    Paper(
        "DNO: Optimizing Diffusion Noise Can Serve As Universal Motion Priors",
        "https://arxiv.org/abs/2312.11994",
        "teasers/dno_optimize.gif",
        author_list(authors, "korrawe", "konpat", "emre", "thabo", "supasorn", "siyu"),
        conferences["cvpr"],
        2024,
        None,
        [
            Link("Project page", "https://korrawe.github.io/dno-project/", None, None),
            Link("Paper", "https://arxiv.org/abs/2312.11994", None, None),
            Link("Code", "https://github.com/korrawe/Diffusion-Noise-Optimization", None, None),
        ]
    ),
    Paper(
        "GMD: Controllable Human Motion Synthesis via Guided Diffusion Models",
        "https://arxiv.org/abs/2305.12577",
        "teasers/gmd.png",
        author_list(authors, "korrawe", "konpat", "supasorn", "siyu"),
        conferences["iccv"],
        2023,
        None,
        [   # Link("Abstract", None, "Robotic grasping of house-hold objects has made remarkable progress in recent years. Yet, human grasps are still difficult to synthesize realistically. There are several key reasons: (1) the human hand has many degrees of freedom (more than robotic manipulators); (2) the synthesized hand should conform to the surface of the object; and (3) it should interact with the object in a semantically and physically plausible manner. To make progress in this direction, we draw inspiration from the recent progress on learning-based implicit representations for 3D object reconstruction. Specifically, we propose an expressive representation for human grasp modelling that is efficient and easy to integrate with deep neural networks. Our insight is that every point in a three-dimensional space can be characterized by the signed distances to the surface of the hand and the object, respectively. Consequently, the hand, the object, and the contact area can be represented by implicit surfaces in a common space, in which the proximity between the hand and the object can be modelled explicitly. We name this 3D to 2D mapping as Grasping Field, parameterize it with a deep neural network, and learn it from data. We demonstrate that the proposed grasping field is an effective and expressive representation for human grasp generation. Specifically, our generative model is able to synthesize high-quality human grasps, given only on a 3D object point cloud. The extensive experiments demonstrate that our generative model compares favorably with a strong baseline and approaches the level of natural human grasps. Furthermore, based on the grasping field representation, we propose a deep network for the challenging task of 3D hand-object interaction reconstruction from a single RGB image. Our method improves the physical plausibility of the hand-object contact reconstruction and achieves comparable performance for 3D hand reconstruction compared to state-of-the-art methods.", None),
            Link("Project page", "https://korrawe.github.io/gmd-project/", None, None),
            Link("Paper", "https://arxiv.org/abs/2305.12577", None, None),
            Link("Code", "https://github.com/korrawe/guided-motion-diffusion", None, None),
        ]
    ),
    Paper(
        "HARP: Personalized Hand Reconstruction from a Monocular RGB Video",
        "https://arxiv.org/abs/2212.09530",
        "teasers/harp.jpg",
        author_list(authors, "korrawe", "sergey", "otmar", "siyu"),
        conferences["cvpr"],
        2023,
        None,
        [   # Link("Abstract", None, "Robotic grasping of house-hold objects has made remarkable progress in recent years. Yet, human grasps are still difficult to synthesize realistically. There are several key reasons: (1) the human hand has many degrees of freedom (more than robotic manipulators); (2) the synthesized hand should conform to the surface of the object; and (3) it should interact with the object in a semantically and physically plausible manner. To make progress in this direction, we draw inspiration from the recent progress on learning-based implicit representations for 3D object reconstruction. Specifically, we propose an expressive representation for human grasp modelling that is efficient and easy to integrate with deep neural networks. Our insight is that every point in a three-dimensional space can be characterized by the signed distances to the surface of the hand and the object, respectively. Consequently, the hand, the object, and the contact area can be represented by implicit surfaces in a common space, in which the proximity between the hand and the object can be modelled explicitly. We name this 3D to 2D mapping as Grasping Field, parameterize it with a deep neural network, and learn it from data. We demonstrate that the proposed grasping field is an effective and expressive representation for human grasp generation. Specifically, our generative model is able to synthesize high-quality human grasps, given only on a 3D object point cloud. The extensive experiments demonstrate that our generative model compares favorably with a strong baseline and approaches the level of natural human grasps. Furthermore, based on the grasping field representation, we propose a deep network for the challenging task of 3D hand-object interaction reconstruction from a single RGB image. Our method improves the physical plausibility of the hand-object contact reconstruction and achieves comparable performance for 3D hand reconstruction compared to state-of-the-art methods.", None),
            Link("Project page", "https://korrawe.github.io/harp-project/", None, None),
            Link("Paper", "https://arxiv.org/abs/2212.09530", None, None),
            Link("Code", "https://github.com/korrawe/harp", None, None),
        ]
    ),
    Paper(
        "HALO: A Skeleton-Driven Neural Occupancy Representation for Articulated Hands",
        "https://arxiv.org/abs/2109.11399",
        "teasers/halo.jpg",
        author_list(authors, "korrawe", "adrian", "zfan", "otmar", "siyu"),
        conferences["3dv"],
        2021,
        "Oral",
        [   # Link("Abstract", None, "Robotic grasping of house-hold objects has made remarkable progress in recent years. Yet, human grasps are still difficult to synthesize realistically. There are several key reasons: (1) the human hand has many degrees of freedom (more than robotic manipulators); (2) the synthesized hand should conform to the surface of the object; and (3) it should interact with the object in a semantically and physically plausible manner. To make progress in this direction, we draw inspiration from the recent progress on learning-based implicit representations for 3D object reconstruction. Specifically, we propose an expressive representation for human grasp modelling that is efficient and easy to integrate with deep neural networks. Our insight is that every point in a three-dimensional space can be characterized by the signed distances to the surface of the hand and the object, respectively. Consequently, the hand, the object, and the contact area can be represented by implicit surfaces in a common space, in which the proximity between the hand and the object can be modelled explicitly. We name this 3D to 2D mapping as Grasping Field, parameterize it with a deep neural network, and learn it from data. We demonstrate that the proposed grasping field is an effective and expressive representation for human grasp generation. Specifically, our generative model is able to synthesize high-quality human grasps, given only on a 3D object point cloud. The extensive experiments demonstrate that our generative model compares favorably with a strong baseline and approaches the level of natural human grasps. Furthermore, based on the grasping field representation, we propose a deep network for the challenging task of 3D hand-object interaction reconstruction from a single RGB image. Our method improves the physical plausibility of the hand-object contact reconstruction and achieves comparable performance for 3D hand reconstruction compared to state-of-the-art methods.", None),
            Link("Project page", "https://korrawe.github.io/HALO/HALO.html", None, None),
            Link("Paper", "https://arxiv.org/abs/2109.11399", None, None),
            Link("Code", "https://github.com/korrawe/halo", None, None),
        ]
    ),
    Paper(
        "Reducing Spelling Inconsistencies in Code-Switching ASR using Contextualized CTC Loss",
        "https://arxiv.org/pdf/2005.07920.pdf",
        "teasers/cctc.jpg",
        author_list(authors, "burin", "thananchai", "korrawe", "shenghui", "ekapol"),
        conferences["icassp"],
        2021,
        None,
        [   # Link("Abstract", None, "Robotic grasping of house-hold objects has made remarkable progress in recent years. Yet, human grasps are still difficult to synthesize realistically. There are several key reasons: (1) the human hand has many degrees of freedom (more than robotic manipulators); (2) the synthesized hand should conform to the surface of the object; and (3) it should interact with the object in a semantically and physically plausible manner. To make progress in this direction, we draw inspiration from the recent progress on learning-based implicit representations for 3D object reconstruction. Specifically, we propose an expressive representation for human grasp modelling that is efficient and easy to integrate with deep neural networks. Our insight is that every point in a three-dimensional space can be characterized by the signed distances to the surface of the hand and the object, respectively. Consequently, the hand, the object, and the contact area can be represented by implicit surfaces in a common space, in which the proximity between the hand and the object can be modelled explicitly. We name this 3D to 2D mapping as Grasping Field, parameterize it with a deep neural network, and learn it from data. We demonstrate that the proposed grasping field is an effective and expressive representation for human grasp generation. Specifically, our generative model is able to synthesize high-quality human grasps, given only on a 3D object point cloud. The extensive experiments demonstrate that our generative model compares favorably with a strong baseline and approaches the level of natural human grasps. Furthermore, based on the grasping field representation, we propose a deep network for the challenging task of 3D hand-object interaction reconstruction from a single RGB image. Our method improves the physical plausibility of the hand-object contact reconstruction and achieves comparable performance for 3D hand reconstruction compared to state-of-the-art methods.", None),
            # Link("Project page", "https://github.com/korrawe/grasping_field", None, None),
            Link("Paper", "https://arxiv.org/pdf/2005.07920.pdf", None, None),
            # Link("Code", "https://github.com/korrawe/grasping_field", None, None),
    #         Link("Bibtex", None, None, """@inproceedings{karunratanakul2020grasping,
    # title = {Grasping Field: Learning Implicit Representations for Human Grasps},
    # author = {Karunratanakul, Korrawe and Yang, Jinlong and Zhang, Yan and Black, Michael and Muandet, Krikamol and Tang, Siyu},
    # booktitle = {2020 International Conference on 3D Vision (3DV)},
    # month = nov,
    # year = {2020}
# }""")
        ]
    ),
    Paper(
        "Grasping Field: Learning Implicit Representations for Human Grasps",
        "https://github.com/korrawe/grasping_field",
        "teasers/grasping_field.jpg",
        author_list(authors, "korrawe", "jinlong", "yanz", "mjb", "krikamol", "siyu"),
        conferences["3dv"],
        2020,
        "Best Paper Award",
        [   # Link("Abstract", None, "Robotic grasping of house-hold objects has made remarkable progress in recent years. Yet, human grasps are still difficult to synthesize realistically. There are several key reasons: (1) the human hand has many degrees of freedom (more than robotic manipulators); (2) the synthesized hand should conform to the surface of the object; and (3) it should interact with the object in a semantically and physically plausible manner. To make progress in this direction, we draw inspiration from the recent progress on learning-based implicit representations for 3D object reconstruction. Specifically, we propose an expressive representation for human grasp modelling that is efficient and easy to integrate with deep neural networks. Our insight is that every point in a three-dimensional space can be characterized by the signed distances to the surface of the hand and the object, respectively. Consequently, the hand, the object, and the contact area can be represented by implicit surfaces in a common space, in which the proximity between the hand and the object can be modelled explicitly. We name this 3D to 2D mapping as Grasping Field, parameterize it with a deep neural network, and learn it from data. We demonstrate that the proposed grasping field is an effective and expressive representation for human grasp generation. Specifically, our generative model is able to synthesize high-quality human grasps, given only on a 3D object point cloud. The extensive experiments demonstrate that our generative model compares favorably with a strong baseline and approaches the level of natural human grasps. Furthermore, based on the grasping field representation, we propose a deep network for the challenging task of 3D hand-object interaction reconstruction from a single RGB image. Our method improves the physical plausibility of the hand-object contact reconstruction and achieves comparable performance for 3D hand reconstruction compared to state-of-the-art methods.", None),
            # Link("Project page", "https://github.com/korrawe/grasping_field", None, None),
            Link("Paper", "https://arxiv.org/pdf/2008.04451.pdf", None, None),
            Link("Code", "https://github.com/korrawe/grasping_field", None, None),
#             Link("Bibtex", None, None, """@inproceedings{karunratanakul2020grasping,
#     title = {Grasping Field: Learning Implicit Representations for Human Grasps},
#     author = {Karunratanakul, Korrawe and Yang, Jinlong and Zhang, Yan and Black, Michael and Muandet, Krikamol and Tang, Siyu},
#     booktitle = {2020 International Conference on 3D Vision (3DV)},
#     month = nov,
#     year = {2020}
# }""")
        ]
    ),
    Paper(
        "Uncovering thousands of new peptides with sequence-mask-search hybrid de novo peptide sequencing framework",
        "https://github.com/cmb-chula/SMSNet",
        "teasers/smsnet.jpg",
        author_list(authors, "korrawe", "hsinyao", "davidw", "ekapol", "sira"),
        conferences["mcp"],
        2019,
        None,
        [   # Link("Abstract", None, "Robotic grasping of house-hold objects has made remarkable progress in recent years. Yet, human grasps are still difficult to synthesize realistically. There are several key reasons: (1) the human hand has many degrees of freedom (more than robotic manipulators); (2) the synthesized hand should conform to the surface of the object; and (3) it should interact with the object in a semantically and physically plausible manner. To make progress in this direction, we draw inspiration from the recent progress on learning-based implicit representations for 3D object reconstruction. Specifically, we propose an expressive representation for human grasp modelling that is efficient and easy to integrate with deep neural networks. Our insight is that every point in a three-dimensional space can be characterized by the signed distances to the surface of the hand and the object, respectively. Consequently, the hand, the object, and the contact area can be represented by implicit surfaces in a common space, in which the proximity between the hand and the object can be modelled explicitly. We name this 3D to 2D mapping as Grasping Field, parameterize it with a deep neural network, and learn it from data. We demonstrate that the proposed grasping field is an effective and expressive representation for human grasp generation. Specifically, our generative model is able to synthesize high-quality human grasps, given only on a 3D object point cloud. The extensive experiments demonstrate that our generative model compares favorably with a strong baseline and approaches the level of natural human grasps. Furthermore, based on the grasping field representation, we propose a deep network for the challenging task of 3D hand-object interaction reconstruction from a single RGB image. Our method improves the physical plausibility of the hand-object contact reconstruction and achieves comparable performance for 3D hand reconstruction compared to state-of-the-art methods.", None),
            # Link("Project page", "https://github.com/korrawe/grasping_field", None, None),
            Link("Paper", "https://www.mcponline.org/article/S1535-9476(20)31650-9/fulltext", None, None),
            Link("Code", "https://github.com/cmb-chula/SMSNet", None, None),
#             Link("Bibtex", None, None, """@inproceedings{karunratanakul2020grasping,
#     title = {Grasping Field: Learning Implicit Representations for Human Grasps},
#     author = {Karunratanakul, Korrawe and Yang, Jinlong and Zhang, Yan and Black, Michael and Muandet, Krikamol and Tang, Siyu},
#     booktitle = {2020 International Conference on 3D Vision (3DV)},
#     month = nov,
#     year = {2020}
# }""")
        ]
    ),
    
#     Paper(
#         "Neural Parts: Learning Expressive 3D Shape Abstractions with Invertible Neural Networks",
#         "https://paschalidoud.github.io/neural_parts",
#         "teasers/neural_parts.png",
#         author_list(authors, "despi", "angelos", "andreas", "sanja"),
#         conferences["cvpr"],
#         2021,
#         None,
#         [   Link("Abstract", None, "Impressive progress in 3D shape extraction led to representations that can capture object geometries with high fidelity. In parallel, primitive-based methods seek to represent objects as semantically consistent part arrangements. However, due to the simplicity of existing primitive representations, these methods fail to accurately reconstruct 3D shapes using a small number of primitives/parts. We address the trade-off between reconstruction quality and number of parts with Neural Parts, a novel 3D primitive representation that defines primitives using an Invertible Neural Network (INN) which implements homeomorphic mappings between a sphere and the target object. The INN allows us to compute the inverse mapping of the homeomorphism, which in turn, enables the efficient computation of both the implicit surface function of a primitive and its mesh, without any additional post-processing. Our model learns to parse 3D objects into semantically consistent part arrangements without any part-level supervision. Evaluations on ShapeNet, D-FAUST and FreiHAND demonstrate that our primitives can capture complex geometries and thus simultaneously achieve geometrically accurate as well as interpretable reconstructions using an order of magnitude fewer primitives than state-of-the-art shape abstraction methods.", None),
#             Link("Project page", "https://paschalidoud.github.io/neural_parts", None, None),
#             Link("Paper", "https://arxiv.org/pdf/2103.10429.pdf", None, None),
#             Link("Code", "https://github.com/paschalidoud/neural_parts", None, None),
#             Link("Bibtex", None, None, """@inproceedings{Paschalidou2021CVPR,
#     title = {Neural Parts: Learning Expressive 3D Shape Abstractions with Invertible Neural Networks},
#     author = {Paschalidou, Despoina and Katharopoulos, Angelos and Geiger, Andreas and Fidler, Sanja},
#     booktitle = {Proceedings IEEE Conf. on Computer Vision and Pattern Recognition (CVPR)},
#     month = jun,
#     year = {2021}
# }""")
#         ]
#     ),
#     Paper(
#         "Learning Unsupervised Hierarchical Part Decomposition of 3D Objects from a Single RGB Image",
#         "http:superquadrics.com/hierarchical_primitives",
#         "teasers/hierarchical_primitives.png",
#         author_list(authors, "despi", "luc", "andreas"),
#         conferences["cvpr"],
#         2020,
#         None,
#         [
#             Link("Abstract", None, "Humans perceive the 3D world as a set of distinct objects that are characterized by various low-level (geometry, reflectance) and high-level (connectivity, adjacency, symmetry) properties. Recent methods based on convolutional neural networks (CNNs) demonstrated impressive progress in 3D reconstruction, even when using a single 2D image as input. However, the majority of these methods focuses on recovering the local 3D geometry of an object without considering its part-based decomposition or relations between parts. We address this challenging problem by proposing a novel formulation that allows to jointly recover the geometry of a 3D object as a set of primitives as well as their latent hierarchical structure without part-level supervision. Our model recovers the higher level structural decomposition of various objects in the form of a binary tree of primitives, where simple parts are represented with fewer primitives and more complex parts are modeled with more components. Our experiments on the ShapeNet and D-FAUST datasets demonstrate that considering the organization of parts indeed facilitates reasoning about 3D geometry.", None),
#             Link("Project page", "http:superquadrics.com/hierarchical_primitives", None, None),
#             Link("Paper", "https://arxiv.org/pdf/2004.01176.pdf", None, None),
#             Link("Poster", "data/Paschalidou2020CVPR_poster.pdf", None, None),
#             Link("Code", "https://github.com/paschalidoud/hierarchical_primitives", None, None),
#             Link("Blog", "https://autonomousvision.github.io/hierarchical-primitives/", None, None),
#             Link("Slides", "http://www.cvlibs.net/publications/Paschalidou2020CVPR_slides.pdf", None, None),
#             Link("Video", "https://www.youtube.com/watch?v=QgD0NHbWVlU&vq=hd1080&autoplay=1", None, None),
#             Link("Bibtex", None, None, """@inproceedings{Paschalidou2020CVPR,
#     title = {Learning Unsupervised Hierarchical Part Decomposition of 3D Objects from a Single RGB Image},
#     author = {Paschalidou, Despoina and Luc van Gool and Geiger, Andreas},
#     booktitle = {Proceedings IEEE Conf. on Computer Vision and Pattern Recognition (CVPR)},
#     month = jun,
#     year = {2020},
# }""")
#         ]
#     ),
#     Paper(
#         "Superquadrics Revisited: Learning 3D Shape Parsing beyond Cuboids",
#         # "https://arxiv.org/pdf/1904.09970.pdf",
#         "http:superquadrics.com",
#         "teasers/superquadrics_revisited.png",
#         author_list(authors, "despi", "osman", "andreas"),
#         conferences["cvpr"],
#         2019,
#         None,
#         [
#             Link("Abstract", None, "Abstracting complex 3D shapes with parsimonious part-based representations has been a long standing goal in computer vision. This paper presents a learning-based solution to this problem which goes beyond the traditional 3D cuboid representation by exploiting superquadrics as atomic elements. We demonstrate that superquadrics lead to more expressive 3D scene parses while being easier to learn than 3D cuboid representations. Moreover, we provide an analytical solution to the Chamfer loss which avoids the need for computational expensive reinforcement learning or iterative prediction. Our model learns to parse 3D objects into consistent superquadric representations without supervision. Results on various ShapeNet categories as well as the SURREAL human body dataset demonstrate the flexibility of our model in capturing fine details and complex poses that could not have been modelled using cuboids.", None),
#             Link("Project page", "http:superquadrics.com/learnable-superquadrics.html", None, None),
#             Link("Paper", "https://arxiv.org/pdf/1904.09970.pdf", None, None),
#             Link("Poster", "data/Paschalidou2019CVPR_poster.pdf", None, None),
#             Link("Code", "https://github.com/paschalidoud/superquadric_parsing", None, None),
#             Link("Blog", "https://autonomousvision.github.io/superquadrics-revisited/", None, None),
#             Link("Video", "https://www.youtube.com/watch?v=eaZHYOsv9Lw", None, None),
#             Link("Bibtex", None, None, """@inproceedings{Paschalidou2019CVPR,
#     title = {Superquadrics Revisited: Learning 3D Shape Parsing beyond Cuboids},
#     author = {Paschalidou, Despoina and Ulusoy, Ali Osman and Geiger, Andreas},
#     booktitle = {Proceedings IEEE Conf. on Computer Vision and Pattern Recognition (CVPR)},
#     month = jun,
#     year = {2019},
# }""")
#         ]
#     ),
#     Paper(
#         "PointFlowNet: Learning Representations for Rigid Motion Estimation from Point Clouds",
#         "https://avg.is.tuebingen.mpg.de/publications/behl2019cvpr",
#         # "http://www.cvlibs.net/publications/Behl2019CVPR.pdf",
#         "teasers/pointflownet.png",
#         author_list(authors, "aseem", "despi", "simon", "andreas"),
#         conferences["cvpr"],
#         2019,
#         None,
#         [
#             Link("Abstract", None, "Despite significant progress in image-based 3D scene flow estimation, the performance of such approaches has not yet reached the fidelity required by many applications. Simultaneously, these applications are often not restricted to image-based estimation: laser scanners provide a popular alternative to traditional cameras, for example in the context of self-driving cars, as they directly yield a 3D point cloud. In this paper, we propose to estimate 3D motion from such unstructured point clouds using a deep neural network. In a single forward pass, our model jointly predicts 3D scene flow as well as the 3D bounding box and rigid body motion of objects in the scene. While the prospect of estimating 3D scene flow from unstructured point clouds is promising, it is also a challenging task. We show that the traditional global representation of rigid body motion prohibits inference by CNNs, and propose a translation equivariant representation to circumvent this problem. For training our deep network, a large dataset is required. Because of this, we augment real scans from KITTI with virtual objects, realistically modeling occlusions and simulating sensor noise. A thorough comparison with classic and learning-based techniques highlights the robustness of the proposed approach.", None),
#             # Link("Project page", "https://avg.is.tuebingen.mpg.de/publications/behl2019cvpr", None, None),
#             Link("Paper", "http://www.cvlibs.net/publications/Behl2019CVPR.pdf", None, None),
#             Link("Code", "https://github.com/aseembehl/pointflownet", None, None),
#             Link("Video", "https://youtu.be/cjJhzYCUNTY", None, None),
#             Link("Bibtex", None, None, """@inproceedings{Behl2019CVPR,
#     title = {PointFlowNet: Learning Representations for Rigid Motion Estimation from Point Clouds },
#     author = {Behl, Aseem and Paschalidou, Despoina and Donne, Simon and Geiger, Andreas},
#     booktitle = {Proceedings IEEE Conf. on Computer Vision and Pattern Recognition (CVPR)},
#     month = jun,
#     year = {2019},
# }""")
#         ]
#     ),
#     Paper(
#         "RayNet: Learning Volumetric 3D Reconstruction with Ray Potentials",
#         # "http://openaccess.thecvf.com/content_cvpr_2018/papers/Paschalidou_RayNet_Learning_Volumetric_CVPR_2018_paper.pdf",
#         "http://raynet-mvs.com",
#         "teasers/raynet.png",
#         author_list(authors, "despi", "osman", "caro", "luc", "andreas"),
#         conferences["cvpr"],
#         2018,
#         "Spotlight Presentation",
#         [
#             Link("Abstract", None, "In this paper, we consider the problem of reconstructing a dense 3D model using images captured from different views. Recent methods based on convolutional neural networks (CNN) allow learning the entire task from data. However, they do not incorporate the physics of image formation such as perspective geometry and occlusion. Instead, classical approaches based on Markov Random Fields (MRF) with ray-potentials explicitly model these physical processes, but they cannot cope with large surface appearance variations across different viewpoints. In this paper, we propose RayNet, which combines the strengths of both frameworks. RayNet integrates a CNN that learns view-invariant feature representations with an MRF that explicitly encodes the physics of perspective projection and occlusion. We train RayNet end-to-end using empirical risk minimization. We thoroughly evaluate our approach on challenging real-world datasets and demonstrate its benefits over a piece-wise trained baseline, hand-crafted models as well as other learning-based approaches.", None),
#             # Link("Project page", "http://raynet-mvs.com", None, None),
#             Link("Paper", "http://openaccess.thecvf.com/content_cvpr_2018/papers/Paschalidou_RayNet_Learning_Volumetric_CVPR_2018_paper.pdf", None, None),
#             Link("Poster", "data/Paschalidou2018CVPR_poster.pdf", None, None),
#             Link("Code", "http://github.com/paschalidoud/raynet", None, None),
#             Link("Video", "https://www.youtube.com/watch?v=PZ0u1VZLLkU&feature=youtu.be", None, None),
#             Link("Bibtex", None, None, """@inproceedings{Paschalidou2018CVPR,
#       title = {RayNet: Learning Volumetric 3D Reconstruction with Ray Potentials},
#       author = {Paschalidou, Despoina and Ulusoy, Ali Osman and Schmitt, Carolin and Gool, Luc and Geiger, Andreas},
#       booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
#       month = jun,
#       year = {2018}
# }""")
#         ]
#     ),
#     Paper(
#         "Learning local feature aggregation functions with backpropagation",
#         "https://arxiv.org/pdf/1706.08580.pdf",
#         "teasers/local_feature_aggregation.png",
#         author_list(authors, "despi", "angelos", "diou", "delo"),
#         conferences["eusipco"],
#         2017,
#         None,
#         [
#             Link("Abstract", None, "This paper introduces a family of local feature aggregation functions and a novel method to estimate their parameters, such that they generate optimal representations for classification (or any task that can be expressed as a cost function minimization problem). To achieve that, we compose the local feature aggregation function with the classifier cost function and we backpropagate the gradient of this cost function in order to update the local feature aggregation function parameters. Experiments on synthetic datasets indicate that our method discovers parameters that model the class-relevant information in addition to the local feature space. Further experiments on a variety of motion and visual descriptors, both on image and video datasets, show that our method outperforms other state-of-the-art local feature aggregation functions, such as Bag of Words, Fisher Vectors and VLAD, by a large margin.", None),
#             Link("Paper", "https://arxiv.org/pdf/1706.08580.pdf", None, None),
#             Link("Poster", "data/eusipco_poster.pdf", None, None),
#             Link("Code", "https://github.com/paschalidoud/feature-aggregation", None, None),
#             Link("Bibtex", None, None, """@inproceedings{katharopoulos2017learning
#       title = {Learning local feature aggregation functions with backpropagation},
#       author = {Paschalidou, Despoina and Katharopoulos, Angelos and Diou, Christos and Delopoulos, Anastasios},
#       publisher = {IEEE},
#       month = aug,
#       year = {2017},
#       url = {http://ieeexplore.ieee.org/Abstract/document/8081307/},
# }""")
#         ]
#     ),
#     Paper(
#         "Fast Supervised LDA for Discovering Micro-Events in Large-Scale Video Datasets",
#         "http://ldaplusplus.com", # "https://mug.ee.auth.gr/wp-content/uploads/fsLDA.pdf",
#         "teasers/fslda.png",
#         author_list(authors, "angelos", "despi", "diou", "delo"),
#         conferences["acmmm"],
#         2016,
#         None,
#         [
#             Link("Abstract", None, "This paper introduces fsLDA, a fast variational inference method for supervised LDA, which overcomes the computational limitations of the original supervised LDA and enables its application in large-scale video datasets. In addition to its scalability, our method also overcomes the drawbacks of standard, unsupervised LDA for video, including its focus on dominant but often irrelevant video information (e.g. background, camera motion). As a result, experiments in the UCF11 and UCF101 datasets show that our method consistently outperforms unsupervised LDA in every metric. Furthermore, analysis shows that class-relevant topics of fsLDA lead to sparse video representations and encapsulate high-level information corresponding to parts of video events, which we denote 'micro-events'", None),
#             # Link("Project page", "http://ldaplusplus.com", None, None),
#             Link("Paper", "https://mug.ee.auth.gr/wp-content/uploads/fsLDA.pdf", None, None),
#             Link("Poster", "data/fslda_poster.pdf", None, None),
#             Link("Code", "https://github.com/angeloskath/supervised-lda", None, None),
#             Link("Blog", "https://mug.ee.auth.gr/discovering-micro-events-video-data-using-topic-modeling/", None, None),
#             Link("Bibtex", None, None, """@inproceedings{katharopoulos2016fast
#         title = {Fast Supervised LDA for Discovering Micro-Events in Large-Scale Video Datasets},
#         author = {Katharopoulos, Angelos and Paschalidou, Despoina and Diou, Christos and Delopoulos, Anastasios},
#         booktitle = {Proceedings of the 2016 ACM on Multimedia Conference},
#         pages = {332,336},
#         month = oct,
#         year = {2016},
#         url = {http://dl.acm.org/citation.cfm?id=2967237},
#         month_numeric = {10}

# }""")
#         ]
#     ),
]


def build_publications_list(publications):
    def image(paper):
        if paper.image is not None:
            return '<img src="{}" alt="{}" />'.format(
                paper.image, paper.title
            )
        else:
            return '&nbsp;'

    def title(paper):
        return '<a href="{}">{}</a>'.format(paper.url, paper.title)

    def authors(paper):
        def author(author):
            if author.is_me:
                return '<strong class="author">{}</strong>'.format(author.name)
            else:
                return '<a href="{}" class="author">{}</a>'.format(
                    author.url, author.name
                )
        return ", ".join(author(a) for a in paper.authors)

    def conference(paper):
        cf = '{}, {}'.format(paper.conference.name, paper.year)
        if paper.special is not None:
            cf = cf + '<div class="special">   ({})</div>'.format(paper.special)
        return cf

    def links(paper):
        def links_list(paper):
            def link(i, link):
                if link.url is not None:
                    # return '<a href="{}">{}</a>'.format(link.url, link.name)
                    return '<a href="{}" data-type="{}">{}</a>'.format(link.url, link.name, link.name)
                else:
                    return '<a href="#" data-type="{}" data-index="{}">{}</a>'.format(link.name, i, link.name)
            return " ".join(
                link(i, l) for i, l in enumerate(paper.links)
            )

        def links_content(paper):
            def content(i, link):
                if link.url is not None:
                    return ""
                return '<div class="link-content" data-index="{}">{}</div>'.format(
                    i, link.html if link.html is not None
                       else '<pre>' + link.text + "</pre>"
                )
            return "".join(content(i, link) for i, link in enumerate(paper.links))
        return links_list(paper) + links_content(paper)

    def paper(p):
        return ('<div class="row paper">'
                    '<div class="image">{}</div>'
                    '<div class="content">'
                        '<div class="paper-title">{}</div>'
                        '<div class="conference">{}</div>'
                        '<div class="authors">{}</div>'
                        '<div class="links">{}</div>'
                    '</div>'
                '</div>').format(
                    image(p),
                    title(p),
                    conference(p),
                    authors(p),
                    links(p)
                )

    return "".join(paper(p) for p in publications)


def main(argv):
    parser = argparse.ArgumentParser(
        description="Create a publication list and insert in into an html file"
    )
    parser.add_argument(
        "file",
        help="The html file to insert the publications to"
    )

    parser.add_argument(
        "--safe", "-s",
        action="store_true",
        help="Do not overwrite the file but create one with suffix .new"
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Do not output anything to stdout/stderr"
    )

    args = parser.parse_args(argv)

    # Read the file
    with open(args.file) as f:
        html = f.read()

    # Find the fence comments
    start_text = "<!-- start publication list -->"
    end_text = "<!-- end publication list -->"
    start = html.find(start_text)
    end = html.find(end_text, start)
    if end < start or start < 0:
        _print(args, "Could not find the fence comments", file=sys.stderr)
        sys.exit(1)

    # Build the publication list in html
    replacement = build_publications_list(publications)

    # Update the html and save it
    html = html[:start+len(start_text)] + replacement + html[end:]

    # If safe is set do not overwrite the input file
    if args.safe:
        with open(args.file[:-5] + "_new.html", "w") as f:
            f.write(html)
    else:
        with open(args.file, "w") as f:
            f.write(html)


if __name__ == "__main__":
    main(None)
