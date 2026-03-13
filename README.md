<<<<<<< HEAD
<p align="center">
  <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/assets/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="docs/assets/logo-light.svg">
      <img height="100" alt="Endee" src="docs/assets/logo-dark.svg">
  </picture>
</p>

<p align="center">
    <b>High-performance open-source vector database for AI search, RAG, semantic search, and hybrid retrieval.</b>
</p>

<p align="center">
    <a href="./docs/getting-started.md"><img src="https://img.shields.io/badge/Quick_Start-Local_Setup-success?style=flat-square" alt="Quick Start"></a>
    <a href="https://docs.endee.io/quick-start"><img src="https://img.shields.io/badge/Docs-Quick_Start-success?style=flat-square" alt="Docs"></a>
    <a href="https://github.com/endee-io/endee/blob/master/LICENSE"><img src="https://img.shields.io/github/license/endee-io/endee?style=flat-square" alt="License"></a>
    <a href="https://discord.gg/5HFGqDZQE3"><img src="https://img.shields.io/badge/Discord-Join_Chat-5865F2?logo=discord&style=flat-square" alt="Discord"></a>
    <a href="https://endee.io/"><img src="https://img.shields.io/badge/Website-Endee-111111?style=flat-square" alt="Website"></a>
    <!-- <a href="https://endee.io/benchmarks"><img src="https://img.shields.io/badge/Benchmarks-Coming_Soon-1F8B4C?style=flat-square" alt="Benchmarks"></a> -->
    <!-- <a href="https://endee.io/cloud"><img src="https://img.shields.io/badge/Cloud-Coming_Soon-2496ED?style=flat-square" alt="Cloud"></a> -->
</p>

<p align="center">
<strong><a href="./docs/getting-started.md">Quick Start</a> • <a href="#why-endee">Why Endee</a> • <a href="#use-cases">Use Cases</a> • <a href="#features">Features</a> • <a href="#api-and-clients">API and Clients</a> • <a href="#docs-and-links">Docs</a> • <a href="#community-and-contact">Contact</a></strong>
</p>

# Endee: Open-Source Vector Database for AI Search

**Endee** is a high-performance open-source vector database built for AI search and retrieval workloads. It is designed for teams building **RAG pipelines**, **semantic search**, **hybrid search**, recommendation systems, and filtered vector retrieval APIs that need production-oriented performance and control.

Endee combines vector search with filtering, sparse retrieval support, backup workflows, and deployment flexibility across local builds and Docker-based environments. The project is implemented in C++ and optimized for modern CPU targets, including AVX2, AVX512, NEON, and SVE2.

If you want the fastest path to evaluate Endee locally, start with the [Getting Started guide](./docs/getting-started.md) or the hosted docs at [docs.endee.io](https://docs.endee.io/quick-start).

## Why Endee

- Built as a dedicated vector database for AI applications, search systems, and retrieval-heavy workloads.
- Supports dense vector retrieval plus sparse search capabilities for hybrid search use cases.
- Includes payload filtering for metadata-aware retrieval and application-specific query logic.
- Ships with operational features already documented in this repo, including backup flows and runtime observability.
- Offers flexible deployment paths: local scripts, manual builds, Docker images, and prebuilt registry images.

## Getting Started

The full installation, build, Docker, runtime, and authentication instructions are in [docs/getting-started.md](./docs/getting-started.md).

Fastest local path:

```bash
chmod +x ./install.sh ./run.sh
./install.sh --release --avx2
./run.sh
```

The server listens on port `8080`. For detailed setup paths, supported operating systems, CPU optimization flags, Docker usage, and authentication examples, use:

- [Getting Started](./docs/getting-started.md)
- [Hosted Quick Start Docs](https://docs.endee.io/quick-start)

## Use Cases

### RAG and AI Retrieval

Use Endee as the retrieval layer for question answering, chat assistants, copilots, and other RAG applications that need fast vector search with metadata-aware filtering.

### Agentic AI and AI Agent Memory

Use Endee as the long-term memory and context retrieval layer for AI agents built with frameworks like LangChain, CrewAI, AutoGen, and LlamaIndex. Store and retrieve past observations, tool outputs, conversation history, and domain knowledge mid-execution with low-latency filtered vector search, so your autonomous agents get the right context without stalling their reasoning loop.

### Semantic Search

Build semantic search experiences for documents, products, support content, and knowledge bases using vector similarity search instead of exact keyword-only matching.

### Hybrid Search

Combine dense retrieval, sparse vectors, and filtering to improve relevance for search workflows where both semantic understanding and term-level precision matter.

### Recommendations and Matching

Support recommendation, similarity matching, and nearest-neighbor retrieval workflows across text, embeddings, and other high-dimensional representations.

## Features

- **Vector search** for AI retrieval and semantic similarity workloads.
- **Hybrid retrieval support** with sparse vector capabilities documented in [docs/sparse.md](./docs/sparse.md).
- **Payload filtering** for structured retrieval logic documented in [docs/filter.md](./docs/filter.md).
- **Backup APIs and flows** documented in [docs/backup-system.md](./docs/backup-system.md).
- **Operational logging and instrumentation** documented in [docs/logs.md](./docs/logs.md) and [docs/mdbx-instrumentation.md](./docs/mdbx-instrumentation.md).
- **CPU-targeted builds** for AVX2, AVX512, NEON, and SVE2 deployments.
- **Docker deployment options** for local and server environments.

## API and Clients

Endee exposes an HTTP API for managing indexes and serving retrieval workloads. The current repo documentation and examples focus on running the server directly and calling its API endpoints.

Current developer entry points:

- [Getting Started](./docs/getting-started.md) for local build and run flows
- [Hosted Docs](https://docs.endee.io/quick-start) for product documentation
- [Release Notes 1.0.0](https://github.com/endee-io/endee/releases/tag/1.0.0) for recent platform changes

## Docs and Links

- [Getting Started](./docs/getting-started.md)
- [Hosted Documentation](https://docs.endee.io/quick-start)
- [Release Notes](https://github.com/endee-io/endee/releases/tag/1.0.0)
- [Sparse Search](./docs/sparse.md)
- [Filtering](./docs/filter.md)
- [Backups](./docs/backup-system.md)

## Community and Contact

- Join the community on [Discord](https://discord.gg/5HFGqDZQE3)
- Visit the website at [endee.io](https://endee.io/)
- For trademark or branding permissions, contact [enterprise@endee.io](mailto:enterprise@endee.io)

## Contributing

We welcome contributions from the community to help make vector search faster and more accessible for everyone.

- Submit pull requests for fixes, features, and improvements
- Report bugs or performance issues through GitHub issues
- Propose enhancements for search quality, performance, and deployment workflows

## License

Endee is open source software licensed under the **Apache License 2.0**. See the [LICENSE](./LICENSE) file for full terms.

## Trademark and Branding

“Endee” and the Endee logo are trademarks of Endee Labs.

The Apache License 2.0 does not grant permission to use the Endee name, logos, or branding in a way that suggests endorsement or affiliation.

If you offer a hosted or managed service based on this software, you must use your own branding and avoid implying it is an official Endee service.

## Third-Party Software

This project includes or depends on third-party software components licensed under their respective open-source licenses. Use of those components is governed by their own license terms.
=======
🤖 AI Error Helper
Stop Googling Errors. Let AI Understand Them.

For most people AI means Artificial Intelligence.
For me, AI also means Aditya’s Intelligence.

This project reflects my curiosity about how intelligent systems can assist developers in solving everyday programming problems. Instead of manually searching through forums and documentation, I wanted to explore how AI could understand programming errors and suggest solutions instantly.

🧑‍💻 The Problem

Every developer has experienced this moment.

You write some code.
You run it confidently.

Then the terminal responds with something like:

IndexError: list index out of range

You stare at it.

You search it on Google.

You open 10 StackOverflow tabs.

And finally… you realize the mistake was tiny.

Maybe an index.
Maybe a missing module.
Maybe a simple syntax error.

This project was built to explore a simple idea:

What if an AI system could instantly understand your error and suggest the most relevant solution?

💡 The Idea

AI Error Helper is a small semantic search tool that helps developers find solutions to programming errors.

Instead of matching exact keywords, the system understands the meaning of the error using vector embeddings.

So even if the user writes:

python list index problem

The system can still identify:

IndexError: list index out of range

and return the correct solution.

⚙️ How It Works

The system works in three main steps.

1️⃣ Error Knowledge Base

A dataset of 100+ common programming errors and their solutions is stored.

Example entry:

ZeroDivisionError: division by zero | Solution: Check the denominator before dividing.

2️⃣ Convert Errors Into Vectors

Each error is transformed into an embedding using Sentence Transformers.

These embeddings represent the meaning of the error.

3️⃣ Semantic Similarity Search

When the user enters an error like:

cannot divide by zero python

The system compares the query embedding with all stored embeddings.

The closest match is returned instantly.

🖥 Example Interaction
Input:
cannot find module pandas  
Output:  
Error:  
ModuleNotFoundError: no module named pandas

Solution:  
Install pandas using pip install pandas

📸 Project Screenshot

![App Screenshot](images/Screenshot%202026-03-13%20132737.png)

Record a 10-second screen recording showing:

1️⃣ Entering an error  
2️⃣ Clicking search  
3️⃣ Solution appearing

🏗 Tech Stack

**Backend**
- Python
- Flask
- AI / Semantic Search
- Sentence Transformers
- NumPy

**Frontend**
- HTML
- CSS

📂 Project Structure
ai-error-helper
│
├── dataset
│ └── errors.txt
│
├── templates
│ └── index.html
│
├── images
│ └── Screenshot 2026-03-13 132737.png
│
├── ingest.py
├── app.py
├── requirements.txt
└── vectors.npy

🚀 Running the Project

1️⃣ Install Dependencies
Run the following command in your terminal:

pip install -r requirements.txt

2️⃣ Generate Embeddings
Generate vector embeddings for all errors:

python ingest.py

3️⃣ Start the Server
Start the Flask server:

python app.py

4️⃣ Open the Application
Open your browser and go to:
http://127.0.0.1:5000

Paste a programming error and the AI will suggest a solution.

🎯 Project Context

This project explores how vector embeddings and semantic search can be used to build intelligent developer tools.

The idea aligns with technologies developed by Endee, which focuses on building AI-powered systems using vector databases and semantic search.

🔮 Future Improvements

Possible next steps:

Larger dataset of programming errors

Show top 3 similar solutions

StackOverflow answer integration

LLM explanation for beginners

Chat-style debugging interface

👨‍💻 Author
Aditya Gautam
>>>>>>> myproject/main
