# DPLL SAT-solver

Name - DPLL SAT-solver

By - Arnav Despande

About - This SAT solver was unable to meet the full scope of my expectations due to time crunches. It is nonetheless complete and in addition to DPLL, implements preprocessing of tautologies, blocked clauses, and unit clauses. I hope to finish integrating CDCL functionality as well as VSIDS, two-pointer tracking, and fast restart capabilities into it sometime soon. Future plans include creating a visualizer for this via openGL.

This can be run on a Linux machine with python installed: cat <CNF_file>.cnf | ./run_ad_DPLL.sh

If permission is denied to run it, then grant the script permission through: chmod +x run_ad_DPLL.sh and try again

This can be run on Windows by running: cat <CNF_file>.cnf | python ad_DPLL.py

Evaluation directories simple_out, medium_out, hard_out can be found in the "Evaluation" folder.

I consent to having my solver and name be included in the evaluation page.
