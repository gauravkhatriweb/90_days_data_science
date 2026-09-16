"""
Day 84 — Consolidation + the endgame decision
==============================================
Eight retrieval tasks, closed book, 3 minutes each. 0 / 0.5 / 1.
Then the last point at which scope can change.
"""

# 1 (D78) -- why does a single tree overfit? why does a forest fix it?
S1 = None
# 2 (D78) -- two reasons to distrust .feature_importances_
S2 = None
# 3 (D79) -- why does Pipeline make preprocessing leakage impossible?
S3 = None
# 4 (D79) -- which models need scaling, and WHY those?
S4 = None
# 5 (D80) -- the three baselines; which is the honest comparison?
S5 = None
# 6 (D82) -- why is the test set touched ONCE?
S6 = None
# 7 (D83) -- a TRUE interpretation sentence, and the FALSE one people say:
#   TRUE :
#   FALSE:
S7 = None
# 8 (D83) -- four limitation categories:
S8 = None


# =============================================================================
# THE ENDGAME. Six days left. Last chance to change scope.
# =============================================================================
#   PRIORITY ORDER IF SOMETHING GIVES:
#     1. Day 88 portfolio     -- three unreadable repos are three that don't count
#     2. Day 85 ship P3       -- unshipped is not a portfolio piece
#     3. Day 90 final review  -- makes the next 90 days informed, not enthusiastic
#     4. Day 89 interviews    -- can move to January
#     5. Day 87 dashboard     -- nice, not essential
#     6. Day 86 k-means/PCA   -- CUT FIRST. No downstream dependency.
#
#   WHAT I AM CUTTING:
#   WHERE THE TIME GOES INSTEAD:
#
#   IS PROJECT 3 GENUINELY READY TO SHIP TOMORROW?  yes / no
#   IF NO, WHAT IS MISSING:


# =============================================================================
# PORTFOLIO PREVIEW -- open each repo as a STRANGER. 90 seconds each.
# =============================================================================
#   Project 1 -- the worst thing a reviewer would see:
#   Project 2 -- the worst thing a reviewer would see:
#   Project 3 -- the worst thing a reviewer would see:
#
#   That list IS Day 88's work.


if __name__ == "__main__":
    scores = [S1, S2, S3, S4, S5, S6, S7, S8]
    done = [s for s in scores if s is not None]
    if done:
        print(f"Score: {sum(done)} / 8")
        print(f"Weak: {[i+1 for i, s in enumerate(scores) if s is not None and s < 1]}")
