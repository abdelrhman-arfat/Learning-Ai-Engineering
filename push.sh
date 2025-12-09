#!/bin/bash

# ===============================================
# Git Commit & Push Script with Colors
# ===============================================

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Header
echo -e "${BLUE}==============================${NC}"
echo -e "${BLUE}  Git Auto Commit & Push  ${NC}"
echo -e "${BLUE}==============================${NC}"

# Read commit message
read -p "Enter commit message: " message

# Check if message is empty
if [ -z "$message" ]; then
    echo -e "${RED}Error: Commit message cannot be empty!${NC}"
    exit 1
fi

# Stage changes
echo -e "${YELLOW}Adding changes...${NC}"
git add .

# Commit
echo -e "${YELLOW}Committing...${NC}"
git commit -m "$message"

# Push
echo -e "${YELLOW}Pushing to remote...${NC}"
git push

# Success message
echo -e "${GREEN}✅ Successfully pushed changes with message: '$message'${NC}"
