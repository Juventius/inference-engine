# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', 'C:\\Users\\juven\\Documents\\Codes\\Python\\HADE\\inference_engine', 'data\\facts.kfb'):
           [1703489207.168558, 'facts.fbc'],
         ('', 'C:\\Users\\juven\\Documents\\Codes\\Python\\HADE\\inference_engine', 'data\\fc_rules_test.krb'):
           [1703489207.1725397, 'fc_rules_test_fc.py'],
        },
        compiler_version)

