# Smell baseline

Twelve heuristics from Fowler's _Refactoring_, ch. 3, via `code-review`. Each reads *what it is* →
*how to fix*. Match each against the diff.

A documented repo standard overrides this list. Every smell here is a judgement call, labelled as one,
and anything tooling already enforces stays out of the report.

- **Mysterious Name** — a name that hides what it does or holds. → rename it; no honest name means the
  design is murky.
- **Duplicated Code** — the same logic shape in two hunks or files. → extract it, call it from both.
- **Feature Envy** — a method reaching into another object's data more than its own. → move it onto the
  data it envies.
- **Data Clumps** — the same few fields or params travelling together. → bundle them into one type.
- **Primitive Obsession** — a primitive standing in for a domain concept. → give the concept a small
  type.
- **Repeated Switches** — the same switch on the same type, recurring. → polymorphism, or one shared
  map.
- **Shotgun Surgery** — one logical change forcing scattered edits. → gather what changes together.
- **Divergent Change** — one file edited for several unrelated reasons. → split it by reason.
- **Speculative Generality** — hooks for needs the spec never had. → delete, inline until one shows.
- **Message Chains** — `a.b().c().d()` navigation the caller should not depend on. → hide the walk.
- **Middle Man** — a layer that mostly delegates onward. → cut it, call the target.
- **Refused Bequest** — a subclass ignoring most of what it inherits. → composition.
