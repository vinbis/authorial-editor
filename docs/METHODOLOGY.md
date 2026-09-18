# Methodology

## Source basis

Authorial Editor is inspired by **StoryScope: Investigating idiosyncrasies in AI fiction** (Russell et al., COLM 2026).

StoryScope studies fiction and extracts interpretable discourse-level narrative features. Its central methodological contribution for this project is not a list of forbidden words. It is the use of structured intermediate representations and feature-level analysis to reason about construction rather than only surface prose.

## What transfers

Authorial Editor adopts four high-level ideas:

1. **Separate structure from surface.**
2. **Use interpretable dimensions instead of one opaque quality score.**
3. **Analyse dimensions in explicit stages.**
4. **Treat surface cleanup as downstream of structural analysis.**

## What does not transfer directly

StoryScope evaluates long-form fiction. Authorial Editor targets articles, essays, analysis, newsletters, and other non-fiction/editorial material.

Therefore the following would be invalid:

- applying StoryScope's reported classification F1 to blog posts;
- describing an editorial feature score as a probability of AI authorship;
- assuming that every fiction-associated human feature improves non-fiction;
- adding nonlinear time structure, ambiguity, direct reader address, or references when the source material does not justify them.

## Editorial adaptation

The initial taxonomy maps selected StoryScope concepts to editorial questions.

Examples:

| StoryScope concept | Editorial adaptation |
| --- | --- |
| Thematic explicitness | Is the thesis explained more often than necessary? |
| Causal-chain continuity | Is the argument artificially single-track? |
| Intertextual strategy | Are supported references concrete and named? |
| Chronological discontinuity | Does the article use time flexibly when source material warrants it? |
| Moral polarity / ambiguity | Does the draft preserve genuine uncertainty? |
| Subplot integration | Are relevant side-arguments and counterarguments allowed to exist? |

See `taxonomy/editorial-core.yaml` for the complete experimental mapping.

## Source Lock

Before rewriting, the engine creates a structured representation of:

- thesis;
- factual assertions;
- opinions;
- experiences;
- inferences;
- named entities;
- numbers;
- links;
- quotations;
- uncertainty;
- material that must not be invented.

This object is a constraint for later stages, not an excuse to "improve" the factual content.

## Discourse Audit

The discourse audit scores each experimental feature from 1 to 5 and must include evidence from the supplied text for flags.

Scores are descriptive. They are not "humanity scores".

## Rewrite

The rewrite happens in two passes.

### Structural pass

May:

- reorder existing arguments;
- remove redundant thesis restatement;
- preserve meaningful uncertainty;
- strengthen supported counterarguments;
- move evidence closer to the claim it supports;
- improve transitions without erasing asymmetry.

Must not:

- add facts;
- invent an anecdote;
- create a source;
- create a quote;
- claim the author personally experienced something that is absent from the input;
- deliberately insert mistakes or randomness.

### Surface pass

Improves rhythm, redundancy, formulaic transitions, repeated constructions, and unnecessary summary language without undoing the structural plan.

## Integrity validation

The final text is compared to the locked source representation.

The validator reports:

- invented claims;
- lost claims;
- distorted claims;
- changed sources;
- overall meaning preservation.

The alpha release does not claim perfect factual verification. It checks consistency between source and revision. External fact verification is a separate problem.

## Future: author-specific feature discovery

The planned v0.3 methodology is:

```text
verified author corpus
        vs
AI mirror corpus on matched briefs
        ↓
structured comparison
        ↓
candidate author-specific features
        ↓
stability + human review
```

This is intentionally different from asking a model to describe an author's "tone" from a handful of samples.
