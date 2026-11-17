---
layout: page
title: Pragmatic Linter
description: From flagging “missed” meaning to locating where meaning diverges
stage: Independent
status: Mar–oct 2025
importance: 1
category: assistive software
---

*Independent · Mar–oct 2025*

I set out to build a tool that would work like a code linter for conversation, flagging information autistic listeners might miss. I built the first components: an interface for logging what was said alongside how it was understood, a database of these heard-versus-understood pairs, and a user profile that an LLM agent, given background on autistic communication, could draw on to predict future misunderstandings.

To design the decoding step, I audited Introduction to Linguistics at NYU Shanghai and brought my plans to Prof. Linmin Zhang. I imagined a “semantic tree” that would map ambiguity and hidden intention the way a syntax tree maps sentence structure. Her response changed the project: in communication, patience matters more than perfect or exhaustive decoding of meaning.

Ambiguity is a feature of language, not a flaw, because it makes communication efficient when speakers share context (Piantadosi, Tily & Gibson, 2012). When context isn’t shared, the misunderstanding belongs to the exchange, not to one speaker’s “poorer” comprehension (Milton, 2012). A tool that decodes only one side places the whole burden of repair on that side. I reframed divergence as a point for open communication between both speakers, and that shift shapes my current work on whether LLM text “adapted” for autistic readers preserves meaning or only looks simpler.
