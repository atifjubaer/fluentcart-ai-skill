#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const os = require('os');

// Helper to copy directory recursively
function copyDir(src, dest) {
    fs.mkdirSync(dest, { recursive: true });
    let entries = fs.readdirSync(src, { withFileTypes: true });

    for (let entry of entries) {
        let srcPath = path.join(src, entry.name);
        let destPath = path.join(dest, entry.name);

        if (entry.isDirectory()) {
            copyDir(srcPath, destPath);
        } else {
            fs.copyFileSync(srcPath, destPath);
        }
    }
}

const args = process.argv.slice(2);
const command = args[0] || 'init';

if (command === 'help' || command === '--help' || command === '-h') {
    console.log(`
FluentCart AI Developer Skill CLI (by Fastrsoft)

Usage:
  npx fluentcart-ai-skill init      Install skill globally and initialize project rules
  npx fluentcart-ai-skill global    Install global Antigravity skill only
  npx fluentcart-ai-skill project   Initialize Cursor and Claude rules in current directory
    `);
    process.exit(0);
}

const homeDir = os.homedir();
const globalSkillDir = path.join(homeDir, '.gemini', 'config', 'skills', 'fluentcart-developer');
const localSkillSrc = path.join(__dirname, '..'); // package root

// Global install function
function installGlobal() {
    console.log('Installing FluentCart Developer Skill globally for Antigravity...');
    try {
        fs.mkdirSync(globalSkillDir, { recursive: true });
        fs.copyFileSync(path.join(localSkillSrc, 'SKILL.md'), path.join(globalSkillDir, 'SKILL.md'));
        
        const refSrc = path.join(localSkillSrc, 'references');
        const refDest = path.join(globalSkillDir, 'references');
        if (fs.existsSync(refSrc)) {
            copyDir(refSrc, refDest);
        }
        console.log('✓ Global skill installed successfully!');
    } catch (err) {
        console.error('Error installing global skill:', err.message);
    }
}

// Project install function
function installProject() {
    console.log('Initializing project-specific rules in the current directory...');
    try {
        const cwd = process.cwd();
        fs.copyFileSync(path.join(localSkillSrc, '.cursorrules'), path.join(cwd, '.cursorrules'));
        fs.copyFileSync(path.join(localSkillSrc, 'CLAUDE.md'), path.join(cwd, 'CLAUDE.md'));
        fs.copyFileSync(path.join(localSkillSrc, 'fluentcart-rules.md'), path.join(cwd, 'fluentcart-rules.md'));
        console.log('✓ Created .cursorrules, CLAUDE.md, and fluentcart-rules.md in the current directory!');
    } catch (err) {
        console.error('Error installing project rules:', err.message);
    }
}

if (command === 'init') {
    installGlobal();
    installProject();
    console.log('\nFluentCart AI Skill is ready to use! 🚀');
} else if (command === 'global') {
    installGlobal();
} else if (command === 'project') {
    installProject();
} else {
    console.log(`Unknown command: ${command}. Run with --help for usage info.`);
}
