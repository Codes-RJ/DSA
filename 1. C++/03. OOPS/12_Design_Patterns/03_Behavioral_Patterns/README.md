# Behavioral Design Patterns

Behavioral patterns organize how objects communicate and how responsibilities move between them. Study them after interfaces, composition, ownership, and callable objects.

## Pattern Index

| Pattern | Use it when | Main caution |
|---|---|---|
| [Command](Command.md) | A request must be queued, logged, composed, or undone | Command classes can add ceremony to simple calls |
| [Observer](Observer.md) | Multiple subscribers react to a change | Define subscription ownership, removal, ordering, and reentrancy |
| [State](State.md) | Behavior changes with an explicit state machine | Make allowed transitions visible and test them |
| [Strategy](Strategy.md) | An algorithm must be replaceable independently of its client | A function or lambda may be simpler than a class hierarchy |
| [Visitor](Visitor.md) | Operations vary while a closed type family stays stable | Adding a new visited type affects every visitor |

## Selection Rule

Start with a direct function, lambda, or small composed object. Introduce a named pattern only when it clarifies a recurring source of change. Document ownership and lifetime for every participant, and test exceptional or reentrant behavior where callbacks are involved.

## Next Step

Return to the parent [Design Patterns](../README.md) index.
