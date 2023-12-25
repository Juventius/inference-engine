from pyke import knowledge_engine
import os
import shutil

# Clear recent fact base
if os.path.exists("compiled_krb"):
    shutil.rmtree("./compiled_krb")

# Load the .kfb file
with open("./data/facts.kfb", "r") as f:
    facts = f.readlines()

# Print all of the facts
print("\n[USER FACTS]")
for fact in facts:
    print(fact.strip())

# Compiling current fact base
print("\n[START ENGINE COMPILE]")
engine = knowledge_engine.engine("./data")
print("[FINISH ENGINE COMPILE]", end="\n\n")

# Activate inference engine
engine.activate('fc_rules_test')

# Proving goals
print("[GENERATED FACTS]")
with engine.prove_goal('facts.tertarik($user, $materi)') as gen:
    for vars, plan in gen:
        print(vars['user'], "tertarik dengan", vars['materi'])
print()
with engine.prove_goal('facts.memahami($user, $materi)') as gen:
    for vars, plan in gen:
        print(vars['user'], "memahami materi", vars['materi'])
print()

# Reset engine
engine.reset()
