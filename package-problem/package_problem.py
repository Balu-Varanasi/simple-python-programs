"""
    You want to send your friend a package with different things. Each
    thing you put inside the package has such parameters as index number,
    weight and cost.

    The package has a weight limit. Your goal is to determine which things
    to put into the package so that the total weight is less than or equal
    to the package limit and the total cost is as large as possible. You
    would prefer to send a package which weights less in case there is more
    than one package with the same price.

    INPUT SAMPLE:

    Your program should accept as its first argument a path to a filename.
    The input file contains several lines. Each line is one test case.

    Each line contains the weight that the package can take (before the colon)
    and the list of things you need to choose. Each thing is enclosed in
    parentheses where the 1st number is a thing's index number, the 2nd is its
    weight and the 3rd is its cost. E.g.

        81 : (1,53.38,$45) (2,88.62,$98) (3,78.48,$3) (4,72.30,$76) \
             (5,30.18,$9) (6,46.34,$48)
        8  : (1,15.3,$34)
        75 : (1,85.31,$29) (2,14.55,$74) (3,3.98,$16) (4,26.24,$55) \
             (5,63.69,$52) (6,76.25,$75) (7,60.02,$74) (8,93.18,$35)\
             (9,89.95,$78)
        56 : (1,90.72,$13) (2,33.80,$40) (3,43.15,$10) (4,37.97,$16)\
             (5,46.81,$36) (6,48.77,$79) (7,81.80,$45) (8,19.36,$79)\
             (9,6.76,$64)


    OUTPUT SAMPLE:

    For each set of things that you put into the package provide a list \
    (items’ index numbers are separated by comma). E.g.

        4
        -
        2,7
        8,9

    CONSTRAINTS:

        Max weight that a package can take is ≤ 100
        There might be up to 15 items you need to choose from
        Max weight and cost of an item is ≤ 100
"""

import sys


class Thing(object):
    """
    Attributes:
        - id
        - weight
        - cost
    """

    def __init__(self, thing_id, thing_weight, thing_cost):
        self.id = thing_id
        self.weight = thing_weight
        self.cost = thing_cost

    def __repr__(self):
        return "Thing %d (weight: %d, cost: $%d)" % (
            self.id, self.weight, self.cost)


class Package(object):
    """
    Attributes:
        - MAX_WEIGHT
        - THINGS_LIMIT
        - given_things
        - things (used things)
        - best weight
        - best cost
    """

    def __init__(self, raw_things, MAX_WEIGHT=100, THINGS_LIMIT=15):
        self.MAX_WEIGHT = int(MAX_WEIGHT)
        self.THINGS_LIMIT = int(THINGS_LIMIT)
        self.given_things = self.parse_raw_things(raw_things, THINGS_LIMIT)

        self.things = None
        self.best_weight = None
        self.best_cost = None

        self.set_things()

    def set_things(self):
        best_weight, best_cost, best_used = self._get_best_packaging(
            self.MAX_WEIGHT, self.given_things)
        self.things = []
        for i in xrange(len(best_used)):
            if best_used[i]:
                self.things.append(self.given_things[i])

    def get_things(self):
        return self.things

    #####################################################
    # Parses the raw string and prepares 'Thing' object #
    #####################################################

    @classmethod
    def parse_raw_things(cls, raw_things, THINGS_LIMIT):
        if len(raw_things) > THINGS_LIMIT:
            raise Exception("things shouldn't be more than %d" % THINGS_LIMIT)
        things = []
        for raw_thing in raw_things:
            things.append(Thing(int(raw_thing.split(',')[0][1:]),
                                float(raw_thing.split(',')[1]),
                                int(raw_thing.split(',')[2][1:-1])))
        return things

    #########################################################################
    # Helper methods to calculate the total weight, cost and best packaging #
    #########################################################################
    @classmethod
    def _get_total_weight_and_cost(cls, used_things, given_things):
        total_weight = 0
        total_cost = 0
        for i in xrange(len(used_things)):
            if used_things[i]:
                weight, cost = given_things[i].weight, given_things[i].cost
                total_weight += weight
                total_cost += cost
        return total_weight, total_cost

    @classmethod
    def _get_best_packaging(cls, max_weight, things, best_weight=float('inf'),
                            best_cost=0, best_used=None, prefix=None):

        if prefix is None:
            prefix = []

        if len(prefix) == len(things):
            weight, cost = cls._get_total_weight_and_cost(prefix, things)

            if weight < max_weight and (
                cost > best_cost or (
                    cost == best_cost and weight < best_weight)):
                return weight, cost, prefix
            else:
                return best_weight, best_cost, best_used

        best_weight, best_cost, best_used = cls._get_best_packaging(
            max_weight, things, best_weight,
            best_cost, best_used, prefix + [False])

        best_weight, best_cost, best_used = cls._get_best_packaging(
            max_weight, things, best_weight,
            best_cost, best_used, prefix + [True])

        return best_weight, best_cost, best_used


def main():

    packages_data = open(sys.argv[1], 'r')

    for package_data in packages_data:
        max_package_weight = package_data.split(':')[0].strip()
        raw_things = package_data.split(':')[1].strip().split(' ')

        package = Package(raw_things, MAX_WEIGHT=max_package_weight)
        print package.get_things()

if __name__ == '__main__':
    main()
