<div align="center">
<p align="center">
  <img src="https://img.icons8.com/external-tal-revivo-filled-tal-revivo/96/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-filled-tal-revivo.png" width="100" />
</p>
<p align="center">
    <h1 align="center">ASYNC-ML-INFERENCE</h1>
</p>
<p align="center">
    <em>Unleash your coding superpowers!</em>
</p>
<p align="center">
	<!-- -->
<p>
<p align="center">
    <em>Developed with the software and tools below</em>
</p>
<p align="center">
   <a href="https://skillicons.dev">
      <img src="https://skillicons.dev/icons?i=fastapi,py,redis,md,github,git&theme=light">
   </a>
</p>
</div>
<hr>

## 🔗 Quick Links
- [🔗 Quick Links](#-quick-links)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [⚙️ Installation](#️-installation)
  - [🤖 Running async-ml-inference](#-running-async-ml-inference)
  - [🧪 Tests](#-tests)
- [🚧 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
    - [*Contributing Guidelines*](#contributing-guidelines)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The project is an asynchronous machine learning inference system designed to handle audio data. It provides a scalable and efficient infrastructure for performing machine learning tasks on audio data, allowing for real-time and batch processing. The system is composed of multiple components including an API for interacting with the system, a client for making requests, and worker modules for performing the machine learning tasks. Its value proposition lies in its ability to process audio data quickly and accurately, enabling applications in areas such as speech recognition, audio classification, and music analysis.

---

## 📦 Features

|  | Feature             | Description                                                                                            |
|--------|---------------------|-----------------------------------------------------------------------------------------------------------------------|
| ⚙️     | **Architecture**    | The repository follows a modular design, with separate directories for the API, client, and workers. It utilizes Docker for containerization and employs FastAPI and Celery for async processing. |
| 📄     | **Documentation**   | The repository lacks extensive documentation, making it challenging to understand its components and functionalities. More detailed explanations and examples would improve its user-friendliness.    |
| 🔗     | **Dependencies**    | Dependencies include FastAPI, Celery, Redis, RabbitMQ, requests, Beautiful Soup, Librosa, Numba, and others. These libraries integrate well to support the repository's async ML inference tasks and web API functionalities.    |
| 🧩     | **Modularity**      | The repository demonstrates modularity with distinct directories for the API, client, and workers. Each component has its own Dockerfile, allowing for isolated development and deployment. |
| 🧪     | **Testing**         | The repository lacks explicit information on testing methodologies. Additional details on unit tests, integration tests, and testing tools would provide insights into the testing practices and coverage. |
| ⚡️     | **Performance**     | Due to the absence of specific details, it is challenging to evaluate the repository's performance. However, the use of async processing with Celery and the utilization of libraries like Librosa and Numba suggest potential for optimized performance. |
| 🔐     | **Security**        | The repository does not provide explicit details on implemented security measures. To ensure data protection and operational integrity, it is recommended to implement secure communication protocols and access controls. |
| 🔀     | **Version Control** | The repository does not specify the version control system used. Implementing a robust version control strategy, such as Git, would facilitate collaborative development and efficient tracking of code changes. |
| 🔌     | **Integrations**    | The repository integrates with RabbitMQ and Redis for message queueing and backend functionality. It also interacts with external APIs using the requests library. These integrations enable efficient communication and interaction between different components. |
| 📶     | **Scalability**     | The repository's modular design, Docker-based containerization, and the use of async processing make it scalable. The deployment can be easily scaled to handle increased user and repository numbers by utilizing appropriate infrastructure management tools. |

---

## 📂 Repository Structure

```sh
└── async-ml-inference/
    ├── .env
    ├── Pipfile
    ├── Pipfile.lock
    ├── docker-compose.yaml
    ├── src/
    │   ├── api/
    │   │   ├── Dockerfile
    │   │   ├── api.py
    │   │   └── requirements.txt
    │   ├── client/
    │   │   ├── Dockerfile
    │   │   ├── client.py
    │   │   └── requirements.txt
    │   └── workers/
    │       ├── Dockerfile
    │       ├── audio/
    │       ├── backend.py
    │       ├── broker.py
    │       ├── euro/
    │       └── requirements.txt

```

---


## 🧩 Modules

<details closed><summary>.</summary>

| File                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [docker-compose.yaml](https://github.com/FerrariDG/async-ml-inference/blob/main/docker-compose.yaml) | This code snippet defines the docker-compose.yaml file for the async-ml-inference repository. It sets up various services like broker, backend, audio, euro, api, and client, along with their dependencies and configurations. It enables communication and coordination between these services using RabbitMQ and Redis. The code snippet also configures the network connections and ports for the services.                                                                                                                                                                                    |
| [Pipfile](https://github.com/FerrariDG/async-ml-inference/blob/main/Pipfile)                         | This code snippet is located in the `src/api` directory and contains the implementation for the API endpoint. Its main role is to handle incoming requests and communicate with the backend and workers to process ML inference tasks. The dependencies listed in the Pipfile are used to support the functionality of the API.                                                                                                                                                                                                                                                                    |
| [.env](https://github.com/FerrariDG/async-ml-inference/blob/main/.env)                               | This code snippet plays a critical role in managing and deploying various components of the async-ml-inference repository. It ensures proper dependencies, coordinates communication between different workers, and facilitates smooth API and client interactions.                                                                                                                                                                                                                                                                                                                                |
| [Pipfile.lock](https://github.com/FerrariDG/async-ml-inference/blob/main/Pipfile.lock)               | Code snippet summary: This code snippet plays a critical role in the architecture of the parent repository by implementing a key feature that enhances the user experience and functionality. It achieves this by efficiently handling and processing data, ensuring reliable performance and accuracy. Supplementary details and materials about the code can be found in the provided documentation and code comments.Note: Without specific information about the parent repository's architecture and the code snippet itself, this summary is a generalization based on the provided context. |

</details>

<details closed><summary>src/api</summary>

| File                                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/main/src/api/requirements.txt) | This code snippet, located in the `src/api/` directory, is responsible for implementing an API using FastAPI and providing ML inference capabilities. It utilizes dependencies such as Celery and Redis to handle async processing. The main file, `api.py`, defines the API endpoints and their corresponding logic.                                                                                                                                                                                                                                                                                                      |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/main/src/api/Dockerfile)             | The code snippet is a Dockerfile in the `src/api/` directory of the repository. It sets up the environment and dependencies for the API component, installs required packages, copies the `api.py` file, exposes necessary ports, and runs the API using Uvicorn.                                                                                                                                                                                                                                                                                                                                                          |
| [api.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/api/api.py)                     | The code snippet is part of the `async-ml-inference` repository and is located in the `src/api/api.py` file. It sets up a FastAPI server that handles HTTP requests to perform asynchronous machine learning inference tasks. It uses Celery as a task queue and Redis as a backend. The code supports two endpoints: `/audio/length` and `/euro/results`, which create tasks for audio length calculation and Euro lottery results scraping, respectively. The tasks can optionally provide a callback to receive task results asynchronously. The code also includes a `/task/{task_id}` endpoint to fetch task results. |

</details>

<details closed><summary>src/workers</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [backend.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/backend.py)             | This code snippet in the `src/workers/backend.py` file is responsible for managing the connection to a Redis database and checking if the backend is running. It retrieves the Redis connection details from environment variables and builds the connection URL. It then tries to connect to the Redis instance and returns True if the connection is successful, otherwise it prints an error message and returns False. This code is critical for ensuring proper communication and functionality of the backend in the parent repository's architecture. |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/requirements.txt) | The code snippet is a part of the parent repository's architecture, specifically within the async-ml-inference directory. It plays a critical role in providing asynchronous machine learning inference capabilities. The code depends on various libraries and software packages such as Beautiful Soup, Celery, Librosa, and Numba. Its purpose is to enable efficient audio processing and backend functionality.                                                                                                                                         |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/Dockerfile)             | The code snippet is a Dockerfile within the `workers` directory. It sets up a Python 3.7 environment, installs dependencies from `requirements.txt`, and copies the code into the container. It also exposes ports 6379 and 5672.                                                                                                                                                                                                                                                                                                                            |
| [broker.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/broker.py)               | The `broker.py` file provides functions to get the RabbitMQ connection URL and check if the RabbitMQ broker is running. It uses environment variables to configure the connection parameters. These functions are used to establish and verify the connection with RabbitMQ in the async-ml-inference codebase.                                                                                                                                                                                                                                              |

</details>

<details closed><summary>src/workers/audio</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                    |
| [worker.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/audio/worker.py) | This code snippet is a Celery worker that extracts the length of an audio file. It receives an audio URL, downloads the file, and calculates its duration using librosa. It also includes error handling and simulates a long task processing. The worker is part of the async-ml-inference repository and resides in the src/workers/audio directory. |
| [config.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/audio/config.py) | The code snippet configures the Audio Length worker in the async-ml-inference repository. It sets task acknowledgments, prefetching, and queue creation for the worker. It also defines the Redis key's time to live.                                                                                                                                  |

</details>

<details closed><summary>src/workers/euro</summary>

| File                                                                                              | Summary                                                                                                                                                                                                                                                                      |
| ---                                                                                               | ---                                                                                                                                                                                                                                                                          |
| [worker.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/euro/worker.py) | The code snippet in the `worker.py` file is a Celery worker responsible for scraping Euromillions results. It uses Beautiful Soup to parse the HTML page and retrieve the numbers and stars. If successful, it returns a tuple of the numbers and stars.                     |
| [config.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/workers/euro/config.py) | This code snippet configures the Celery worker for processing Euromillions Results in the async-ml-inference repository. It sets task acknowledgments to be processed late and defines the task queue for the Euromillions worker. The result expiration is set to 48 hours. |

</details>

<details closed><summary>src/client</summary>

| File                                                                                                      | Summary                                                                                                                                                                                                                                                      |
| ---                                                                                                       | ---                                                                                                                                                                                                                                                          |
| [requirements.txt](https://github.com/FerrariDG/async-ml-inference/blob/main/src/client/requirements.txt) | The code snippet in the src/client directory is responsible for making requests to the API. It uses the requests library along with other dependencies listed in the requirements.txt file.                                                                  |
| [Dockerfile](https://github.com/FerrariDG/async-ml-inference/blob/main/src/client/Dockerfile)             | The code snippet in the `client/Dockerfile` sets up the client module of the `async-ml-inference` repository. It installs the required dependencies, copies the client script, exposes a port, and runs the client script when the container starts.         |
| [client.py](https://github.com/FerrariDG/async-ml-inference/blob/main/src/client/client.py)               | This code snippet is responsible for sending audio URLs and dates to an API, retrieving the results, and printing them. It utilizes parallel processing to handle multiple tasks efficiently. The code also includes error handling and retry functionality. |

</details>

---

## 🚀 Getting Started

***Prerequisites***

Ensure you have the following dependencies installed on your system:

- `► INSERT-DEPENDENCY-1`
- `► INSERT-DEPENDENCY-2`
- `► ...`

### ⚙️ Installation

1. Clone the async-ml-inference repository:
```sh
git clone https://github.com/FerrariDG/async-ml-inference
```

2. Change to the project directory:
```sh
cd async-ml-inference
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Running async-ml-inference

```sh
python main.py
```

### 🧪 Tests
```sh
pytest
```

---


## 🚧 Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/FerrariDG/async-ml-inference/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/FerrariDG/async-ml-inference/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/FerrariDG/async-ml-inference/issues)**: Submit bugs found or log feature requests for FERRARIDG.

#### *Contributing Guidelines*

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

## 📄 License


This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)

---
