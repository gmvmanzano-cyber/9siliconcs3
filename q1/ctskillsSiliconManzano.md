# Computational Thinking Exercise
## [Smart School Canteen Queue]
**Name:** Gabriel Matthew V. Manzano
**Section:** 9-Silicon
**Last Name:** Manzano
**Date:** August 20, 2026
---

## Step 1: Identify the Big Problem
### Main Problem
The problem is that the serving system of the canteen takes too long, causing crowding.
---
## Step 2: Identify the Sub-Problems
1. Students have no time to decide what to order.
2. The purchase recording system is manual and inefficient.
3. No system for supply management.
4. The canteen is small and has little space to line up.
---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| Students have no time to decide what to order. | Pattern Recognition: Are there specific meals or combinations that are ordered most frequently? How could identifying these trends speed up the decision making process? | Identify the most frequently bought items and group them into “combos” to minimize the choices students need to evaluate. |
| The purchase recording system is manual and inefficient. | Algorithm Design: What is the step-by-step logical process a digital system would follow to process an order, calculate totals and change, and confirm the transaction? | Create a step-by-step automated checkout process: Scan item barcode, deduct exact amount from cash/online cash system. |
| No system for supply management. | Decomposition: What specific data elements need to be tracked to monitor inventory accurately? | Break down the inventory database into manageable categories and automatically subtract one unit in their respective categories each time an item is purchased. |
| The canteen is small and has little space to line up. | Pattern Recognition: Analyze average foot traffic to identify peak entry times and specific place where bottlenecks occur. (e.g., Water dispenser). | Make designated line paths in high capacity areas to maximize line capacity while also giving way for people to walk. |
---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
Write the sub-problem you selected.
### Pseudocode
START
    frequent _items = FIND_MOST_POPULAR_ITEMS()
    CREATE “Combo A” USING frequent_items(Top 1 and 2)
    CREATE “Combo B” USING frequent_items(Top 3 and 4)
    DISPLAY “Combo A and B” AT MENU BOARD
END
