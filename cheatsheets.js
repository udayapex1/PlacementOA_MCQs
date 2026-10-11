const snippet = (language, title, code) => ({ language, title, code });

export const CHEATSHEETS = [
  {
    id: 'oops',
    name: 'OOPs',
    subtitle: 'Design clean objects and explain the four pillars with confidence.',
    accent: '#56a8ff',
    sections: [
      {
        title: 'The four pillars',
        items: [
          { term: 'Encapsulation', detail: 'Bundle state and behavior together; control state access through methods or properties.' },
          { term: 'Abstraction', detail: 'Expose what an object does and hide how it does it. Interfaces and abstract classes are common tools.' },
          { term: 'Inheritance', detail: 'Reuse or extend behavior through an is-a relationship. Prefer composition when inheritance is not a true subtype.' },
          { term: 'Polymorphism', detail: 'One interface, many implementations. Overloading is compile-time; overriding and virtual dispatch are runtime.' },
        ],
      },
      {
        title: 'Interview comparisons',
        items: [
          { term: 'Class vs object', detail: 'A class is a blueprint or type; an object is a runtime instance with identity and state.' },
          { term: 'Interface vs abstract class', detail: 'An interface defines a contract; an abstract class can share state and partial implementation.' },
          { term: 'Composition vs inheritance', detail: 'Composition models has-a and allows behavior to be swapped; inheritance models is-a and couples types.' },
          { term: 'Shallow vs deep copy', detail: 'Shallow copy shares referenced objects; deep copy recursively duplicates owned mutable state.' },
          { term: 'Overloading vs overriding', detail: 'Overloading changes the parameter list in one scope; overriding replaces an inherited implementation with the same contract.' },
          { term: 'SOLID', detail: 'Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion.' },
        ],
      },
      {
        title: 'High-value keywords',
        items: [
          { term: 'C++', detail: 'virtual enables dynamic dispatch; override documents an override; const protects a value; RAII ties cleanup to object lifetime.' },
          { term: 'Java', detail: 'extends creates class inheritance; implements fulfills an interface; final prevents change or extension; this and super select current or parent members.' },
          { term: 'Python', detail: 'self refers to the instance; __init__ initializes it; @property exposes controlled attributes; duck typing focuses on supported behavior.' },
          { term: 'Dependency inversion', detail: 'High-level policy should depend on abstractions, not concrete low-level details. Inject dependencies at the boundary.' },
        ],
      },
      {
        title: 'Code patterns',
        snippets: [
          snippet('C++', 'Runtime polymorphism', String.raw`#include <iostream>

struct Shape {
    virtual double area() const = 0;
    virtual ~Shape() = default;
};

struct Circle : Shape {
    double radius;
    explicit Circle(double r) : radius(r) {}
    double area() const override { return 3.14159 * radius * radius; }
};

void printArea(const Shape& shape) {
    std::cout << shape.area(); // dynamic dispatch
}`),
          snippet('Java', 'Interface + implementation', String.raw`interface Payment {
    void pay(double amount);
}

final class CardPayment implements Payment {
    @Override
    public void pay(double amount) {
        System.out.println("Paid: " + amount);
    }
}

Payment payment = new CardPayment();
payment.pay(499.0);`),
          snippet('Python', 'Encapsulation with property', String.raw`class Account:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount`),
        ],
      },
    ],
  },
  {
    id: 'os',
    name: 'Operating Systems',
    subtitle: 'Keep processes, memory, scheduling, and synchronization straight in interviews.',
    accent: '#ffc45c',
    sections: [
      {
        title: 'Processes and threads',
        items: [
          { term: 'Process', detail: 'An executing program with its own virtual address space, resources, and process control block (PCB).' },
          { term: 'Thread', detail: 'The smallest execution unit. Threads in one process share code, data, and open files but have their own stack and registers.' },
          { term: 'Context switch', detail: 'The OS saves the current execution state and loads another process or thread. It adds overhead without doing user work.' },
          { term: 'System call', detail: 'A controlled entry from user mode to kernel mode for services such as read, write, fork, and exec.' },
          { term: 'IPC', detail: 'Inter-process communication includes pipes, shared memory, message queues, sockets, and signals.' },
        ],
      },
      {
        title: 'CPU scheduling',
        items: [
          { term: 'FCFS', detail: 'First Come First Served: simple and non-preemptive, but can create the convoy effect.' },
          { term: 'SJF / SRTF', detail: 'Shortest Job First minimizes average waiting time when burst lengths are known; SRTF is its preemptive form.' },
          { term: 'Round Robin', detail: 'Each ready process receives a time quantum. A small quantum improves response but increases context switches.' },
          { term: 'Priority scheduling', detail: 'Runs the highest-priority work first. Aging gradually raises waiting processes to reduce starvation.' },
          { term: 'Key formulas', detail: 'Turnaround = completion − arrival. Waiting = turnaround − burst. Response = first run − arrival.' },
        ],
      },
      {
        title: 'Memory management',
        items: [
          { term: 'Virtual memory', detail: 'Gives each process a large logical address space backed by RAM and disk, allowing isolation and overcommit.' },
          { term: 'Paging', detail: 'Splits virtual memory into fixed-size pages and physical memory into frames. A page table maps pages to frames.' },
          { term: 'TLB', detail: 'A fast cache of recent page-table translations. A TLB hit avoids an extra page-table memory lookup.' },
          { term: 'Page fault', detail: 'Occurs when a referenced page is not in RAM. The OS loads it from storage and may evict another page.' },
          { term: 'Thrashing', detail: 'Excessive page faults leave the system spending more time swapping than executing. Reduce multiprogramming or add memory.' },
          { term: 'Fragmentation', detail: 'Internal fragmentation wastes space inside allocated blocks; external fragmentation leaves unusable gaps between blocks.' },
        ],
      },
      {
        title: 'Synchronization and deadlocks',
        items: [
          { term: 'Critical section', detail: 'Code that accesses shared state and must not be executed by conflicting threads at the same time.' },
          { term: 'Mutex vs semaphore', detail: 'A mutex provides ownership-based mutual exclusion; a counting semaphore controls access to a number of permits.' },
          { term: 'Race condition', detail: 'The result depends on timing because concurrent operations access shared data without adequate synchronization.' },
          { term: 'Deadlock conditions', detail: 'Mutual exclusion, hold and wait, no preemption, and circular wait must all hold for deadlock.' },
          { term: 'Deadlock handling', detail: 'Prevent a condition, avoid unsafe states, detect and recover, or accept the risk depending on the system.' },
        ],
      },
      {
        title: 'Concurrency snippets',
        snippets: [
          snippet('C++', 'Mutex protects shared state', String.raw`#include <mutex>

std::mutex m;
int counter = 0;

void increment() {
    std::lock_guard<std::mutex> lock(m);
    ++counter; // critical section
}`),
          snippet('Java', 'Thread-safe counter', String.raw`final class Counter {
    private int value;

    public synchronized void increment() {
        value++;
    }

    public synchronized int get() {
        return value;
    }
}`),
          snippet('Python', 'Lock around shared data', String.raw`from threading import Lock

lock = Lock()
counter = 0

def increment():
    global counter
    with lock:
        counter += 1`),
        ],
      },
    ],
  },
  {
    id: 'dbms',
    name: 'DBMS',
    subtitle: 'Revise keys, normalization, transactions, indexing, and database design fast.',
    accent: '#51d6a4',
    sections: [
      {
        title: 'Database foundations',
        items: [
          { term: 'DBMS', detail: 'Software that defines, stores, queries, secures, and manages data while providing concurrency and recovery.' },
          { term: 'Schema', detail: 'The logical structure of a database: tables, columns, constraints, views, indexes, and relationships.' },
          { term: 'Instance', detail: 'The actual data stored in the database at a particular moment.' },
          { term: 'Data independence', detail: 'The ability to change storage or logical structure with minimal impact on applications.' },
          { term: 'Relational model', detail: 'Represents data as relations (tables) connected through keys and constrained by integrity rules.' },
        ],
      },
      {
        title: 'Keys and constraints',
        items: [
          { term: 'Primary key', detail: 'Chosen candidate key; uniquely identifies each row and cannot be NULL.' },
          { term: 'Candidate key', detail: 'A minimal set of attributes that uniquely identifies a row. One is selected as the primary key.' },
          { term: 'Foreign key', detail: 'A column or column set that references a key in another or the same table.' },
          { term: 'Composite key', detail: 'A key formed from multiple columns, useful when no single column is unique.' },
          { term: 'Integrity rules', detail: 'Entity integrity protects primary keys; referential integrity protects valid relationships; domain rules validate values.' },
        ],
      },
      {
        title: 'Normalization',
        items: [
          { term: '1NF', detail: 'Atomic values, no repeating groups, and one value per cell.' },
          { term: '2NF', detail: '1NF plus no partial dependency of a non-key attribute on part of a composite key.' },
          { term: '3NF', detail: '2NF plus no transitive dependency of a non-key attribute on another non-key attribute.' },
          { term: 'BCNF', detail: 'Every determinant in a non-trivial functional dependency is a candidate key.' },
          { term: 'Denormalization', detail: 'Intentionally duplicates data to reduce joins or improve reads, trading storage and write complexity for speed.' },
          { term: 'Anomalies', detail: 'Insert, update, and delete anomalies are symptoms of poorly organized redundancy.' },
        ],
      },
      {
        title: 'Transactions and indexing',
        items: [
          { term: 'ACID', detail: 'Atomicity (all or nothing), Consistency (valid state), Isolation (controlled concurrency), Durability (committed data persists).' },
          { term: 'Serializability', detail: 'A concurrent schedule is serializable when it has the same effect as some serial order of transactions.' },
          { term: 'Index', detail: 'An alternate access path that speeds suitable reads but consumes space and adds write-maintenance cost.' },
          { term: 'Clustered index', detail: 'Associates table storage with an index order where supported; a table generally has at most one clustered ordering.' },
          { term: 'Deadlock', detail: 'Transactions wait in a cycle. Systems detect, prevent, avoid, or time out and abort one participant.' },
        ],
      },
      {
        title: 'Application access patterns',
        snippets: [
          snippet('Python', 'Parameterized SQLite query', String.raw`import sqlite3

with sqlite3.connect("app.db") as db:
    rows = db.execute(
        "SELECT id, name FROM users WHERE email = ?",
        (email,),
    ).fetchall()`),
          snippet('Java', 'Prepared statement', String.raw`String sql = "SELECT id, name FROM users WHERE email = ?";
try (PreparedStatement ps = connection.prepareStatement(sql)) {
    ps.setString(1, email);
    try (ResultSet rs = ps.executeQuery()) {
        while (rs.next()) {
            System.out.println(rs.getString("name"));
        }
    }
}`),
        ],
      },
    ],
  },
  {
    id: 'sql',
    name: 'SQL',
    subtitle: 'Keep the query patterns, joins, aggregates, windows, and performance rules close at hand.',
    accent: '#c88cff',
    sections: [
      {
        title: 'Query skeleton',
        snippets: [
          snippet('SQL', 'Readable SELECT order', String.raw`SELECT
    department_id,
    COUNT(*) AS employee_count,
    AVG(salary) AS average_salary
FROM employees
WHERE status = 'active'
GROUP BY department_id
HAVING COUNT(*) >= 5
ORDER BY average_salary DESC;`),
        ],
        items: [
          { term: 'Logical order', detail: 'FROM / JOIN → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT or FETCH.' },
          { term: 'Aliases', detail: 'Use short table aliases for joins and clear column aliases for calculated output.' },
          { term: 'NULL', detail: 'NULL is unknown or missing. Use IS NULL, IS NOT NULL, COALESCE, and NULL-safe comparisons where supported.' },
        ],
      },
      {
        title: 'Joins and set operations',
        snippets: [
          snippet('SQL', 'Common join patterns', String.raw`-- Matching rows only
SELECT o.id, c.name
FROM orders AS o
JOIN customers AS c ON c.id = o.customer_id;

-- Keep customers with no orders too
SELECT c.name, o.id
FROM customers AS c
LEFT JOIN orders AS o ON o.customer_id = c.id;`),
        ],
        items: [
          { term: 'INNER JOIN', detail: 'Returns only matching rows from both inputs.' },
          { term: 'LEFT JOIN', detail: 'Keeps every left row; unmatched right columns become NULL.' },
          { term: 'FULL OUTER JOIN', detail: 'Keeps matches and unmatched rows from both inputs where supported.' },
          { term: 'CROSS JOIN', detail: 'Cartesian product. Use deliberately; a missing join condition can create the same explosion.' },
          { term: 'UNION vs UNION ALL', detail: 'UNION removes duplicate result rows; UNION ALL preserves them and is usually cheaper.' },
        ],
      },
      {
        title: 'Aggregates, subqueries, and CTEs',
        snippets: [
          snippet('SQL', 'Top-N per group', String.raw`WITH ranked AS (
    SELECT
        employee_id,
        department_id,
        salary,
        ROW_NUMBER() OVER (
            PARTITION BY department_id
            ORDER BY salary DESC
        ) AS position
    FROM employees
)
SELECT *
FROM ranked
WHERE position <= 3;`),
        ],
        items: [
          { term: 'COUNT(*)', detail: 'Counts rows. COUNT(column) ignores NULL; COUNT(DISTINCT column) counts unique non-NULL values.' },
          { term: 'WHERE vs HAVING', detail: 'WHERE filters rows before grouping; HAVING filters groups after aggregation.' },
          { term: 'EXISTS', detail: 'Tests whether a correlated subquery returns at least one row; useful for semi-joins.' },
          { term: 'WITH', detail: 'Defines a CTE for readable, reusable query steps. Recursive CTEs traverse hierarchies.' },
          { term: 'Window functions', detail: 'Calculate across related rows without collapsing them. Use OVER, PARTITION BY, and ORDER BY.' },
        ],
      },
      {
        title: 'DDL, DML, and transactions',
        snippets: [
          snippet('SQL', 'Safe transaction pattern', String.raw`BEGIN;

UPDATE accounts
SET balance = balance - 500
WHERE id = 1 AND balance >= 500;

UPDATE accounts
SET balance = balance + 500
WHERE id = 2;

-- COMMIT only after checking both statements
COMMIT;`),
        ],
        items: [
          { term: 'DDL', detail: 'CREATE, ALTER, and DROP define or change database objects. TRUNCATE removes all rows in supported systems.' },
          { term: 'DML', detail: 'SELECT, INSERT, UPDATE, and DELETE query or change row data.' },
          { term: 'DCL / TCL', detail: 'GRANT and REVOKE manage privileges; COMMIT, ROLLBACK, and SAVEPOINT manage transactions.' },
          { term: 'Constraints', detail: 'PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, CHECK, and DEFAULT protect data quality.' },
          { term: 'Upsert', detail: 'Insert-or-update behavior using MERGE or dialect-specific conflict handling.' },
        ],
      },
      {
        title: 'Performance and safety',
        items: [
          { term: 'EXPLAIN', detail: 'Inspect the query plan: scans, joins, estimates, indexes, and sort or aggregate steps.' },
          { term: 'Sargable predicates', detail: 'Keep indexed columns searchable; avoid wrapping them in functions when a range rewrite is possible.' },
          { term: 'Composite indexes', detail: 'Column order matters. A B-tree on (a, b) commonly helps predicates starting with a.' },
          { term: 'SQL injection', detail: 'Never concatenate untrusted input into SQL. Use parameterized queries or prepared statements.' },
          { term: 'Pagination', detail: 'Large OFFSET values can be slow; keyset pagination uses the last seen ordered key as a cursor.' },
        ],
      },
    ],
  },
];
