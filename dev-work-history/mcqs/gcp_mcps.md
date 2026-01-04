# Google Cloud Platform (GCP) Interview Questions - Complete Edition

## **GCP QUESTIONS** (74 Unique Questions)

---

### **📌 GCP FUNDAMENTALS & IAM** (7 Questions)

#### **Question 1**
What is the hierarchy of resources in Google Cloud Platform?

*   A) Projects → Folders → Organization
*   B) Organization → Folders → Projects → Resources
*   C) Resources → Projects → Organization
*   D) Folders → Organization → Projects

**Answer: B**
> **Explanation:** GCP resource hierarchy is: Organization (root) → Folders (grouping) → Projects (container for resources) → Resources (VMs, databases, etc.). IAM policies are inherited downward.

---

#### **Question 2**
What is a GCP Project and why is it important?

*   A) It's optional for organizing resources
*   B) It's the base-level organizing entity that contains all GCP resources, enables billing, and controls access
*   C) It's only used for billing purposes
*   D) It's the same as a Folder

**Answer: B**
> **Explanation:** A Project is the fundamental organizational unit in GCP. All resources belong to a project, billing is enabled per project, and IAM policies can be applied at the project level.

---

#### **Question 3**
What is the purpose of GCP Service Accounts?

*   A) To manage billing
*   B) To provide an identity for applications or VMs to authenticate and authorize API calls
*   C) To send emails to users
*   D) To create user accounts

**Answer: B**
> **Explanation:** Service accounts are special accounts used by applications, VMs, or services to authenticate to GCP APIs and other services, not representing human users.

---

#### **Question 4**
What is IAM in Google Cloud Platform?

*   A) Internet Access Management
*   B) Identity and Access Management - controls who can do what on which resources
*   C) Internal Application Monitoring
*   D) Instance Availability Manager

**Answer: B**
> **Explanation:** IAM (Identity and Access Management) lets you manage access control by defining who (identity) has what access (role) for which resource.

---

#### **Question 5**
What is the principle of least privilege in GCP IAM?

*   A) Give all users admin access
*   B) Grant users only the permissions they need to perform their tasks, no more
*   C) Use only service accounts
*   D) Disable all access by default permanently

**Answer: B**
> **Explanation:** The principle of least privilege means giving users the minimum permissions necessary to complete their work, reducing security risks.

---

#### **Question 6**
What are the three types of IAM roles in GCP?

*   A) Read, Write, Delete
*   B) Basic (Primitive), Predefined, and Custom roles
*   C) Owner, Editor, Viewer only
*   D) Admin, User, Guest

**Answer: B**
> **Explanation:** GCP has:
> - **Basic roles**: Owner, Editor, Viewer (broad permissions)
> - **Predefined roles**: Granular, service-specific roles managed by Google
> - **Custom roles**: User-defined combinations of permissions

---

#### **Question 7**
What is the difference between gcloud, gsutil, and bq command-line tools?

*   A) They are all the same tool
*   B) gcloud manages GCP resources, gsutil manages Cloud Storage, bq manages BigQuery
*   C) gsutil is deprecated
*   D) bq is for managing VMs

**Answer: B**
> **Explanation:** 
> - **gcloud**: Main CLI for managing GCP resources and services
> - **gsutil**: Specifically for Cloud Storage operations
> - **bq**: Specifically for BigQuery operations

---

### **📌 REGIONS, ZONES & NETWORKING BASICS** (3 Questions)

#### **Question 8**
What is a VPC (Virtual Private Cloud) in GCP?

*   A) A physical data center
*   B) A logically isolated virtual network for GCP resources with global scope
*   C) A type of virtual machine
*   D) A database service

**Answer: B**
> **Explanation:** A VPC is a virtual network that provides networking functionality for GCP resources. Unlike other clouds, GCP VPCs are global and subnets are regional.

---

#### **Question 9**
What is the difference between a Region and a Zone in GCP?

*   A) They are the same thing
*   B) A Region is a geographic area containing multiple Zones; a Zone is an isolated deployment area within a Region
*   C) A Zone is larger than a Region
*   D) Zones are only for storage

**Answer: B**
> **Explanation:** 
> - **Region**: Geographic location (e.g., us-central1)
> - **Zone**: Isolated location within a region (e.g., us-central1-a)
> - Resources like VMs are zonal; some services are regional or global

---

#### **Question 10**
What is Cloud Shell in GCP?

*   A) A mobile application
*   B) A browser-based command-line interface with pre-installed tools and persistent storage
*   C) A desktop application
*   D) A virtual machine type

**Answer: B**
> **Explanation:** Cloud Shell is an interactive shell environment accessible from the GCP Console. It comes with pre-installed SDKs, 5GB persistent home directory, and authenticated gcloud CLI.

---

### **📌 COMPUTE ENGINE** (8 Questions)

#### **Question 11**
What is a Compute Engine Instance Template?

*   A) A running VM
*   B) A resource that defines machine type, disk, and network configuration used to create VM instances or managed instance groups
*   C) A billing template
*   D) A logging configuration

**Answer: B**
> **Explanation:** Instance templates define the machine type, boot disk image, network settings, and other configuration used when creating VMs or Managed Instance Groups.

---

#### **Question 12**
What is a Managed Instance Group (MIG) in GCP?

*   A) A collection of unrelated VMs
*   B) A group of identical VM instances managed as a single entity with autoscaling, autohealing, and rolling updates
*   C) A network security group
*   D) A database cluster

**Answer: B**
> **Explanation:** MIGs contain identical VMs based on an instance template and provide features like autoscaling, autohealing, load balancing integration, and rolling updates.

---

#### **Question 13**
What is the difference between Preemptible VMs and Spot VMs in GCP?

*   A) They are identical
*   B) Both are discounted interruptible VMs; Spot VMs are the newer version with more features like no maximum runtime limit
*   C) Preemptible VMs are more expensive
*   D) Spot VMs cannot be used with MIGs

**Answer: B**
> **Explanation:** Both offer significant discounts (60-91%) but can be preempted. Spot VMs (newer) have no 24-hour maximum runtime limit and offer dynamic pricing, replacing Preemptible VMs.

---

#### **Question 14**
What is a Sole-Tenant Node in GCP?

*   A) A shared VM
*   B) A physical Compute Engine server dedicated exclusively to your workloads for compliance or licensing requirements
*   C) A network node
*   D) A type of container

**Answer: B**
> **Explanation:** Sole-tenant nodes are physical servers dedicated to hosting only your project's VMs, useful for compliance, licensing, or performance isolation requirements.

---

#### **Question 15**
How does Compute Engine autoscaling work?

*   A) It only scales manually
*   B) It automatically adds or removes VM instances based on load metrics like CPU utilization or custom metrics
*   C) It only scales storage
*   D) It requires Kubernetes

**Answer: B**
> **Explanation:** Autoscaling in MIGs adds or removes instances based on metrics (CPU, memory, load balancing, custom Cloud Monitoring metrics) and configured target utilization levels.

---

#### **Question 16**
What is the purpose of a Compute Engine Startup Script?

*   A) To authenticate users
*   B) To run commands automatically when a VM instance boots up for configuration and setup
*   C) To bill the instance
*   D) To create backups

**Answer: B**
> **Explanation:** Startup scripts are executed when a VM boots, commonly used to install software, configure settings, or register with other services during instance initialization.

---

#### **Question 17**
What are the persistent disk types available in Compute Engine?

*   A) Only HDD
*   B) Standard (HDD), Balanced (SSD), SSD, and Extreme persistent disks
*   C) Only local SSD
*   D) Only SSD

**Answer: B**
> **Explanation:** GCP offers:
> - **Standard (pd-standard)**: HDD, cost-effective
> - **Balanced (pd-balanced)**: SSD, balanced performance/cost
> - **SSD (pd-ssd)**: High performance
> - **Extreme (pd-extreme)**: Highest IOPS for demanding workloads

---

#### **Question 18**
What is Live Migration in Compute Engine?

*   A) Migrating data to another cloud
*   B) Moving a running VM to another host without interruption during maintenance events
*   C) A backup process
*   D) Moving VMs between projects

**Answer: B**
> **Explanation:** Live migration moves running VMs to different physical hosts during maintenance events without rebooting, maintaining uptime and service availability.

---

### **📌 CLOUD STORAGE** (7 Questions)

#### **Question 19**
What are the storage classes in Google Cloud Storage?

*   A) Only Standard
*   B) Standard, Nearline, Coldline, and Archive
*   C) Hot and Cold only
*   D) Premium and Standard

**Answer: B**
> **Explanation:** Cloud Storage offers:
> | Class | Access Frequency | Min Storage | Use Case |
> |-------|-----------------|-------------|----------|
> | Standard | Frequent | None | Hot data |
> | Nearline | Monthly | 30 days | Backups |
> | Coldline | Quarterly | 90 days | DR |
> | Archive | Yearly | 365 days | Compliance |

---

#### **Question 20**
What is Object Lifecycle Management in Cloud Storage?

*   A) A backup feature
*   B) Rules that automatically transition objects between storage classes or delete them based on conditions
*   C) A versioning feature
*   D) An encryption feature

**Answer: B**
> **Explanation:** Lifecycle Management applies rules to objects based on age, creation date, or other conditions to automatically change storage class, delete objects, or manage versions.

---

#### **Question 21**
What is the difference between uniform and fine-grained access control in Cloud Storage?

*   A) They are identical
*   B) Uniform uses only IAM; fine-grained uses both IAM and ACLs for per-object permissions
*   C) Fine-grained is deprecated
*   D) Uniform is only for public buckets

**Answer: B**
> **Explanation:** 
> - **Uniform access**: Uses only IAM policies at bucket level (recommended)
> - **Fine-grained**: Allows ACLs on individual objects plus IAM, providing more granular control

---

#### **Question 22**
What is a Signed URL in Cloud Storage?

*   A) A permanent URL
*   B) A time-limited URL that provides temporary access to a specific object without requiring authentication
*   C) An encrypted URL
*   D) A URL with digital signature verification

**Answer: B**
> **Explanation:** Signed URLs provide time-limited read or write access to specific Cloud Storage objects without requiring users to have GCP accounts or authentication.

---

#### **Question 23**
What is Object Versioning in Cloud Storage?

*   A) A naming convention
*   B) A feature that retains previous versions of objects when overwritten or deleted
*   C) A compression feature
*   D) Only available in Archive class

**Answer: B**
> **Explanation:** When enabled, versioning keeps historical versions of objects. Deleting an object creates a "delete marker" and previous versions can be restored.

---

#### **Question 24**
How does Cloud Storage handle data consistency?

*   A) Eventually consistent for all operations
*   B) Strong global consistency for all operations including read-after-write and list-after-write
*   C) Only consistent within regions
*   D) Requires manual synchronization

**Answer: B**
> **Explanation:** Cloud Storage provides strong global consistency. After a write completes successfully, reads will always return the latest version of the object globally.

---

#### **Question 25**
What is the maximum object size in Cloud Storage?

*   A) 1 GB
*   B) 5 TB
*   C) Unlimited
*   D) 100 GB

**Answer: B**
> **Explanation:** The maximum size for a single object in Cloud Storage is 5 TB. For objects larger than 5 GB, multipart/resumable uploads are recommended.

---

### **📌 CLOUD SQL & DATABASE SERVICES** (9 Questions)

#### **Question 26**
What database engines does Cloud SQL support?

*   A) Only MySQL
*   B) MySQL, PostgreSQL, and SQL Server
*   C) Only PostgreSQL
*   D) MongoDB and MySQL

**Answer: B**
> **Explanation:** Cloud SQL is a fully managed relational database service supporting MySQL, PostgreSQL, and SQL Server engines.

---

#### **Question 27**
What is the Cloud SQL Auth Proxy?

*   A) A load balancer
*   B) A client-side tool that provides secure, IAM-based authentication to Cloud SQL without whitelisting IPs or SSL certificates
*   C) A backup tool
*   D) A migration tool

**Answer: B**
> **Explanation:** The Cloud SQL Auth Proxy handles authentication to Cloud SQL using IAM permissions and encrypts connections, eliminating the need for IP whitelisting or managing SSL certificates.

---

#### **Question 28**
What is Cloud Spanner?

*   A) A NoSQL database
*   B) A globally distributed, horizontally scalable relational database with strong consistency
*   C) A caching service
*   D) A file storage service

**Answer: B**
> **Explanation:** Cloud Spanner is a fully managed, globally distributed relational database that provides ACID transactions, SQL support, and horizontal scaling with strong consistency.

---

#### **Question 29**
What is Firestore in GCP?

*   A) A relational database
*   B) A flexible, scalable NoSQL document database for web, mobile, and server development
*   C) A file storage service
*   D) A caching service

**Answer: B**
> **Explanation:** Firestore is a NoSQL document database that supports real-time synchronization, offline support, and automatic multi-region replication.

---

#### **Question 30**
What is the difference between Firestore Native mode and Datastore mode?

*   A) They are identical
*   B) Native mode has all features including real-time updates; Datastore mode is for existing Datastore apps with some limitations
*   C) Datastore mode is newer
*   D) Native mode is deprecated

**Answer: B**
> **Explanation:** 
> - **Firestore Native mode**: All features including real-time listeners, offline support
> - **Datastore mode**: Compatibility for existing Datastore applications, without some Native features like real-time updates

---

#### **Question 31**
What is Cloud Memorystore?

*   A) A disk storage service
*   B) A fully managed in-memory data store service supporting Redis and Memcached
*   C) A database backup service
*   D) A CDN service

**Answer: B**
> **Explanation:** Cloud Memorystore is a fully managed in-memory data store for Redis and Memcached, providing caching, session management, and real-time analytics.

---

#### **Question 32**
What is the purpose of read replicas in Cloud SQL?

*   A) To write data faster
*   B) To offload read queries from the primary instance and improve read performance
*   C) To replace backups
*   D) To manage user access

**Answer: B**
> **Explanation:** Read replicas are read-only copies of the primary instance that handle read queries, improving read performance and providing geographic distribution of read traffic.

---

#### **Question 33**
What is Cloud Bigtable?

*   A) A relational database
*   B) A fully managed, scalable NoSQL wide-column database for large analytical and operational workloads
*   C) A file storage service
*   D) A caching service

**Answer: B**
> **Explanation:** Cloud Bigtable is a petabyte-scale, fully managed NoSQL database service. It's ideal for:
> - Time-series data
> - IoT data
> - Financial data
> - Marketing data
> - Graph data
> 
> Same database that powers Google Search, Maps, and Gmail.

---

#### **Question 34**
What is AlloyDB?

*   A) A MongoDB-compatible database
*   B) A fully managed, PostgreSQL-compatible database with high performance and availability
*   C) A MySQL-only service
*   D) A deprecated service

**Answer: B**
> **Explanation:** AlloyDB is a fully managed, PostgreSQL-compatible database that offers:
> - Up to 4x faster than standard PostgreSQL
> - 100% PostgreSQL compatibility
> - High availability with automatic failover
> - Integrated with Vertex AI for ML queries

---

### **📌 CLOUD RUN & SERVERLESS** (6 Questions)

#### **Question 35**
What is Cloud Run?

*   A) A VM service
*   B) A fully managed serverless platform for running stateless containers that scales automatically
*   C) A Kubernetes cluster
*   D) A CI/CD tool

**Answer: B**
> **Explanation:** Cloud Run is a fully managed serverless platform that runs stateless containers. It automatically scales based on traffic, including scaling to zero when not in use.

---

#### **Question 36**
What is the difference between Cloud Run (fully managed) and Cloud Run for Anthos?

*   A) They are identical
*   B) Fully managed runs on Google's infrastructure; Cloud Run for Anthos runs on GKE/Anthos clusters you manage
*   C) Cloud Run for Anthos is deprecated
*   D) Fully managed is more expensive

**Answer: B**
> **Explanation:** 
> - **Cloud Run (fully managed)**: Runs on Google's serverless infrastructure
> - **Cloud Run for Anthos**: Runs on your GKE clusters, providing more control over the underlying infrastructure

---

#### **Question 37**
What is Cloud Functions?

*   A) A container service
*   B) A serverless execution environment for running event-driven functions without managing infrastructure
*   C) A VM service
*   D) A database service

**Answer: B**
> **Explanation:** Cloud Functions is a serverless, event-driven compute service that executes code in response to events (HTTP, Pub/Sub, Cloud Storage, etc.) without server management.

---

#### **Question 38**
What triggers can invoke a Cloud Function?

*   A) Only HTTP requests
*   B) HTTP requests, Cloud Storage events, Pub/Sub messages, Firestore changes, and more
*   C) Only Pub/Sub messages
*   D) Only scheduled triggers

**Answer: B**
> **Explanation:** Cloud Functions can be triggered by:
> - HTTP requests
> - Cloud Storage events (create, delete, etc.)
> - Pub/Sub messages
> - Firestore/Firebase events
> - Cloud Scheduler
> - Other GCP events

---

#### **Question 39**
What is the cold start problem in serverless computing?

*   A) VMs running cold
*   B) The latency experienced when a function instance needs to be initialized after being idle
*   C) A cooling system issue
*   D) A billing issue

**Answer: B**
> **Explanation:** Cold start occurs when a new function instance must be initialized, including loading the runtime and code. This causes initial latency. Minimum instances can mitigate this.

---

#### **Question 40**
What is the maximum execution time for Cloud Functions (2nd gen)?

*   A) 1 minute
*   B) Up to 60 minutes
*   C) Unlimited
*   D) 9 minutes

**Answer: B**
> **Explanation:** 
> - **Cloud Functions 2nd gen**: Up to 60 minutes
> - **Cloud Functions 1st gen**: 9 minutes (event-driven), 60 minutes (HTTP)

---

### **📌 GOOGLE KUBERNETES ENGINE (GKE)** (7 Questions)

#### **Question 41**
What is GKE Autopilot?

*   A) A deprecated feature
*   B) A mode where Google manages cluster infrastructure including nodes, letting you focus on workloads
*   C) An auto-scaling feature only
*   D) A backup feature

**Answer: B**
> **Explanation:** GKE Autopilot is a hands-off Kubernetes experience where Google manages the cluster infrastructure, including nodes, security, and scaling. You only manage workloads.

---

#### **Question 42**
What is the difference between GKE Standard and GKE Autopilot?

*   A) They are identical
*   B) Standard gives full node control and management; Autopilot manages infrastructure automatically, billing per-pod
*   C) Autopilot is more expensive always
*   D) Standard doesn't support autoscaling

**Answer: B**
> **Explanation:** 
> | Feature | GKE Standard | GKE Autopilot |
> |---------|--------------|---------------|
> | Node management | You manage | Google manages |
> | Billing | Per node | Per pod resources |
> | Customization | Full control | Limited |
> | Maintenance | Your responsibility | Automatic |

---

#### **Question 43**
What is a GKE Node Pool?

*   A) A swimming pool monitoring system
*   B) A group of nodes within a cluster with the same configuration (machine type, disk, etc.)
*   C) A networking configuration
*   D) A storage pool

**Answer: B**
> **Explanation:** A node pool is a group of nodes with identical configuration. Clusters can have multiple node pools with different machine types for various workload requirements.

---

#### **Question 44**
What is Workload Identity in GKE?

*   A) A naming convention
*   B) The recommended way for GKE workloads to access GCP services using Kubernetes service accounts mapped to GCP service accounts
*   C) A logging feature
*   D) A billing feature

**Answer: B**
> **Explanation:** Workload Identity links Kubernetes service accounts to GCP service accounts, allowing pods to authenticate to GCP APIs without storing service account keys.

---

#### **Question 45**
What is the purpose of GKE Container-Native Load Balancing?

*   A) To balance storage
*   B) To route traffic directly to pods instead of nodes, providing better load distribution and health checking
*   C) To manage containers
*   D) To balance billing

**Answer: B**
> **Explanation:** Container-native load balancing routes traffic directly to pods using Network Endpoint Groups (NEGs), providing more accurate health checks and eliminating extra network hops.

---

#### **Question 46**
What is a GKE private cluster?

*   A) A cluster with no nodes
*   B) A cluster where nodes have internal IP addresses only and the control plane can have private or public endpoints
*   C) An encrypted cluster
*   D) A deleted cluster

**Answer: B**
> **Explanation:** In private clusters, nodes have only internal IP addresses, isolating them from the internet. The control plane can be accessed privately, publicly, or both.

---

#### **Question 47**
What is VPC-native cluster in GKE?

*   A) A cluster using public IPs
*   B) A cluster using alias IP ranges for pod IPs, making pods directly routable within the VPC
*   C) A deprecated configuration
*   D) A cluster without networking

**Answer: B**
> **Explanation:** VPC-native clusters use alias IP addresses for pods, making them directly routable within the VPC network and enabling native integration with VPC features.

---

### **📌 NETWORKING & LOAD BALANCING** (8 Questions)

#### **Question 48**
What types of load balancers are available in GCP?

*   A) Only HTTP(S)
*   B) External/Internal HTTP(S), SSL Proxy, TCP Proxy, Network (TCP/UDP), and Internal TCP/UDP
*   C) Only external
*   D) Only TCP

**Answer: B**
> **Explanation:** GCP load balancers:
> | Type | Layer | Use Case |
> |------|-------|----------|
> | HTTP(S) | L7 | Web apps, APIs |
> | SSL Proxy | L4 | SSL termination |
> | TCP Proxy | L4 | TCP with proxy |
> | Network | L4 | TCP/UDP passthrough |
> | Internal | L4/L7 | Internal services |

---

#### **Question 49**
What is Cloud CDN?

*   A) A database service
*   B) A content delivery network that caches content at Google's global edge locations
*   C) A container service
*   D) A DNS service

**Answer: B**
> **Explanation:** Cloud CDN uses Google's global edge network to cache HTTP(S) content close to users, reducing latency and offloading origin servers.

---

#### **Question 50**
What is Cloud Armor?

*   A) A backup service
*   B) A DDoS protection and WAF service that protects applications behind load balancers
*   C) An encryption service
*   D) A monitoring service

**Answer: B**
> **Explanation:** Cloud Armor provides:
> - DDoS protection
> - WAF (Web Application Firewall) capabilities
> - Security policies with custom rules
> - Works with global load balancers

---

#### **Question 51**
What is the difference between Cloud NAT and a standard NAT gateway?

*   A) They are identical
*   B) Cloud NAT is a distributed, software-defined managed service with no single point of failure
*   C) Cloud NAT is hardware-based
*   D) Standard NAT is managed by Google

**Answer: B**
> **Explanation:** Cloud NAT is a fully managed, distributed NAT service. Unlike traditional NAT gateways, it doesn't rely on specific instances or single points of failure.

---

#### **Question 52**
What is Cloud DNS?

*   A) A content delivery service
*   B) A scalable, reliable, and managed authoritative DNS service
*   C) A VPN service
*   D) A database service

**Answer: B**
> **Explanation:** Cloud DNS is a high-availability, global DNS service that publishes domain names to the global DNS using Google's infrastructure for low-latency, high-availability DNS serving.

---

#### **Question 53**
What is VPC Peering?

*   A) A security feature only
*   B) A networking connection between two VPC networks enabling internal IP communication
*   C) A load balancing feature
*   D) A DNS feature

**Answer: B**
> **Explanation:** VPC Peering connects two VPC networks (same or different projects/organizations) allowing resources to communicate using internal IPs. Traffic stays on Google's network, reducing latency and costs.

---

#### **Question 54**
What is Shared VPC?

*   A) A public VPC
*   B) A VPC that can be shared across multiple projects within an organization, enabling centralized network management
*   C) A deprecated feature
*   D) A VPC template

**Answer: B**
> **Explanation:** Shared VPC allows an organization to connect resources from multiple projects to a common VPC network. Features:
> - Centralized network administration
> - Host project owns the VPC
> - Service projects use the shared network
> - Maintains project-level separation for billing/IAM

---

#### **Question 55**
What is the difference between Cloud VPN and Cloud Interconnect?

*   A) They are identical
*   B) Cloud VPN uses encrypted tunnels over public internet; Cloud Interconnect provides dedicated private connections to Google's network
*   C) Cloud VPN is faster
*   D) Cloud Interconnect is deprecated

**Answer: B**
> **Explanation:** 
> | Feature | Cloud VPN | Cloud Interconnect |
> |---------|-----------|-------------------|
> | Connection | Encrypted over internet | Dedicated private |
> | Bandwidth | Up to 3 Gbps per tunnel | 10-200 Gbps |
> | Latency | Variable | Consistent, lower |
> | Cost | Lower | Higher |
> | Use case | Small/medium workloads | Enterprise, high bandwidth |

---

### **📌 PUB/SUB** (5 Questions)

#### **Question 56**
What is Cloud Pub/Sub?

*   A) A database service
*   B) A fully managed, real-time messaging service for asynchronous communication between services
*   C) A file storage service
*   D) A compute service

**Answer: B**
> **Explanation:** Pub/Sub is an asynchronous messaging service that decouples services:
> - Publishers send messages to **topics**
> - Subscribers receive messages from **subscriptions**
> - Enables event-driven architectures
> - Scales automatically to millions of messages per second

---

#### **Question 57**
What is the difference between Push and Pull subscriptions in Pub/Sub?

*   A) They are identical
*   B) Push sends messages to an endpoint via HTTP; Pull requires subscribers to request messages
*   C) Pull is deprecated
*   D) Push is only for Cloud Functions

**Answer: B**
> **Explanation:** 
> | Feature | Push | Pull |
> |---------|------|------|
> | Message delivery | Pub/Sub sends to endpoint | Subscriber requests messages |
> | Endpoint | Requires HTTPS endpoint | No endpoint needed |
> | Control | Less control | More control over processing |
> | Use case | Cloud Run, App Engine | GKE, Compute Engine, custom apps |

---

#### **Question 58**
What is a Dead Letter Topic in Pub/Sub?

*   A) A deleted topic
*   B) A topic where messages that can't be processed after maximum delivery attempts are sent
*   C) An encrypted topic
*   D) A backup topic

**Answer: B**
> **Explanation:** Dead letter topics receive messages that couldn't be processed successfully after the configured number of delivery attempts:
> - Prevents message loss
> - Allows investigation of failed messages
> - Configure max delivery attempts (5-100)
> - Messages include delivery attempt metadata

---

#### **Question 59**
What is message ordering in Pub/Sub?

*   A) Alphabetical sorting of messages
*   B) A feature that ensures messages with the same ordering key are delivered in the order they were published
*   C) A deprecated feature
*   D) Automatic message priority

**Answer: B**
> **Explanation:** Message ordering guarantees that messages with the same ordering key are delivered in publish order:
> - Enabled per subscription
> - Requires ordering key in message
> - May reduce throughput
> - Best for scenarios requiring strict order (e.g., database changes)

---

#### **Question 60**
What is the difference between Pub/Sub and Pub/Sub Lite?

*   A) They are identical
*   B) Pub/Sub is global with higher cost; Pub/Sub Lite is zonal with lower cost for predictable workloads
*   C) Pub/Sub Lite has more features
*   D) Pub/Sub is deprecated

**Answer: B**
> **Explanation:** 
> | Feature | Pub/Sub | Pub/Sub Lite |
> |---------|---------|--------------|
> | Scope | Global | Zonal/Regional |
> | Pricing | Per-message | Provisioned capacity |
> | Cost | Higher | 80-90% lower |
> | Use case | Variable workloads | Predictable, high-volume |
> | Capacity | Automatic | Pre-provisioned |

---

### **📌 BIGQUERY** (6 Questions)

#### **Question 61**
What is BigQuery?

*   A) A transactional database
*   B) A serverless, highly scalable, and cost-effective multi-cloud data warehouse
*   C) A caching service
*   D) A file storage service

**Answer: B**
> **Explanation:** BigQuery is a fully managed, serverless data warehouse that:
> - Enables fast SQL queries on large datasets
> - Uses columnar storage format
> - Scales to petabytes of data
> - Supports standard SQL
> - Integrates with ML (BigQuery ML)

---

#### **Question 62**
What is the difference between partitioning and clustering in BigQuery?

*   A) They are identical
*   B) Partitioning divides table by column (date/integer); clustering sorts data within partitions by specified columns
*   C) Clustering is deprecated
*   D) Partitioning is only for small tables

**Answer: B**
> **Explanation:** 
> | Feature | Partitioning | Clustering |
> |---------|-------------|------------|
> | Division | By column values | Sorting within partitions |
> | Columns | 1 partition column | Up to 4 cluster columns |
> | Types | Time, integer range, ingestion time | Any column type |
> | Pruning | Eliminates entire partitions | Eliminates blocks within partition |
> | Best for | Filtering by date/range | High-cardinality columns |

---

#### **Question 63**
What are BigQuery slots?

*   A) Storage containers
*   B) Units of computational capacity used to execute SQL queries
*   C) Network bandwidth
*   D) Memory allocations

**Answer: B**
> **Explanation:** Slots are BigQuery's unit of computational capacity:
> - **On-demand**: Shared pool, pay per query (per TB scanned)
> - **Flat-rate**: Reserved slots, predictable costs
> - **Flex slots**: Short-term commitments (60 seconds min)
> - **Autoscaling**: Dynamic slot allocation

---

#### **Question 64**
What is BigQuery ML?

*   A) A separate ML service
*   B) A feature that allows creating and executing ML models using SQL queries directly in BigQuery
*   C) A data migration tool
*   D) A visualization tool

**Answer: B**
> **Explanation:** BigQuery ML enables:
> - Creating ML models with SQL (CREATE MODEL)
> - Training on data in BigQuery
> - Predictions with SQL (ML.PREDICT)
> - Supported models: Linear regression, logistic regression, k-means, time series, deep neural networks, etc.

---

#### **Question 65**
What is the difference between streaming and batch loading in BigQuery?

*   A) They are identical
*   B) Streaming inserts data in real-time with higher cost; batch loading is free but has latency
*   C) Batch loading is real-time
*   D) Streaming is deprecated

**Answer: B**
> **Explanation:** 
> | Feature | Streaming | Batch |
> |---------|-----------|-------|
> | Latency | Real-time (seconds) | Minutes to hours |
> | Cost | Per-row pricing | Free (storage only) |
> | Availability | Immediate | After job completes |
> | Use case | Real-time dashboards | ETL, data migration |
> | Quotas | Row and size limits | File size limits |

---

#### **Question 66**
What are materialized views in BigQuery?

*   A) Regular views
*   B) Precomputed views that cache query results and automatically refresh when base tables change
*   C) A deprecated feature
*   D) A visualization feature

**Answer: B**
> **Explanation:** Materialized views in BigQuery:
> - Store precomputed results (unlike regular views)
> - Auto-refresh when base tables change
> - Automatically rewrite queries to use materialized view
> - Reduce query costs and latency
> - Support aggregations on single table

---

### **📌 CLOUD LOGGING & MONITORING** (5 Questions)

#### **Question 67**
What is Cloud Operations Suite (formerly Stackdriver)?

*   A) A compute service
*   B) An integrated monitoring, logging, and diagnostics suite for GCP and hybrid environments
*   C) A database service
*   D) A networking service

**Answer: B**
> **Explanation:** Cloud Operations Suite includes:
> - **Cloud Monitoring**: Metrics, dashboards, alerting
> - **Cloud Logging**: Log storage and analysis
> - **Error Reporting**: Error tracking and notification
> - **Cloud Trace**: Distributed tracing
> - **Cloud Profiler**: CPU and memory profiling
> - **Cloud Debugger**: Production debugging

---

#### **Question 68**
What are log-based metrics in Cloud Logging?

*   A) Storage metrics
*   B) Custom metrics derived from log entries that can be used for monitoring and alerting
*   C) Billing metrics
*   D) Network metrics

**Answer: B**
> **Explanation:** Log-based metrics extract metric data from logs:
> - **Counter metrics**: Count log entries matching filter
> - **Distribution metrics**: Extract numeric values from logs
> - Create charts and dashboards
> - Set up alerting policies
> - Example: Count of 5xx errors per minute

---

#### **Question 69**
What is Cloud Trace?

*   A) A logging service
*   B) A distributed tracing system that collects latency data from applications
*   C) A debugging tool
*   D) A deployment service

**Answer: B**
> **Explanation:** Cloud Trace:
> - Collects latency data across services
> - Visualizes request flow through microservices
> - Identifies performance bottlenecks
> - Integrates with Cloud Run, GKE, App Engine
> - Supports OpenTelemetry

---

#### **Question 70**
What are Uptime Checks in Cloud Monitoring?

*   A) A backup verification
*   B) Probes that monitor the availability of URLs, TCP ports, or custom services from multiple global locations
*   C) A billing check
*   D) A storage check

**Answer: B**
> **Explanation:** Uptime checks:
> - Monitor HTTP(S), TCP endpoints
> - Check from multiple global locations
> - Configure check frequency (1-15 minutes)
> - Create alerts on failures
> - Support authentication and custom headers

---

#### **Question 71**
What is an Alerting Policy in Cloud Monitoring?

*   A) A security policy
*   B) A configuration that defines conditions under which notifications are sent when metrics cross thresholds
*   C) A billing policy
*   D) An access policy

**Answer: B**
> **Explanation:** Alerting policies:
> - Define conditions (metric thresholds, absence, etc.)
> - Set notification channels (email, SMS, PagerDuty, Slack, etc.)
> - Configure duration before alerting
> - Support multiple conditions with AND/OR logic
> - Include documentation for responders

---

### **📌 SECURITY** (4 Questions)

#### **Question 72**
What is Secret Manager in GCP?

*   A) A password generator
*   B) A secure storage system for API keys, passwords, certificates, and other sensitive data
*   C) An encryption service only
*   D) A user management service

**Answer: B**
> **Explanation:** Secret Manager:
> - Stores secrets as binary blobs or text
> - Provides versioning for secrets
> - IAM-based access control
> - Audit logging of access
> - Automatic rotation support
> - Regional or global replication

---

#### **Question 73**
What is Cloud KMS (Key Management Service)?

*   A) Kubernetes Management Service
*   B) A service for creating, managing, and using cryptographic keys for encryption
*   C) A monitoring service
*   D) A storage service

**Answer: B**
> **Explanation:** Cloud KMS:
> - Create and manage encryption keys
> - Symmetric and asymmetric keys
> - HSM-backed keys (Cloud HSM)
> - Customer-managed encryption keys (CMEK)
> - Key rotation policies
> - Integrates with GCP services for encryption

---

#### **Question 74**
What is VPC Service Controls?

*   A) A billing feature
*   B) A security perimeter around GCP resources to prevent data exfiltration and control access
*   C) A networking feature only
*   D) A deprecated feature

**Answer: B**
> **Explanation:** VPC Service Controls:
> - Creates security perimeters around GCP services
> - Prevents data exfiltration
> - Controls access to resources within perimeter
> - Works with BigQuery, Cloud Storage, etc.
> - Allows access levels based on identity, IP, device

---

#### **Question 75**
What is Binary Authorization?

*   A) A code signing tool
*   B) A deploy-time security control that ensures only trusted container images are deployed to GKE
*   C) A binary file storage
*   D) An authentication service

**Answer: B**
> **Explanation:** Binary Authorization:
> - Enforces policies for container deployment
> - Requires attestations (signatures) on images
> - Integrates with Artifact Registry
> - Works with GKE and Cloud Run
> - Prevents deployment of untrusted images

---

### **📌 CI/CD & DEVOPS** (4 Questions)

#### **Question 76**
What is Cloud Build?

*   A) A VM provisioning service
*   B) A fully managed CI/CD platform that executes builds on Google Cloud infrastructure
*   C) A monitoring service
*   D) A storage service

**Answer: B**
> **Explanation:** Cloud Build:
> - Executes builds in isolated containers
> - Supports any language/framework
> - Integrates with GitHub, Bitbucket, Cloud Source Repos
> - Uses cloudbuild.yaml for build configuration
> - Builds Docker images
> - Deploys to GKE, Cloud Run, App Engine

---

#### **Question 77**
What is Artifact Registry?

*   A) A code repository
*   B) A fully managed repository for storing, managing, and securing build artifacts and dependencies
*   C) A logging service
*   D) A deprecated service

**Answer: B**
> **Explanation:** Artifact Registry:
> - Stores Docker images (replaces Container Registry)
> - Stores language packages (npm, Maven, Python, etc.)
> - IAM-based access control
> - Vulnerability scanning
> - Regional and multi-regional
> - Integrates with Cloud Build

---

#### **Question 78**
What is Cloud Deploy?

*   A) A VM deployment service
*   B) A fully managed continuous delivery service for deploying applications to GKE and Cloud Run
*   C) A monitoring service
*   D) A security service

**Answer: B**
> **Explanation:** Cloud Deploy:
> - Managed continuous delivery service
> - Defines delivery pipelines with targets
> - Supports progressive rollouts
> - Approval workflows
> - Rollback capabilities
> - Integrates with Cloud Build

---

#### **Question 79**
What is Cloud Scheduler?

*   A) A VM scheduler
*   B) A fully managed cron job service that triggers actions on a schedule
*   C) A database scheduler
*   D) A networking service

**Answer: B**
> **Explanation:** Cloud Scheduler:
> - Triggers Pub/Sub messages
> - Invokes HTTP/S endpoints
> - Calls Cloud Functions
> - Uses standard cron syntax
> - Configurable retry behavior
> - Time zone support

---

---

## 📊 **FINAL SUMMARY**

| Category | Question Count |
|----------|----------------|
| GCP Fundamentals & IAM | 7 |
| Regions, Zones & Networking Basics | 3 |
| Compute Engine | 8 |
| Cloud Storage | 7 |
| Cloud SQL & Database Services | 9 |
| Cloud Run & Serverless | 6 |
| Google Kubernetes Engine (GKE) | 7 |
| Networking & Load Balancing | 8 |
| Pub/Sub | 5 |
| BigQuery | 6 |
| Cloud Logging & Monitoring | 5 |
| Security | 4 |
| CI/CD & DevOps | 4 |
| **TOTAL** | **79 Questions** |

---

## ✅ **Coverage Rating: 9/10** ⭐⭐⭐⭐⭐⭐⭐⭐⭐☆

### **Now Covered:**
- ✅ IAM & Fundamentals
- ✅ Compute Engine
- ✅ Cloud Storage
- ✅ All Database Services (SQL, Spanner, Firestore, Bigtable, AlloyDB, Memorystore)
- ✅ Serverless (Cloud Run, Functions)
- ✅ GKE
- ✅ Networking & Load Balancing
- ✅ Pub/Sub
- ✅ BigQuery
- ✅ Monitoring & Logging
- ✅ Security (KMS, Secret Manager, VPC SC, Binary Auth)
- ✅ CI/CD (Cloud Build, Artifact Registry, Cloud Deploy)

### **Optional Advanced Topics (not included):**
- App Engine (Standard vs Flexible)
- Dataflow (Apache Beam)
- Dataproc (Hadoop/Spark)
- Cloud Composer (Airflow)
- Vertex AI / AI Platform
- Anthos deep dive
- Organization Policies
- Billing & Cost Management