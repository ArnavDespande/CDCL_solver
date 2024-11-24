# DPLL SAT-solver

Name - DPLL SAT-solver

By - Arnav Despande

About - This SAT solver was unable to meet the full scope of expectations due to external circumstances limiting my time to work on it. It is nonetheless complete and in addition to DPLL, implements preprocessing of tautologies, blocked clauses, and unit clauses. I hope to finish integrating CDCL functionality as well as VSIDS, two-pointer tracking, and fast restart capabilities into it sometime soon. Future plans include creating a visualizer for this via openGL.

This can be run on a Linux machine with python installed: cat <CNF_file>.cnf | ./run_ad_DPLL.sh
Windows machines with python can run it by running: cat <CNF_file>.cnf | python ad_DPLL.py

Evaluation directories simple_out, medium_out, hard_out can be found in the "evaluation" folder.

I consent to having my solver and name be included in the evaluation page.
