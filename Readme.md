# SprintYeti API Reference

This README provides detailed documentation for each endpoint in the SprintYeti backend API.

**Base URL:** `http://localhost:5000/api/v1`

---

## Authentication

All protected endpoints require a valid JWT Bearer token in the `Authorization` header:

```
Authorization: Bearer <ACCESS_TOKEN>
```

*Note: Authentication endpoints (login/refresh) are not shown here but should be implemented using Flask-JWT-Extended.*

---

## Users

### GET /users

* **Description:** Retrieve a list of all users.
* **Response:** `200 OK` with JSON array of `User` objects.

### POST /users

* **Description:** Create a new user.
* **Request Body:**

  ```json
  {
    "name": "string",
    "email": "string",
    "password": "string (min 6 chars)"
  }
  ```
* **Response:** `201 Created` with the created `User` object (without password).

### GET /users/{user\_id}

* **Description:** Retrieve a single user by ID.
* **Response:** `200 OK` with a `User` object or `404 Not Found`.

### PUT /users/{user\_id}

* **Description:** Update a user’s details.
* **Request Body:** Partial fields:

  ```json
  {
    "name": "new name",
    "email": "new@example.com",
    "password": "newpass"
  }
  ```
* **Response:** `200 OK` with the updated `User`.

### DELETE /users/{user\_id}

* **Description:** Delete a user.
* **Response:** `200 OK` with a deletion confirmation.

### GET /users/{user\_id}/projects

* **Description:** List projects owned by the user.
* **Response:** `200 OK` with JSON array of `Project` objects.

### GET /users/{user\_id}/tasks

* **Description:** List tasks assigned to the user.
* **Response:** `200 OK` with JSON array of `Task` objects.

---

## Teams

### GET /teams

* **Description:** Retrieve all teams.
* **Response:** `200 OK` with JSON array of `Team` objects.

### POST /teams

* **Description:** Create a new team.
* **Request Body:**

  ```json
  {
    "name": "string",
    "owner_id": number
  }
  ```
* **Response:** `201 Created` with the created `Team`.

### GET /teams/{team\_id}/projects

* **Description:** List projects associated with the team.
* **Response:** `200 OK` with array of `Project`.

### GET /teams/{team\_id}/tasks

* **Description:** List tasks assigned to the team.
* **Response:** `200 OK` with array of `Task`.

---

## Roles

### GET /roles

* **Description:** List all user roles.
* **Response:** `200 OK` with array of `Role` objects.

### POST /roles

* **Description:** Create a new role.
* **Request Body:** `{ "name": "string" }`
* **Response:** `201 Created` with the created `Role`.

---

## Subscription Plans

### GET /plans

* **Description:** List all subscription plans.
* **Response:** `200 OK` with array of `Plan` objects.

### POST /plans

* **Description:** Create a new subscription plan.
* **Request Body:**

  ```json
  {
    "name": "string",
    "monthly_price": number,
    "included_tokens": number,
    "overage_price": number,
    "overage_token_unit": number
  }
  ```
* **Response:** `201 Created` with the created `Plan`.

---

## Subscriptions

### POST /subscriptions

* **Description:** Assign a subscription to a user.
* **Request Body:**

  ```json
  {
    "user_id": number,
    "plan_id": number,
    "status": "active|past_due|canceled",
    "remaining_tokens": number
  }
  ```
* **Response:** `201 Created` with the created `Subscription`.

### GET /subscriptions/{user\_id}

* **Description:** List subscriptions for a user.
* **Response:** `200 OK` with array of `Subscription`.

---

## Token Usage

### GET /usage

* **Description:** Retrieve token usage logs.
* **Response:** `200 OK` with array of `TokenUsage` records.

### POST /usage

* **Description:** Log a token usage event.
* **Request Body:** `{ "user_id": number, "feature": "string", "tokens_used": number }`
* **Response:** `201 Created` with `TokenUsage`.

---

## Projects

### GET /projects

* **Description:** List all projects.
* **Response:** `200 OK` with array of `Project`.

### POST /projects

* **Description:** Create a new project.
* **Request Body:**

  ```json
  {
    "name": "string",
    "description": "string",
    "owner_id": number,
    "team_id": number | null
  }
  ```
* **Response:** `201 Created` with the created `Project`.

### GET /projects/{project\_id}/tasks

* **Description:** List tasks under a project.
* **Response:** `200 OK` with array of `Task`.

### POST /projects/{project\_id}/breakdown

* **Description:** Trigger AI-driven task breakdown using the project description. Persists and returns new tasks.
* **Response:** `200 OK` with array of newly created `Task`.

---

## Tasks

### GET /tasks

* **Description:** List all tasks.
* **Response:** `200 OK` with array of `Task`.

### POST /tasks

* **Description:** Create a new task manually.
* **Request Body:**

  ```json
  {
    "title": "string",
    "description": "string",
    "importance": "critical|important_not_urgent|urgent_not_important|non_urgent_non_important",
    "status": "pending|not_started|in_progress|done|rework",
    "deadline": "ISO8601 timestamp | null",
    "project_id": number,
    "assigned_user_id": number | null,
    "assigned_team_id": number | null
  }
  ```
* **Response:** `201 Created` with the created `Task`.

---

## Commands

### POST /commands

* **Description:** Process a natural-language command (DSL) to create or update tasks via AI parsing.
* **Request Body:**

  ```json
  {
    "user_id": number,
    "team_id": number | null,
    "text": "string (e.g. \"Add task: 'Setup CI'; Status: pending; ...\")",
    "deadline": "ISO8601 timestamp | null",
    "tech_stack": "string",
    "phase_focus": "string"
  }
  ```
* **Response:** `201 Created` with the parsed `Command` object.

---

## Labels

### GET /labels

* **Description:** List all task labels.
* **Response:** `200 OK` with array of `Label`.

### POST /labels

* **Description:** Create a new label.
* **Request Body:** `{ "name": "string", "color": "#hex" }`
* **Response:** `201 Created` with `Label`.

---

## Comments

### GET /comments

* **Description:** List all comments.
* **Response:** `200 OK` with array of `Comment`.

### POST /comments

* **Description:** Add a comment to a task.
* **Request Body:** `{ "task_id": number, "author_id": number, "content": "string" }`
* **Response:** `201 Created` with `Comment`.

---

## Attachments

### GET /attachments

* **Description:** List all attachments.
* **Response:** `200 OK` with array of `Attachment`.

### POST /attachments

* **Description:** Link or upload an attachment.
* **Request Body:** `{ "task_id": number, "filename": "string", "url": "string" }`
* **Response:** `201 Created` with `Attachment`.

---

## Notifications

### GET /notifications

* **Description:** List all notifications.
* **Response:** `200 OK` with array of `Notification`.

### POST /notifications/{user\_id}/mark\_read

* **Description:** Mark all notifications for a user as read.
* **Response:** `204 No Content`.

---

## Kanban

### GET /kanban/boards

* **Description:** List all Kanban boards.
* **Response:** `200 OK` with array of `KanbanBoard`.

### POST /kanban/boards

* **Description:** Create a board for a project.
* **Request Body:** `{ "project_id": number, "name": "string" }`
* **Response:** `201 Created` with `KanbanBoard`.

### POST /kanban/columns

* **Description:** Add a column to a board.
* **Request Body:** `{ "board_id": number, "name": "string", "position": number }`
* **Response:** `201 Created` with `KanbanColumn`.

---

## Table Views

### GET /table\_views

* **Description:** List custom table views.
* **Response:** `200 OK` with array of `TableView`.

### POST /table\_views

* **Description:** Create a table view.
* **Request Body:** `{ "project_id": number, "filters": object, "columns": ["string"] }`
* **Response:** `201 Created` with `TableView`.

---

## Postman Collection

Import `docs/Postman_Collection.json` into Postman to explore and test all endpoints interactively.

*Keep this README updated as the API evolves.*
