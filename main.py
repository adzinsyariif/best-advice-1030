# Judge criteria (from competition.yaml, most important first):
# 1. Single sentence about the best advice the writer ever received
# 2. Worth carrying: specific, earned, true beyond the moment
# 3. Real voice recalling a real moment, not a slogan / fortune cookie
# 4. Tight: every word earns its place, reads in one breath
# 5. Lands: leaves the reader something to keep after the last word
#
# --- Four candidate lines of my own, scored 1-5 per criterion ---
#
# A: "My dad, fixing our sink with a butter knife, said never force a stuck thing — wiggle it, wait, and it will tell you how it wants to move."
#    scores: c1=5 (clearly advice received), c2=4 (earned, generalises),
#            c3=5 (butter knife detail feels lived), c4=3 (a little long),
#            c5=4 (nice closing image)  -> total 21
#
# B: "When I wanted to quit, my coach said: don't decide on a bad day, because tired you is a liar and rested you has to live with it."
#    scores: c1=5, c2=5 (very carry-able rule), c3=4 (real but coach
#            voice is a touch generic), c4=4, c5=5 (strong last clause)
#            -> total 23
#
# C: "My grandmother told me while shelling peas: feed people before you ask them for anything, including forgiveness."
#    scores: c1=5, c2=5 (specific act, true far beyond the kitchen),
#            c3=5 (shelling peas = a real moment, not a slogan),
#            c4=5 (tight, one breath), c5=5 (forgiveness twist lands)
#            -> total 25  *** WINNER ***
#
# D: "An old nurse told me: if you don't know what to say to someone grieving, just make tea and sit there — silence with company beats perfect words alone."
#    scores: c1=5, c2=4, c3=4 (kind, but edges toward greeting-card),
#            c4=3 (two clauses compete), c5=4  -> total 20
#
# Winner: C. It is the only one that is simultaneously a concrete
# remembered scene, a rule I actually use, and short enough to keep.
#
# Revision 1: put the scene first ("Shelling peas beside me") so the
# line opens inside the moment instead of reporting it; cut
# "told me while" and swap "including" for the shorter, sharper
# "even" so the forgiveness beat hits harder. Still one sentence.

import os

LINE = "Shelling peas beside me, my grandmother said: feed people before you ask them for anything, even forgiveness."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
