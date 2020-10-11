from collections import defaultdict

import numpy as np
from scipy.optimize import linprog


class LinearOptimizer:

    def __init__(
            self,
            items_count,
            a_ineq,
            b_ineq,
            dest,
            target,
            compromise_weight
    ):
        self.items_count = items_count
        self.a_ineq = a_ineq
        self.b_ineq = b_ineq
        self.dest = dest
        self.target = target
        self.compromise_weight = compromise_weight
        self.opt = None

    def plain_linear_optimize(self):
        result = dict()
        if self.opt:
            return self.opt

        for i in self.dest:
            sign = -1 if self.target[i] == 'max' else 1
            opt = linprog(c=(sign * self.dest[i]).tolist(),
                                     A_ub=self.a_ineq.tolist(),
                                     b_ub=self.b_ineq.tolist(),
                                     bounds=[(0, float('inf')) for x in range(self.items_count)],
                                     method='simplex')
            if not opt.success:
                raise Exception('Bad result')
            result[i] = dict()
            result[i]['F'] = sign * opt.fun
            result[i]['X'] = opt.x

        self.opt = result
        return result

    def hybrid_linear_optimize(self):
        if not self.opt:
            self.plain_linear_optimize()
        left_restrictions = np.concatenate((self.a_ineq, np.zeros((len(self.a_ineq), 3))), axis=1)
        a_eq = []
        iter = 0
        for i in self.dest:
            add_row = np.zeros(len(self.target))
            sign = 1 if self.target[i] == 'max' else -1
            add_row[iter] = sign * self.opt[i]['F']
            a_eq.append(np.concatenate((self.dest[i], np.array(add_row))))
            iter += 1
        b_eq = []
        for i in self.opt:
            b_eq.append(self.opt[i]['F'])

        compromise_criteria = np.concatenate((np.zeros(self.items_count), np.array(self.compromise_weight)))
        compromise_opt = linprog(c=compromise_criteria.tolist(),
                                 A_ub=left_restrictions.tolist(),
                                 b_ub=self.b_ineq.tolist(),
                                 A_eq=a_eq,
                                 b_eq=b_eq,
                                 bounds=[(0, float('inf')) for x in range(len(compromise_criteria))],
                                 method='simplex')
        if not compromise_opt.success:
            raise Exception('Bad result')
        res = dict()
        res['F'] = compromise_opt.fun
        res['X'] = compromise_opt.x
        return res
