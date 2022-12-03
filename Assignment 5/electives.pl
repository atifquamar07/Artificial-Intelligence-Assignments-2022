:- dynamic take/1.
:- dynamic suggest_course/1.

suggest_course('ML'):-
    take('ML'),
    write("**********************************************************************************"), nl,
    write("CSE343/CSE543/ECE563: MACHINE LEARNING"), nl,
    write("**********************************************************************************"), nl, nl,
    write("This is an introductory course on Machine Learning (ML) that is offered to undergraduate and graduate students. The contents are designed to cover both theoretical and practical aspects of several well-established ML techniques. The assignments will contain theory and programming questions that help strengthen the theoretical foundations as well as learn how to engineer ML solutions to work on simulated and publicly available real datasets. The project(s) will require students to develop a complete Machine Learning solution requiring preprocessing, design of the classifier/regressor, training and validation, testing and evaluation with quantitative performance comparisons."), nl, nl.

suggest_course('NLP'):-
    take('NLP'),
    write("**********************************************************************************"), nl,
    write("CSE556: NATURAL LANGUAGE PROCESSING (NLP)"), nl,
    write("**********************************************************************************"), nl, nl,
    write("This course will cover a broad range of topics related to NLP, including basic text processing (such as tokenization, stemming), language modeling, morphology, syntax, dependency parsing, distributional and lexical Semantics, sense disambiguation, information extraction etc. We will also introduce underlying theory from probability, statistics, machine learning that are essential to understand fundamental algorithms in NLP such as language modeling, HMM etc. This course will end with more advanced topics in NLP such as stylometry analysis, sentiment analysis, named-entity disambiguation, machine translation etc. The term projects will provide opportunity to the students to get hands-on experience on designing different real-world NLP models."), nl, nl.

suggest_course('ICN'):-
    take('ICN'),
    write("**********************************************************************************"), nl,
    write("BIO534: INTRODUCTION TO COMPUTATIONAL NEUROSCIENCE"), nl,
    write("**********************************************************************************"), nl, nl,
    write("This introductory neuroscience provides basic understanding of neuronal systems and their respective mathematical models that describes the behavior of the neurons under various conditions. The aim of this course is to encourage Computational biology students to diversify into the area of neuroscience. This course in not about neural networks and machine learning, but about the use of the tools of dynamical systems theory toundertand oscillatory properties of single cell neurons. Nonlinear ODE and PDE models will be constructed, analyzed and simulated using MATLAB to understand different firing patterns of the neuronal systems under normal and pathalogical conditions."), nl, nl.

suggest_course('CIA'):-
    take('CIA'),
    write("**********************************************************************************"), nl,
    write("MTH311: COMBINATORICS AND ITS APPLICATIONS"), nl,
    write("**********************************************************************************"), nl, nl,
    write("The aim of this course is to familiarize students with fundamental concepts in combinatorics, especially those used in enumeration. Topics covered include permutation groups, linear codes, Stirling and Bell numbers. Generating functions are introduced and their applications are discussed. Applications of group theory to enumeration: Burnside’s Lemma and Polya’s theory of counting are covered. Students are introduced to error correcting codes and linear codes over finite fields."), nl, nl.


suggest_course('CRN'):-
    take('CRN'),
    write("**********************************************************************************"), nl,
    write("MTH544: CALCULUS IN R(N) AND ITS APPLICATIONS"), nl,
    write("**********************************************************************************"), nl, nl,
    write("This an introductory course on smooth differential forms on smooth manifolds. It will attempt to serve as a sequel to abstracting calculus beyond real and multivariable analysis to higher dimensional vector spaces and manifolds. The primary emphasis will be on understanding calculus in R^n to begin with, first for n = 3, and then more generally via differential forms. The course also has an applied theme and will conclude with three different applications of concepts: to engineering via optimization on manifolds, to mathematics via de Rham cohomology of manifolds, and to physics via modeling of Maxwell’s equations. We shall review basic concepts from multivariable calculus, linear algebra, algebra, geometry and topology first as well as intersperse them later as and when needed. Initially, this shall include geometry in linear algebra, partial and directional derivatives, multiple integrals, alternating multilinear algebra, parametric curves and surfaces, and tangent vectors and spaces. Next, we shall introduce differential forms via integration, the exterior derivative, wedge product of forms, and properties of differential forms in R^n. This will be followed by a quick discussion of Riemannian metric, the Hodge star map, and inner product of differential forms in this context. Discussion of Stoke’s theorem, an introduction to smooth manifolds, notion of vector fields, push forward and pullback maps will form the last conceptual module. In the end, we will discuss three applications, namely computational methods for linear optimization on manifolds with geometric constraints, de Rham cohomology of manifolds, and differential forms modeling of Maxwells equations."), nl, nl.


suggest_course('DVD'):-
    take('CRN'),
    write("**********************************************************************************"), nl,
    write("ECE314/ECE514: DIGITAL VLSI DESIGN"), nl,
    write("**********************************************************************************"), nl, nl,
    write("This course introduces students to CMOS circuits, develops first-order current-voltage and capacitance-voltage models for transistors, transfer characteristics of CMOS inverter, performance estimation for circuits through logical effort, interconnects, combinational circuit design, circuit families, sequential circuit design including clocking and latching techniques, design of datapath subsystems (adders, shifters, multipliers etc.), design of memory subsystems. A course project using state-of-the-art computer aided design (CAD) tools in VLSI gives students hands-on exposer to the most current technology/process."), nl, nl.


suggest_course('IBC'):-
    take('IBC'),
    write("**********************************************************************************"), nl,
    write("CSE528: INTRODUCTION TO BLOCKCHAIN AND CRYPTOCURRENCY"), nl,
    write("**********************************************************************************"), nl, nl,
    write("From this course, we will learn about basics of blockchains and cryptocurrency. Topics to be covered include how cryptocurrency such as Bitcoin and Ethereum work, blockchain and other decentralized consensus protocols, digital coin mining, security and privacy of cryptocurrencies, scalability, cryptographic techniques for digital currency, and applications of blockchain to smart contracts, and financial exchanges."), nl, nl.


suggest_course('DIP'):-
    take('DIP'),
    write("**********************************************************************************"), nl,
    write("CSE340/CSE540/ECE340: DIGITAL IMAGE PROCESSING"), nl,
    write("**********************************************************************************"), nl, nl,
    write("This Course includes fundamental theories and algorithms of digital image acquisition, color representation, sampling and quantization, frequency transform via DFT, enhancement, filtering, restoration, analysis, feature extraction, segmentation, morphological transform, and compression. Practical applications such as JPEG compression will be covered."), nl, nl.


main:-
    suggest_course(_).


