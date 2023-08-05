from pyke import knowledge_engine
import os
import shutil

# Clear recent fact base
if os.path.exists("compiled_krb"):
    shutil.rmtree("./compiled_krb")

# Compiling current fact base
print("\n[START COMPILE]")
engine = knowledge_engine.engine("./data")
print("[FINISH COMPILE]", end="\n\n")

# Activate inference engine
engine.activate('fc_HADE_rules_test')

# Proving goals
print("[PROVING GOALS]")
with engine.prove_goal('facts.tertarik($user, $materi)') as gen:
    for vars, plan in gen:
        print(vars['user'], "tertarik dengan", vars['materi'])
print()
with engine.prove_goal('facts.memahami($user, $materi)') as gen:
    for vars, plan in gen:
        print(vars['user'], "memahami materi", vars['materi'])
print()
with engine.prove_goal('facts.selesai_tepat_waktu($user, $materi)') as gen:
    for vars, plan in gen:
        print(vars['user'], "dapat menyelesaikan materi", vars['materi'], "tepat waktu")
print()

# Reset engine
engine.reset()