# fc_rules_test_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def tertarik_dengan_materi(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'mencari', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'membuka', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'tertarik',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def memahami(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'tertarik', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'selesai_kurang_dari_30_menit', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'nilai_di_atas_70', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('facts', 'memahami',
                               (rule.pattern(0).as_data(context),
                                rule.pattern(1).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc_rules_test')
  
  fc_rule.fc_rule('tertarik_dengan_materi', This_rule_base, tertarik_dengan_materi,
    (('facts', 'mencari',
      (contexts.variable('user'),
       contexts.variable('materi'),),
      False),
     ('facts', 'membuka',
      (contexts.variable('user'),
       contexts.variable('materi'),),
      False),),
    (contexts.variable('user'),
     contexts.variable('materi'),))
  
  fc_rule.fc_rule('memahami', This_rule_base, memahami,
    (('facts', 'tertarik',
      (contexts.variable('user'),
       contexts.variable('materi'),),
      False),
     ('facts', 'selesai_kurang_dari_30_menit',
      (contexts.variable('user'),
       contexts.variable('materi'),),
      False),
     ('facts', 'nilai_di_atas_70',
      (contexts.variable('user'),
       contexts.variable('materi'),),
      False),),
    (contexts.variable('user'),
     contexts.variable('materi'),))


Krb_filename = '..\\data\\fc_rules_test.krb'
Krb_lineno_map = (
    ((12, 16), (3, 3)),
    ((17, 21), (4, 4)),
    ((22, 24), (6, 6)),
    ((33, 37), (10, 10)),
    ((38, 42), (11, 11)),
    ((43, 47), (12, 12)),
    ((48, 50), (14, 14)),
)
