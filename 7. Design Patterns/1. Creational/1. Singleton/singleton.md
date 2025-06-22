Ex: Three components lead to three network comm. instances to one server
singleton means single instance of network comm.

Only one instance

Single point of access for a resource

Uses

1. Network manager
2. Database access
3. Logging
4. Utility class(es)

Disadvantages:

1. Breaks single responsibility (manage its own state and allow
other to create their own instances)
2. Testability issues
3. State for life