#!/bin/bash
# Quick Start Script — Intelligence Synthesis Engine
# Usage: ./quickstart.sh [--input <path>] [--output-dir <dir>]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEST_INPUT="${SCRIPT_DIR}/test_input_wiki.md"
OUTPUT_DIR="${SCRIPT_DIR}/output"

show_usage() {
    echo "Intelligence Synthesis Engine — Quick Start Script"
    echo ""
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --input <path>   Input wiki page (default: test_input_wiki.md)"
    echo "  --output-dir <d> Output directory (creates if doesn't exist)"
    echo "  --help           Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0                           # Run with test input (demo mode)"
    echo "  $0 --input ~/projects/wiki/trusted-shops.md"
    echo "  $0 --output-dir ~/portfolio/intel-briefings"
    echo ""
}

run_demo() {
    echo "═══════════════════════════════════════════════════════════"
    echo "🧠 Intelligence Synthesis Engine — Dry-Run Demo Mode"
    echo "═══════════════════════════════════════════════════════════"
    echo ""
    
    # Verify test input exists
    if [ ! -f "$TEST_INPUT" ]; then
        echo "❌ Error: Test input not found at $TEST_INPUT"
        exit 1
    fi
    
    # Create output directory
    mkdir -p "$OUTPUT_DIR"
    echo "[SETUP] Created output directory: $OUTPUT_DIR"
    
    # Run the engine
    echo ""
    echo "[RUNNING] Executing three-stage orchestration pipeline..."
    echo ""
    python3 "${SCRIPT_DIR}/run_intelligence_engine.py" \
        --input "$TEST_INPUT" \
        --output-dir "$OUTPUT_DIR" || exit 1
    
    echo ""
    echo "═══════════════════════════════════════════════════════════"
    echo "✅ Demo Complete!"
    echo "═══════════════════════════════════════════════════════════"
    echo ""
    echo "Generated briefing available at:"
    echo "  📄 ${OUTPUT_DIR}/test_input_wiki_briefing.md"
    echo ""
    echo "Review the output for strategic intelligence synthesis."
}

parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            --input|-i)
                TEST_INPUT="$2"
                shift 2
                ;;
            --output-dir|-o)
                OUTPUT_DIR="$2"
                shift 2
                ;;
            --help|-h)
                show_usage
                exit 0
                ;;
            *)
                echo "Unknown option: $1"
                show_usage
                exit 1
                ;;
        esac
    done
}

# Parse command line arguments
parse_args "$@"

# Run demo mode (or with user-provided input)
run_demo
