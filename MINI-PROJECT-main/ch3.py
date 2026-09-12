# ── Chapter 3: Methodology ───────────────────────────────────
heading1("CHAPTER 3")
heading1("METHODOLOGY")

heading2("3.1 Methodology Overview")
body("The AI Based Automatic Documentation Generator follows a systematic eight-stage pipeline that transforms a raw GitHub repository URL into a fully formatted academic PDF report. Each stage is designed to be modular, independently testable, and fault-tolerant, ensuring reliable output even when individual components encounter errors. The overall pipeline is orchestrated by the AcademicProjectDocumentationGenerator class, which coordinates all sub-systems from ingestion through export.")

heading2("3.2 Stage-wise Methodology")
heading3("Stage 1 — User Authentication and Repository Selection")
body("The user accesses the web application and signs in using GitHub OAuth facilitated by Clerk authentication. Upon successful authentication, a GitHub personal access token is obtained, which is used to authorize all subsequent API calls via the Octokit REST client. The user then selects a target GitHub repository from their accessible repository list displayed on the dashboard. This secure authentication layer ensures that private repository access is properly authorized and that all API rate limits are managed per authenticated user.")

heading3("Stage 2 — Repository Ingestion via GitHub API")
body("The GitHubClient class performs recursive traversal of the selected repository's file tree using the Octokit repos.getContent API endpoint. The traversal fetches up to 200 source files while automatically skipping irrelevant directories including .git, node_modules, .next, dist, build, coverage, .vscode, and public. Files larger than 500 KB are excluded to prevent memory overload. Additionally, the client attempts to fetch critical configuration files that may exist deep in the tree including schema.prisma, docker-compose.yml, .env.example, and Dockerfile, ensuring these important architectural artifacts are captured for analysis.")

heading3("Stage 3 — Deep Code Analysis")
body("The EnhancedCodeAnalyzer processes all fetched source files through multiple specialized analysis passes. The extractCodeStructure method identifies class definitions, exported functions, and module boundaries. The detectArchitecture method examines package dependencies and directory structures to identify the primary framework in use. The extractAPIEndpoints method scans route definitions across Express, Next.js API routes, FastAPI, and Django URL patterns. The extractDatabaseInfo method identifies ORM usage patterns and table definitions. The extractPrismaSchema method parses Prisma schema files to extract model definitions with their fields and relationships. The classifyFileRoles method assigns each file a semantic role such as controller, service, model, utility, or configuration. Finally, extractDeepCodeSummary produces a structured per-file behavioral summary that is injected into AI generation prompts.")

heading3("Stage 4 — Multi-Model AI Chapter Generation")
body("The ModelRouter class implements an intelligent multi-provider AI routing strategy. Twelve distinct DocTask types are defined, each configured with a specific AI model, provider, temperature setting, and maximum output token limit. All tasks route to Google Gemini 1.5 Pro as the primary provider using the free tier that allows fifteen requests per minute. Temperature is tuned per task type: code-analysis and diagram-generation tasks use 0.2 for high precision, implementation and design chapters use 0.5 for balanced accuracy, and introduction, literature, and conclusion chapters use 0.7 for fluent academic prose. If Gemini fails due to rate limits or API errors, the router automatically retries up to three times before falling back to OpenAI GPT-4o if an API key is configured, and finally to a local Ollama instance as the last resort.")

heading3("Stage 5 — Mermaid.js Diagram Generation")
body("The DiagramRenderer class generates four standard academic diagrams by first prompting the ModelRouter to produce valid Mermaid.js syntax for each diagram type. The system architecture diagram illustrates the high-level component layout. The component diagram shows internal module interactions. The API sequence diagram depicts the request-response flow for the primary documentation generation endpoint. The entity-relationship diagram defines data models used in the system. Each Mermaid.js code string is serialized to JSON, base64url-encoded, and appended to the mermaid.ink public SVG rendering endpoint URL, producing embeddable image URLs that Puppeteer loads during PDF generation via networkidle0 waiting.")

heading3("Stage 6 — Document Assembly")
body("The AcademicProjectDocumentationGenerator assembles all AI-generated chapter texts, diagram URLs, front matter sections, and reference lists into a single structured Markdown document. Page-break markers are inserted between chapters. A dynamically generated Table of Contents with section numbers and page references is injected after the abstract. Code snippets extracted from the actual repository are embedded in fenced code blocks within the implementation chapter to ensure technical accuracy and specificity.")

heading3("Stage 7 — Markdown to HTML Rendering")
body("The custom buildAcademicRenderer function extends the marked.js Renderer class to map each Markdown element to a semantically styled HTML element. Heading level one is rendered as a centered, uppercase chapter title with a bottom border. Heading level two becomes an underlined section heading. Heading level three becomes a bold subsection. Body paragraphs receive justified text alignment. Tables are styled with bordered cells, header row shading, and zebra-striped rows. Code blocks use Courier New monospace font with a left border accent. Horizontal rule markers are converted to page-break div elements.")

heading3("Stage 8 — PDF Export via Puppeteer")
body("The PDFGenerator class launches a headless Chromium browser instance using Puppeteer with sandboxing disabled for server compatibility. The fully styled HTML document is loaded into a browser page using setContent with a networkidle0 wait condition to ensure all mermaid.ink diagram images have fully loaded. An additional two-second wait ensures Google Fonts have rendered. The page.pdf API is then called with A4 format, academic margins of 25mm top and bottom and 30mm left and 20mm right, and custom header and footer templates displaying the repository name and page numbers in nine-point Times New Roman.")

heading2("3.3 System Requirements")
heading3("3.3.1 Hardware Requirements")
add_table(
    ["Component", "Minimum Specification", "Recommended Specification"],
    [
        ["Processor", "Intel Core i5 (8th Gen)", "Intel Core i7 (10th Gen) or above"],
        ["RAM", "8 GB", "16 GB or above"],
        ["Storage", "256 GB SSD", "512 GB SSD"],
        ["Network", "Broadband Internet (10 Mbps)", "Broadband Internet (50 Mbps)"],
        ["GPU", "Not required", "Not required (cloud-based AI)"],
        ["Display", "1366 x 768 resolution", "1920 x 1080 resolution"],
    ],
    col_widths=[4, 5, 5]
)

heading3("3.3.2 Software Requirements")
add_table(
    ["Component", "Technology / Tool", "Version"],
    [
        ["Operating System", "Windows 10+ / Ubuntu 20.04+ / macOS 12+", "—"],
        ["Runtime Environment", "Node.js", "18.0 or above"],
        ["Web Framework", "Next.js (App Router)", "16.1.6"],
        ["Authentication", "Clerk", "6.37.3"],
        ["AI Model — Primary", "Google Gemini 1.5 Pro", "Via @google/generative-ai 0.24.1"],
        ["AI Model — Secondary", "OpenAI GPT-4o", "Via openai 6.33.0"],
        ["AI Model — Fallback", "Ollama (Local, gemma2)", "Latest"],
        ["GitHub Client", "Octokit REST", "22.0.1"],
        ["AST Parser", "@babel/parser + @babel/traverse", "7.29.0"],
        ["Markdown Renderer", "marked.js", "18.0.0"],
        ["Diagram Engine", "Mermaid.js + mermaid.ink", "11.12.3"],
        ["PDF Renderer", "Puppeteer", "24.37.2"],
        ["Language", "TypeScript", "5.x"],
        ["Package Manager", "npm", "10.x"],
        ["IDE", "Visual Studio Code", "Latest"],
    ],
    col_widths=[4, 7, 3.5]
)
add_page_break()
