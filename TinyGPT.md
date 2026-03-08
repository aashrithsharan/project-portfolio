# TinyGPT - A Miniature GPT-style Language Model

A minimal, educational implementation of a GPT-style transformer for character-level language modeling, built from scratch in PyTorch.

## Overview

This project implements a small decoder-only transformer (similar to GPT) that can be trained on any text corpus to learn patterns and generate new text. It's designed to be:

- **Understandable**: Clean, well-commented code with clear structure
- **Trainable**: Small enough to train in hours on a single GPU
- **Educational**: Demonstrates core transformer concepts without framework abstractions

## Model Architecture

- **Type**: Decoder-only transformer (GPT-style)
- **Tokenization**: Character-level (simple vocab)
- **Parameters**: ~0.5-1M (configurable)
- **Default config**:
  - Embedding dimension: 128
  - Attention heads: 4
  - Transformer layers: 4
  - Context length: 128 characters
  - Dropout: 0.1

## Project Structure

```
tiny-gpt/
├── config.py       # Hyperparameters and settings
├── dataset.py      # Data loading and vocabulary
├── model.py        # TinyTransformer architecture
├── train.py        # Training loop
├── generate.py     # Text generation CLI
├── data/
│   └── input.txt   # Training corpus (you provide this)
└── README.md       # This file
```

## Setup

### Requirements

- Python 3.8+
- PyTorch 2.0+
- CUDA-capable GPU (optional but recommended)

```bash
pip install torch
```

### Prepare Your Data

Create a `data/` directory and add your training text:

```bash
mkdir data
# Add your text file as data/input.txt
# For example, download a book, Shakespeare plays, code, etc.
```

The model will train on any plain text file. Larger and more diverse text will produce better results.

## Usage

### 1. Configure Hyperparameters

Edit `config.py` to adjust model size, training duration, etc.:

```python
n_embd = 128        # Embedding dimension
n_layer = 4         # Number of transformer blocks
n_head = 4          # Number of attention heads
max_iters = 5000    # Training iterations
```

### 2. Train the Model

```bash
python train.py
```

This will:
- Load and tokenize `data/input.txt`
- Initialize the model
- Train for the specified iterations
- Save a checkpoint to `checkpoint.pt`

Training progress will be printed every 500 steps showing train/val loss.

### 3. Generate Text

```bash
# Generate with default settings
python generate.py --prompt "Hello" --max-new-tokens 500

# Generate with temperature control (lower = more conservative)
python generate.py --prompt "To be or not to be" --temperature 0.8 --max-new-tokens 300

# Generate with top-k sampling (only sample from top k most likely tokens)
python generate.py --prompt "Chapter 1" --top-k 50 --max-new-tokens 1000
```

## How It Works

### Architecture Components

1. **Token + Position Embeddings**: Convert character indices to dense vectors and add positional information
2. **Transformer Blocks**: Stack of self-attention + feedforward layers with residual connections
3. **Causal Self-Attention**: Each position can only attend to previous positions (for autoregressive generation)
4. **Language Model Head**: Final linear layer to predict next token probabilities

### Training

- **Objective**: Predict the next character given previous context
- **Loss**: Cross-entropy between predicted and actual next characters
- **Optimizer**: AdamW with gradient clipping
- **Regularization**: Dropout in attention and feedforward layers

### Generation

Autoregressive sampling:
1. Start with prompt
2. Predict next token probabilities
3. Sample from distribution (with temperature/top-k)
4. Append to sequence
5. Repeat

## Customization

- **Larger model**: Increase `n_embd`, `n_layer`, `n_head` in `config.py`
- **BPE tokenization**: Replace `CharDataset` with a BPE tokenizer (e.g., using `tiktoken`)
- **Learning rate schedule**: Add a scheduler in `train.py`
- **Longer training**: Increase `max_iters`

## Expected Results

With the default configuration and a decent text corpus:
- Training time: 1-3 hours on GPU, longer on CPU
- Final train loss: ~1.5-2.5 (depending on data)
- Generated text: Should show learned patterns, basic grammar, vocabulary from training data

The model won't produce perfect text, but should demonstrate clear learning of character patterns, common words, and basic structure.

## Learning Resources

This implementation demonstrates:
- Multi-head self-attention mechanism
- Causal masking for autoregressive models
- Residual connections and layer normalization
- Positional encodings
- Temperature and top-k sampling strategies

## License

MIT - Feel free to use for learning and experimentation!
