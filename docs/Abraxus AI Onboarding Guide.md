# Abraxus AI Onboarding Guide

This document serves as a comprehensive guide for new contributors and users to get started with the Abraxus AI project. It covers everything from setting up your development environment to understanding the project's structure and how to contribute.

## For New Developers

### Setting Up Your Environment

1.  **Prerequisites:** Ensure you have Git, Node.js (LTS version recommended), and Python 3.8+ installed on your system.
2.  **Clone the Repository:** Begin by cloning the Abraxus AI GitHub repository to your local machine:
    ```bash
    git clone https://github.com/your-username/Abraxus-AI.git
    cd Abraxus-AI
    ```
3.  **Install Python Dependencies:** Navigate to the root directory of the cloned repository and install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Install JavaScript Dependencies (if applicable):** If the project incorporates a frontend or specific JavaScript tools, install their dependencies using npm or yarn:
    ```bash
    # npm install
    # or
    # yarn install
    ```
5.  **Configure API Keys:** The Abraxus AI relies on various external APIs. Open `core/config/agx_kernel.json` and replace the placeholder API keys with your actual credentials. **Do not commit your actual API keys to version control.** Consider using environment variables for production deployments.

### Understanding the Project Structure

Familiarize yourself with the modular layout of the repository:

*   `/core/`: This directory is the heart of the project, containing all core logic, scripts (both JavaScript and Python), and configuration files. It is further divided into `config/` for JSON configurations and `scripts/` for executable code.
*   `/knowledge/`: This is the repository for the AI's knowledge base. It includes `pdfs/` for original PDF documents, `txts/` for raw text files, and `extracted_text/` for text extracted from PDFs or other sources, optimized for semantic search and RAG (Retrieval-Augmented Generation).
*   `/docs/`: This directory holds all project documentation, including the vision, manifesto, this onboarding guide, and reference materials. It is crucial for understanding the project's philosophy and operational guidelines.
*   `/archive/`: This folder is designated for prototype or legacy code that is no longer actively maintained but is kept for historical reference or potential future use. It helps keep the main codebase clean while preserving valuable development history.
*   `/tests/`: This directory is reserved for future testing scripts and frameworks. As the project evolves, comprehensive testing will be essential to ensure stability and functionality.

### Contribution Guidelines

We welcome and encourage contributions from the community! To ensure a smooth collaborative process, please adhere to the following guidelines:

*   **Code Style:** Follow the established code style for both Python and JavaScript files. (Further details will be provided in `docs/CONTRIBUTING.md`).
*   **Branching Strategy:** Use a feature-branch workflow. Create a new branch for each new feature or bug fix.
*   **Commit Messages:** Write clear, concise, and descriptive commit messages.
*   **Pull Requests:** Submit pull requests to the `main` branch. Ensure your code is well-tested and documented.
*   **Issue Tracking:** Report bugs and suggest features using the GitHub Issues tracker.

## For New Users

While the Abraxus AI is primarily a development project, future releases will include user-friendly interfaces. For now, users interested in interacting with the AI will primarily do so through command-line interfaces or specific API endpoints. Detailed instructions for user interaction will be provided as these features are developed.

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository. We will do our best to provide timely support.

