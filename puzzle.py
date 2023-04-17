from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave))),
    And(Or(AKnave, AKnight), Not(And(AKnave, AKnight)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave))),
    And(Or(AKnave, AKnight), Not(And(AKnave, AKnight))),
    And(Or(BKnave, BKnight), Not(And(BKnave, BKnight)))

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight)))),
    And(Or(AKnave, AKnight), Not(And(AKnave, AKnight))),
    And(Or(BKnave, BKnight), Not(And(BKnave, BKnight)))


    # TODO
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    And(Or(AKnave, AKnight), Not(And(AKnave, AKnight))),
    And(Or(BKnave, BKnight), Not(And(BKnave, BKnight))),
    And(Or(CKnave, CKnight), Not(And(CKnave, CKnight))),

    # If a is a knight, then a is a knave or a is a knight
    Implication(AKnight, Or(AKnight, AKnave)),
    # If a is a knave, then a is not a knave and a knight
    Implication(AKnave, Not(Or(AKnight, AKnave))),



    # If b is a night, then c is a knave
    Implication(BKnight, CKnave),
    # If b is a knave, then c is a knight
    Implication(BKnave, CKnight),

    #If b is a knight, then A says I am a knave
    Implication(BKnight, And(
      Implication(AKnight, AKnave),
      Implication(AKnave, Not(AKnave)))),

    #If b is a knave, then A says I am a knight
    Implication(BKnave, And(
        Implication(AKnight, AKnight),
        Implication(AKnave, Not(AKnight)))),

    
    #If c is a knight, then A is a night
    Implication(CKnight, AKnight),
    #if c is a knave, then a is not a knight
    Implication(CKnave, Not(AKnight))
    



)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
