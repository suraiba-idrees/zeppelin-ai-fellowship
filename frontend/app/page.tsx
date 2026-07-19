"use client";

import { FormEvent, useState } from "react";

export default function Home() {
  const [resumeFile, setResumeFile] = useState<File | null>(null);
  const [jobDescription, setJobDescription] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    if (!resumeFile || !jobDescription.trim()) {
      alert("Please fill out all the analysis parameters.");
      return;
    }

    setIsLoading(true);

    // Backend/API integration will be added in Chunk 2.
    console.log("Resume:", resumeFile);
    console.log("Job Description:", jobDescription);

    setTimeout(() => {
      setIsLoading(false);
    }, 1000);
  }

  return (
    <div className="app-viewport-wrapper">
      <header className="app-global-navbar">
        <div className="navbar-container">
          <div className="brand-identity-block">
            <span className="brand-text-label">
              Zeppelin <span className="logo-accent-node">Labs</span>
            </span>
          </div>

          <div className="navbar-utility-status">
            <span className="pulse-indicator-node"></span>
            <span className="status-framework-tag">
             {/* Resume Feedback Engine v2.0 */}
            </span>
          </div>
        </div>
      </header>

      <div className="viewport-workspace-flow">
        <div className="workspace-bounded-container">
          <div className="app-marketing-heading">
            <div className="badge-status-pill">
              Powered by Gemini & Claude
            </div>

            <h1>
              Optimize Your Resume For{" "}
              <span className="chrome-indigo-gradient">
                ATS Alignment
              </span>
            </h1>

            <p>
              Scan your profile against target market framework metrics,
              extract missing keyword parameters, and build clear alignment
              scores instantly.
            </p>
          </div>

          <main className="product-interactive-canvas">
            <form id="screenerForm" onSubmit={handleSubmit}>
              <div className="canvas-workflow-section">
                <div className="workflow-header-label">
                  <span className="workflow-step-badge">01</span>
                  <label htmlFor="resumeFile">
                    Ingest Candidate Profile
                  </label>
                </div>

                <div className="mega-dropzone-interactive-container">
                  <input
                    type="file"
                    id="resumeFile"
                    accept=".pdf,.doc,.docx"
                    onChange={(event) => {
                      const file = event.target.files?.[0] || null;
                      setResumeFile(file);
                    }}
                    required
                  />

                  <div className="dropzone-graphic-render-view">
                    <div className="vector-icon-circle-shell">
                      <svg
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                      >
                        <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
                        <polyline points="14 2 14 8 20 8" />
                        <line x1="12" y1="18" x2="12" y2="12" />
                        <polyline points="9 15 12 12 15 15" />
                      </svg>
                    </div>

                    <h3>
                      {resumeFile
                        ? resumeFile.name
                        : "Drag & drop your resume file here"}
                    </h3>

                    <p>
                      or{" "}
                      <span className="browse-action-link">
                        browse from local disk
                      </span>
                    </p>

                    <span className="file-specification-metadata">
                      Supports PDF and DOCX documents up to 10MB
                    </span>
                  </div>
                </div>
              </div>

              <div className="canvas-workflow-section">
                <div className="workflow-header-label">
                  <span className="workflow-step-badge">02</span>
                  <label htmlFor="jobDescription">
                    Target Framework / Job Description
                  </label>
                </div>

                <div className="textarea-input-wrapper-shell">
                  <textarea
                    id="jobDescription"
                    value={jobDescription}
                    onChange={(event) =>
                      setJobDescription(event.target.value)
                    }
                    placeholder="Paste the complete job description, operational guidelines, or technical key rules from the target company layout here..."
                    required
                  />
                </div>
              </div>

              <div className="canvas-action-footer-panel">
                <button
                  type="submit"
                  id="submitBtn"
                  className="premium-action-trigger-btn"
                  disabled={isLoading}
                >
                  <span>
                    {isLoading
                      ? "Processing Core Parameters..."
                      : "Scan & Generate AI Matrix Analysis"}
                  </span>

                  {!isLoading && (
                    <svg
                      className="chevron-arrow-icon"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    >
                      <line x1="5" y1="12" x2="19" y2="12" />
                      <polyline points="12 5 19 12 12 19" />
                    </svg>
                  )}
                </button>
              </div>
            </form>
          </main>

          <section id="resultPanel" className="hidden">
            <div id="analysisContent"></div>
          </section>
        </div>
      </div>
    </div>
  );
}