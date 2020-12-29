#!/bin/bash
export PYTHONPATH=src
CASE=${CASE:-"1"}

echo "Running mutation testing ${CASE}"

mut.py \
    --target src/mutation_testing_${CASE}.py \
    --unit-test tests/test_mutation_testing_${CASE}.py \
    --operator AOD  `# delete arithmetic operator` \
    --operator AOR  `# replace arithmetic operator` \
    --operator COD  `# delete conditional operator` \
    --operator COI  `# insert conditional operator` \
    --operator CRP  `# replace constant` \
    --operator ROR  `# replace relational operator` \
    --show-mutants
