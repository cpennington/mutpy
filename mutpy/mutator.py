from mutpy import operator

class Mutator:
    def __init__(self, target_ast, mutation_cfg):
        self.target_ast = target_ast
        self.mutation_cfg = mutation_cfg
    def mutate(self):
        op = operator.ArithmeticOperatorReplacement()
        for mutant in op.incremental_visit(self.target_ast):
            yield mutant