---
layout: page
title: Capacity-Aware Scheduler
description: Planning around cognitive load instead of hiding it
stage: Independent
status: mar 2025 – Present
importance: 2
category: assistive software
---

*Independent · mar 2025 – Present*

A standard calendar leaves three costs to the user. They must break large tasks into steps they can start, which is itself executive-function work. They can’t see cognitive load, so several hours of demanding deep work look the same as several hours of light tasks, and work goes undone once energy runs out. And calendars place tasks back to back, leaving no time to reset or travel between them. For autistic and other neurodivergent people, who often carry extra load from masking, these costs build up into burnout.

I’m building a scheduler that runs locally and treats each day as having a limited cognitive budget. It warns when a day’s plan reaches full capacity rather than packing in more. It adds buffers between tasks for reset and transit, and it schedules a mandatory rest day each week, so work stays sustainable over weeks, not just within a day. It also groups similar tasks to reduce the cost of switching between them (Monsell, 2003).

Next, I’m modeling energy as a latent variable: how it rises and falls across the day, and which events drain more than they appear to, in the spirit of spoon theory (Miserandino, 2003). The goal is a scheduler that learns each person’s patterns instead of assuming a typical day.
