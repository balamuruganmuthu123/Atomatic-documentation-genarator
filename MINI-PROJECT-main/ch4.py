# ── Chapter 4: System Design ─────────────────────────────────
heading1("CHAPTER 4")
heading1("SYSTEM DESIGN")

heading2("4.1 System Architecture")
body("The system architecture of the AI Based Automatic Documentation Generator is composed of five primary layers that work in concert to deliver automated academic documentation. The Presentation Layer consists of the Next.js 16 App Router frontend which provides the user interface for repository selection, generation progress tracking, and PDF download. The Authentication Layer is implemented using Clerk, which manages GitHub OAuth tokens and protects all API routes via middleware. The Business Logic Layer encompasses the GitHubClient, CodeAnalyzer, EnhancedCodeAnalyzer, and ModelRouter classes that perform the core ingestion, analysis, and AI generation tasks. The Integration Layer manages communication with three external AI providers — Google Gemini via the Generative AI SDK, OpenAI via the OpenAI Node.js client, and Ollama via an OpenAI-compatible local endpoint. The Output Layer contains the DiagramRenderer, PDFGenerator, and marked.js renderer that assemble and export the final document.")
body("Data flows unidirectionally through the system from user input to PDF output. The user's GitHub OAuth token flows from Clerk into the GitHubClient. The fetched source files flow from the client into the EnhancedCodeAnalyzer. The extracted code context flows as structured prompt data into the ModelRouter. The generated chapter texts and diagram URLs flow into the document assembler. The assembled Markdown flows into the HTML renderer, which feeds Puppeteer for final PDF generation and download.")

figure_placeholder("4.1", "System Architecture Diagram — Five-Layer Architecture of the AI Documentation Generator")

heading2("4.2 Flow Diagram")
body("The flow diagram illustrates the complete end-to-end workflow of the AI Based Automatic Documentation Generator, from user sign-in to PDF download. The process begins when the user authenticates via GitHub OAuth. The system retrieves the repository file tree recursively, filters irrelevant files, and passes the source files through the deep code analysis pipeline. The assembled context drives AI generation for each of the eight report chapters. Generated Mermaid.js diagram code is encoded and embedded as SVG URLs. All content is assembled into a structured Markdown document, rendered to HTML, and exported as a Puppeteer-generated A4 PDF.")

add_table(
    ["Step", "Process", "Component Responsible"],
    [
        ["1", "User signs in via GitHub OAuth", "Clerk Authentication"],
        ["2", "GitHub repositories listed", "GitHubClient.getUserRepositories()"],
        ["3", "User selects repository", "Next.js Frontend Dashboard"],
        ["4", "Files fetched recursively (max 200)", "GitHubClient.getAllFiles()"],
        ["5", "Code structure analyzed (AST, roles, schemas)", "EnhancedCodeAnalyzer"],
        ["6", "12 documentation tasks routed to AI models", "ModelRouter.generate()"],
        ["7", "Gemini 1.5 Pro generates chapter content", "Google Generative AI SDK"],
        ["8", "Fallback to OpenAI GPT-4o if Gemini fails", "OpenAI Node.js Client"],
        ["9", "Final fallback to local Ollama", "LocalOpenAI (Ollama endpoint)"],
        ["10", "4 Mermaid.js diagrams generated and encoded", "DiagramRenderer"],
        ["11", "All chapters assembled into Markdown", "AcademicProjectDocumentationGenerator"],
        ["12", "Markdown rendered to academic HTML", "marked.js + buildAcademicRenderer()"],
        ["13", "HTML loaded in headless Chrome, PDF rendered", "Puppeteer PDFGenerator"],
        ["14", "A4 PDF downloaded by user", "Next.js API Route /api/generate"],
    ],
    col_widths=[1.5, 7, 5]
)

figure_placeholder("4.2", "Flow Diagram — End-to-End Documentation Generation Workflow")

heading2("4.3 Use Case Diagram")
body("The use case diagram identifies the primary actors and their interactions with the AI Based Automatic Documentation Generator system. Two actors are identified: the Student/Developer (primary actor) who interacts with the web interface, and the AI System (secondary actor) representing the collection of AI providers — Gemini, OpenAI, and Ollama — that generate documentation content.")
add_table(
    ["Actor", "Use Case", "Description"],
    [
        ["Student / Developer", "Sign In with GitHub", "Authenticate using GitHub OAuth via Clerk"],
        ["Student / Developer", "Select Repository", "Browse and select a target GitHub repository"],
        ["Student / Developer", "Trigger Documentation", "Initiate the documentation generation pipeline"],
        ["Student / Developer", "Preview Document", "View generated chapters in the browser interface"],
        ["Student / Developer", "Download PDF", "Export the final A4 academic PDF"],
        ["AI System (Gemini)", "Generate Chapter Text", "Produce academic prose for each of the 8 chapters"],
        ["AI System (Gemini)", "Generate Diagram Code", "Produce Mermaid.js syntax for 4 diagram types"],
        ["AI System (OpenAI)", "Fallback Generation", "Generate content when Gemini is unavailable"],
        ["AI System (Ollama)", "Offline Generation", "Provide local AI inference as last-resort fallback"],
        ["GitHub API", "Fetch Repository Files", "Supply source code files via Octokit REST"],
    ],
    col_widths=[3.5, 4, 6]
)
figure_placeholder("4.3", "Use Case Diagram — Actors and Interactions in the Documentation System")

heading2("4.4 Sequence Diagram")
body("The sequence diagram describes the chronological message flow between system components during a single documentation generation request. The interaction begins with the user submitting a repository URL through the frontend, which calls the Next.js API route. The API route verifies the Clerk session token before proceeding. The CodeAnalyzer is invoked first to fetch and analyze the repository. The ModelRouter then generates each chapter sequentially. The DiagramRenderer encodes the diagrams. The PDFGenerator renders the final document and returns the binary PDF buffer to the API route, which streams it to the browser as a downloadable file.")

add_table(
    ["Sequence", "From", "To", "Message"],
    [
        ["1", "User Browser", "Next.js Frontend", "Submit repository URL"],
        ["2", "Next.js Frontend", "API Route /api/generate", "POST request with repo URL"],
        ["3", "API Route", "Clerk Middleware", "Verify session token"],
        ["4", "Clerk Middleware", "API Route", "Return authenticated user + GitHub token"],
        ["5", "API Route", "GitHubClient", "getAllFiles(owner, repo)"],
        ["6", "GitHubClient", "GitHub REST API", "Octokit repos.getContent() recursive calls"],
        ["7", "GitHub REST API", "GitHubClient", "Return file tree and file contents"],
        ["8", "GitHubClient", "EnhancedCodeAnalyzer", "Pass fetched CodeFile[] array"],
        ["9", "EnhancedCodeAnalyzer", "API Route", "Return RepositoryAnalysis object"],
        ["10", "API Route", "ModelRouter", "generate('chapter-introduction', prompt)"],
        ["11", "ModelRouter", "Gemini 1.5 Pro", "generateContent(prompt, config)"],
        ["12", "Gemini 1.5 Pro", "ModelRouter", "Return generated chapter text"],
        ["13", "ModelRouter", "API Route", "Return chapter string (repeat for all 8 chapters)"],
        ["14", "API Route", "DiagramRenderer", "render(mermaidCode, caption, id)"],
        ["15", "DiagramRenderer", "API Route", "Return SVG URL strings"],
        ["16", "API Route", "PDFGenerator", "generatePDFFromMarkdown(markdown)"],
        ["17", "PDFGenerator", "Puppeteer", "Launch headless Chrome, load HTML"],
        ["18", "Puppeteer", "mermaid.ink CDN", "Fetch diagram SVG images"],
        ["19", "Puppeteer", "PDFGenerator", "Return PDF buffer"],
        ["20", "PDFGenerator", "User Browser", "Stream PDF as downloadable file"],
    ],
    col_widths=[1.5, 3.5, 3.5, 5.5]
)
figure_placeholder("4.4", "Sequence Diagram — Message Flow During Documentation Generation")

heading2("4.5 Activity Diagram")
body("The activity diagram represents the complete decision-making workflow within the system. The process begins at the user login activity. Upon successful authentication, the user selects a repository, triggering the file ingestion activity. A decision node checks whether the repository is accessible — if not, an error is displayed and the user is prompted to re-enter the URL. If accessible, the code analysis activity runs. After analysis, the system enters the AI generation loop, iterating over twelve task types. For each task, a decision checks Gemini availability. If Gemini is rate-limited, a fallback decision checks for OpenAI availability. If OpenAI is also unavailable, the task routes to Ollama. After all tasks complete, diagram generation runs, followed by document assembly, HTML rendering, and PDF export. The process ends with the user receiving the downloadable PDF.")
figure_placeholder("4.5", "Activity Diagram — Decision Flow and Activity States")

heading2("4.6 Data Flow Diagram")
heading3("4.6.1 Level 0 DFD (Context Diagram)")
body("The Level 0 Data Flow Diagram shows the system as a single process interacting with four external entities: the Student/Developer who provides the GitHub repository URL and receives the PDF report; the GitHub API which supplies source code files and repository metadata; the AI Providers (Gemini, OpenAI, Ollama) which receive generation prompts and return chapter text; and the mermaid.ink CDN which renders diagram SVGs for PDF embedding.")
figure_placeholder("4.6", "Level 0 DFD — Context Diagram Showing External Entities")

heading3("4.6.2 Level 1 DFD (System Decomposition)")
add_table(
    ["Process ID", "Process Name", "Input Data", "Output Data"],
    [
        ["P1", "Authentication", "GitHub OAuth code", "Access token + User session"],
        ["P2", "Repository Ingestion", "Repository URL + Access token", "CodeFile[] array"],
        ["P3", "Code Analysis", "CodeFile[] array", "RepositoryAnalysis object"],
        ["P4", "AI Generation", "RepositoryAnalysis + prompts", "Chapter texts + Mermaid code"],
        ["P5", "Diagram Rendering", "Mermaid.js syntax strings", "SVG URL strings"],
        ["P6", "Document Assembly", "Chapter texts + SVG URLs", "Full Markdown document"],
        ["P7", "HTML Rendering", "Markdown document", "Styled HTML string"],
        ["P8", "PDF Export", "Styled HTML string", "A4 PDF binary buffer"],
    ],
    col_widths=[2, 4, 5, 5]
)
add_page_break()
