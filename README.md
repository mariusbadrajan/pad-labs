# Peer-to-Peer Student Finance Platform

The Peer-to-Peer Student Finance Platform is a user-friendly digital ecosystem for students, designed to simplify financial management within the academic environment. It enables students to effortlessly split bills and make direct transactions and payments. The platform employs microservices architecture, utilizing .NET for user and transaction management and Go for the API gateway, service registry/discovery, and load balancers, ensuring scalability, flexibility, and robustness. It's a game-changer for students seeking a seamless and collaborative approach to handling their finances while fostering a sense of community.

## Application Suitability

### Why my platform is a good fit for microservices and why a distributed system is necessary?

**Simplifying Complexity and Scaling:** My platform involves complex components like user management, transaction handling, real-time updates, and financial calculations. Microservices are my solution to breaking down this complexity into manageable, independent units. They enable me to develop and scale specific microservices as student populations grow, ensuring I can meet the increasing demand for financial transactions and user interactions.

**Independent Development and Deployment:** Microservices grant me the ability to independently develop and deploy crucial features. For instance, I can focus on developing the user management microservice separately from the transaction management microservice. This independence empowers different teams to work on various aspects of the platform without impacting one another. It's especially advantageous when I need to respond swiftly to evolving student finance needs and regulatory changes.

**Leveraging Technology Diversity:** My platform demands diverse technologies to cater to various functionalities. While real-time updates may thrive in an event-driven architecture, transaction processing might involve different databases and technologies. With microservices, I have the flexibility to choose the ideal technology stack for each microservice, optimizing both performance and functionality.

**Enhancing Resilience and Redundancy:** In the finance sector, high availability and data integrity are non-negotiable. Microservices inherently provide the resilience and redundancy I require. If one microservice encounters an issue, others continue functioning, minimizing downtime and ensuring uninterrupted financial services for students. This is paramount for maintaining user trust and compliance with financial regulations.

**Adapting to Changing User Needs:** Student finance needs are dynamic, influenced by factors like new regulations, economic shifts, or changes in student demographics. Microservices grant me the agility to adapt my platform to these evolving needs. I can seamlessly introduce new microservices or modify existing ones to incorporate fresh features, integrate with financial institutions, or fortify security measures as necessary.

### Real-world examples of well-known projects that are similar to my idea and employ microservices:

- **PayPal:** PayPal employs microservices to power payment processing, fraud detection, and user management independently, ensuring high availability and rapid development. This architecture enables PayPal to handle millions of daily transactions securely.

- **Revolut:** Revolut harnesses microservices to deliver banking, currency exchange, and cryptocurrency trading services while maintaining scalability and real-time analytics. This approach allows Revolut to rapidly introduce new financial features and provide users with a seamless, personalized experience.

- **Square:** Square relies on microservices for its point-of-sale systems, payment processing, and inventory management, enabling rapid adaptation to changing payment needs and regulations. By breaking down its services into modular components, Square ensures high availability and flexibility in serving businesses of all sizes.

## Service Boundaries

The Peer-to-Peer Student Finance Platform comprises a set of core services, including:

- **API Gateway** (for routing client requests),
- **Load Balancer** (for efficient request distribution),
- **Service Discovery** (for dynamic service registration and discovery),
- **User Service** (handling user-related operations),
- **Account Balance Service** (handling account balance operations),
- **Transaction Service** (managing financial transactions).

Additionally, the platform employs:

- A **Cache** component (linked to the API Gateway) for temporary data storage to enhance response times,
- A **Database** component to serve as the central repository for critical application data.

Each of these components plays a distinct role in delivering a seamless and efficient user experience.

![The Architecture Diagram of the System](https://github.com/mariusbadrajan/pad-labs/blob/main/Assets/ArchitectureDiagram.png)

### API Gateway:

- **Description:** The API Gateway serves as the entry point for client requests in the Peer-to-Peer Student Finance Platform. It routes incoming requests to the appropriate service clusters based on the requested functionality.
- **Role:** Route the client requests to the proper service cluster.

### Service Discovery:

- **Description:** The Service Discovery component keeps a registry of existing service addresses and monitors the health of these services. If a service's health is unsatisfactory, it notifies other services not to route requests through it and logs the defect. It enables dynamic service registration and discovery.
- **Role:** Keep a registry of the existing service addresses and periodically check their health. Notify other services not to route through unhealthy services.

### Load Balancer:

- **Description:** The Load Balancer is responsible for distributing incoming requests among multiple instances of the same service within a service cluster. It ensures even distribution of requests and can help manage traffic spikes.
- **Role:** Select a service to handle the incoming request from the assigned cluster.

### User Service:

- **Description:** The User Service is responsible for handling HTTP requests related to user-related operations, including user registration, login, user profiles, profile updates, user searches, and related functionalities. It manages user profiles and authentication.
- **Role:** Handle HTTP requests related to user-related operations.

### Account Balance Service:

- **Description:** The Account Balance Service is dedicated to managing user account balances and supporting financial operations, including checking balances, topping up accounts, and initiating withdrawals. It ensures users have easy access to their financial information.
- **Role:** Handle account balance-related operations.

### Transaction Service:

- **Description:** The Transaction Service is a core component of the Peer-to-Peer Student Finance Platform, responsible for managing financial transactions. It handles a range of financial operations to ensure a seamless experience within the platform.
- **Role:** Handle financial transaction-related operations.

### Cache (Linked to API Gateway):

- **Description:** The Cache component is linked to the API Gateway and temporarily stores frequently accessed data to improve response times and reduce the load on the underlying services. It can cache data such as user profiles, transaction details, and other frequently accessed information.
- **Role:** Temporarily store frequently accessed data to reduce service load and improve response times.

### Database:

- **Description:** The Database component serves as the foundational data storage and retrieval system for the Peer-to-Peer Student Finance Platform. It stores essential application data, including user information, financial transactions, account balances, transaction history, and other critical data required for platform functionalities.
- **Role:** Manage and store data, facilitate data retrieval, and ensure data integrity for various platform functionalities, including user operations and financial transactions. Serve as the central repository for application data.

## Technology Stack and Communication Patterns

In this platform, the User and Transaction Services, critical for financial operations, are developed using .NET (C#), while the API Gateway, serving as the entry point, is implemented in Go. Communication patterns include RESTful for the API Gateway and gRPC for the User, Account Balance and Transaction Services, ensuring an efficient and secure financial experience for students.

### API Gateway (Go):

- **Technology Stack:** I'll implement the API Gateway in Go.
- **Communication Pattern:** I will communicate with the API Gateway using RESTful endpoints. It will route incoming RESTful requests to the appropriate microservices.

### Load Balancer (Go):

- **Technology Stack:** I'll implement the Load Balancer in Go.
- **Communication Pattern:** Load balancers work at the transport layer, handling routing and load distribution. They are agnostic to the communication patterns used by the services.

### Service Discovery (Go):

- **Technology Stack:** For service discovery, I'll use tools like Consul or Eureka, which have client libraries available for Go.
- **Communication Pattern:** Service discovery involves RESTful communication for registration and querying. It keeps a registry of existing service addresses and periodically checks their health.

### User Service (C# Microservice):

- **Technology Stack:** I'll implement the User Service in ASP.NET Core (C#).
- **Communication Pattern:** I will communicate with the User Service via gRPC for efficient and strongly typed interactions related to user operations.

### Account Balance Service (C# Microservice):

- **Technology Stack:** I'll implement the Account Balance Service in ASP.NET Core (C#).
- **Communication Pattern:** I will communicate with the Account Balance Service via gRPC for efficient and strongly typed interactions related to account balance operations.

### Transaction Service (C# Microservice):

- **Technology Stack:** I'll implement the Transaction Service in ASP.NET Core (C#).
- **Communication Pattern:** I will communicate with the Transaction Service via gRPC for efficient and strongly typed interactions related to financial transactions.

### Cache (Linked to API Gateway):

- **Technology Stack:** For caching, I can use caching libraries like Redis with client libraries available for both C# and Go.
- **Communication Pattern:** Caching itself doesn't dictate a specific communication pattern. It enhances performance by reducing repeated communication with the underlying services.

### Database (MSSQL):

- **Technology Stack:** Microsoft SQL Server (MSSQL) is suitable for relational database needs and integrates well with C# through appropriate database drivers.
- **Communication Pattern:** Database communication typically uses SQL queries and is independent of REST or gRPC.

## Data Management

### User Microservice:

**Description**: The User Management Service is responsible for managing user accounts, authentication, and user profiles. It allows users to register, log in, view and update their profiles, and search for other users.

**Endpoints**:

1. **User Registration**
   - **Endpoint**: `POST /api/users/register`
   - **Description**: Allows users to register by providing necessary information like username, email, and password.
   - **Request Header**: None
   - **Request Body**:
     ```json
     {
       "username": "example_user",
       "email": "user@example.com",
       "password": "secure_password"
     }
     ```
   - **Response Body**:
     ```json
     {
       "userId": "123456",
       "username": "example_user",
       "email": "user@example.com"
     }
     ```
   - **Response Code**: 201 Created

2. **User Login**
   - **Endpoint**: `POST /api/users/login`
   - **Description**: Enables users to log in by providing valid credentials (email/username and password) and returns an access token for subsequent requests.
   - **Request Header**: None
   - **Request Body**:
     ```json
     {
       "username": "example_user",
       "password": "secure_password"
     }
     ```
   - **Response Body**:
     ```json
     {
       "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
     }
     ```
   - **Response Code**: 200 OK

3. **User Profile**
   - **Endpoint**: `GET /api/users/profile/{userId}`
   - **Description**: Retrieves the user's profile information based on their user ID.
   - **Request Header**:
     - `Authorization: Bearer {access_token}`
   - **Response Body**:
     ```json
     {
       "userId": "123456",
       "username": "example_user",
       "email": "user@example.com",
       "profilePicture": "https://example.com/profile.jpg"
     }
     ```
   - **Response Code**: 200 OK

4. **User Update Profile**
   - **Endpoint**: `PUT /api/users/profile/{userId}`
   - **Description**: Allows users to update their profile information, such as contact information and profile picture.
   - **Request Header**:
     - `Authorization: Bearer {access_token}`
   - **Request Body**:
     ```json
     {
       "email": "updated_email@example.com",
       "profilePicture": "https://example.com/updated_profile.jpg"
     }
     ```
   - **Response Body**:
     ```json
     {
       "message": "Profile updated successfully."
     }
     ```
   - **Response Code**: 200 OK

5. **User Search**
   - **Endpoint**: `GET /api/users/search?query={searchQuery}`
   - **Description**: Enables users to search for other users based on criteria like name or username.
   - **Request Header**:
     - `Authorization: Bearer {access_token}`
   - **Response Body**:
     ```json
     [
       {
         "userId": "234567",
         "username": "another_user",
         "email": "another_user@example.com"
       },
       {
         "userId": "345678",
         "username": "third_user",
         "email": "third_user@example.com"
       }
     ]
     ```
   - **Response Code**: 200 OK

### Account Balance Microservice:

**Description**: The Account Balance Management Service is responsible for managing user account balances and core financial operations. It allows users to check their balances, top up their accounts, and initiate withdrawals.

**Endpoints**:

1. **Account Balance**
   - **Endpoint**: `GET /api/transactions/balance/{userId}`
   - **Description**: Returns the current account balance for a user.
   - **Request Header**:
     - `Authorization: Bearer {access_token}`
   - **Response Body**:
     ```json
     {
       "balance": 450.0
     }
     ```
   - **Response Code**: 200 OK

2. **Top-Up Account**
   - **Endpoint**: `POST /api/transactions/topup`
   - **Description**: Enables users to top up their account balances by specifying the amount to add.
   - **Request Header**:
     - `Authorization: Bearer {access_token}`
   - **Request Body**:
     ```json
     {
       "amount": 100.0
     }
     ```
   - **Response Body**:
     ```json
     {
       "message": "Account topped up successfully."
     }
     ```
   - **Response Code**: 200 OK

3. **Account Withdrawal**
   - **Endpoint**: `POST /api/accounts/withdraw`
   - **Description**: Allows users to initiate withdrawals from their account balances to an external bank account.
   - **Request Header**:
     - `Authorization: Bearer {access_token}`
   - **Request Body**:
     ```json
     {
       "amount": 50.0,
       "bankAccount": "1234567890"
     }
     ```
   - **Response Body**:
     ```json
     {
       "message": "Withdrawal request submitted successfully."
     }
     ```
   - **Response Code**: 200 OK

### Transaction Microservice:

**Description**: The Transaction Management Service is responsible for creating and managing financial transactions, including P2P payments, expense sharing, and payments to entities. It allows users to create, view, and manage transactions.

**Endpoints**:

1. **Create Transaction**
   - **Endpoint**: `POST /api/transactions/create`
   - **Description**: Allows users to create various types of financial transactions, including Peer-to-Peer (P2P) Payments, Expense Sharing, and Payments to Entities.
   - **Request Header**:
     - `Authorization: Bearer {access_token}`
   - **Request Body**:
     ```json
     {
       "type": "payment",  // Can be "payment", "expense", or "entity_payment"
       "amount": 50.0,
       "description": "Transaction description",
       "participants": [
           {
               "userId": "234567",
               "share": 30.0
           },
           {
               "userId": "345678",
               "share": 20.0
           }
       ]
     }
     ```
   - **Response Body**:
     ```json
     {
       "transactionId": "987654",
       "type": "payment",  // Reflects the transaction type
       "amount": 50.0,
       "description": "Transaction description",
       "timestamp": "2023-10-01T12:00:00Z",
       "participants": [
           {
               "userId": "234567",
               "share": 30.0
           },
           {
               "userId": "345678",
               "share": 20.0
           }
       ],
       "status": "completed"
     }
     ```
   - **Response Code**: 201 Created

2. **Transaction History**
   - **Endpoint**: `GET /api/transactions/history/{userId}`
   - **Description**: Retrieves the transaction history for a specific user, showing all past transactions.
   - **Request Header**:
     - `Authorization: Bearer {access_token}`
   - **Response Body**:
     ```json
     [
       {
         "transactionId": "123456",
         "type": "payment",
         "amount": 25.0,
         "description": "Dinner with friends",
         "timestamp": "2023-09-15T19:30:00Z"
       },
       {
         "transactionId": "234567",
         "type": "expense",
         "amount": 100.0,
         "description": "Shared groceries",
         "timestamp": "2023-09-20T11:45:00Z"
       }
     ]
     ```
   - **Response Code**: 200 OK

3. **Transaction Details**
   - **Endpoint**: `GET /api/transactions/details/{transactionId}`
   - **Description**: Retrieves comprehensive information about a specific transaction, including participants, amounts, and descriptions.
   - **Request Header**:
     - `Authorization: Bearer {access_token}`
   - **Response Body**:
     ```json
     {
       "transactionId": "987654",
       "type": "payment",
       "amount": 50.0,
       "description": "Transaction description",
       "timestamp": "2023-10-01T12:00:00Z",
       "participants": [
           {
               "userId": "234567",
               "share": 30.0
           },
           {
               "userId": "345678",
               "share": 20.0
           }
       ],
       "status": "completed"
     }
     ```
   - **Response Code**: 200 OK

4. **Transaction Cancellation**
   - **Endpoint**: `POST /api/transactions/cancel/{transactionId}`
   - **Description**: Allows users to cancel a specific transaction, reversing the associated funds if applicable.
   - **Request Header**:
     - `Authorization: Bearer {access_token}`
   - **Request Body**:
     ```json
     {
       "reason": "Transaction was initiated in error."
     }
     ```
   - **Response Body**:
     ```json
     {
       "message": "Transaction canceled successfully. Funds returned."
     }
     ```
   - **Response Code**: 200 OK

5. **Transaction Approval and Rejection**
   - **Endpoint**: `POST /api/transactions/approve/{transactionId}` and `POST /api/transactions/reject/{transactionId}`
   - **Description**: Participants can approve or reject transactions to proceed or deny their involvement.
   - **Request Header**:
     - `Authorization: Bearer {access_token}`
   - **Request Body**:
     ```json
     {
       "userId": "234567",
       "approve": true
     }
     ```
   - **Response Body**:
     ```json
     {
       "message": "Transaction approved successfully."
     }
     ```
     or
     ```json
     {
       "message": "Transaction rejected successfully."
     }
     ```
   - **Response Code**: 200 OK

## Deployment and Scaling

To run the project:
```json
docker-compose up
```

I'll use Docker for containerization and Kubernetes for orchestration to effectively manage deployment and scaling in my project. This combination offers flexibility and scalability for my microservices architecture.

## Working endpoints

### Account Microservice:

**Endpoints**:

1. **Get User Accounts**
   - **Endpoint**: `GET /accounts/user/{userId}`
   - **Description**: Retrieves a list of user accounts for a specific user.

2. **Get Account by Id**
   - **Endpoint**: `GET /accounts/{accountId}`
   - **Description**: Retrieves account details for a specific account by its ID.

3. **Create Account**
   - **Endpoint**: `POST /accounts`
   - **Description**: Creates a new user account.
   - **Request Body**:
     ```json
     {
       "userId": 1
     }
     ```

4. **Update Account**
   - **Endpoint**: `PUT /accounts`
   - **Description**: Updates account information, including the balance, for a specific account.
   - **Request Body**:
     ```json
     {
       "balance": 600,
       "id": 1005,
       "userId": 1
     }
     ```

5. **Delete Account**
   - **Endpoint**: `DELETE /accounts/{accountId}`
   - **Description**: Deletes a specific account by its ID.

### Transaction Microservice:

**Endpoints**:

1. **Get User Transactions**
   - **Endpoint**: `GET /transactions/user/{userId}`
   - **Description**: Retrieves a list of transactions associated with a specific user.

2. **Get Account Transactions**
   - **Endpoint**: `GET /transactions/account/{accountId}`
   - **Description**: Retrieves a list of transactions associated with a specific account by its ID.

3. **Get Transaction by Id**
   - **Endpoint**: `GET /transactions/{transactionId}`
   - **Description**: Retrieves transaction details for a specific transaction by its ID.

4. **Create Transaction**
   - **Endpoint**: `POST /transactions`
   - **Description**: Creates a new transaction.
   - **Request Body**:
     ```json
     {
       "userId": 1,
       "accountId": 1003,
       "amount": 200
     }
     ```

4. **Update Transaction**
   - **Endpoint**: `PUT /transactions`
   - **Description**: Updates transaction information, including the type, amount, and status, for a specific transaction.
   - **Request Body**:
     ```json
     {
       "id": 1004,
       "userId": 1,
       "accountId": 1003,
       "type": "Payment",
       "amount": 2000,
       "status": "Completed"
     }
     ```

5. **Delete Transaction**
   - **Endpoint**: `DELETE /transactions/{transactionId}`
   - **Description**: Deletes a specific transaction by its ID.