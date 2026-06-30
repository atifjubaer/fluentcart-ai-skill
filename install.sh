#!/bin/bash
# Simple installation script for macOS/Linux (FluentCart Developer Skill)

DEST_DIR="$HOME/.gemini/config/skills/fluentcart-developer"
echo "Installing FluentCart Developer Skill globally for Antigravity/Gemini..."

# Create destination folder if it doesn't exist
mkdir -p "$DEST_DIR"

# Copy SKILL.md and references
cp SKILL.md "$DEST_DIR/SKILL.md"
if [ -d "references" ]; then
    mkdir -p "$DEST_DIR/references"
    cp -R references/* "$DEST_DIR/references/"
fi

echo "Global skill installed successfully!"

# Install project-specific configurations if path is specified
if [ ! -z "$1" ]; then
    PROJECT_PATH="$1"
    if [ -d "$PROJECT_PATH" ]; then
        echo "Installing project-specific rules to $PROJECT_PATH..."
        cp .cursorrules "$PROJECT_PATH/.cursorrules"
        cp CLAUDE.md "$PROJECT_PATH/CLAUDE.md"
        echo "Project rules installed successfully!"
    else
        echo "Warning: Project path '$PROJECT_PATH' does not exist."
    fi
fi
