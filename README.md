<div align="right">

[![CN](https://img.shields.io/badge/CN-🇨🇳-white?style=plastic)](https://github.com/eli64s/readme-ai/blob/main/docs/README-zh-CN.md)
[![CN](https://img.shields.io/badge/DE-🇩🇪-white?style=plastic)](https://github.com/eli64s/readme-ai/blob/main/docs/README-de.md)
[![FR](https://img.shields.io/badge/FR-🇫🇷-white?style=plastic)](https://github.com/eli64s/readme-ai/blob/main/docs/README-fr.md)
</div>

<div align="center">
    <h1 align="center">
        <img src="https://img.icons8.com/?size=512&id=55494&format=png" width="80" />
        <img src="https://img.icons8.com/?size=512&id=kTuxVYRKeKEY&format=png" width="80" />
        <br>README-AI
    </h1>
    <h3>◦ Generate beautiful and informative <i>README</i> files</h3>
    <h3>◦ Developed with OpenAI's GPT language model APIs</h3>
    <br>
    <p align="center">
        <img src="https://img.shields.io/badge/Markdown-000000.svg?&logo=Markdown&logoColor=white" alt="Markdown" />
        <img src="https://img.shields.io/badge/OpenAI-412991.svg?&logo=OpenAI&logoColor=white" alt="OpenAI" />
        <img src="https://img.shields.io/badge/Python-3776AB.svg?&logo=Python&logoColor=white" alt="Python" />
        <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?&logo=Pytest&logoColor=white" alt="pytest" />
        <img src="https://img.shields.io/badge/Docker-2496ED.svg?style&logo=Docker&logoColor=white" alt="Docker" />
        <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style&logo=GitHub-Actions&logoColor=white" alt="actions" />
    </p>
    <a href="https://pypi.org/project/readmeai/">
        <img src="https://img.shields.io/pypi/v/readmeai?color=5D6D7E&logo=pypi" alt="pypi-version" />
    </a>
    <a href="https://pypi.org/project/readmeai/">
        <img src="https://img.shields.io/pypi/pyversions/readmeai?color=5D6D7E&logo=python" alt="pypi-python-version" />
    </a>
    <img src="https://img.shields.io/github/commit-activity/m/eli64s/readme-ai.svg?color=5D6D7E" alt="commits-month" />
    <img src="https://img.shields.io/github/license/eli64s/readme-ai?color=5D6D7E" alt="license" />
    <br>
    <!--
    <a href="https://pypi.org/project/readmeai/">
    <img src="https://img.shields.io/pypi/dm/readmeai?color=5D6D7E" alt="pypi-downloads" />
    </a>
    -->
</div>

---

## 📖 Table of Contents

- [📖 Table of Contents](#-table-of-contents)
- [🔭 Overview](#-overview)
- [🤖 Demos](#-demos)
- [💫 Features](#-features)
- [👩‍💻 Usage](#-usage)
  - [📦 Installation](#-installation)
  - [⚙️ Configuration](#️-configuration)
  - [🚀 Running *README-AI*](#-running-readme-ai)
  - [🧪 Tests](#-tests)
- [🛠 Roadmap](#-roadmap)
- [📒 Changelog](#-changelog)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

## 🔭 Overview

<table>
    <tr>
        <td>
            <strong>👋 About</strong>
            <br><br>
            <em>README-AI</em> is a command-line tool that generates robust README.md files for your software and data projects. By simply providing a remote repository URL or path to your codebase, this tool auto-generates documentation for your entire project, leveraging the capabilities OpenAI's GPT language model APIs.
            <br><br>
            <strong>🎯 Motivations</strong>
            <br><br>
            Simplifies the process of writing and maintaining high-quality project documentation, enhancing developer productivity and workflow. The ultimate goal of <em>readme-ai</em> is to improve the adoption and usability of open-source software, enabling all skill levels to better understand complex codebases and easily use open-source tools.
            <br><br>
            <strong>⚠️ Disclaimer</strong>
            <br><br>
            This project is currently under development and has an opinionated configuration. While <em>readme-ai</em> provides an excellent starting point for documentation, its important to review all text generated by the OpenAI API to ensure it accurately represents your codebase.
        </td>
        <td>
            <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/dalle-readmeai" width="2500" />
        </td>
    </tr>
</table>

---

## 🤖 Demos

***Command-Line Interface***

‣ Run <i>readme-ai</i> in your terminal via PyPI, Docker, and more!

[cli-demo](https://github.com/eli64s/readme-ai/assets/43382407/645c2336-6ea7-444c-a927-5450930c5255)

<br>

***Streamlit Community Cloud***

‣ Use *readme-ai* directly in your browser! Zero installation, zero code!

[streamlit-demo](https://github.com/eli64s/readme-ai/assets/43382407/e8260e78-b684-4e72-941c-b3046b90c452)

---

## 💫 Features

<br>
<div>
<details>
    <summary style="display: flex; align-items: center;">
        <span style="font-size: 2.0em;"> ❶ Shieldsio Badges</span>
    </summary>
    <table>
        <tr>
            <td>
                <h4><i>Project Slogan and Badges</i></h4>
                <p>
                    ‣ A slogan to highlight your poject is generated by <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L56">prompting</a> OpenAI's GPT engine.
                    </p>
                <p>
                    ‣ Codebase dependencies and metadata are visualized using <a href="https://shields.io/">Shields.io</a> badges.
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/badges.png" alt="badges" />
            </td>
        </tr>
    </table>
    <table>
        <p>
            ‣ Use the CLI option <code>--badges</code> to select the style of badges for your README! 3 styles are currently supported:
        </p>
        <tr>
            <td>
                <h4 style="text-align:left;">1. Shieldsio default badge style</h4>
                <p style="text-align:left;">Command: none as its the default style for <em>readme-ai</em></p>
                <div style="text-align:center;">
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/badges-shieldsio-default.png" alt="badges-shieldsio-default" />
                </div>
            </td>
        </tr>
        <tr>
            <td>
                <h4 style="text-align:left;">2. Shieldsio <em>for-the-badge</em> style</h4>
                <p style="text-align:left;">Command: <code>--badges shields</code></p>
                <div style="text-align:center;">
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/badges-shieldsio-flat.png" alt="badges-shieldsio-flat" />
                </div>
            </td>
        </tr>
        <tr>
            <td>
                <h4 style="text-align:left;">3. Square <em>iOS style</em> badges</h4>
                <p style="text-align:left;">Command: <code>--badges square</code></p>
                <div style="text-align:center;">
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/badges-square.png" alt="badges-square" />
                </div>
            </td>
        </tr>
    </table>
</details>
</div>
<br>
<div>
    <details>
        <summary style="display: flex; align-items: center;">
            <span style="font-size: 2.0em;"> ❷ Codebase Documentation</span>
        </summary>
        <table>
            <tr>
                <td colspan="2">
                    <h4><i>Directory Tree and File Summaries</i></h4>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <p>‣ Your project's directory structure is visualized using a custom tree function.</p>
                    <p>‣ Each file in the codebase is summarized by OpenAI's <i>GPT</i> model.</p>
                </td>
            </tr>
            <tr>
                <td align="center">
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/repository-tree.png" alt="repository-tree" />
                </td>
                <td align="center">
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/code-summaries.png" alt="code-summaries" />
                </td>
            </tr>
        </table>
    </details>
</div>
<br>
<div>
    <details>
        <summary style="display: flex; align-items: center;">
            <span style="font-size: 2.0em;"> ❸ Overview and Features Table</span>
        </summary>
        <table>
            <tr>
                <td>
                    <h4><i>Prompted Text Generation</i></h4>
                    <p>
                        ‣ An overview paragraph and features table are generated using <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L31">detailed prompts</a>, embedded with project metadata.
                    </p>
                </td>
            </tr>
            <tr>
                <td>
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/feature-table.png" alt="feature-table" />
                </td>
            </tr>
        </table>
    </details>
</div>
<br>
<div>
    <details>
        <summary style="display: flex; align-items: center;">
            <span style="font-size: 2.0em;"> ❹ Dynamic Usage Instructions</span><br>
        </summary>
        <table>
            <tr>
                <td>
                    <h4><i>Installation, Running, and Test</i></h4>
                    <p>
                        ‣ Generates instructions for installing, running, and testing your project. Instructions are created by identifying the codebase's top language and referring to our <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/conf/language_setup.toml">language_setup.toml</a> configuration file.
                    </p>
                </td>
            </tr>
            <tr>
                <td>
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/usage-instructions.png" alt="usage-instructions" />
                </td>
            </tr>
        </table>
    </details>
</div>
<br>
<div>
    <details>
        <summary style="display: flex; align-items: center;">
            <span style="font-size: 2.0em;"> ❺ Contributing Guidelines and more!</span><br>
        </summary>
        <table>
            <tr>
                <td>
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/roadmap.png" alt="roadmap" />
                </td>
            </tr>
            <br>
            <tr>
                <td>
                    <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/imgs/license.png" alt="license" />
                </td>
            </tr>
        </table>
    </details>
</div>
<br>
<div>
<details>
    <summary style="display: flex; align-items: center;">
        <span style="font-size: 2.0em;">❻ Templates Coming Soon</span><br>
    </summary>
    <table>
        <tr>
            <td>
                <p>‣ Developing CLI option letting users select from a variety of README styles</p>
                <p>‣ Templates for use-cases such as data, machine learning, web development, and more!</p>
            </td>
        </tr>
        <tr>
            <td>
                <h3>AI and ML README Template Concept</h3>
                <ul>
                    <li><strong><a href="#overview">概述</a></strong>：项目目标、范围和预期结果的总结。</li>
                    <li><strong><a href="#project-structure">项目结构</a></strong>：项目组织和主要组成部分的概述。</li>
                    <li><strong><a href="#data-collection-and-preprocessing">数据预处理</a></strong>：数据源、收集方法和数据类型</li>
                    <li><strong><a href="#feature-engineering">特征工程</a></strong>：特征工程的重要性及其对模型性能的影响。</li>
                    <li><strong><a href="#model-architecture-and-development">模型架构和开发</a></strong>：模型选择、开发策略和实施算法。</li>
                    <li><strong><a href="#training-and-validation">训练和验证</a></strong>：关于模型训练程序、超参数调整和验证策略的信息。</li>
                    <li><strong><a href="#testing-and-evaluation">测试和评估</a></strong>：模型测试结果、性能分析和与基准的比较。</li>
                    <li><strong><a href="#deployment-and-integration">部署和集成</a></strong>：与其他系统、API和用户界面的集成</li>
                    <li><strong><a href="#usage-and-maintenance">使用和维护</a></strong>：关于如何使用部署的模型和界面的用户指南。</li>
                    <li><strong><a href="#results-and-discussion">结果和讨论</a></strong>：影响、限制和未来的工作。</li>
                    <li><strong><a href="#ethical-considerations">伦理考虑</a></strong>：伦理方面、数据隐私和模型预测中的公平性。</li>
                    <li><strong><a href="#contributing">贡献</a></strong>：提交贡献、报告问题和提出增强功能的程序。</li>
                    <li><strong><a href="#acknowledgements">致谢</a></strong>：用到的资源、库和框架的引用。</li>
                    <li><strong><a href="#license">许可</a></strong>：使用权、限制和属性要求的解释。</li>
                </ul>
            </td>
        </tr>
    </table>
</details>
</div>
<br>
<div>
    <details>
        <summary style="display: flex; align-items: center;">
            <span style="font-size: 2.0em;"> ❼ Example README Files</span><br>
        </summary>
        <table>
            <thead>
                <tr>
                    <th></th>
                    <th>Output File</th>
                    <th>Repository</th>
                    <th>Languages</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1️⃣</td>
                    <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-python.md">readme-python.md</a></td>
                    <td><a href="https://github.com/eli64s/readme-ai">readme-ai</a></td>
                    <td>Python</td>
                </tr>
                <tr>
                    <td>2️⃣</td>
                    <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-typescript.md">readme-typescript.md</a></td>
                    <td><a href="https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript">chatgpt-app-react-typescript</a></td>
                    <td>TypeScript, React</td>
                </tr>
                <tr>
                    <td>3️⃣</td>
                    <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-javascript.md">readme-javascript.md</a></td>
                    <td><a href="https://github.com/idosal/assistant-chat-gpt-javascript">assistant-chat-gpt-javascript</a></td>
                    <td>JavaScript, React</td>
                </tr>
                <tr>
                    <td>4️⃣</td>
                    <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-kotlin.md">readme-kotlin.md</a></td>
                    <td><a href="https://github.com/rumaan/file.io-Android-Client">file.io-android-client</a></td>
                    <td>Kotlin, Java, Android</td>
                </tr>
                <tr>
                    <td>5️⃣</td>
                    <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-rust-c.md">readme-rust-c.md</a></td>
                    <td><a href="https://github.com/DownWithUp/CallMon">rust-c-app</a></td>
                    <td>C, Rust</td>
                </tr>
                <tr>
                    <td>6️⃣</td>
                    <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-go.md">readme-go.md</a></td>
                    <td><a href="https://github.com/olliefr/docker-gs-ping">go-docker-app</a></td>
                    <td>Go</td>
                </tr>
                <tr>
                    <td>7️⃣</td>
                    <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-java.md">readme-java.md</a></td>
                    <td><a href="https://github.com/avjinder/Minimal-Todo">java-minimal-todo</a></td>
                    <td>Java</td>
                </tr>
                <tr>
                    <td>8️⃣</td>
                    <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-fastapi-redis.md">readme-fastapi-redis.md</a></td>
                    <td><a href="https://github.com/FerrariDG/async-ml-inference">async-ml-inference</a></td>
                    <td>Python, FastAPI, Redis</td>
                </tr>
                <tr>
                    <td>9️⃣</td>
                    <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-mlops.md">readme-mlops.md</a></td>
                    <td><a href="https://github.com/GokuMohandas/mlops-course">mlops-course</a></td>
                    <td>Python, Jupyter</td>
                </tr>
                <tr>
                    <td>🔟</td>
                    <td><a href="https://github.com/eli64s/readme-ai/blob/main/examples/readme-pyflink.md">readme-pyflink.md</a></td>
                    <td><a href="https://github.com/eli64s/flink-flow">flink-flow</a></td>
                    <td>PyFlink</td>
                </tr>
            </tbody>
        </table>
    </details>
</div>
<br>

<p align="right">
    <a href="#top"><b>🔝 返回</b></a>
</p>

---

## 👩‍💻 Usage

***Dependencies***

Please ensure you have the following dependencies installed on your system:

- *Python version 3.9 or higher*
- *Package manager (i.e. pip, conda, poetry) or Docker*
- *OpenAI API paid account and API key*

<br>

***Repository***

A remote repository URL or local directory path to your project is needed to use *readme-ai*. The following platforms are currently supported:
- *GitHub*
- *GitLab*
- *Bitbucket*
- *File System*

<br>

***OpenAI API***

An OpenAI API account and API key are needed to use *readme-ai*. The steps below outline this process:

<details closed><summary>🔐 OpenAI API - Setup Instructions</summary>

1. Go to the [OpenAI website](https://platform.openai.com/).
2. Click the "Sign up for free" button.
3. Fill out the registration form with your information and agree to the terms of service.
4. Once logged in, click on the "API" tab.
5. Follow the instructions to create a new API key.
6. Copy the API key and keep it in a secure place.

</details>

<details closed><summary>⚠️ OpenAI API - Cautionary Guidelines</summary>

1. **Review Sensitive Information**: Before running the application, ensure that all content in your repository is free of sensitive information. Please note that *readme-ai* does not filter out sensitive data from the README file, and it does not modify any files in your repository.

2. **API Usage Costs**: The OpenAI API is not free, and you will be charged for each request made. Costs can accumulate rapidly, so it's essential to be aware of your usage. You can monitor your API usage and associated costs by visiting the [OpenAI API Usage Dashboard](https://platform.openai.com/account/usage).

3. **Paid Account Recommended**: Setting up a paid account with OpenAI is highly recommended to avoid potential issues. Without a payment method on file, your API usage will be restricted to base GPT-3 models. This limitation can result in less accurate README file generation and may lead to API errors due to request limits.

4. **Runtime Considerations**: README file generation typically takes less than a minute. If the process exceeds a few minutes (e.g., 3 minutes), it's advisable to terminate *readme-ai* to prevent extended processing times.

</details>

---

### 📦 Installation

***Using Pip***

Pip is the recommended installation method for most users.

```sh
pip install readmeai
```
<br>

***Using Docker***

Docker is recommended for users wanting to run the application in a containerized environment.

```sh
docker pull zeroxeli/readme-ai:latest
```

<!--
<br>

<details><summary><b><i>Manually Install</i></b></summary>
-->
<br>

***Manually***

1️⃣ Clone the readme-ai repository.
```sh
git clone https://github.com/eli64s/readme-ai
```

2️⃣ Navigate to readme-ai directory.

```sh
cd readme-ai
```

3️⃣ Install dependencies using a method below.

***Using Bash***
```sh
bash setup/setup.sh
```

***Using Conda***
```sh
conda create -n readmeai python=3.9 -y && \
conda activate readmeai && \
pip install -r requirements.txt
```

***Using Poetry***
```sh
poetry shell && \
poetry install
```

</details>

---

### ⚙️ Configuration

<br>

***Command-Line Arguments***

To generate a *README.md* file, use the `readmeai` command in your terminal, along with the arguments below.

| Short Flag | Long Flag      | Description                                         | Status       |
|------------|----------------|-----------------------------------------------------|--------------|
| `-k`       | `--api-key`    | Your language model API secret key.                 | Optional     |
| `-b`       | `--badges`     | Select 'shields' or 'square' to change badge style. | Optional     |
| `-f`       | `--offline-mode`| Run offline without calling the OpenAI API.        | Optional     |
| `-m`       | `--model`      | Large language model engine (gpt-3.5-turbo)         | Optional     |
| `-o`       | `--output`     | The output path for your README.md file.            | Optional     |
| `-r`       | `--repository` | The URL or path to your code repository.            | Required     |
| `-t`       | `--temperature`| The temperature (randomness) of the model.          | Optional     |
| `-l`       | `--language`   | The language of text to write README in.            | Coming Soon! |
| `-s`       | `--style`      | The README template style to build.                 | Coming Soon! |

<br>

***Custom Settings***

To customize the README file generation process, you can modify the project's [configuration file:](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml)

- [*api*](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L2) - OpenAI language model API configuration settings.
- [*git*](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L12) - Default git repository settings used if no repository is provided.
- [*paths*](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L17) - Directory paths and files used by the *readme-ai* application.
- [*prompts*](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L26) - Large language model prompts used to generate the README file.
- [*md*](https://github.com/eli64s/readme-ai/blob/main/readmeai/settings/config.toml#L59) - Dynamic Markdown section code templates used to build the README file.

---

### 🚀 Running *README-AI*

***Using Pip***

```sh
# Option 1: Run readmeai command with all required command-line arguments.
readmeai --api-key "YOUR_API_KEY" --output readme-ai.md --repository https://github.com/eli64s/readme-ai
```
```sh
# Option 2: Run readmeai command with OpenAI API key set as environment variable.
export OPENAI_API_KEY="YOUR_API_KEY"
readmeai -o readme-ai.md -r https://github.com/eli64s/readme-ai -b shields
```

<br>

***Using Docker***

```sh
# Option 1: Run Docker container with all required command-line arguments.
docker run -it \
-e OPENAI_API_KEY="YOUR_API_KEY" \
-v "$(pwd)":/app zeroxeli/readme-ai:latest \
readmeai -o readme-ai.md -r https://github.com/eli64s/readme-ai
```
```sh
# Option 2: Run Docker container with OpenAI API key set as environment variable.
export OPENAI_API_KEY="YOUR_API_KEY"
docker run -it \
-e OPENAI_API_KEY=$OPENAI_API_KEY \
-v "$(pwd)":/app zeroxeli/readme-ai:latest \
readmeai -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

<!--
<br>

<details><summary><b><i>Manually Run</i></b></summary>
-->
<br>

***Using Conda***
```sh
conda activate readmeai
export OPENAI_API_KEY="YOUR_API_KEY"
python3 -m readmeai.cli.commands -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

<br>

***Using Poetry***
```sh
poetry shell
export OPENAI_API_KEY="YOUR_API_KEY"
poetry run python3 -m readmeai.cli.commands -o readme-ai.md -r https://github.com/eli64s/readme-ai
```

<br>

***Using Streamlit***

Use the app directly in your browser via Streamlit Community Cloud.

- [🛸 Take me to *readme-ai* on Streamlit!](https://readmeai.streamlit.app/)

</details>

---

### 🧪 Tests

Execute the test suite using the command below.

```sh
bash scripts/test.sh
```

---

## 🛠 Roadmap

- [X] Publish project as a Python library via PyPI for easy installation.
  - [*PyPI - readmeai*](https://pypi.org/project/readmeai/)
- [X] Make project available as a Docker image on Docker Hub.
  - [*Docker Hub - readme-ai*](https://hub.docker.com/repository/docker/zeroxeli/readme-ai/general)
- [X] Integrate and deploy app with Streamlit to make tool more widely accessible.
  - [*Streamlit Community Cloud - readmeai*](https://readmeai.streamlit.app/)
- [ ] Refactor our large language model engine to enable more robust README generation.
  - [ ] Explore [LangChain 🦜️🔗](https://python.langchain.com/docs/get_started/introduction) as an alternative to using the OpenAI API directly.
  - [ ] Explore [LlamaIndex 🦙](https://gpt-index.readthedocs.io/en/stable/index.html) framework and Retrieval augmented generation (RAG) paradigm.
- [ ] Add support for generating README files in any language (i.e. CN, ES, FR, JA, KO, RU).
- [ ] Design README output templates for a variety of use-cases (i.e. data, web-dev, minimal, etc.)
- [ ] Develop GitHub Actions script to automatically update the README file when new code is pushed.

---

## 📒 Changelog

[Changelog](https://github.com/eli64s/readme-ai/blob/main/CHANGELOG.md)

---

## 🤝 Contributing

Looking to contribute to *readme-ai*? Here is what you can do to help:

- 🐍 Look for opportunities to make the code more efficient and readable.
- 🤖 Exception handling and bug fixes are always welcome!
- 📝 Improve documentation and add more examples to the README.
- 🔡 Add support for generating README files in any language (i.e. CN, ES, FR, JA, KO, RU).
- 🎨 Create new templates for different use-cases (i.e. data, web-dev, minimal, etc.).
  - The README is constructed in sections, defined in the [config.toml] file.
  - Follow the existing format to get started.

[Contributing Guidelines](https://github.com/eli64s/readme-ai/blob/main/CONTRIBUTING.md)

---

## 📄 License

[MIT](https://github.com/eli64s/readme-ai/blob/main/LICENSE)

---

## 👏 Acknowledgments

*Badge Icons*
  - [Shields.io](https://shields.io/)
  - [Aveek-Saha/GitHub-Profile-Badges](https://github.com/Aveek-Saha/GitHub-Profile-Badges)
  - [Ileriayo/Markdown-Badges](https://github.com/Ileriayo/markdown-badges)
  - [tandpfun/skill-icons](https://github.com/tandpfun/skill-icons)


<p align="right">
  <a href="#top"><b>🔝 Return </b></a>
</p>

---
