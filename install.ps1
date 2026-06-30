# install.ps1
# Simple one-line installation script for Windows (FluentCart Developer Skill)
param (
    [string]$ProjectPath = ""
)

$destDir = "$env:USERPROFILE\.gemini\config\skills\fluentcart-developer"
Write-Host "Installing FluentCart Developer Skill globally for Antigravity/Gemini..." -ForegroundColor Cyan

# Create destination folder if it doesn't exist
if (!(Test-Path $destDir)) {
    New-Item -ItemType Directory -Path $destDir -Force | Out-Null
}

# Copy SKILL.md and references
Copy-Item -Path "SKILL.md" -Destination "$destDir\SKILL.md" -Force
if (Test-Path "references") {
    if (!(Test-Path "$destDir\references")) {
        New-Item -ItemType Directory -Path "$destDir\references" -Force | Out-Null
    }
    Copy-Item -Path "references\*" -Destination "$destDir\references\" -Recurse -Force
}

Write-Host "Global skill installed successfully!" -ForegroundColor Green

# Install project-specific configurations if path is specified
if ($ProjectPath -ne "") {
    if (Test-Path $ProjectPath) {
        Write-Host "Installing project-specific rules to $ProjectPath..." -ForegroundColor Cyan
        Copy-Item -Path ".cursorrules" -Destination "$ProjectPath\.cursorrules" -Force
        Copy-Item -Path "CLAUDE.md" -Destination "$ProjectPath\CLAUDE.md" -Force
        Write-Host "Project rules installed successfully!" -ForegroundColor Green
    } else {
        Write-Warning "Project path '$ProjectPath' does not exist."
    }
}
