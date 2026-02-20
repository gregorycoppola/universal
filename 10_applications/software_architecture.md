# Software Architecture as Logic

## The Claim

A software architecture diagram — boxes and arrows showing components,
dependencies, and data flow — is a factor graph. The boxes are entities.
The arrows are Horn clauses. The question "what breaks if this service
goes down?" is backward inference via lambda messages.

The QBBN can represent, type-check, and verify software architectures
using the same machinery it uses for natural language reasoning.

## Components as Entities

Every service, module, database, and API endpoint is an entity with a type:

    entity auth_service : service
    entity postgres : database
    entity user_api : endpoint
    entity cache : service

## Capabilities as Predicates

What each component does is a predicate:

    predicate handles_auth {service: e}
    predicate stores_data {service: e, schema: e}
    predicate rate_limits {service: e}

Ground facts declare the current state:

    handles_auth(service: auth_service)
    stores_data(service: postgres, schema: user_schema)

## Dependencies as Rules

Architectural dependencies are Horn clauses:

    always [r:e]:
      incoming_request(request: r)
      & handles_auth(service: auth_service)
      & rate_limits(service: gateway)
      -> authenticated_request(request: r)

    always [r:e]:
      authenticated_request(request: r)
      & stores_data(service: postgres, schema: user_schema)
      -> can_serve_user_data(request: r)

## Failure Analysis as Backward Inference

"What happens if the database goes down?" is:

    not stores_data(service: postgres, schema: user_schema)

The NEG factor propagates backward: if postgres can't store data,
then can_serve_user_data becomes false for all requests. This is
modus tollens applied to architecture — the same inference rule
that derives "Zeus is not a man" from "Zeus is not mortal."

## Soft Dependencies

Not all dependencies are hard. The cache improves performance but
isn't required:

    usually [r:e]:
      authenticated_request(request: r)
      & caches_data(service: cache)
      -> fast_response(request: r)

    always [r:e]:
      authenticated_request(request: r)
      -> eventual_response(request: r)

The modal quantifier — usually vs always — captures exactly the
architectural distinction between "nice to have" and "required."