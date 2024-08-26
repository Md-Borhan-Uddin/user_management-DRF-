


## Basic User Management API Reference

#### user sign-up

```http
  POST /accounts/sign-up
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required**. Your Valid Email |
| `first_name` | `string` | first name |
| `last_name` | `string` | last name |
| `password` | `string` | **Required**. Enter Password |
| `confirm_password` | `string` | **Required**. Enter same as password |

#### Get Users

```http
  GET /accounts/users
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email` | `string` | Your Valid Email |
| `first_name` | `string` | First name |
| `last_name` | `string` | Last name |

#### Add User

```http
  POST /accounts/users
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required**. Your Valid Email |
| `first_name` | `string` | First name |
| `last_name` | `string` | Last name |
| `password` | `string` | **Required**. Enter Password |
| `confirm_password` | `string` | **Required**. Enter same as password |

#### Update User

```http
  PUT & PATCH /accounts/user/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `first_name` | `string` | First name |
| `last_name` | `string` | Last name |


#### Delete User

```http
  DELETE /accounts/user/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
